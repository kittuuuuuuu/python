def cube(number):
    return number*number*number
def three_cube(number):
    if number%3==0:
        return cube(number)
    else:
        return False
number=int(input("enter a number"))
print(three_cube(number))
    