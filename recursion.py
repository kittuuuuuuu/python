def factorial(x):
    """This is factorial program"""
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
n=int(input("enter a number"))   
print(factorial(n))
print(factorial.__doc__)
