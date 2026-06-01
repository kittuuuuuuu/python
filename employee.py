class person:
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
    def display(self):
        print(self.name)
        print(self.idno)
class employee(person):
    def __init__(self,name,idno,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idno)
a=employee("kritika",8890,40000,"Intern")
a.display()
print(a.salary,a.post)