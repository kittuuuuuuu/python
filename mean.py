mean1=int(input("enter mean of the observations"))
wrongnumber=int(input("enter a wrong number"))
rightnumber=int(input("enter a right number"))
totalnumbers=int(input("enter the total number of observations"))
sum=mean1*totalnumbers
print("the sum is", sum)
sum2=sum-wrongnumber+rightnumber
mean2=sum2/totalnumbers
print("the correct mean is",mean2)