__author__ = 'pavan'


def isArrayInSortedOrder(A):
    #Base case
    if len(A) == 1:
        return True
    return A[0]<=A[1] and isArrayInSortedOrder(A[1:])
A=[1,2,3,4,5,6,7]
print(isArrayInSortedOrder(A))