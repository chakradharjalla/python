__author__ = 'pavan'

if __name__ == '__main__':

    digit = str(raw_input("enter the number :"))

    y = 0
    for ch in digit:
        number = int(ch)
        x = number*2
        print x
        y +=x
    print ("the number you have entered got squared by each digit: "), y
    if y >10:
        sum = 1+ y % 10
    else:
        sum = y

    print ("the number you have entered got squared by each digit: "), sum
