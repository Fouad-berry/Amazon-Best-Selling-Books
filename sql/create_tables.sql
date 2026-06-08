-- create_tables.sql
-- DDL for DuckDB (local) or BigQuery.
-- DuckDB: duckdb books.duckdb < sql/create_tables.sql

CREATE TABLE IF NOT EXISTS books (
    rank                INTEGER,
    title               VARCHAR,
    author              VARCHAR,
    category            VARCHAR,
    sub_genre           VARCHAR,
    format              VARCHAR,
    price_usd           DOUBLE,
    rating              DOUBLE,
    reviews             DOUBLE,
    weeks_on_list       DOUBLE,
    publisher           VARCHAR,
    year_published      INTEGER,
    isbn                VARCHAR,
    amazon_bsr          DOUBLE,
    -- Engineered
    rank_tier           VARCHAR,
    price_bucket        VARCHAR,
    rating_tier         VARCHAR,
    review_tier         VARCHAR,
    longevity_tier      VARCHAR,
    pub_era             VARCHAR,
    value_score         DOUBLE,
    engagement_score    DOUBLE,
    is_fiction          INTEGER,
    PRIMARY KEY (isbn)
);

-- Load from processed CSV (DuckDB syntax)
-- COPY books FROM 'data/processed/books_clean.csv' (HEADER TRUE);