"""
load_data.py
------------
Load and validate the raw Amazon Best-Selling Books CSV.
"""

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

RAW_PATH = Path(__file__).parents[2] / "data" / "raw" / "amazon_bestselling_books.csv"

EXPECTED_COLUMNS = [
    "Rank",
    "Title",
    "Author",
    "Category",
    "Sub-Genre",
    "Format",
    "Price (USD)",
    "Rating",
    "Reviews",
    "Weeks on List",
    "Publisher",
    "Year Published",
    "ISBN",
    "Amazon BSR",
    "Amazon URL",
]

VALID_CATEGORIES = {"Fiction", "Non-Fiction"}
VALID_FORMATS = {"Paperback", "Hardcover", "Audiobook", "Kindle Edition", "Board Book"}


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """Load and validate the raw CSV."""
    log.info(f"Loading data from {path}")
    df = pd.read_csv(path)

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    df = df[EXPECTED_COLUMNS]

    # Cast types
    df["Rank"] = df["Rank"].astype(int)
    df["Price (USD)"] = pd.to_numeric(df["Price (USD)"], errors="coerce")
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
    df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")
    df["Weeks on List"] = pd.to_numeric(df["Weeks on List"], errors="coerce")
    df["Year Published"] = pd.to_numeric(df["Year Published"], errors="coerce")
    df["Amazon BSR"] = pd.to_numeric(df["Amazon BSR"], errors="coerce")

    log.info(f"Loaded {len(df):,} rows × {len(df.columns)} columns")
    validate(df)
    return df


def validate(df: pd.DataFrame) -> None:
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]
    if not nulls.empty:
        log.warning(f"Null values:\n{nulls}")

    dupes = df["ISBN"].duplicated().sum()
    if dupes:
        log.warning(f"{dupes} duplicate ISBNs")

    bad_rating = ((df["Rating"] < 0) | (df["Rating"] > 5)).sum()
    if bad_rating:
        log.warning(f"{bad_rating} ratings outside [0, 5]")

    bad_cat = (~df["Category"].isin(VALID_CATEGORIES)).sum()
    if bad_cat:
        log.warning(f"{bad_cat} unexpected Category values")

    bad_format = (~df["Format"].isin(VALID_FORMATS)).sum()
    if bad_format:
        log.warning(f"{bad_format} unexpected Format values")

    bad_rank = ((df["Rank"] < 1) | (df["Rank"] > 500)).sum()
    if bad_rank:
        log.warning(f"{bad_rank} ranks outside [1, 500]")

    bad_price = (df["Price (USD)"] <= 0).sum()
    if bad_price:
        log.warning(f"{bad_price} non-positive prices")

    bad_year = (df["Year Published"] < 1900) | (df["Year Published"] > 2027)
    if bad_year.sum():
        log.warning(f"{bad_year.sum()} years outside [1900, 2027]")

    bad_reviews = (df["Reviews"] < 0).sum()
    if bad_reviews:
        log.warning(f"{bad_reviews} negative review counts")

    bad_weeks = (df["Weeks on List"] < 0).sum()
    if bad_weeks:
        log.warning(f"{bad_weeks} negative weeks on list")

    log.info("Validation complete ✓")


if __name__ == "__main__":
    df = load_raw()
    print(df.head())
    print(df.dtypes)
