import math
__author__ = 'pavan'


"""binary to decimal number program"""
def bin_dec(int,power):
    z = p * pow(2,power)
    return z


if __name__ == '__main__':
    x = int(raw_input("enter the binary number :"))
list_of_ints = [int(i) for i in str(x)]

print "the entred value is ",x
print "after converting them to seperate integeres " , list_of_ints


for p in list_of_ints:
    print p
    power = -1
    power +=1
    print power
    roger = bin_dec(p,power)
    print roger