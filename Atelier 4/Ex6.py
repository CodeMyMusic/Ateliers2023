def sort_list(lst: list):
    len_lst = len(lst)
    rev_list = []
    len_lst_pair = len_lst - (len_lst % 2)
    len_moitie_lst = int(len_lst_pair / 2)
    for i in range(len_lst, 0):
        if lst[len_moitie_lst] > lst[len_lst]:
            
