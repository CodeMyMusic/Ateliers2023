import math

def longueur(lst: list)-> int:
    if lst:
        lst.pop(0)
        length = 1 + longueur(lst)
    else:
        length = 0
    
    return length

# print(longueur([1, 2, 3, 5, 7]))


def findMin(lst : list)-> int:
    if lst:
        minVal = lst.pop(0)
        minVal_lst_recursive = findMin(lst)
        if minVal > minVal_lst_recursive:
            minVal = minVal_lst_recursive
    else:
        minVal = math.inf
    return minVal

# print(findMin([115155, 500000, 100000, 51888, 51889]))

def listPairs(lst: list)-> list:
    if lst:
        elmt = lst[0]
        if elmt % 2 == 1:
            lst.pop(0)
            pair_list = []
        else:
            pair_list = [lst.pop(0)]
        for elmt in listPairs(lst):
            pair_list.append(elmt)
    else:
        pair_list = []
        
    return pair_list

# print(listPairs([0, 1, 2, 3, 4, 5, 6, 7, 8]))

def concat_list(lst: list)-> list:
    if lst:
        deb = lst.pop(-1)
        lst_deconcated = concat_list(lst)
        for elmt in deb:
            lst_deconcated.append(elmt)
    else:
        lst_deconcated = []
        
    return lst_deconcated

print(concat_list([[0, 1], [2, 3], [4], [6, 7]]))