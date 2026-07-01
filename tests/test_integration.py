import sys
import tempfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1]))

from src.transformation.clean_transform import PROCESSED_PATH, EXPORT_PATH, run_pipeline


def test_run_pipeline_returns_dataframe():
    df = run_pipeline()
    assert df is not None
    assert len(df) == 500


def test_run_pipeline_creates_processed_csv():
    run_pipeline()
    assert PROCESSED_PATH.exists()
    assert PROCESSED_PATH.stat().st_size > 0


def test_run_pipeline_creates_export_csv():
    run_pipeline()
    assert EXPORT_PATH.exists()
    assert EXPORT_PATH.stat().st_size > 0
