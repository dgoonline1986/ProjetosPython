
class Vendedor():
    
    def __init__(self,nome):
        self.nome=nome 
        self.vendas=0
        
        
    def vendeu(self,vendas):
        self.vendas=vendas
        
    def bateu_meta(self,meta):
        if self.vendas>meta:
            print(self.nome, "bateu a meta")
        else:
            print("Não bateua meta")
            
Vendedor1=Vendedor("Diego")
Vendedor1.vendeu(120)
Vendedor1.bateu_meta(600)

print(Vendedor1.vendas)



Vendedor2=Vendedor("Diego 2")
Vendedor2.vendeu(2000)
Vendedor2.bateu_meta(600)

print(Vendedor2.vendas)
        
        

