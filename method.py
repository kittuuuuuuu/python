class IOSstring:
    def __init__(self):
        self.str=""
    def kritika(self):
        self.str=input("enter a string")
    def print_str(self):
        print(self.str.upper())
s=IOSstring()
s.kritika()
s.print_str()