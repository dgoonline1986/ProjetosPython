import pandas as pd

import os


from playwright.sync_api import sync_playwright

df=pd.read_excel('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/BasePesquisa.xlsx')


print(df['Pesquisa'][0])

print(df)




class Funcs():

    #localizar planilha no diretorio 
    def localizar_planilha(self,planilha=df):
        self.planilha=planilha

        print(planilha)
       


        return self.planilha

    #entrar no site para pesquisar 
    
    def abrir_site(self,texto_busca):
        print(f'Essa é a planilha {self.planilha}')
        
        print(f'encontrei {texto_busca}')
        
    
        with sync_playwright() as p:

            browser=p.chromium.launch(headless=False)

            page = browser.new_page()

            page.goto("https://www.google.com.br")

            page.locator("#APjFqb").fill(f'{texto_busca} preços')#usando selector
            
            page.click('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')

            page.wait_for_timeout(500)

            page.get_by_role("link", name="Shopping", exact=True).click()

            page.wait_for_timeout(500)


            self.rows = page.locator('span.a8Pemb.OFFNJ')

            title = page.locator('h3.tAxDx')

            shopping = page.locator('div.aULzUe.IuHnof')

            self.i = 0

            self.pesquisa=[]

            for self.i in range(1):

                print(title.nth(self.i).inner_text())

                print(shopping.nth(self.i).inner_text())

                print(self.rows.nth(self.i).inner_text(), "\n")

                self.pesquisa=self.rows.nth(self.i).inner_text()

               
            page.close()

           

            browser.close()



            return self.pesquisa

            
            
    def procurar_informacao(self):
        
        
        resultado=[]
        
        self.t=0
        
        
        
        for c in range(len(df)):
            
            self.abrir_site(df['Pesquisa'][self.t])
            
            print(f'estou acessando {self.planilha}')
            print(f'imprimindo resultado {self.pesquisa}')
            
            resultado.append(self.pesquisa)
            
            self.t= self.t + 1
            
        df['Valor_Retorno']=resultado
            
        
        print(df)
        self.salvando_informacoes()
      

    def salvando_informacoes(self):
        df.to_excel('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/BasePesquisa.xlsx', sheet_name='Apurado', index=False)
        print('Informacoes salvas com sucesso') 



class Aplication(Funcs):

    def __init__(self):

        self.localizar_planilha()
        self.procurar_informacao()
    


x = Aplication()


