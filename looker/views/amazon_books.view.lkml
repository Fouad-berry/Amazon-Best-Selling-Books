# amazon_books.view.lkml

view: amazon_books {
  sql_table_name: `your_project.your_dataset.books` ;;

  # ─── Dimensions ───────────────────────────────────────────────────────────

  dimension: isbn {
    primary_key: yes
    type: string
    sql: ${TABLE}.isbn ;;
  }

  dimension: rank {
    type: number
    sql: ${TABLE}.rank ;;
  }

  dimension: title {
    type: string
    sql: ${TABLE}.title ;;
    link: { label: "View on Amazon" url: "https://www.amazon.com/s?k={{ value | encode_uri }}" }
  }

  dimension: author {
    type: string
    sql: ${TABLE}.author ;;
  }

  dimension: category {
    type: string
    sql: ${TABLE}.category ;;
  }

  dimension: sub_genre {
    type: string
    sql: ${TABLE}.sub_genre ;;
  }

  dimension: format {
    type: string
    sql: ${TABLE}.format ;;
  }

  dimension: publisher {
    type: string
    sql: ${TABLE}.publisher ;;
  }

  dimension: year_published {
    type: number
    sql: ${TABLE}.year_published ;;
  }

  dimension: rank_tier {
    type: string
    sql: ${TABLE}.rank_tier ;;
  }

  dimension: price_bucket {
    type: string
    sql: ${TABLE}.price_bucket ;;
  }

  dimension: rating_tier {
    type: string
    sql: ${TABLE}.rating_tier ;;
  }

  dimension: review_tier {
    type: string
    sql: ${TABLE}.review_tier ;;
  }

  dimension: longevity_tier {
    type: string
    sql: ${TABLE}.longevity_tier ;;
  }

  dimension: pub_era {
    type: string
    sql: ${TABLE}.pub_era ;;
  }

  dimension: is_fiction {
    type: yesno
    sql: ${TABLE}.is_fiction = 1 ;;
  }

  # ─── Numeric dimensions ───────────────────────────────────────────────────

  dimension: price_usd {
    type: number
    sql: ${TABLE}.price_usd ;;
    value_format: "$#,##0.00"
  }

  dimension: rating {
    type: number
    sql: ${TABLE}.rating ;;
    value_format_name: decimal_1
  }

  dimension: reviews {
    type: number
    sql: ${TABLE}.reviews ;;
    value_format_name: decimal_0
  }

  dimension: weeks_on_list {
    type: number
    sql: ${TABLE}.weeks_on_list ;;
  }

  dimension: amazon_bsr {
    type: number
    sql: ${TABLE}.amazon_bsr ;;
    label: "Amazon BSR"
  }

  dimension: value_score {
    type: number
    sql: ${TABLE}.value_score ;;
    value_format_name: decimal_3
  }

  dimension: engagement_score {
    type: number
    sql: ${TABLE}.engagement_score ;;
    value_format_name: decimal_2
  }

  # ─── Measures ─────────────────────────────────────────────────────────────

  measure: book_count {
    type: count
    label: "Number of Books"
    drill_fields: [title, author, category, sub_genre, rank]
  }

  measure: avg_rank {
    type: average
    sql: ${TABLE}.rank ;;
    value_format_name: decimal_1
  }

  measure: avg_price {
    type: average
    sql: ${TABLE}.price_usd ;;
    value_format: "$#,##0.00"
  }

  measure: avg_rating {
    type: average
    sql: ${TABLE}.rating ;;
    value_format_name: decimal_2
  }

  measure: total_reviews {
    type: sum
    sql: ${TABLE}.reviews ;;
    value_format_name: decimal_0
  }

  measure: avg_reviews {
    type: average
    sql: ${TABLE}.reviews ;;
    value_format_name: decimal_0
  }

  measure: avg_weeks_on_list {
    type: average
    sql: ${TABLE}.weeks_on_list ;;
    value_format_name: decimal_1
  }

  measure: avg_bsr {
    type: average
    sql: ${TABLE}.amazon_bsr ;;
    label: "Avg Amazon BSR"
    value_format_name: decimal_0
  }

  measure: avg_value_score {
    type: average
    sql: ${TABLE}.value_score ;;
    value_format_name: decimal_3
  }

  measure: avg_engagement {
    type: average
    sql: ${TABLE}.engagement_score ;;
    value_format_name: decimal_2
  }
}
