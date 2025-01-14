#Practice2

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Indicates whether the book is available for lending

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List of books borrowed by the member

    def __str__(self):
        return f"Member {self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []  # List of books in the library
        self.members = []  # List of registered members

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member registered: {member}")

    def lend_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{book} has been lent to {member.name}")
        else:
            print(f"Sorry, {book} is not available for lending")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{book} has been returned by {member.name}")
        else:
            print(f"{member.name} did not borrow {book}")


# Example usage:
if __name__ == "__main__":
    # Create books
    book1 = Book("Dracula", "Bram Stoker")
    book2 = Book("The Antique Collector Guide", "London Publishing HOuse")

    # Create members
    member1 = Member("Hazel", 101)
    member2 = Member("Brynn", 102)

    # Create library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Register members
    library.register_member(member1)
    library.register_member(member2)

    # Test lending and returning books
    library.lend_book(book1, member1)  # Lending book1 to member1
    library.lend_book(book2, member2)  # Lending book2 to member2
    library.return_book(book1, member1)  # Returning book1 by member1
    library.return_book(book2, member1)  # This should fail as book2 was not borrowed by member1

    #Terminal Output:
    Running] python -u "g:\My Drive\Software Engineering with AI\Build a Library System Exercise\tempCodeRunnerFile.python"
Book added: 'Dracula' by Bram Stoker
Book added: 'The Antique Collector Guide' by London Publishing HOuse
Member registered: Member Hazel (ID: 101)
Member registered: Member Brynn (ID: 102)
'Dracula' by Bram Stoker has been lent to Hazel
'The Antique Collector Guide' by London Publishing HOuse has been lent to Brynn
'Dracula' by Bram Stoker has been returned by Hazel
Hazel did not borrow 'The Antique Collector Guide' by London Publishing HOuse

[Done] exited with code=0 in 0.224 seconds