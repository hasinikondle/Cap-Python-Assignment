class LibraryBook:
    
    fine_per_day = 10
    
    def __init__(self, title, author, days_late=0):
        self.title = title
        self.author = author
        self.days_late = days_late
        self.is_issued = False
    
    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book Issued:", self.title)
        else:
            print("Already Issued")
    
    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print("Book Returned:", self.title)
        else:
            print("Book was not issued")
    
    def calculate_fine(self):
        fine = self.days_late * LibraryBook.fine_per_day
        print("Fine:", fine)
    
    @classmethod
    def update_fine_per_day(cls, new_fine):
        cls.fine_per_day = new_fine


book1 = LibraryBook("Python Basics", "Guido", 3)


book1.issue_book()
book1.calculate_fine()

print()


LibraryBook.update_fine_per_day(20)


book1.calculate_fine()

print()

book1.return_book()