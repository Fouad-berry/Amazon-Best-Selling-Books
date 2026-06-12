# 📚 Amazon Best-Selling Books — Data Analysis Project

End-to-end data analysis pipeline on 500 Amazon best-selling books, exploring rankings, pricing, ratings, reviews, and publisher trends — with Python ETL, SQL analytics, and Looker Studio dashboards.

---

## 📁 Project Structure

```
amazon-books-analysis/
│
├── data/
│   ├── raw/                                  # Original CSV (do not modify)
│   ├── processed/                            # Cleaned & feature-engineered data
│   └── exports/                              # Aggregated CSVs ready for Looker
│
├── notebooks/
│   ├── 01_exploration.ipynb                  # EDA — distributions, nulls, correlations
│   ├── 02_cleaning.ipynb                     # Cleaning walkthrough
│   └── 03_analysis.ipynb                     # Business insights & visualisations
│
├── sql/
│   ├── create_tables.sql                     # DDL for DuckDB / BigQuery
│   ├── rankings_analysis.sql                 # Rank, BSR & weeks on list
│   ├── price_rating_reviews.sql              # Price vs rating vs reviews
│   ├── publisher_authors.sql                 # Top publishers & prolific authors
│   └── genre_format_trends.sql               # Sub-genre & format breakdown
│
├── src/
│   ├── ingestion/load_data.py                # Load & validate raw CSV
│   ├── transformation/clean_transform.py     # Cleaning + feature engineering
│   └── analysis/metrics.py                  # KPIs + aggregated export tables
│
├── looker/
│   ├── models/amazon_books.model.lkml
│   ├── views/amazon_books.view.lkml
│   ├── explores/books_explore.lkml
│   └── dashboards/books_overview.dashboard.lookml
│
├── docs/
│   ├── data_dictionary.md                    # Column descriptions & types
│   └── looker_setup.md                       # Connect Looker to this project
│
├── .github/workflows/ci.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗂️ Dataset

**File:** `data/raw/amazon_bestselling_books.csv`
**Rows:** 500 | **Columns:** 15
**Source:** Amazon Best Sellers list

| Column | Type | Description |
|---|---|---|
| `Rank` | int | Amazon Best Sellers rank (1–500) |
| `Title` | str | Book title |
| `Author` | str | Author name |
| `Category` | str | Fiction / Non-Fiction |
| `Sub-Genre` | str | 48 sub-genres (Self-Help, Romantasy, …) |
| `Format` | str | Paperback / Hardcover / Kindle / Audiobook / Board Book |
| `Price (USD)` | float | Retail price in USD |
| `Rating` | float | Average customer rating (0–5) |
| `Reviews` | float | Number of customer reviews |
| `Weeks on List` | float | Number of weeks on the best-seller list |
| `Publisher` | str | Publisher name (56 unique) |
| `Year Published` | float | Publication year (1965–2026) |
| `ISBN` | str | ISBN-13 identifier |
| `Amazon BSR` | float | Amazon Best Seller Rank (store-wide) |
| `Amazon URL` | str | Link placeholder |

---

## 🚀 Quick Start

```bash
git clone https://github.com/<your-username>/amazon-books-analysis.git
cd amazon-books-analysis
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/transformation/clean_transform.py
python src/analysis/metrics.py
jupyter lab
```

---

## 📊 Looker Studio Dashboards

See [`docs/looker_setup.md`](docs/looker_setup.md) for connection instructions.

| Dashboard | Key charts |
|---|---|
| 📌 Overview | Rank distribution, top authors, category split |
| 💰 Price & Value | Price by format/genre, rating vs price scatter |
| ⭐ Ratings & Reviews | Top-rated books, review volume by sub-genre |
| 🏢 Publishers | Top publishers by volume, avg rating, longevity |
| 📅 Trends | Publication year trends, weeks on list |

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.11 |
| Data manipulation | pandas, numpy |
| Visualisation | matplotlib, seaborn, plotly |
| SQL | DuckDB (local) / BigQuery (cloud) |
| BI | Looker Studio |
| CI | GitHub Actions |

---

## 📄 License

Réalisé par Fouad MOUTAIROU
POrtfolio : https://portfolio-fouad.netlify.app/

MIT