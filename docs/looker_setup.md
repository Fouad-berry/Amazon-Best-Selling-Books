# Looker Studio Setup Guide

---

## Option A — Looker Studio (free)

1. Run the pipeline:
   ```bash
   python src/transformation/clean_transform.py
   python src/analysis/metrics.py
   ```

2. Upload these files to Google Drive:
   - `data/exports/books_looker.csv` (main dataset, 500 rows)
   - `data/exports/agg_genre.csv`
   - `data/exports/agg_format.csv`
   - `data/exports/agg_top_authors.csv`
   - `data/exports/agg_publishers.csv`
   - `data/exports/agg_pub_era.csv`
   - `data/exports/agg_price_bucket.csv`

3. Open [lookerstudio.google.com](https://lookerstudio.google.com) → New Report → Add Data Source → Google Sheets.

4. Suggested dashboard pages:

| Page | Source | Chart types |
|---|---|---|
| Overview | `books_looker.csv` | Scorecards, pie (category), bar (format) |
| Genre Deep-Dive | `agg_genre.csv` | Bar: book count, table: avg rating & reviews |
| Price & Value | `agg_price_bucket.csv` | Bar: avg rating by price, scatter: price vs rating |
| Publishers | `agg_publishers.csv` | Bar: titles, table with avg metrics |
| Authors | `agg_top_authors.csv` | Ranked table, bar: total reviews |
| Trends | `agg_pub_era.csv` | Line: books by era, `books_looker.csv` scatter |

---

## Option B — BigQuery

```python
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client(project="your-project")
df = pd.read_csv("data/processed/books_clean.csv")
job = client.load_table_from_dataframe(
    df, "your-project.amazon_books.books",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE"),
)
job.result()
```

Set Looker connection name to `amazon_books_bq`.

---

## Key Metrics to Build

| Metric | Formula |
|---|---|
| Avg rating | AVG(Rating) |
| Avg price | AVG(Price) |
| Avg reviews | AVG(Reviews) |
| Avg weeks on list | AVG(Weeks on List) |
| Value score | AVG(value_score) = AVG(Rating / Price) |
| Engagement score | AVG(log10(Reviews+1) × Rating) |
| % Fiction | AVG(is_fiction) × 100 |