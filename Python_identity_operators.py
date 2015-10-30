__author__ = 'pavan'
"""Identity operators compare the memory locations of two objects. There are two Identity operators as explained below"""

a = 45
b = 45

if (a is b):
    print'a and b have same identity'
else:
    print "a and b does not have same identitity"
if(id(a)==id(b)):
    print 'a and b have same identity'
else:
    print"a and b does not have same identity"

if(a is not b ):
    print"a and b do not have same identity"
else:
    print"a and b have same identity"

b = 30
if(id(a)==id(b)):
    print 'a and b have same identity'
else:
    print"a and b does not have same identity"

if(a is not b ):
    print"a and b do not have same identity"
else:
    print"a and b have same identity"
