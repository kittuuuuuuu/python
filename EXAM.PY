x=input("enter y if you are ill else enter n if you are not ill")
if x=="y":
    print("you are eligible for examination")
else:
    z=int(input("enter thr attendence"))
    if z>=75:
        print("you are eligible for examination")
    else:
        print("you are not eligible for examination")