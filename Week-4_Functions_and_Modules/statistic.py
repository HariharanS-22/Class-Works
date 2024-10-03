# Statistics Module

def mean(list1):
    return sum(list1)/len(list1)
def median(list1):
    list1.sort()
    n = len(list1)
    if n % 2 == 1:
        return list1[n//2]
    else:
        return (list1[(n//2) - 1] + list1[n//2])/2
def mode(list1):
    return max(list1 , key=list1.count)
    
