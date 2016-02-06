__author__ = 'pavan'

"""program to find the largest among 3 numbers """

first_number = int(raw_input("enter the 1st number"))

second_number = int(raw_input("enter the 2nd number"))

third_number = int(raw_input("enter the 3rd number"))

if(first_number>second_number)and(first_number>third_number):
    print "first number is greater"
if(second_number>first_number)and(second_number>third_number):
    print "second number is greater"
if(third_number>first_number)and(third_number>first_number):
    print "third number is greater"