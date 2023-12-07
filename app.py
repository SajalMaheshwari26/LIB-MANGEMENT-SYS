from flask import Flask, request, jsonify
import supabase

app = Flask(__name__)

# Configure Supabase credentials
supabase_url = 'https://rihpswtdvlicapxueytj.supabase.co'  # Replace with your Supabase URL
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpaHBzd3RkdmxpY2FweHVleXRqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDE4OTQwNzUsImV4cCI6MjAxNzQ3MDA3NX0.JpeBx0jmtTnYgyNXxvmP-P3dIaPwIJJGXP_V6dsMmrk'  # Replace with your Supabase key

# Initialize Supabase client
supabase_client = supabase.create_client(supabase_url, supabase_key)


# Endpoint 1: Retrieve All Books
@app.route('/api/books', methods=['GET'])
def get_all_books():
    try:
        # Query all books from Supabase
        response = supabase_client.from_('books').select('*').execute()
        
        # Access the data from the response
        books = response.data

        return jsonify({'books': books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# Endpoint 2: Add a New Book
@app.route('/api/books', methods=['POST'])
def add_new_book():
    try:
        data = request.get_json()

        # Validate request payload
        if 'title' not in data or 'author' not in data:
            return jsonify({'error': 'Title and author are required fields'}), 400

        title = data['title']
        author = data['author']

        if not title or not author:
            return jsonify({'error': 'Title and author cannot be empty'}), 400

        if len(title) > 100:
            return jsonify({'error': 'Title must be 100 characters or less'}), 400

        if len(author) > 50:
            return jsonify({'error': 'Author must be 50 characters or less'}), 400

        # Check if a book with the same title and author already exists
        response = supabase_client.from_('books').select('*').eq('title', title).eq('author', author).execute()
        existing_book = response.data

        if existing_book:
            return jsonify({'error': 'Book already exists'}), 409  # Conflict status code

        # Insert a new book into the Supabase database
        new_book_data = {'title': title, 'author': author}
        response = supabase_client.from_('books').insert([new_book_data]).execute()
        return jsonify({'success' : 'Book added'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

   
# Endpoint 3: Update a Book
@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    try:
        data = request.get_json()

        # Validate request payload
        if 'title' not in data or 'author' not in data:
            return jsonify({'error': 'Title and author are required fields'}), 400

        title = data['title']
        author = data['author']

        # Use Supabase to update the book in the database
        response = supabase_client.from_('books').upsert([{'id': id, 'title': title, 'author': author}], returning='representation').execute()
        return jsonify({'success' : 'Book updated'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
