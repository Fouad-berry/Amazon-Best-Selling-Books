# amazon_books.model.lkml

connection: "amazon_books_bq"   # Replace with your Looker connection name

include: "/looker/views/*.view.lkml"
include: "/looker/explores/*.lkml"

label: "Amazon Best-Selling Books"
