a=int(input('enter the speed of a'))
b=int(input("enter the speed of b"))
c=int(input("enter the pseed of c"))
avg=(a+b+c)/3
if avg>a and avg>b and avg>c:
    print("avg speed is greater than the three",avg,a,b,c)
elif avg>a and avg>b:
    print("the avg speed is greater than the two",avg,a,b)
elif avg>a and avg>c:
    print("the avg speed is greater than the two", avg,a,c)
elif avg>b and avg>c:
    print("the avg speed is greater than the two",avg,b,c)
elif avg>a:
    print("the avg is greater than 1",avg,a)
elif avg>b:
    print("the avg is greater than 1",avg,b)
elif avg>c:
    print("the avg is greater than 1",avg,c)
else:
    print("average speed is not greater than any one of them")