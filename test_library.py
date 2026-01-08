from library import library_book_details

def test_library_book_details():
    result = library_book_details(
        101,
        "Python Programming",
        "Guido van Rossum",
        2020
    )
 

    expected_output = (
        "Book ID: 101\n"
        "Book Title: Python Programming\n"
        "Author Name: Guido van Rossum\n"
        "Year of Publication: 2020"
    )

    assert result == expected_output
