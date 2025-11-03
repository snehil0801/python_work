"""
Selection Sort Algorithm Implementation
Two"""

def findMinInList(list):
    """Returns the minimum values in a list"""
    n=len(list)
    min=list[0]
    pos = 0
    for i in range(n):
        if list[i] < min:
            pos = i
            min = list[i]
        else:
            continue
    return min,pos
def selecionSort(list):
    list2 = []
    min,pos = 0,0
    for i in range(len(list)):
        min,pos = findMinInList(list)
        list2.append(min)
        del list[pos]
    print(list2)

L=[5,3,6,2,10,1,4,8,7]
L1=[2,-4,-1,-1,3,5,6,10,23,-23]
selecionSort(L1)
