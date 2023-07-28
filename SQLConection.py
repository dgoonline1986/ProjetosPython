#pip install pyodbc

import pyodbc

dados_conexao=(
    
    "Driver={SQL Server};"
    "Server=STFSAON005209-L\ESTUDOS;"
    "Database=Barnabe;"
)

conexao=pyodbc.connect(dados_conexao)
print('Conexão bem sucedida')

cursor=conexao.cursor()

id=6
Nome='Severino'
idade='95'
endereco='Rua 2'
profissao='Pleno'
salario=5000

comando=f"""INSERT INTO Cadastro (Id,Nome,Idade,Endereco,Profissao,Salario)values
	({id},'{Nome}','{idade}','{endereco}','{profissao}','{salario}')"""
 
cursor.execute(comando)
cursor.commit()

def imprimir(valor):
    print(valor)
    
imprimir(comando)




 
cursor.close()
print('Banco fechado')

 
 

