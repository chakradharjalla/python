__author__ = 'pavan'

a = input("enter the number  --- > ")
fact = 1

if (a < 0):
    print ("factorial does not exit for negative numbers")
elif (a == 0) or (a == 1):
    print ("factorial is 1")
else:
    for i in range (1,a+1):
        fact = fact *i
    print ("the factorial of number is : "),fact
