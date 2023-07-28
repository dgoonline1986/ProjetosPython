
import pandas as pd 

#import os

#os.path.isfile('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/Financeiro.xlsx')

#arquivo=os.listdir('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao')

df=pd.read_excel('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/Financeiro.xlsx')
 
df['Resultado']=''




   
class Funcs():
    
 def analisar(self,planilha=df):
     
    self.planilha=planilha
    print('capturado')
    #print(self.planilha)
    self.linhas=(len(self.planilha))
    print(f'Existem {self.linhas} de linhas')
        
    self.df2=[]
        
  
    i=0
    while i < self.linhas:     
        self.df2.append('Pago')
        i=i+1
            
    self.planilha['Resultado']=self.df2
    
    
    print(self.planilha)
    
    return self.planilha
    

class Aplication(Funcs):
    def __init__(self):
        self.analisar()
        

Processar=Aplication().analisar()

        
    