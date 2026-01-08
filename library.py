def library_book_details(book_id, book_title, author_name, year_of_publication):
    return (
        f"Book ID: {book_id}\n"
        f"Book Title: {book_title}\n"
        f"Author Name: {author_name}\n"
        f"Year of Publication: {year_of_publication}"
    )
from library import library_book_details

result = library_book_details(
    101,
    "Python Programming",
    "Guido van Rossum",
    2020
)

print(result)
