class bookclass():
    def __init__(self,title,author,is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self):
        self.is_borrowed=True
        print("you have bowrroed the book",self.title)
    def return_book(self):
        self.is_borrowed=False
        print("you have to return the book",self.title)
a=bookclass("statistics","dp morgan",False)
b=bookclass("accounts","xyz",False)
c=bookclass("english","zye",False)
a.borrow()
a.return_book()
b.borrow()
b.return_book()
c.borrow()
c.return_book()

