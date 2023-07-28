# pip install PyPDF2
#pip install tabula-py

import tabula 
import pyPDF2
from IPython.display import display
import pandas as pd

#importando para avisar mensagem de erros 
import warnings

#carregando o arquivo pdf
lista_tabelas=tabula.read_pdf('formatado.pdf', pages='all')

#exibindo quantas paginas foram carregada
print(len(lista_tabelas))

for tabela in lista_tabelas:
    display(tabela)

#obtendo somente a pagina 1
tabela1=lista_tabelas[0]
tabela1

tabela2=lista_tabelas[1]
tabela2

#listando todas as linhas exceto a primeira 

tabela3=tabela2[1:]
tabela3
tabela3=pd.DataFrame(tabela3)
tabela4=[]
listaColun=['Data','Dia','Entrada','Saida Almoço','Retorno Almoço','Saida']
tabela4.append(listaColun)
print(tabela4)

for linha in tabela3:
    df=pd.DataFrame(tabela4)
    print(tabela4)
    
    
    
    

#tirando espaço
#tabela2=tabela2['']

#https://www.youtube.com/watch?v=GpB6mNuaB-M

#10:26

