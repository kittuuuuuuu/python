class bird:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def display(self):
        print(self.name)
        print(self.colour)
class penguin(bird):
    def __init__(self,name,colour,age):
        self.age=age
        super().__init__(name,colour)
a=penguin("kritika","black",4)
a.display()
print(a.age)