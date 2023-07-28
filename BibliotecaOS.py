import os
import shutil


#listando arquivos

arquivos=os.listdir(r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop\Automacao_pasta')
print(arquivos)

#listando diretorio especifico 
arquivos=os.listdir(r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop\Automacao_pasta\Vendas')
print(arquivos)

# o caminho da pasta que esta sendo usado atualmente
os.getcwd()
print(arquivos)

#para trocar o nome do arquivo 
os.rename(r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop\Automacao_pasta\Vendas- 1.xlsx',r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop\Automacao_pasta\Vendas 1.xlsx')



#copiar arquivo para outra pasta 

shutil.copy2(r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop\Automacao_pasta\Vendas 1.xlsx',r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop\Automacao_pasta\Vendas\Vendas 1.xlsx')



lista_arquivos=os.listdir(r'C:\Users\dnsilva2\OneDrive - Stefanini\Desktop\Automacao_pasta')

for arquivo in lista_arquivos:
    if 'xlsx' in arquivo:
        print(arquivo)
        if"Compras" in arquivo:
            os.rename(f'C:/Users/dnsilva2/OneDrive - Stefanini/Desktop/Automacao_pasta//{arquivo}',f'C:/Users/dnsilva2/OneDrive - Stefanini/Desktop/Automacao_pasta/Compras//{arquivo}')
        elif "Vendas" in arquivo:
            os.rename(f'C:/Users/dnsilva2/OneDrive - Stefanini/Desktop/Automacao_pasta//{arquivo}',f'C:/Users/dnsilva2/OneDrive - Stefanini/Desktop/Automacao_pasta/Vendas//{arquivo}')
            
            

    



#https://docs.python.org/pt-br/3/library/os.path.html#:~:text=os.path.relpath%28path%2C,start%3Dos.curdir%29%20%C2%B6
