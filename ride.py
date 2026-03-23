x=input("enter your choice B for bike and C for car")
if x=="B":
    print("you have chosen bike")
    y=input("choose your bike if you want splender or R15")
    if y=="splender":
        print("you have chosen splender")
    elif y=="R15":
        print("you have chosen R15")
    else:
        print("you have chosen some other bike")
elif x=="C":
    print("you have chosen car")
    z=input("choose your car if you want hondacity or thar")
    if z=="hondacity":
        print("you have chosen honda city")
    elif z=="thar":
        print("you have chosen thar")
    else:
        print("you have chosen some other car")
else:
    print("invalid content")


