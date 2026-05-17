a=[2,4,6,8]
b=["kritika","malika","seema","ravinder"]
result=zip(a,b)
print(list(result))

a=[3,4,6,7]
b=[5,7,8,0]
for i,j in zip(a,b[::-1]):
    print(i,j)