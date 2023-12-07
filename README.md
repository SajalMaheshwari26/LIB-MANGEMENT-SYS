# Supabase Flask API

This is a simple Flask API integrated with Supabase, a cloud database service. The API allows you to manage a collection of books, including retrieving all books, adding a new book, and updating an existing book.

# Table of Contents
  - [Install Dependencies](#install-dependencies)
  - [Set Up Supabase Credentials](#set-up-supabase-credentials)
  - [Run the Application](#run-the-application)
- [Seeding the Database](#seeding-the-database)
- [API Documentation](#api-documentation)
  - [Retrieve All Books](#retrieve-all-books)
  - [Add a New Book](#add-a-new-book)
  - [Update a Book](#update-a-book)

# Instal Dependencies
Open a terminal or command prompt.
Run the following command to install Flask and supabase using pip:
pip install Flask
pip install supabase-py


# Set Up Supabase Credentials
Replace SUPABASE_URL and SUPABASE_KEY in app.py with your Supabase URL and key.


# Run the Application
In bash : python app.py
The API will be available at http://localhost:5000.

It would be better to run the app first on one terminal and run another file such as client.py (containing queries POST, PUT etc.) on another terminal.


# To seed the database with mock data, run the following command: (U dont need to do this as database already has content)
in bash: python seed_database.py
This will add a few sample books to your Supabase database.


# API Documentation
  ## Retrieve All Books
  Endpoint: /api/books
  Method: GET
  Description: Retrieve a list of all books.
  
  ### Response Format: 
  {
      "books": [
          {
              "id": 1,
              "title": "Sample Title",
              "author": "Sample Author"
          },
          {
              "id": 2,
              "title": "Another Title",
              "author": "Another Author"
          },
          ...
      ]
  }

  ## Add a New Book
  Endpoint: /api/books
  Method: POST
  Description: Add a new book to the database.
  
  ### Request Format:
  {
      "title": "New Title",
      "author": "New Author"
  }

  ### Response Format:
  {
      "success": "Book added"
  }

  ## Update a Book
  Endpoint: /api/books/<int:id>
  Method: PUT
  Description: Update an existing book.
  
  ### Request Format:
  {
      "title": "Updated Title",
      "author": "Updated Author"
  }
  
  ### Response Format:
  {
      "success": "Book updated"
  }

  
      
