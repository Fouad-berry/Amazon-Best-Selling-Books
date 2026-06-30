"""
metrics.py
----------
Compute KPIs and aggregated export tables for Looker.
"""

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

PROCESSED_PATH = Path(__file__).parents[2] / "data" / "processed" / "books_clean.csv"
EXPORTS_DIR    = Path(__file__).parents[2] / "data" / "exports"


def load_processed() -> pd.DataFrame:
    return pd.read_csv(PROCESSED_PATH)


# ─── KPIs ─────────────────────────────────────────────────────────────────────

def avg_price(df):       return round(df["Price (USD)"].mean(), 2)
def avg_rating(df):      return round(df["Rating"].mean(), 2)
def avg_reviews(df):     return round(df["Reviews"].mean(), 0)
def avg_weeks(df):       return round(df["Weeks on List"].mean(), 1)
def top_author(df):      return df.groupby("Author")["Rank"].count().idxmax()
def top_publisher(df):   return df.groupby("Publisher")["Rank"].count().idxmax()
def pct_fiction(df):     return round(df["is_fiction"].mean() * 100, 1)


# ─── Aggregated tables ────────────────────────────────────────────────────────

def agg_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Category")
        .agg(
            book_count=("Rank", "count"),
            avg_rank=("Rank", "mean"),
            avg_price=("Price (USD)", "mean"),
            avg_rating=("Rating", "mean"),
            avg_reviews=("Reviews", "mean"),
            avg_weeks=("Weeks on List", "mean"),
            avg_bsr=("Amazon BSR", "mean"),
        )
        .round(2).reset_index()
    )


def agg_by_genre(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["Category", "Sub-Genre"])
        .agg(
            book_count=("Rank", "count"),
            avg_rank=("Rank", "mean"),
            avg_price=("Price (USD)", "mean"),
            avg_rating=("Rating", "mean"),
            avg_reviews=("Reviews", "mean"),
            avg_weeks=("Weeks on List", "mean"),
            avg_engagement=("engagement_score", "mean"),
        )
        .round(2).reset_index()
        .sort_values("book_count", ascending=False)
    )


def agg_by_format(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Format")
        .agg(
            book_count=("Rank", "count"),
            avg_price=("Price (USD)", "mean"),
            avg_rating=("Rating", "mean"),
            avg_reviews=("Reviews", "mean"),
            avg_weeks=("Weeks on List", "mean"),
            pct_fiction=("is_fiction", "mean"),
        )
        .round(2).reset_index()
        .sort_values("book_count", ascending=False)
    )


def agg_top_authors(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Author")
        .agg(
            titles_on_list=("Rank", "count"),
            best_rank=("Rank", "min"),
            avg_rank=("Rank", "mean"),
            avg_rating=("Rating", "mean"),
            total_reviews=("Reviews", "sum"),
            avg_price=("Price (USD)", "mean"),
            avg_weeks=("Weeks on List", "mean"),
        )
        .round(2).reset_index()
        .sort_values("titles_on_list", ascending=False)
        .head(30)
    )


def agg_top_publishers(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Publisher")
        .agg(
            titles_on_list=("Rank", "count"),
            avg_rank=("Rank", "mean"),
            avg_rating=("Rating", "mean"),
            avg_reviews=("Reviews", "mean"),
            avg_price=("Price (USD)", "mean"),
            avg_weeks=("Weeks on List", "mean"),
            avg_bsr=("Amazon BSR", "mean"),
        )
        .round(2).reset_index()
        .sort_values("titles_on_list", ascending=False)
        .head(20)
    )


def agg_by_pub_era(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("pub_era", observed=True)
        .agg(
            book_count=("Rank", "count"),
            avg_rank=("Rank", "mean"),
            avg_rating=("Rating", "mean"),
            avg_reviews=("Reviews", "mean"),
            avg_weeks=("Weeks on List", "mean"),
        )
        .round(2).reset_index()
    )


def agg_by_price_bucket(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("price_bucket", observed=True)
        .agg(
            book_count=("Rank", "count"),
            avg_rank=("Rank", "mean"),
            avg_rating=("Rating", "mean"),
            avg_reviews=("Reviews", "mean"),
            avg_weeks=("Weeks on List", "mean"),
        )
        .round(2).reset_index()
    )


# ─── Main ─────────────────────────────────────────────────────────────────────

def run_all():
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    df = load_processed()

    tables = {
        "agg_category.csv":     agg_by_category(df),
        "agg_genre.csv":        agg_by_genre(df),
        "agg_format.csv":       agg_by_format(df),
        "agg_top_authors.csv":  agg_top_authors(df),
        "agg_publishers.csv":   agg_top_publishers(df),
        "agg_pub_era.csv":      agg_by_pub_era(df),
        "agg_price_bucket.csv": agg_by_price_bucket(df),
    }

    for fname, table in tables.items():
        path = EXPORTS_DIR / fname
        table.to_csv(path, index=False)
        log.info(f"Exported {fname} ({len(table)} rows)")

    print("\n" + "=" * 44)
    print("📚  KEY METRICS SUMMARY")
    print("=" * 44)
    print(f"Books analysed:        {len(df):>8,}")
    print(f"Avg price:             ${avg_price(df):>7.2f}")
    print(f"Avg rating:            {avg_rating(df):>8.2f} / 5")
    print(f"Avg reviews:           {avg_reviews(df):>8,.0f}")
    print(f"Avg weeks on list:     {avg_weeks(df):>8.1f}w")
    print(f"% Fiction:             {pct_fiction(df):>7.1f}%")
    print(f"Most prolific author:  {top_author(df)}")
    print(f"Top publisher:         {top_publisher(df)}")


if __name__ == "__main__":
    run_all()