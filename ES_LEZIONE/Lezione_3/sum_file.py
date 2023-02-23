def sum_csv(file_name):
    
    my_file=open(file_name,'r')

    s=0
    
    if my_file==[]:
        return None
    
    for line in my_file:
        elements=line.split(',')
        if elements[0]!='Date':
            try:
                value=float(elements[1])
                s = s + value
            except:
                value = None
    if s==0:
        return None

    return s
            





 