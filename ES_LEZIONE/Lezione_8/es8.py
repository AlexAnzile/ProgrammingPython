data = [50,52,60]

class Model():
 def fit(self, data):
     raise NotImplementedError('Metodo non implementato')

def predict(self, data):
     raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):
    
    def predict(self, data):
        w=0
        somma=0
        for item in data:
            if w>0:
                somma+=data[w]-data[w-1]
            w+=1
                
        if w<=1:
            return None
                
        media= somma/(w-1)
        prediction = media+data[-1]   
        return prediction 


m=IncrementModel()
print("Il risultato è:{}".format(m.predict(data)))
