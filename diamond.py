n=int(input("enter a number"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for j in range(n-1):
    print(" "*(j+1)+'*'*(2*(n-j-1)-1))