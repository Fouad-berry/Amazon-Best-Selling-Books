-- publisher_authors.sql
-- Publisher dominance and prolific author analysis.

-- 1. Top 15 publishers by number of best-sellers
SELECT
    publisher,
    COUNT(*)                            AS titles_on_list,
    ROUND(AVG(rank), 1)                 AS avg_rank,
    ROUND(AVG(rating), 2)               AS avg_rating,
    ROUND(AVG(reviews), 0)              AS avg_reviews,
    ROUND(AVG(price_usd), 2)            AS avg_price,
    ROUND(AVG(weeks_on_list), 1)        AS avg_weeks,
    ROUND(AVG(amazon_bsr), 0)           AS avg_bsr
FROM books
GROUP BY publisher
ORDER BY titles_on_list DESC
LIMIT 15;

-- 2. Authors with multiple best-sellers
SELECT
    author,
    COUNT(*)                            AS titles_on_list,
    MIN(rank)                           AS best_rank,
    ROUND(AVG(rating), 2)               AS avg_rating,
    SUM(reviews)                        AS total_reviews,
    ROUND(AVG(price_usd), 2)            AS avg_price,
    STRING_AGG(title, ' | ')            AS titles
FROM books
GROUP BY author
HAVING COUNT(*) > 1
ORDER BY titles_on_list DESC, avg_rating DESC;

-- 3. Publisher × category breakdown
SELECT
    publisher,
    category,
    COUNT(*)                            AS book_count,
    ROUND(AVG(rating), 2)               AS avg_rating
FROM books
WHERE publisher IN (
    SELECT publisher FROM books
    GROUP BY publisher
    ORDER BY COUNT(*) DESC
    LIMIT 10
)
GROUP BY publisher, category
ORDER BY publisher, book_count DESC;
