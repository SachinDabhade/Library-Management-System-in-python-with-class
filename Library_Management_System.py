# ----------------------------------------library made by SACHIN DABHADE--------------------------------------------------

# Importing Libraries
from datetime import datetime

# Class for the mini project
class Library:
    # This is the doc sentence
    """ This class is mainly work as a library which can be give us books from the library which we add here. Also this is efficient library code as per me...! """

    # Initializing the variable through __init__()
    def __init__(self, library_name, booklist):
        self.username = library_name
        self.booklist = booklist
        self.lend = {}

    # Display the information of books and the librery 
    def details(self):
        print(f"The name of library is {self.username} and the books are {self.booklist}")

    # This will display the books in library
    def display_books(self):
        print(f"\nWe have the following books in the library: {self.username} \n")
        for books in self.booklist:
            print(books)
    
    # The lending process is handel by this function
    def lend_book(self):
        a = input("Please enter your name:")
        b = input("Please enter the book that you want to lend:")
        if b.capitalize() not in self.booklist:
            print("Sorry... The book is not available at this movement...")
        elif b.capitalize() not in self.lend.values():
            self.lend.update({a.capitalize(): b.capitalize()})
            print(f"The book {b.capitalize()} is successfully given to {a.capitalize()}...!")
            with open("record.txt", "a") as f:
                f.write(f"The book: {b.capitalize()} is added by {a.capitalize()} on {datetime.now()}\n")
        else:
            print(f"The books are already using by {self.lend}")
    
    # The returning of book is done by this process
    def return_book(self):
        a = input("Hello Sir...! Please enter your name:")
        b = input("Please enter the book that you want to return:")
        if b.capitalize() not in self.booklist:
            print("Invalid input...!")
        elif b.capitalize() in self.lend.values():
            self.lend.clear()
            print(f"Thanks You..! Your book: {b.capitalize()} is successfully returned to the database of {self.username} ")
            with open("record.txt", "a") as f:
                f.write(f"The book: {b.capitalize()} is added by {a.capitalize()} on {datetime.now()}\n")
        else:
            print(f"Sorry... The book: {b.capitalize()} is not given to any of the user...! please try again...!")
    
    # This will add of book in library 
    def add_book(self):
        a = input("Please enter your name:")
        book = input(f"Enter the book you want to add in {x.capitalize()}'s' library:")
        if book.capitalize() not in self.booklist:
            self.booklist.append(book.capitalize())
            print(f"The Book: {book.capitalize()} is successfully added to the database of {self.username}'s")
            with open("record.txt", "a") as f:
                f.write(f"The book: {book.capitalize()} is added by {a.capitalize()} on {datetime.now()}\n")
        else:
            print(f"Sorry...! The book already in the Library: {self.username}")

    # Loop for continuing game
    @staticmethod
    def play_loop():
        play_game = input("\n\nEnter any key to continue or \"Q\" to quit: ")
        while True:
            if play_game.capitalize() == "Q":
                print("Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
                exit()
            break


if __name__ == '__main__':
    
    # Add library here, this are the libraries of our program
    Sachin = Library("Sachin", ["Python", "C++", "Java", "Javascript", "C#"])
    Vaibhav = Library("Vaibhav", ["Javascript", "C#"])
    library = ["Sachin", "Vaibhav"]
    print(
        "\n\n---------------------------------Welcome to the book library made by Sachin Dabhade---------------------------------\n")
    
    # Add library here..
    print(f"The library's are:{library}")
    x = input("\nHello Sir...! Please enter the library name:")

    while True:
        # edit int for new function
        int = ["1", "2", "3", "4", "Q"]
        order = input("\n\n1: Display book \n2: Lend book \n3: Return book \n4: Add book \n\nEnter your choice:")

        # Checking is order in Integer
        if order.capitalize() in int:
        
            if order == "1":  # Required elif statement for new library
                if x.capitalize() == "Sachin":
                    Sachin.display_books()
                elif x.capitalize() == "Vaibhav":
                    Vaibhav.display_books()
                else:
                    print("Invalid input...! Please enter a valid option...!")
        
            elif order == "2":  # Required elif statement for new library
                if x.capitalize() == "Vaibhav":
                    Vaibhav.lend_book()
                elif x.capitalize() == "Sachin":
                    Sachin.lend_book()
                else:
                    print("Invalid input...! Please enter a valid option...!")
        
            elif order == "3":  # Required elif statement for new library
                if x.capitalize() == "Vaibhav":
                    Vaibhav.return_book()
                elif x.capitalize() == "Sachin":
                    Sachin.return_book()
                else:
                    print("Invalid input...! Please enter a valid option...!")
        
            elif order == "4":  # Required elif statement for new library
                if x.capitalize() == "Vaibhav":
                    Vaibhav.add_book()
                elif x.capitalize() == "Sachin":
                    Sachin.add_book()
                else:
                    print("Invalid input...! Please enter a valid option...!")
        
        else:
            print("Invalid input...! Please enter a valid option...!")
        
        Library.play_loop()
        continue
