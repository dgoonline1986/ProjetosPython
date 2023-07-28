
from tkinter import *
from tkinter import ttk
import sqlite3

root=Tk()

#não vai precisar de init por causa que sera chamada dentro da classe aplication
class Funcs():
    def limpar_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
    def conecta_bd(self):
        self.conn=sqlite3.connect("clientes.bd")
        self.cursor=self.conn.cursor(); print("conectando ao banco de dados")
    def desconecta_db(self):
        self.conn.close(); print("desconectando ao banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        #criando caracteristica da tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes(
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER (20),
            cidade CHAR(40)
            
            );
        """)
        
        self.conn.commit(); print("banco de dados Criado")
        self.desconecta_db()
    def variaveis(self):
        self.codigo=self.codigo_entry.get()
        self.nome=self.nome_entry.get()
        self.telefone=self.telefone_entry.get()
        self.cidade=self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        #execução do comando SQL
        self.cursor.execute("""INSERT INTO clientes(nome_cliente,telefone,cidade) VALUES(?,?,?);""",(self.nome,self.telefone,self.cidade))
        self.conn.commit()
        self.select_lista()
        self.limpar_tela()
        self.desconecta_db
    #criando funcao select para mostrar na lista(Frame2)
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())#sempre deletar ante de inserir
        self.conecta_bd()
        lista=self.cursor.execute("""SELECT cod,nome_cliente,telefone,cidade FROM clientes ORDER BY nome_cliente ASC;""")
        #organizando na tabela
        for i in lista:
            self.listaCli.insert("",END,values=i)
        self.desconecta_db()
    #função duplo click
    def OnDoubleClick(self,event):
        self.limpar_tela()  
        self.listaCli.selection()
        #vai marcar a coluna indicada, trazer para entry o que ja esta gravado 
        for n in self.listaCli.selection():
            col1,col2,col3,col4=self.listaCli.item(n,'values')
            self.codigo_entry.insert(END,col1)
            self.nome_entry.insert(END,col2)
            self.telefone_entry.insert(END,col3)
            self.cidade_entry.insert(END,col4)
            
    #função deletar cliente 
    def deleta_cliente(self):
        self.variaveis() #chamar a função 
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod=?""",(self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.limpar_tela()
        self.select_lista()#vai atualizar a selecao
        #8:32
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente=?,telefone=?,cidade=? WHERE COD= ? """, (self.nome, self.telefone,self.cidade,self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_tela
        
        
        
        
        
        

#funcs esta em aplication porque ela vai usar a classe 
class Aplication(Funcs):
    def __init__(self):
        self.root=root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro")
        self.root.configure(background='#1e3743')
        self.root.geometry("788x588")
        self.root.resizable(True,True)
        self.root.maxsize(width=988,height=788)
        self.root.minsize(width=400,height=300)
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
        #segundo botao
        self.bt_buscar=Button(self.frame_1,text='Buscar',bd=4,bg='#107db2',fg='white')
        self.bt_buscar.place(relx=0.3,rely=0.1,relwidth=0.1,relheight=0.15)#posição do botão
        #terceiro botao
        self.bt_novo=Button(self.frame_1,text='Novo',bd=4,bg='#107db2',fg='white', font=('verdana',8,'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)#posição do botão
        #terceiro botao
        self.bt_alterar=Button(self.frame_1,text='Alterar',bd=4,bg='#107db2',fg='white',command=self.altera_cliente)
        self.bt_alterar.place(relx=0.7,rely=0.1,relwidth=0.1,relheight=0.15)#posição do botão
        #Quarto botao
        self.bt_apagar=Button(self.frame_1,text='Apagar',bd=4,bg='#107db2',fg='white', command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8,rely=0.1,relwidth=0.1,relheight=0.15)#posição do botão
        
        ##criação da label e entrada do codigo
        self.lb_codigo=Label(self.frame_1, text="Codigo",fg='#107db2')
        self.lb_codigo.place(relx=0.05,rely=0.05)
        
        self.lb_nome=Label(self.frame_1, text="Nome",fg='#107db2')
        self.lb_nome.place(relx=0.05,rely=0.35)
        
        self.lb_cidade=Label(self.frame_1, text="Cidade",fg='#107db2')
        self.lb_cidade.place(relx=0.5,rely=0.6)
        
        self.lb_telefone=Label(self.frame_1, text="Telefone",fg='#107db2')
        self.lb_telefone.place(relx=0.05,rely=0.6)
    
        #entrada de texto
        self.codigo_entry=Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05,rely=0.15,relwidth=0.08)
        
        self.nome_entry=Entry(self.frame_1)
        self.nome_entry.place(relx=0.05,rely=0.45,relwidth=0.8)
        
        self.telefone_entry=Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05,rely=0.7,relwidth=0.4)
        
        self.cidade_entry=Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5,rely=0.7,relwidth=0.4)
        

        
    def lista_frame2(self):
        self.listaCli=ttk.Treeview(self.frame_2,height=3,column=("col1","col2","col3","col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        
        #dando caracteristica as colunas 
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        
        self.listaCli.place(relx=0.01,rely=0.1,relwidth=0.95,relheight=0.85)
        
        #barra de rolagem
        self.scroolLista=Scrollbar(self.frame_2,orient='vertical')
        #mostrando que abarra de rolagem pertence a lista 
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.85)
        #função para chamar o double click
        self.listaCli.bind("<Double-1>",self.OnDoubleClick)
        
#aula9

Aplication()

       


