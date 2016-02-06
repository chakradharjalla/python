__author__ = 'pavan'
"""this program prints all  the prime numbers withing that range"""



lower_range=int(raw_input("enter the lower range number :"))

upper_range=int(raw_input("enter the upper  range number :"))

for num in range (lower_range,upper_range+1):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)





