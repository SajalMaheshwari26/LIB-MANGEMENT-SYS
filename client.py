import requests
import json  # Add this line to import the 'json' module


new_book_data = {
    'title': 'The hell in the nightw ',
    'author': 'JDs. Salinger'
}

# Make a POST request to add a new book
response = requests.post('http://localhost:5000/api/books', json=new_book_data)
print(response.json())
updated_book_data = {
    'title': 'New Titlest',
    'author': 'Newestest'
}

# Make a PUT request to update a book with id=1
response = requests.put('http://localhost:5000/api/books/1', json=updated_book_data)
print(response.json())
