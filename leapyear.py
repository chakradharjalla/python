"""In general terms the algorithm for calculating a leap year is as follows...

A year will be a leap year if it is divisible by 4 but not by 100. If a year is divisible by 4 and by 100, it is not a leap year unless it is also divisible by 400."""

year = int(raw_input("enter the year :"))

if (year % 4) == 0:
	if (year % 100) == 0:
		if(year % 400) == 0:
			print "yes it is a leap year"
		else:
			print "it is not a leap year"

	else:
		print"it is a leap year"

		
else:
	print"it is not a leap year."