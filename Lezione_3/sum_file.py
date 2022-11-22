values = []

def sum_csv(file_name):
    
    my_file=open('shampoo_sales.csv','r')
    for line in my_file:
        elements=line.split(',')

        if elements[0]!='Date':
            value = elements[1]
            value_float = float(value)
            values.append(value_float)
            s=0
            for item in values:
                s=s+item
            print (s)
            
sum_csv(values)   




 