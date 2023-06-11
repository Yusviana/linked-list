class Node:
    def __init__(self, visitor_name, book_name):
        self.visitor_name = visitor_name
        self.book_name = book_name
        self.next = None

class Library:
    def __init__(self):
        self.head = None

    def add_record(self, visitor_name, book_name):
        new_record = Node(visitor_name, book_name)
        if self.head is None:
            self.head = new_record
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_record

    def print_records(self):
        current = self.head
        while current:
            print("Visitor Name:", current.visitor_name)
            print("Book Name:", current.book_name)
            print("----------------------")
            current = current.next

# Contoh penggunaan program
library = Library()

# Menambahkan data peminjam
library.add_record("Rudi", "Harry Potter")
library.add_record("Sinta", "The Great Gatsby")
library.add_record("Budi", "To Kill a Mockingbird")
library.add_record("Rudi", "The Catcher in the Rye")

# Mencetak daftar buku yang dipinjam oleh setiap pengunjung
library.print_records()