import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Big_Brother_Brasil_21'

html = pd.read_html(url, match='Resultado')

type(html[0])

tabela_BBB = html[0]

tabela_BBB.to_excel(r'C:\Users\dnsilva2\Downloads\teste.xlsx', index=False)

tabela_BBB.head()