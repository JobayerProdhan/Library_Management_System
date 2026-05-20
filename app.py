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
    
    def find_student(self,id): 
        for s in self.students: 
            if s.student_id == id:
                return s 
            return None
    
    def issue_books(self,isbn,id):
        book = self.find_book(isbn)
        student = self.find_student(id)
        
        if not book: 
            print('Book not found!!')
        
        if not student :
            print('Student not found!!!')
        
        if book.is_available:
            book.is_available = False 
            student.issued_books.append(book)
            print('Books issued')
        else:
            print('Book already issued!')
                
    def return_book(self,isbn,id):
        student = self.find_student(id)
        
        if not student:
            print('Student not found')
        
        for book in student.issued_books:
            if book.isbn ==   True
            student.issued_books.remove(book)
            print('Book Returned!')
            return 
        
        print('Book not found in issued list.')
    
    def show_student_books(self,id):
        student = self.find_student(id)
        if  not student:
            print('Student not found')
            return 
        
        print(f'\n Books issued to {student.name}:')
        if not student.issued_books:
            print('No books issued')
        for b in student.issued_books:
            print(b)  
            
    
                 


        
        