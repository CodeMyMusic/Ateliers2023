import math

lst_test1 = [1.5, 12, 3, -4, 5, -1.7]

lst_test2 = [11, -9, 6, -1, -2, -3, 10]

def close_to_zero(nb_lst: list) -> float:
    """Renvoie le nombre le plus proche de 0 dans
    une liste

    Args:
        nb_lst (list): la liste de nombres

    Returns:
        float: le nombre le plus proche de zéro
    """
    val_min = nb_lst[0]

    len_nb_lst = len(nb_lst)
    for i in range(1, len_nb_lst):
        if abs(nb_lst[i]) < abs(val_min):
                val_min = nb_lst[i]
    return val_min


def main():
    print(close_to_zero(lst_test1))
    print(close_to_zero(lst_test2))

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()
