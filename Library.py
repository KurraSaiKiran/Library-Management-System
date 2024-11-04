from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def addBook(self, title):
        # Adds a new book if it doesn't exist in the library
        if title not in self.books:
            self.books[title] = {'available': True, 'borrowed_by': None, 'due_date': None}
            print(f"Book '{title}' added to the library.")
        else:
            print(f"Book '{title}' already exists in the library.")

    def showBooks(self):
        # Displays all books with availability status
        print(f"The Library has {len(self.books)} books. The books are:")
        for title, details in self.books.items():
            status = "Available" if details['available'] else f"Borrowed by {details['borrowed_by']} (Due on {details['due_date']})"
            print(f"{title} - {status}")

    def addUser(self, user_id, user_name):
        # Adds a new user to the library
        if user_id not in self.users:
            self.users[user_id] = {'name': user_name, 'borrowed_books': []}
            print(f"User '{user_name}' added to the system.")
        else:
            print(f"User ID '{user_id}' already exists.")

    def borrowBook(self, title, user_id):
        # Allows a user to borrow a book if available
        if user_id not in self.users:
            print("User not registered.")
            return
        
        if title in self.books:
            if self.books[title]['available']:
                self.books[title]['available'] = False
                self.books[title]['borrowed_by'] = user_id
                due_date = datetime.now() + timedelta(days=7)  # 7 days borrowing period
                self.books[title]['due_date'] = due_date.strftime("%Y-%m-%d")
                self.users[user_id]['borrowed_books'].append(title)
                print(f"Book '{title}' borrowed by {self.users[user_id]['name']}. Due on {self.books[title]['due_date']}.")
            else:
                print(f"Book '{title}' is currently borrowed by {self.books[title]['borrowed_by']}.")
        else:
            print(f"Book '{title}' not found in the library.")

    def returnBook(self, title, user_id):
        # Allows a user to return a borrowed book
        if title in self.books and not self.books[title]['available'] and self.books[title]['borrowed_by'] == user_id:
            self.books[title]['available'] = True
            self.books[title]['borrowed_by'] = None
            self.books[title]['due_date'] = None
            self.users[user_id]['borrowed_books'].remove(title)
            print(f"Book '{title}' returned by {self.users[user_id]['name']}.")
        else:
            print(f"Return failed: '{title}' not borrowed by user {user_id} or book not found.")

    def calculateFine(self, title):
        # Calculates fine if book is overdue
        if title in self.books and not self.books[title]['available']:
            due_date = datetime.strptime(self.books[title]['due_date'], "%Y-%m-%d")
            days_overdue = (datetime.now() - due_date).days
            if days_overdue > 0:
                fine = days_overdue * 5  # 5 units fine per day overdue
                print(f"Book '{title}' is overdue by {days_overdue} days. Fine: {fine} units.")
            else:
                print(f"Book '{title}' is not overdue.")
        else:
            print(f"Book '{title}' is either not borrowed or does not exist in the library.")

# Example usage
library = Library()

# Adding books
library.addBook("Treasure Island")
library.addBook("Romeo and Juliet")
library.addBook("The Merchant of Venice")
library.addBook("The Great Gatsby")
library.addBook("Wealth of Nations")
library.addBook("Origin of Species")

# Showing books
library.showBooks()

# Adding users
library.addUser("U001", "Alice")
library.addUser("U002", "Bob")

# Borrowing books
library.borrowBook("The Great Gatsby", "U001")
library.borrowBook("Romeo and Juliet", "U002")

# Showing updated book list
library.showBooks()

# Returning a book
library.returnBook("The Great Gatsby", "U001")

# Showing final book list
library.showBooks()

# Checking fines
library.calculateFine("Romeo and Juliet")
