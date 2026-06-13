from abc import ABC,abstractmethod
class parent(ABC):
    def print(self,x):
        print("passed value",x)
    @abstractmethod
    def task(self):
        print("we are in parent class")
class test_class(parent):
    def task(self):
        print("we are in child class")
test_obj=test_class()
test_obj.task()
test_obj.print(90)

