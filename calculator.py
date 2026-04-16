def calculator(a,b,operator):
    if operator=="+":
        return(a+b)
    elif operator=="-":
        return(a-b)
    elif operator=='*':
        return(a*b)
    else:
        return(a/b) 
a=int(input("enter a value of a"))
b=int(input("enter a value of b"))
operator=input("enter a operator")
print(calculator(a,b,operator))
