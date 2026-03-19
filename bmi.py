a=float(input('enter height of a person'))
b=float(input("enter weight of a person"))
bmi=b/(a/100)**2
print('bmi of a person',bmi)
if bmi<=18.4:
    print("the person is underweight")
elif bmi<=24.9:
    print("ther perosn is healthy")
elif bmi<=29.9:
    print("the person is overweight")
elif bmi<=34.9:
    print("the person is severely overwweight")
elif bmi<=39.9:
    print("the person is obese")
else:
    print("the person is severly obsese")

