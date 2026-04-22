try:
    number=int(input("enter a number"))
    print("the enterred number is", number)
except ValueError as ex:
    print("exception:", ex)