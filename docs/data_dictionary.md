# Data Dictionary

## Source: `amazon_bestselling_books.csv`

500 rows · 14 usable columns + 8 engineered columns

---

### Raw columns

| Column | Type | Range / Values | Description |
|---|---|---|---|
| `Rank` | int | 1 – 500 | Amazon Best Sellers list rank |
| `Title` | str | 500 unique | Book title |
| `Author` | str | 168 unique | Author name |
| `Category` | str | Fiction / Non-Fiction | Main category |
| `Sub-Genre` | str | 48 unique | Detailed genre (Self-Help, Romantasy, …) |
| `Format` | str | Paperback / Hardcover / Kindle / Audiobook / Board Book | Physical or digital format |
| `Price (USD)` | float | $4.23 – $34.09 | Retail price |
| `Rating` | float | 0 – 5 | Avg customer rating |
| `Reviews` | float | 0 – 130 000+ | Number of customer reviews |
| `Weeks on List` | float | 1 – 200+ | Consecutive weeks on the best-seller list |
| `Publisher` | str | 56 unique | Publishing house |
| `Year Published` | float | 1965 – 2026 | Year of publication |
| `ISBN` | str | 500 unique | ISBN-13 identifier |
| `Amazon BSR` | float | 30 – 9 600 | Store-wide Amazon Best Seller Rank |

> `Amazon URL` was dropped (always "View", zero analytical value).

---

### Engineered columns (added in `clean_transform.py`)

| Column | Type | Values | Description |
|---|---|---|---|
| `rank_tier` | str | Top 10 / Top 11-50 / Top 51-100 / Top 101-500 | Rank bucket |
| `price_bucket` | str | Budget / Mid / Standard / Premium | Price range bracket |
| `rating_tier` | str | Below Average / Good / Very Good / Excellent | Rating bracket |
| `review_tier` | str | Niche / Moderate / Popular / Viral | Review volume bucket |
| `longevity_tier` | str | New / Short Run / Established / Long-Running | Weeks on list bracket |
| `pub_era` | str | Classic / 2000s-2014 / 2015-2019 / 2020-2022 / 2023+ | Publication era |
| `value_score` | float | — | `Rating / Price` — quality per dollar |
| `engagement_score` | float | — | `log10(Reviews+1) × Rating` — composite popularity |
| `is_fiction` | int | 0 / 1 | 1 if Category = Fiction |