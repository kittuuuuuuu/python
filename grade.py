a=int(input("enter marks of maths"))
b=int(input('enter marks of english'))
c=int(input('enter marks of chemistry'))
d=int(input('enter marks of physics'))
e=int(input('enter marks of computer science'))
x=(a+b+c+d+e)/5
print("average of students mars is",x)
if x>=91 and x<100:
    print("the grade of  student is A")
elif x>=81 and x<=90:
    print("the grade of student is B")
elif x>=71 and x<=80:
    print("the grade of student is C")
else:
    print("the grade of student is D")
