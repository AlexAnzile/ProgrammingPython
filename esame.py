class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):
        time_series = []

        try:
            my_file = open(self.name, 'r') #leggo il file
        except:
            raise ExamException('Errore apertura file non riuscita') #se non viene letto alzo un eccezione
            
        if(my_file.readline() == ''):        #controllo se il file è vuoto
            raise ExamException('File vuoto') #se il file è vuoto alzo un eccezione

        for line in my_file:
            elements = line.strip('\n').split(',')  #divido la riga tra la data e i passeggeri quindi divido in due la riga dopo la virgola

            if elements[0] != 'date':   #controllo se il primo elemento è diverso da date
                try:
                    date_division = elements[0].split('-') #divido l'anno dal mese
                    
                    date_division[0] = int(date_division[0]) #converto in int i mesi e gli anni
                    date_division[1] = int(date_division[1])
                except:
                    continue

                if not isinstance(date_division[0], int): #controllo se un il valore dell'anno è un int altrimenti continuo
                    continue
                
                if not isinstance(date_division[1], int): #controllo se un il valore del mese è un int altrimenti continuo
                    continue
                    
                if not 1 <= date_division[1] <= 12: #controllo che il valore vada da 0 a 12 altrimenti continuo
                    continue
                            
                    last_time_series = time_series[-1]#viene impostata una variabile uguale all'ultimo valore della time_series 
                    if elements[0] == last_time_series[0]:       #confronto gli elementi per vedere se sono presenti duplicati
                        raise ExamException('Due date combaciano')  #se sono presenti due date uguali alzo un'eccezione            
               
                                                  
                    last_year = int(time_series[-1][0].split('-')[0]) #viene associato a una variabile l'ultimo della lista fino a questo momento valore dell'anno trasformato in int
                    current_year = int(date_division[0]) #la variabile current_year viene associata a l'anno scelto
                    if current_year < last_year:   #si controlla che l'anno corrente sia minore di last years
                        raise ExamException('Gli anni non sono in ordine') #se il controllo va a buonfine viene alzata un'eccezione
                   
                
                
                    last_date = time_series[-1][0]   #una variabile viene impostata come l'ultimo valore data della lista fino a questo momento
                    last_year, last_month = map(int, last_date.split('-'))  #vado ad associare il valore int dell'anno a last year e dell mese a last moth
                    current_year, current_month = map(int, date_division[:2]) #vado ad assegnare a current year il valore dell'anno trasformato in int e faccio la stessa cosa con con il mese
                    if current_year == last_year and current_month < last_month: #controllo che l'anno precedente sia lo stesso e che il mese corrente sia minore dell'mese precedente 
                        raise ExamException('I mesi non sono in ordine') # se il controllo va a buon fine alzo un ecezzione

                try:
                    elements[1] = int(elements[1])    #trasformo il valore dei passeggeri in un valore int
                except:
                    continue                          #se non avviene la conversione vado avanti  
                    
                if (elements[1] < 0):                 #controllo che il valore dei passeggeri sia minore di 0 se è così vado avanti
                    continue
                    
                time_series.append(elements) #aggiungio a time_series l'elemento 
        
        my_file.close()  #chiudo il file
        return time_series  #ritorno la lista time_series

                    
def detect_similar_monthly_variations(time_series, years):
    try:
        controllo_1=int(years[0])    #converto il primo anno in int 
        controllo_2=int(years[1])    #converto il secondo anno in int
    except:
        raise ExamException('Il valore inserito non è un numero')
        
    if abs(controllo_2-controllo_1) >1 or controllo_2-controllo_1 == 0:  #controllo che sia due anni successivi 
        raise ExamException('Anni non successivi')                  #alzo un eccezione se non lo sono 
    
    primo_anno=[None]*12                       # Crea una lista di 12 elementi inizializzati a None  
    secondo_anno=[None]*12                     # Crea una lista di 12 elementi inizializzati a None
    anno_presente_1 = False                    #Creo una Flag per vedere se l'anno è presente
    anno_presente_2 = False                    #Creo una Flag per vedere se l'anno è presente
    
    for item in time_series:
        item[0]=item[0].split('-')            #Vado a dividere l'anno dalla mese               
        
        if item[0][0] == years[0]:            #Controllo se l'anno è uguale all'anno selezionato
            mese = int(item[0][1])            #Associo il mese ad una variabile                  
            primo_anno[mese-1] = int(item[1]) #Vado ad inserire all'interno della lista primo anno il valore dei passeggeri 
            anno_presente_1 = True            #La flag viene messa a TRUE se viene trovato l'anno
            
        if item[0][0] == years[1]:
            mese = int(item[0][1])               
            secondo_anno[mese-1] = int(item[1])  
            anno_presente_2 = True

    if not anno_presente_1 or not anno_presente_2: #Se non viene trovato uno dei due anni viene alzata un eccezione
        raise ExamException('Anno non presente')
        
    variazione_primo_anno=[]                  #creo una lista per a variazione dei passeggeri del primo anno
    variazione_secondo_anno=[]                #creo una lista per a variazione dei passeggeri del secondo anno
    
    for i in range(1,12):
        try:
            variazione_primo_anno.append(primo_anno[i]-primo_anno[i-1]) #vado ad aggiungere ad per il primo anno la varizione di passeggeri per ogni coppia di mesi
        except:
            variazione_primo_anno.append(None) #se la sottrazione non viene eseguita viene aggiuto None 
    for i in range(1,12):            
        try:
            variazione_secondo_anno.append(secondo_anno[i]-secondo_anno[i-1])#vado ad aggiungere ad per il secondo anno la varizione di passeggeri per ogni coppia di mesi  
        except:
           variazione_secondo_anno.append(None)  #se la sottrazione non viene eseguita viene aggiuto None 
            
    differenza = []    #creo una lista per la differenza tra la variazione di due mesi da un anno all'altro
    lista_finale = []  #creo la lista finale che conterrà True o False in base a al risultato della differenza
   
    for i in range(0,11):
        try:
            differenza = abs(abs(variazione_secondo_anno[i])-abs(variazione_primo_anno[i]))  #calcolo differenza tra le variazioni
            if  differenza <= 2:                     #controllo se il valore per ogni coppia di mesi è minore o uguale a due  
                lista_finale.append(True)            #se il controllo è verificato aggiungo True        
            else:
                lista_finale.append(False)           #altrimenti aggiungo False 
        except:
            lista_finale.append(False)               #se non riesce a fare il cacolo aggiunge False
       
    
    return lista_finale                              #ritorno il la lista finale composta da true o false
