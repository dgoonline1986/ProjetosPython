import schedule
import time 

def automatico():
    print('Iniciando a Função')
    
schedule.every(10).seconds.do(automatico)


executar=0

while True:
    schedule.run_pending()
    print('carregando')
    executar+=1
    time.sleep(1)
    if executar==15:
        break 
       