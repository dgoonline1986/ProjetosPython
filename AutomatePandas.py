import pandas as pd 

#import os

#os.path.isfile('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/Financeiro.xlsx')

#arquivo=os.listdir('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao')

df=pd.read_excel('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/Financeiro.xlsx')

  
df['Resultado']=''

print(df)


    
def Capturar(planilha):
    #planilha=planilha
    print('capturado')
    print(planilha)
    linhas=(len(planilha))
    print(f'Existem {linhas} de linhas')
        
    df2=[]
        
  
    i=0
    while i < linhas:     
        df2.append('Pago')
        i=i+1
            
    planilha['Resultado']=df2
    
    
    print(planilha)
        
            
Capturar(df)



#classificar_dados=Preparar.add_coluna()




