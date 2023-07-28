import requests
from tkinter import *

def pegar_cotacoes():
    requisicao=requests.get('https://economia.awsomeapi.com.br/last/USD-BRL,EUR')
    
    requisicao_dic=requisicao.json()
    
    cotacao_dolar=requisicao_dic['USDBRL']['bid']
    cotacao_euro=requisicao_dic['EUBRL']['bid']
    cotacao_btc=requisicao_dic['BTCBRL']['bid']
    
    texto=f'''
    dolar: {cotacao_dolar}
    Euro: {cotacao_euro} 
    BTC: {cotacao_btc}'''
    
    texto_cotacoes["text"]=texto
    
   #rodar a função
    #pegar_cotacoes() não precisa porque sera cionada pelo botão
    
    "inerface"
    janela=Tk()
    
    janela.title("Cotação atual das moedas")
    #configuração do tamanho da janela
    janela.geometry("400x400")
    
    texto_orientacao=Lab
    el(janela,text='Clique no botão para exebir a informação')
    #posição da coluna
    texto_orientacao.grid(column=0,row=0,padx=10,pady=10)
                #referencia
    botao=Button(janela,text="buscar cotações",command=pegar_cotacoes)
    #posição do botão
    botao.grid(column=0,row=1)
    
    #resulado da busca
    texto_cotacoes=Label(janela,text="",padx=10,pady=10)
    texto.cotacoes.grid(column=0,row=2)
    
    janela.mainloop()
    

    