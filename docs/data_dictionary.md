# Data Dictionary

## Source: `amazon_bestselling_books.csv`

500 rows · 14 usable columns + 9 engineered columns

---

### Raw columns (after rename to snake_case)

| Column | Type | Range / Values | Description |
|---|---|---|---|
| `rank` | int | 1 – 500 | Amazon Best Sellers list rank |
| `title` | str | 500 unique | Book title |
| `author` | str | 168 unique | Author name |
| `category` | str | Fiction / Non-Fiction | Main category |
| `sub_genre` | str | 48 unique | Detailed genre (Self-Help, Romantasy, …) |
| `format` | str | Paperback / Hardcover / Kindle / Audiobook / Board Book | Physical or digital format |
| `price_usd` | float | $4.23 – $34.09 | Retail price |
| `rating` | float | 0 – 5 | Avg customer rating |
| `reviews` | float | 0 – 130 000+ | Number of customer reviews |
| `weeks_on_list` | float | 1 – 200+ | Consecutive weeks on the best-seller list |
| `publisher` | str | 56 unique | Publishing house |
| `year_published` | float | 1965 – 2026 | Year of publication |
| `isbn` | str | 500 unique | ISBN-13 identifier |
| `amazon_bsr` | float | 30 – 9 600 | Store-wide Amazon Best Seller Rank |

> `amazon_url` was dropped (always "View", zero analytical value).

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
| `value_score` | float | — | `rating / price_usd` — quality per dollar |
| `engagement_score` | float | — | `log10(reviews+1) × rating` — composite popularity |
| `is_fiction` | int | 0 / 1 | 1 if category = Fiction |
