# Python program to swap first and last element of a list
# Swap function
def swaplist(sl):
    n=len(sl)

    #swapping
    temp = sl[0]
    sl[0]=sl[n-1]
    sl[n-1]=temp

    return sl
l=[10,14,5,9,56,12]
print(l)
print("swapped list:",swaplist(l))