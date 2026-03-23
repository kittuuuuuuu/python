x=int(input("enter no of electrical units consumed"))
if x<=50:
    print("you have to pay",x*2.60+25)
elif x>50 and x<100:
    print("you have yo pay",x*3.25+35)
elif x>=100 and x<200:
    print("you have to pay",x*5.26+45)
else:
    print("you have to pay",x*8.45+75)
