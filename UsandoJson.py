import json

with open("arquivo.json", encoding='UTF-8') as meu_json:
    dados=json.load(meu_json)
    
#print(dados)

for i in dados:
    print(i['secretBase'])
    