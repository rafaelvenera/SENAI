arquivo = open("rafael.txt", 'r')
lista  = []
inverso = ""

for linha in arquivo:
    lista.extend(linha)

for r in reversed(lista):
    if (r == "A"):
        inverso += "T"
    elif (r == "T"):
        inverso += "A"
    elif (r == "C"):
        inverso += "G"
    elif (r == "G"):
        inverso += "C"

arquivo.close()

gerado = open('complRafael.txt','w') 
gerado.write(inverso)
gerado.close() 

