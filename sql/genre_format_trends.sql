-- genre_format_trends.sql
-- Sub-genre and format breakdown with temporal trends.

-- 1. Top 15 sub-genres by number of titles
SELECT
    sub_genre,
    category,
    COUNT(*)                            AS book_count,
    ROUND(AVG(rank), 1)                 AS avg_rank,
    ROUND(AVG(price_usd), 2)            AS avg_price,
    ROUND(AVG(rating), 2)               AS avg_rating,
    ROUND(AVG(reviews), 0)              AS avg_reviews,
    ROUND(AVG(weeks_on_list), 1)        AS avg_weeks
FROM books
GROUP BY sub_genre, category
ORDER BY book_count DESC
LIMIT 15;

-- 2. Format trends by publication era
SELECT
    pub_era,
    format,
    COUNT(*)                            AS book_count,
    ROUND(AVG(price_usd), 2)            AS avg_price,
    ROUND(AVG(rating), 2)               AS avg_rating
FROM books
GROUP BY pub_era, format
ORDER BY pub_era, book_count DESC;

-- 3. Most reviewed sub-genres
SELECT
    sub_genre,
    COUNT(*)                            AS book_count,
    ROUND(AVG(reviews), 0)              AS avg_reviews,
    ROUND(MAX(reviews), 0)              AS max_reviews,
    ROUND(AVG(rating), 2)               AS avg_rating,
    ROUND(AVG(engagement_score), 2)     AS avg_engagement
FROM books
GROUP BY sub_genre
ORDER BY avg_reviews DESC
LIMIT 15;
