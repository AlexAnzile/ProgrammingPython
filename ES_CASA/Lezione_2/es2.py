def sum_list(my_list):
    s=0
    if my_list == []:
        return None
    for item in my_list:
        s=s+item
    return s