__author__ = 'pavan'


a = int(raw_input("enter the number"))

if (a == 0) or (a == 1) :
    print 'zero and one is neither prime  nor composite '
if a > 1:
    for n in range (2,a):
        if (a % n) == 0:
            print "it is a composite number"
            print (n, "times",a//n,"is",a)
            break

    else:
        print (a,"is a prime number")

else:
   print(a,"is not a prime number")

