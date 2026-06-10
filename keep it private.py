class myclass:
    __privatevariable=1
    def __privatemeth(self):
        print("i am inside class")
    def hello(self):
        print("private variable is value is", myclass.__privatevariable)
foo=myclass()
foo.hello()
foo.__privatemeth()