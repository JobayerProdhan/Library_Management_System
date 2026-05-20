class Book: 
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author 
        self.isbn = isbn 
        self.is_available = True
    
    def __str__(self):
        if self.is_available == True:
            status = 'available'
        else:
            status = 'issued'
        
        return f'{self.title} by {self.author} [{status}]'


class Student: 
    def __init__(self,name ,student_id):
        self.name = name 
        self.student_id = student_id 
        self.issued_books = []
    
    def __str__(self):
        return f'{self.name} ({self.student_id})'

class Library: 
    def __init__(self):
        self.books = [] 
        self.students = [] 
    
    def add_book(self,book):
        self.books.append(book)
        print('Book Added!')
        
    def show_books(self): 
        if not self.books:
            print('No books available')
            return 
        for book in self.books: 
            print(book)
            
    def find_book(self,isbn):
        for b in self.books: 
            if b.isbn == isbn:
                return b 
        return None
    
    
    def add_student(self,student):
        self.students.append(student)
        print('Student added!')
    
                 


        
        