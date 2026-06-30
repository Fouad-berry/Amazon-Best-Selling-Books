"""
clean_transform.py
------------------
Clean and feature-engineer the Amazon Best-Selling Books dataset.
"""

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd

_PROJECT_ROOT = str(Path(__file__).parents[2])
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from src.ingestion.load_data import load_raw  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

PROCESSED_PATH = Path(__file__).parents[2] / "data" / "processed" / "books_clean.csv"
EXPORT_PATH = Path(__file__).parents[2] / "data" / "exports" / "books_looker.csv"


def clean(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Cleaning …")
    df = df.copy()

    # Standardise strings
    for col in ["Category", "Sub-Genre", "Format", "Publisher"]:
        df[col] = df[col].str.strip()

    # Drop the URL column (always "View", no analytical value)
    df = df.drop(columns=["Amazon URL"], errors="ignore")

    # Clip rating
    df["Rating"] = df["Rating"].clip(0, 5)

    # Ensure non-negative prices
    df["Price (USD)"] = df["Price (USD)"].clip(lower=0)

    # Fill missing Reviews with 0 (new books) and clamp negatives
    df["Reviews"] = df["Reviews"].fillna(0).clip(lower=0)

    # Fill missing Weeks on List with 1 and clamp negatives
    df["Weeks on List"] = df["Weeks on List"].fillna(1).clip(lower=1)

    # Ensure non-negative Amazon BSR
    df["Amazon BSR"] = df["Amazon BSR"].clip(lower=0)

    log.info("Cleaning done ✓")
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Engineering features …")
    df = df.copy()

    # Rank tier (Top 10 / 11-50 / 51-100 / 101-500)
    df["rank_tier"] = pd.cut(
        df["Rank"],
        bins=[0, 10, 50, 100, 500],
        labels=["Top 10", "Top 11-50", "Top 51-100", "Top 101-500"],
    )

    # Price bucket
    df["price_bucket"] = pd.cut(
        df["Price (USD)"],
        bins=[0, 10, 15, 20, 40],
        labels=["Budget (<$10)", "Mid ($10-15)", "Standard ($15-20)", "Premium ($20+)"],
    )

    # Rating tier
    df["rating_tier"] = pd.cut(
        df["Rating"],
        bins=[0, 3.5, 4.0, 4.5, 5.0],
        labels=["Below Average (<3.5)", "Good (3.5-4.0)", "Very Good (4.0-4.5)", "Excellent (4.5+)"],
    )

    # Review volume tier (log-scale buckets)
    df["review_tier"] = pd.cut(
        df["Reviews"],
        bins=[-1, 500, 5_000, 30_000, df["Reviews"].max() + 1],
        labels=["Niche (<500)", "Moderate (500-5k)", "Popular (5k-30k)", "Viral (30k+)"],
    )

    # Longevity on list
    df["longevity_tier"] = pd.cut(
        df["Weeks on List"],
        bins=[0, 4, 12, 52, 9999],
        labels=["New (≤4w)", "Short Run (4-12w)", "Established (12-52w)", "Long-Running (52w+)"],
    )

    # Publication era
    df["pub_era"] = pd.cut(
        df["Year Published"],
        bins=[1960, 2000, 2015, 2020, 2023, 2027],
        labels=["Classic (pre-2000)", "2000s-2014", "2015-2019", "2020-2022", "2023+"],
    )

    # Value score: rating / price (higher = better value)
    df["value_score"] = (df["Rating"] / df["Price (USD)"].replace(0, float("nan"))).round(4)

    # Engagement score: log10(reviews + 1) * rating
    df["engagement_score"] = (np.log10(df["Reviews"] + 1) * df["Rating"]).round(3)

    # Is Fiction flag
    df["is_fiction"] = (df["Category"] == "Fiction").astype(int)

    log.info("Feature engineering done ✓")
    return df


def save(df: pd.DataFrame) -> None:
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    log.info(f"Saved processed → {PROCESSED_PATH}")
    df.to_csv(EXPORT_PATH, index=False)
    log.info(f"Saved Looker export → {EXPORT_PATH}")


def run_pipeline() -> pd.DataFrame | None:
    try:
        df = load_raw()
        df = clean(df)
        df = feature_engineering(df)
        save(df)
        log.info(f"Pipeline complete — {len(df):,} books.")
        return df
    except FileNotFoundError as e:
        log.error(f"File not found: {e}")
    except pd.errors.EmptyDataError:
        log.error("CSV file is empty.")
    except Exception as e:
        log.error(f"Pipeline failed: {e}")
    return None


if __name__ == "__main__":
    run_pipeline()
