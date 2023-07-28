
from playwright.sync_api import Playwright, sync_playwright,expect
from datetime import date,datetime
import mysql.conector

import time

def run(playwright: Playwright)->None:
    browser=playwright.chromium.launch(headless=False)
    
#abrindo nova pagina
page=context.new_page()
data_atual=date.today()
data=str(data_atual)

#go to https://www.youtube.com

page.goto('https://www.youtube.com')
page.wait_for_timeout(300)

#click text-Atividade 
a=page.locator().all_text_contents()
d=page.locator().all_inner_texts()
b=page.locator().all_text_contents()
c=page.locator().all_text_contents()


print(len(a))


for i in range(len(a)):
    #if i% 2 ==0
    ids=data+a[i].strip()
    aa=(a[i].strip())
    print(a[i].strip())
    print(b[i])
    print(c[i])
    
    
    
    #abrir conexão com banco de dados 
    
    conectar=mysql.connector.connect(host='',database='',user='',password='')
    dados=''
    comando="""INSERT web"""
    sql=comando+dados
    #popular dados
    try:
        cursor=conectar.cursor()
        #executar comando
        cursor.execute(sql)
        conectar.commit()
    except:
        continue
conectar.close()

#não esta aplicado 
#https://www.youtube.com/watch?v=DcWCnPgrhhk




    
    

