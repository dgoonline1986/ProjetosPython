from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    DataInicial=str(input('Digite mes e ano inicial [mm/aaaa]: '))
    Datafinal=str(input('Digite mes e ano final [mm/aaaa]: '))
    ValorPesq=str(input('Digite o valor para pesquisa: '))
    page = browser.new_page()
    page.goto("https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormCorrecaoValores.do?method=exibirFormCorrecaoValores&aba=1")
    page.wait_for_timeout(5000)
    page.fill('//*[@id="corrigirPorIndiceForm"]/div[1]/table/tbody/tr[4]/td[2]/input',DataInicial)
    page.fill('//*[@id="corrigirPorIndiceForm"]/div[1]/table/tbody/tr[5]/td[2]/input',Datafinal)
    page.fill('//*[@id="corrigirPorIndiceForm"]/div[1]/table/tbody/tr[6]/td[2]/input',ValorPesq)
    page.click('//*[@id="corrigirPorIndiceForm"]/div[2]/input[1]')
    page.wait_for_timeout(5000)
    table_element = page.query_selector('body > div:nth-child(14) > table > tbody > tr > td > div.centralizado > table.tabela > tbody')
    rows = table_element.query_selector_all('tr')
    
    
    values =[]
    
    
    for row in rows:
        cells = row.query_selector_all('td')
        row_values = []
        for cell in cells:
            value = cell.inner_text()
            row_values.append(value)
            values.append(row_values)
 
            
    df = pd.DataFrame(values)
    
    df=df.drop_duplicates(subset=[0] , keep='first')
    #df=df[0]="informação"
    df = df.rename(columns={0: 'informacao'})
    df = df.rename(columns={1: 'valor'})
    
       
    print(page.title())
    
    print(df)
    
    df.to_excel('TestePesquisaInflacao.xlsx','pesquisa1',index=False)

    
    browser.close()