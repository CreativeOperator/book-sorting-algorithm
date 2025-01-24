# Algorithm Implementation

def book_sort(books):
    # Sample implementation of a book-sorting algorithm
    sorted_books = sorted(books, key=lambda x: (x['author'], x['title']))
    return sorted_books

# Example usage
books = [
    {'title': 'Book A', 'author': 'Author X'},
    {'title': 'Book B', 'author': 'Author Y'},
    {'title': 'Book C', 'author': 'Author X'},
]

sorted_books = book_sort(books)
print(sorted_books)
