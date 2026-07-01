-- price_rating_reviews.sql
-- Pricing, rating quality, and review volume analysis.

-- 1. Avg price & rating by format
SELECT
    format,
    COUNT(*)                            AS book_count,
    ROUND(AVG(price_usd), 2)            AS avg_price,
    MIN(price_usd)                      AS min_price,
    MAX(price_usd)                      AS max_price,
    ROUND(AVG(rating), 2)               AS avg_rating,
    ROUND(AVG(reviews), 0)              AS avg_reviews,
    ROUND(AVG(value_score), 4)          AS avg_value_score
FROM books
GROUP BY format
ORDER BY avg_price;

-- 2. Price bucket vs rating & reviews
SELECT
    price_bucket,
    COUNT(*)                            AS book_count,
    ROUND(AVG(rating), 2)               AS avg_rating,
    ROUND(AVG(reviews), 0)              AS avg_reviews,
    ROUND(AVG(weeks_on_list), 1)        AS avg_weeks
FROM books
GROUP BY price_bucket
ORDER BY price_bucket;

-- 3. Best value books (highest value_score, min 1000 reviews)
SELECT
    "rank", title, author, sub_genre, format,
    price_usd, rating, reviews,
    ROUND(value_score, 4)               AS value_score
FROM books
WHERE reviews >= 1000
ORDER BY value_score DESC
LIMIT 20;

-- 4. Rating tier distribution by category
SELECT
    category,
    rating_tier,
    COUNT(*)                            AS book_count,
    ROUND(AVG(reviews), 0)              AS avg_reviews
FROM books
GROUP BY category, rating_tier
ORDER BY category, rating_tier;