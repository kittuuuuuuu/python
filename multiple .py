try:
    num1,num2=eval(input("enter two numbers, seperated by comma: "))
    result=num1/num2
    print("this is the result", result)
except ZeroDivisionError:
    print("this is zero division error")
except SyntaxError:
    print("this is syntax error")
except:
    print("Inavlid")
else:
    print("NO exceptions")
finally:
    print("this will run no matter what") 
