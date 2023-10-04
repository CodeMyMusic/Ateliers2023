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

def concat_list_corr(lst: list)-> list:
    if not list:
        return []
    else:
        return lst[0] + concat_list_corr(lst[1:])
    

def concat_list_corr2(lst: list, res=[])-> list:
    if not list:
        return res
    else:
        res += lst[0]
    return concat_list_corr2(lst, res)

print(concat_list_corr([[0, 1], [2, 3], [4], [6, 7]]))

# séparer une liste en deux (une paire une impaire)
def separe(lst: list)-> (list, list):
    if lst == []:
        return ([], [])
    else:
        pile = separe(lst[1:])
        if lst[0]%2 == 0:
            pile[1].append(lst[0])
        else:
            pile[0].append(lst[1])
        return pile

# def incluse(lst_1 : list, lst_2: list)-> bool:
#     """Vérifie que les éléments de la première liste
#     sont tous présents dans la deuxième

#     Args:
#         lst_1 (list): _description_
#         lst_2 (list): _description_

#     Returns:
#         bool: _description_
#     """
#     incluse = True
#     if (lst_1[0] == lst_2[0]):
