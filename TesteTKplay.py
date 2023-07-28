from tkinter import *
from tkinter import ttk
from teste_copy import Pesquisa

#sem banco de dados 


root=Tk()#estrutura essencial 

class Funcs():
     def limpar_tela(self):
        self.data_inic_entry.delete(0,END)
        self.data_fim_entry.delete(0,END)
        self.valor_entry.delete(0,END)
        
    
          
     def variaveis(self):
        self.Data1=self.data_inic_entry.get()
        self.Data2=self.data_fim_entry.get()
        self.valor=self.valor_entry.get()
    
     def calcular(self):
        
         self.variaveis()
         self.resp = Pesquisa(self.Data1,self.Data2,self.valor)
         #print(self.resp.values.tolist())
         print(f'Este cara é o self.resp \n {self.resp}')
         
         #print(type(self.resp))
         for i in self.resp:
        #print(self.resp[i])
            #self.listaCli.insert("",END,values=i,iid=1)
            self.listaCli.insert(index=0, values=self.resp, parent="", iid=0 )
           
         self.limpar_tela()
            
            
        
    
          
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
        self.widgets_frame1()
        self.lista_frame2()
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
        self.bt_calcular=Button(self.frame_1,text='Calcular',bd=4,bg='#107db2',fg='white', font=('verdana',8,'bold'),command=self.calcular)
        self.bt_calcular.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)#posição do botão
        
        
         ##criação da label e entrada do codigo
        self.lb_data_inic=Label(self.frame_1, text="Data Inicial",fg='#107db2')
        self.lb_data_inic.place(relx=0.1,rely=0.6)
        
        self.lb_data_fim=Label(self.frame_1, text="Data Final",fg='#107db2')
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
        self.listaCli.heading("#2", text="Data Final ")
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
