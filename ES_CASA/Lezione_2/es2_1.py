my_list=[1,2,3,4]

def sum_list(my_list):
    r=0
    if my_list == []:
        return None
        
    for item in my_list:
        r = r + item
        
    print("La somma è: {}".format(r))
    return r
    

    