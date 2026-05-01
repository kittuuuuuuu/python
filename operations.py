import random
l=[]
n=int(input("enter number of elemenets in list"))
for i in range(n):
    l.append(random.randint(0,10))
print(l)
sum=0
for i in l:
    sum=sum+i
print(sum)
average=sum/len(l)
print(average)
print(l[0])
print(l[-1])