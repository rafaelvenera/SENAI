import os
import csv

def quebra(arquivo, delimitador=',', limite=5000):

    contador = 1
    
    leitura = csv.reader(arquivo, delimiter=delimitador)
    limite_atual = limite
        
    cria_csv = csv.writer(open('trains_' + str(contador) + '.csv', 'w', newline=''), delimiter=delimitador)
    
    for i, linha in enumerate(leitura):
        if i + 1 > limite_atual:
            contador += 1
            limite_atual = limite * contador
            cria_csv = csv.writer(open('trains_' + str(contador) + '.csv', 'w', newline=''), delimiter=delimitador)
            
        cria_csv.writerow(linha)
            
                
quebra(open('train.csv', 'r', encoding='UTF-8'))
print("terminou")

