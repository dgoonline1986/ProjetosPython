
import pandas as pd

import os

from playwright.sync_api import sync_playwright

#caminho=os.listdir('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/BasePesquisa.xlsx')

df=pd.read_excel('C:/Users/dnsilva2/OneDrive - Stefanini/KPI/Autuomacao/BasePesquisa.xlsx')


df=df.values.tolist()



class Funcs():

    def localizar_planilha(self,planilha=df):
        self.planilha=planilha
        print(planilha)

        return self.planilha
    
    def entrar_site(self):
        #self.t=1
        v=(df[0])
        #print(v[0])
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.pichau.com.br/hardware")
            page.locator('#__next > div.jss786 > div.jss788 > div > div > div').click()
            page.locator("#__next > divjss570 >div.jss572 > div > div > div > svg").fill(f'{v[0]} ')#usando selector 
            page.click()
            page.wait_for_timeout(5000)
            #page.locator('#cnt > div:nth-child(8) > div > div > div.xhjkHe > div.TrmO7 > div > a:nth-child(2)').click()
            page.wait_for_timeout(5000)
            #resultado = page.inner_text('xpath=//*[@id="_qbW6ZML0N7fR5OUPwu--2A0_17"]/div[1]/div/div/div[1]/a/div[3]/div/div[1]/span[1]/span/b')
          
            #print(resultado)
            
                
            
            browser.close()
            
            
            
    def procurar_informacao(self):
        i=0
        self.t=0
        
        for i in self.Tamanho_linhas:
            self.entrar_site()
            i=i+1
            self.t=self.t+1
        
            
            
         

class Aplication(Funcs):
    def __init__(self):
        self.localizar_planilha()
        self.entrar_site()
        #self.procurar_informacao()
        #self.retornar_planilha()
        

    

Aplication()

    


