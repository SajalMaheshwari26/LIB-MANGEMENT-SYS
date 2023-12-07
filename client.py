import requests
import json  

# Just a demo client file where u can run ur POST, PUT etc. queries.
# Just a demo client file where u can run ur POST, PUT etc. queries.
# Just a demo client file where u can run ur POST, PUT etc. queries.

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
