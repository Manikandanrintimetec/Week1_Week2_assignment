import pickle


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_lent = False 
    def __str__(self):
        status = "Available" if not self.is_lent else "Lent out"
        return f"{self.book_id}: {self.title} by {self.author} ({status})"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.borrowed_books = [] 

    def __str__(self):
        return f"{self.student_id}: {self.name}"


class Library:
    def __init__(self):
        self.books = self.load_data("books.pkl") 
        self.students = self.load_data("students.pkl") 


    def save_data(self, data, filename):
        with open(filename, "wb") as f:
            pickle.dump(data, f)

    def load_data(self, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return [] 

    def add_book(self, book):
        self.books.append(book)
        self.save_data(self.books, "books.pkl")
        print(f"Book '{book.title}' added successfully!")

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_data(self.books, "books.pkl")
                print(f"Book '{book.title}' deleted successfully!")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Available Books:")
        for book in self.books:
            print(book)

    def add_student(self, student):
        self.students.append(student)
        self.save_data(self.students, "students.pkl")
        print(f"Student '{student.name}' added successfully!")

    def display_students(self):
        if not self.students:
            print("No students registered.")
            return
        print("Registered Students:")
        for student in self.students:
            print(student)

    def lend_book(self, student_id, book_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not student:
            print("Student not found.")
            return
        if not book:
            print("Book not found.")
            return
        if book.is_lent:
            print(f"Book '{book.title}' is already lent out.")
            return

        book.is_lent = True
        student.borrowed_books.append(book.book_id)
        self.save_data(self.books, "books.pkl")
        self.save_data(self.students, "students.pkl")
        print(f"Book '{book.title}' lent to {student.name} successfully!")

    def receive_book(self, student_id, book_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not student or book_id not in student.borrowed_books:
            print("This book was not borrowed by the student.")
            return

        book.is_lent = False
        student.borrowed_books.remove(book_id)
        self.save_data(self.books, "books.pkl")
        self.save_data(self.students, "students.pkl")
        print(f"Book '{book.title}' returned successfully!")

def main():
    library = Library()

    while True:
        print("**University Library**")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Delete a book")
        print("4. Display students")
        print("5. Add a student")
        print("6. Lend a book")
        print("7. Receive a book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(Book(book_id, title, author))
        elif choice == "3":
            book_id = input("Enter book ID to delete: ")
            library.delete_book(book_id)
        elif choice == "4":
            library.display_students()
        elif choice == "5":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            library.add_student(Student(student_id, name))
        elif choice == "6":
            student_id = input("Enter student ID: ")
            book_id = input("Enter book ID to lend: ")
            library.lend_book(student_id, book_id)
        elif choice == "7":
            student_id = input("Enter student ID: ")
            book_id = input("Enter book ID to receive: ")
            library.receive_book(student_id, book_id)
        elif choice == "0":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()