arquivo = open("rafael.txt", 'r')
lista  = []
contador = 0

for linha in arquivo:
    lista.extend(linha)

for i in range(len(lista)):
    if (lista[i] == "C" or lista[i] == "G"):
        contador += 1

perc = float((contador * 100) / len(lista))

arquivo.close()

gerado = open('RafaelCG.txt','w') 
gerado.write("Percentual de CG: %f" %(perc)) 
gerado.close() 




