import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1]))

from src.ingestion.load_data import EXPECTED_COLUMNS, VALID_CATEGORIES, VALID_FORMATS, load_raw
from src.transformation.clean_transform import clean, feature_engineering


@pytest.fixture
def df():
    return load_raw()


def test_load_raw_returns_500_rows(df):
    assert len(df) == 500


def test_load_raw_has_all_expected_columns(df):
    assert set(EXPECTED_COLUMNS) == set(df.columns)


def test_load_raw_no_nulls(df):
    assert df.isnull().sum().sum() == 0


def test_validate_categories(df):
    assert df["Category"].isin(VALID_CATEGORIES).all()


def test_validate_formats(df):
    assert df["Format"].isin(VALID_FORMATS).all()


def test_validate_rating_range(df):
    assert df["Rating"].between(0, 5).all()


def test_validate_rank_range(df):
    assert df["Rank"].between(1, 500).all()


def test_validate_positive_price(df):
    assert (df["Price (USD)"] > 0).all()


def test_clean_drops_amazon_url(df):
    cleaned = clean(df)
    assert "Amazon URL" not in cleaned.columns


def test_clean_fills_reviews(df):
    cleaned = clean(df)
    assert cleaned["Reviews"].isnull().sum() == 0


def test_clean_fills_weeks(df):
    cleaned = clean(df)
    assert cleaned["Weeks on List"].isnull().sum() == 0


def test_feature_engineering_adds_columns(df):
    cleaned = clean(df)
    fe = feature_engineering(cleaned)
    expected = [
        "rank_tier", "price_bucket", "rating_tier", "review_tier",
        "longevity_tier", "pub_era", "value_score", "engagement_score",
        "is_fiction",
    ]
    for col in expected:
        assert col in fe.columns, f"Missing engineered column: {col}"


def test_feature_engineering_value_score_no_inf(df):
    cleaned = clean(df)
    fe = feature_engineering(cleaned)
    assert not fe["value_score"].isnull().all()
    assert not fe["value_score"].isin([float("inf"), float("-inf")]).any()
