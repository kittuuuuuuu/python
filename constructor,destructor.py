class employee:
    def __init__(self):
        print("the employee is hired")
    def __del__(self):
        print("the employee is fired")
a=employee()
del a
print(a)