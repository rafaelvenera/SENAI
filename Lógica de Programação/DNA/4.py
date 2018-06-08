arquivo1 = open("rafael.txt", 'r')
arquivo2 = open("rafael2.txt", 'r')

contador = 0

lista1  = []
lista2 = []

for linha in arquivo1:
    lista1.extend(linha)

for linha in arquivo2:
    lista2.extend(linha)

for letra1, letra2 in zip(lista1, lista2):
    if (letra1 != letra2):
        contador += 1

arquivo1.close()
arquivo2.close()


gerado = open('DHRafael.txt','w') 
gerado.write(str(contador))
gerado.close() 

    
