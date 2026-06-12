# books_overview.dashboard.lookml

- dashboard: books_overview
  title: "Amazon Best-Selling Books — Overview"
  layout: newspaper
  preferred_viewer: dashboards-next

  filters:
    - name: category
      title: "Category"
      type: field_filter
      explore: amazon_books
      field: amazon_books.category
      default_value: ""
      allow_multiple_values: true

    - name: format
      title: "Format"
      type: field_filter
      explore: amazon_books
      field: amazon_books.format
      default_value: ""
      allow_multiple_values: true

    - name: pub_era
      title: "Publication Era"
      type: field_filter
      explore: amazon_books
      field: amazon_books.pub_era
      default_value: ""

  elements:

    # ── KPI scorecards ───────────────────────────────────────────────────────
    - title: "Total Books"
      name: kpi_count
      model: amazon_books
      explore: amazon_books
      type: single_value
      fields: [amazon_books.book_count]
      row: 0
      col: 0
      width: 6
      height: 4

    - title: "Avg Price"
      name: kpi_price
      model: amazon_books
      explore: amazon_books
      type: single_value
      fields: [amazon_books.avg_price]
      row: 0
      col: 6
      width: 6
      height: 4

    - title: "Avg Rating"
      name: kpi_rating
      model: amazon_books
      explore: amazon_books
      type: single_value
      fields: [amazon_books.avg_rating]
      row: 0
      col: 12
      width: 6
      height: 4

    - title: "Avg Weeks on List"
      name: kpi_weeks
      model: amazon_books
      explore: amazon_books
      type: single_value
      fields: [amazon_books.avg_weeks_on_list]
      row: 0
      col: 18
      width: 6
      height: 4

    # ── Fiction vs Non-Fiction split (pie) ───────────────────────────────────
    - title: "Fiction vs Non-Fiction"
      name: category_split
      model: amazon_books
      explore: amazon_books
      type: looker_pie
      fields: [amazon_books.category, amazon_books.book_count]
      row: 4
      col: 0
      width: 8
      height: 8

    # ── Books by Format (bar) ────────────────────────────────────────────────
    - title: "Books by Format"
      name: format_bar
      model: amazon_books
      explore: amazon_books
      type: looker_column
      fields: [amazon_books.format, amazon_books.book_count, amazon_books.avg_rating]
      sorts: [amazon_books.book_count desc]
      row: 4
      col: 8
      width: 8
      height: 8

    # ── Top Sub-genres (bar) ─────────────────────────────────────────────────
    - title: "Top 10 Sub-Genres by Volume"
      name: subgenre_bar
      model: amazon_books
      explore: amazon_books
      type: looker_bar
      fields: [amazon_books.sub_genre, amazon_books.book_count]
      sorts: [amazon_books.book_count desc]
      limit: 10
      row: 4
      col: 16
      width: 8
      height: 8

    # ── Top Publishers (bar) ─────────────────────────────────────────────────
    - title: "Top 10 Publishers"
      name: publisher_bar
      model: amazon_books
      explore: amazon_books
      type: looker_bar
      fields: [amazon_books.publisher, amazon_books.book_count, amazon_books.avg_rating]
      sorts: [amazon_books.book_count desc]
      limit: 10
      row: 12
      col: 0
      width: 12
      height: 8

    # ── Avg Rating by Sub-Genre (column) ─────────────────────────────────────
    - title: "Avg Rating by Sub-Genre (Top 10)"
      name: rating_by_genre
      model: amazon_books
      explore: amazon_books
      type: looker_column
      fields: [amazon_books.sub_genre, amazon_books.avg_rating, amazon_books.avg_reviews]
      sorts: [amazon_books.avg_reviews desc]
      limit: 10
      row: 12
      col: 12
      width: 12
      height: 8

    # ── Books published per year (line) ──────────────────────────────────────
    - title: "Best-Sellers by Publication Year"
      name: pub_year_line
      model: amazon_books
      explore: amazon_books
      type: looker_line
      fields: [amazon_books.year_published, amazon_books.book_count, amazon_books.avg_rating]
      sorts: [amazon_books.year_published asc]
      row: 20
      col: 0
      width: 24
      height: 8
