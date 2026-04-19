n=int(input("enter a number"))
for i in range(n,0,-1):
    if i==5:
        continue
    else:
        print("the current value is",i)
print("good bye")