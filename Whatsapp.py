from pickle import TRUE
from re import S
import numpy as np
from selenium import webdriver
import time
import pandas as pd
import random

navegador = webdriver.Chrome()

#Escanear Qrcode
navegador.get('https://web.whatsapp.com')


#=============================Carrega a planilha com nome, contato que quiser =============================
lista = pd.read_excel(r'lista.xlsx')
time.sleep(random.choice(range(20,40)))

totalContatos = lista['Telefone'].count()
totalMensagens = lista['Mensagem'].count()
lista['Telefone'] = lista['Telefone'].values.astype(np.int64)

for x in range(0,totalContatos):
    try:
        time.sleep(2.5)
        contato = lista['Telefone'][x]    
        nomeContato = lista['Nome'][x]
        time.sleep(random.choice(range(5,20)))
        navegador.get(f'https://web.whatsapp.com/send?phone={contato}')

        time.sleep(random.choice(range(10,20)))
        print('Enviando mensagem para: {} numero {} '.format(nomeContato,contato))        
        for c in range(0,totalMensagens):
            mensagem = lista['Mensagem'][c]
            time.sleep(random.choice(range(5,20)))
            navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(mensagem)
            time.sleep(random.choice(range(5,20)))
            navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            print('Mensagem {} enviada para {}'.format(c, nomeContato))
                

        #============================= Terminou ====================================
        time.sleep(random.choice(range(30,60)))
    except Exception as e:
        navegador.get('https://web.whatsapp.com')
        print('Contato {} falhou'.format(nomeContato))
