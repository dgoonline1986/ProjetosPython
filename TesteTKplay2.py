from tkinter import *
from tkinter import ttk
from teste_copy import Pesquisa


import sqlite3

#com banco de dados 

root=Tk()#estrutura essencial 

class Funcs():
    def limpar_tela(self):
        self.data_inic_entry.delete(0,END)
        self.data_fim_entry.delete(0,END)
        self.valor_entry.delete(0,END)
        
    def conecta_bd(self):
        self.conn=sqlite3.connect("clientes.bd")
        self.cursor=self.conn.cursor(); print("conectando ao banco de dados")
        
    def desconecta_db(self):
        self.conn.close(); print("desconectando ao banco de dados")
    
    def montaTabelas(self):
        self.conecta_bd()
        #criando caracteristica da tabela
        self.cursor.execute("""
        
        CREATE TABLE IF NOT EXISTS Pesquisadb(
            Data_inicio CHAR(10) NOT NULL,
            Data_fim CHAR(10) NOT NULL,
            Valor_pesquisado CHAR(20) NOT NULL,
            Valor_retorno CHAR(20) NOT NULL
                    
            );
        """)
        
        self.conn.commit(); print("banco de dados Criado")
        self.desconecta_db()
    
    def add_pesquisa(self):
       try: 
            self.variaveis()
            self.conecta_bd()
            
            self.resp = Pesquisa(self.Data1,self.Data2,self.valor)
            
            #execução do comando SQL
            self.cursor.execute("""INSERT INTO Pesquisadb(Data_inicio,Data_fim,Valor_pesquisado,Valor_retorno) VALUES(?,?,?,?);""",(self.Data1,self.Data2,self.resp[2],self.resp[3]))
            self.conn.commit()
            self.select_lista()
            self.limpar_tela()
            self.desconecta_db
            
       
       except AttributeError:
            import telaerro as te
            te.tratativaDeErro('Você é burro não ta vendo os parametros no nome da caixinha? ')
       
       except:       
            import telaerro as te
            te.tratativaDeErro('Erro inesperado')
       finally:
           ('programa encerrado')
           
        
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())#sempre deletar ante de inserir
        self.conecta_bd()
        lista=self.cursor.execute("""SELECT Data_inicio,Data_fim,Valor_pesquisado,Valor_retorno FROM Pesquisadb;""")
        #organizando na tabela
        for i in lista:
            self.listaCli.insert("",END,values=i)
        self.desconecta_db()
    
    #fazer o get somentedo que ja esta preecnido o retorno da pesquisa no insert sql    
    def variaveis(self):
        self.Data1=self.data_inic_entry.get()
        self.Data2=self.data_fim_entry.get()
        self.valor=self.valor_entry.get()
    
        
        #print(lista)
        
    def OnDoubleClick(self,event):
        self.limpar_tela()  
        self.listaCli.selection()
        #vai marcar a coluna indicada, trazer para entry o que ja esta gravado 
        for n in self.listaCli.selection():
            col1,col2,col3=self.listaCli.item(n,'values')
            self.data_inic_entr.insert(END,col1)
            self.ata_fim_entry.insert(END,col2)
            self.valor_entry.insert(END,col3)
            
        
        

    
class Aplication(Funcs):
    def __init__(self):
        self.root=root
        self.tela()
        self.frames_da_tela()
        self.montaTabelas() 
        self.widgets_frame1()
        self.lista_frame2()
        self.select_lista()
        root.mainloop()#estrutura essencial 
        
    
            
    def tela(self):
        self.root.title("Calculadora Banco Central")
        self.root.configure(background='#1e3743')
        self.root.geometry("788x588")
        self.root.resizable(True,True)
        self.root.maxsize(width=988,height=788)
        self.root.minsize(width=400,height=300)

#padroes da tela
    def frames_da_tela(self):
        self.frame_1=Frame(self.root, bd=4, bg='#def3ee' ,highlightbackground='#759fe6',highlightthickness='3' )
        #place pack grid
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.5)#dimensionamento da tela
        
        self.frame_2=Frame(self.root, bd=4, bg='#def3ee' ,highlightbackground='#759fe6',highlightthickness='3' )
        #place pack grid
        self.frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.5)#dimensionamento da tela
        
    def widgets_frame1(self):
        self.bt_limpar=Button(self.frame_1,text='Limpar',bd=4,bg='#107db2',fg='white',command=self.limpar_tela) #bd= borda e bg=cor de fundo fg= cor do texto
        self.bt_limpar.place(relx=0.2,rely=0.1,relwidth=0.1,relheight=0.15)#posição do botão
        self.bt_calcular=Button(self.frame_1,text='Calcular',bd=4,bg='#107db2',fg='white', font=('verdana',8,'bold'),command=self.add_pesquisa)
        self.bt_calcular.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)#posição do botão
        
        
        ##criação da label e entrada do codigo
        self.lb_data_inic=Label(self.frame_1, text="Data Inicial [mm/aaaa]",fg='#107db2')
        self.lb_data_inic.place(relx=0.1,rely=0.6)
        
        self.lb_data_fim=Label(self.frame_1, text="Data Final [mm/aaaa]",fg='#107db2')
        self.lb_data_fim.place(relx=0.3,rely=0.6)
        
        self.lb_valor=Label(self.frame_1, text="Valor",fg='#107db2')
        self.lb_valor.place(relx=0.7,rely=0.6)
        
        #entrada de texto
        self.data_inic_entry=Entry(self.frame_1)
        self.data_inic_entry.place(relx=0.1,rely=0.7,relwidth=0.2)
        
        self.data_fim_entry=Entry(self.frame_1)
        self.data_fim_entry.place(relx=0.3,rely=0.7,relwidth=0.2)
        
        self.valor_entry=Entry(self.frame_1)
        self.valor_entry.place(relx=0.6,rely=0.7,relwidth=0.3)
        
    
        
        
        
    def lista_frame2(self):
        self.listaCli=ttk.Treeview(self.frame_2,height=3,column=("col1","col2","col3","col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Data inicial")
        self.listaCli.heading("#2", text="Data Final")
        self.listaCli.heading("#3", text="valor Pesquisado")
        self.listaCli.heading("#4", text="valor retorno")
        
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=200)
        self.listaCli.column("#4", width=200)
        #tamando do frame
        self.listaCli.place(relx=0.01,rely=0.1,relwidth=0.95,relheight=0.85)
        


        

Aplication()#estrutura essencial 



