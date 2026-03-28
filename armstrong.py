n=int(input("enter a number"))
sum=0
temp=n
while temp>0:
    r=temp%10
    sum=sum + r**3
    temp=temp//10
if sum==n:
    print("the number is armstrong")
else:
    print("the number is not armstrong")
