class Library:
    def __init__(self):
        self.file1 = open("books.txt", "a+")

    def __del__(self):
        self.file1.close()

    def list_books(self):
        self.file1.seek(0)
        books = self.file1.read().splitlines()
        new_list = []
        for book in books:
            book_info = book.split(",")
            ins = book_info[0], book_info[1]
            new_list.append(ins)
        print(new_list)

    def add_book(self):
        name = input("Please write the name of the book:")
        author = input("Please write the author of the book:")
        release_date = input("Please write the release date of the book:")
        number_of_pages = input("Please write the number of pages of the book:")
        new_book = f"{name},{author},{release_date},{number_of_pages}\n"
        self.file1.write(new_book)
        print("Process is successful")

    def remove_book(self):
        book_name_to_remove = input("Please type the name of the book you want to delete: ")
        lines = self.file1.readlines()
        self.file1.seek(0)
        for line in lines:
            if book_name_to_remove not in lines:
                self.file1 += line + '\n'
        self.file1.truncate()
        print("Process is successful")

lib = Library()

while True:
    choice = input("""***** Please Select Your Request *****
    1- List All the Books
    2- Add a New Book
    3- Remove Book
    Q- Quit""")

    if choice == "1":
        lib.list_books()

    elif choice == "2":
        lib.add_book()

    elif choice == "3":
        lib.remove_book()

    elif choice.upper() == "Q":
        print("Exit is successful")
        break

    else:
        print("Please enter a valid value.")