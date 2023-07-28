def Pesquisa(V1,V2,V3):

    from playwright.sync_api import sync_playwright
    import pandas as pd
    
 


    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        #DataInicial=str(input('Digite mes e ano inicial [mm/aaaa]: '))
        #Datafinal=str(input('Digite mes e ano final [mm/aaaa]: '))
        #ValorPesq=str(input('Digite o valor para pesquisa: '))
        page = browser.new_page()
        page.goto("https://www3.bcb.gov.br/CALCIDADAO/publico/exibirFormCorrecaoValores.do?method=exibirFormCorrecaoValores&aba=1")
        page.wait_for_timeout(50)
        page.fill('//*[@id="corrigirPorIndiceForm"]/div[1]/table/tbody/tr[4]/td[2]/input',V1)
        page.fill('//*[@id="corrigirPorIndiceForm"]/div[1]/table/tbody/tr[5]/td[2]/input',V2)
        page.fill('//*[@id="corrigirPorIndiceForm"]/div[1]/table/tbody/tr[6]/td[2]/input',V3)
        page.click('//*[@id="corrigirPorIndiceForm"]/div[2]/input[1]')
        page.wait_for_timeout(30)
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
        
        df = df.rename(columns={0: 'informacao'})
        df = df.rename(columns={1: 'valor'})
        
       
        print(f'Este cara é o df \n {df}')
    

    
        
        #df.to_excel('TestePesquisaInflacao.xlsx','pesquisa1',index=False)

        
        browser.close()
        
        response = []
        response.append(df['valor'][0])
        response.append(df['valor'][2])
        response.append(str(df['valor'][4]).replace('\xa0','').replace('( REAL )',''))
        response.append(str(df['valor'][11]).replace('\xa0','').replace('( REAL )',''))
        
        return response