a=int(input("enter a lower range"))
b=int(input("enter a upper range"))
for num in range(a,b+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print("this is a prime number", num)
