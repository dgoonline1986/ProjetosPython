import pandas as pd

import os


from playwright.sync_api import sync_playwright


#caminho=os.listdir('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/BasePesquisa.xlsx')


df=pd.read_excel('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/BasePesquisa.xlsx')


print(df)

df2=df

df=df.values.tolist()

df['Valor_Retorno']=list





class Funcs():




    def localizar_planilha(self,planilha=df):

        self.planilha=planilha

        print(planilha)




        return self.planilha

   

    def entrar_site(self,v):

        self.valor=[]


        with sync_playwright() as p:

            browser=p.chromium.launch(headless=False)

            page = browser.new_page()

            page.goto("https://www.google.com.br")

            page.locator("#APjFqb").fill(f'{v} preços')#usando selector

           

            page.click('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')

            page.wait_for_timeout(50)

            page.get_by_role("link", name="Shopping", exact=True).click()

            page.wait_for_timeout(50)


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
        
        t=0

        for c in self.planilha:

            self.entrar_site(df[t][0])
            
            print(f'imprimendo resultado {self.pesquisa}')
            
            resultado.append(self.pesquisa)
            

            t+=1
            
        print(resultado)
            
        df2['Valor_Retorno']=resultado
        
        print(df2)
        

        
        
        print(type(self.valor))
        print(self.valor)


           

           

class Aplication(Funcs):

    def __init__(self):

        self.localizar_planilha()

        self.procurar_informacao()

       

       




   




Aplication()




   