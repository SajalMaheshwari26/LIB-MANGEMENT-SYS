import requests
import json  # Add this line to import the 'json' module

# Example data for a new book
updated_book_data = {
    'title': 'New Title',
    'author': 'New Author'
}

# Make a PUT request to update a book with id=1
response = requests.put('http://localhost:5000/api/books/1', json=updated_book_data)
print(response)
