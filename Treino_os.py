import os

#chamaa biblioteca e uma função dela
sistema=os.environ
print(sistema)

print(sistema['username'])

print(sistema['PROGRAMDATA'])

#mapeando a pasta atual 
os.getcwd

novo_caminho=r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop'
os.chdir(novo_caminho)
print(os.getcwd())