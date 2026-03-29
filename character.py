z=input("enter a name")
character=input("enter a character")
count=0
i=0
while i<len(z):
    if (z[i]==character):
        count=count+1
    i=i+1
print("the numebr of times the character occurs is equal to",count)
    