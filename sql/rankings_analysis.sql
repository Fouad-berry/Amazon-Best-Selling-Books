-- rankings_analysis.sql
-- Best-seller rank, Amazon BSR, and longevity analysis.

-- 1. Average rank by category and format
SELECT
    category,
    format,
    COUNT(*)                            AS book_count,
    ROUND(AVG("rank"), 1)               AS avg_rank,
    ROUND(AVG(amazon_bsr), 0)           AS avg_bsr,
    ROUND(AVG(weeks_on_list), 1)        AS avg_weeks,
    ROUND(AVG(rating), 2)               AS avg_rating
FROM books
GROUP BY category, format
ORDER BY category, avg_rank;

-- 2. Longevity tiers — what keeps books on the list?
SELECT
    longevity_tier,
    COUNT(*)                            AS book_count,
    ROUND(AVG("rank"), 1)               AS avg_rank,
    ROUND(AVG(rating), 2)               AS avg_rating,
    ROUND(AVG(reviews), 0)              AS avg_reviews,
    ROUND(AVG(price_usd), 2)            AS avg_price,
    ROUND(AVG(engagement_score), 2)     AS avg_engagement
FROM books
GROUP BY longevity_tier
ORDER BY longevity_tier;

-- 3. Top 20 books by engagement score
SELECT
    "rank", title, author, category, sub_genre, format,
    rating, reviews, weeks_on_list,
    ROUND(engagement_score, 2)          AS engagement_score
FROM books
ORDER BY engagement_score DESC
LIMIT 20;