arquivo = open("rafael.txt", 'r')
lista  = []
rna = ""

for linha in arquivo:
    lista.extend(linha)

for r in lista:
    if (r == "T"):
        rna += "U"
    else:
        rna += r

arquivo.close()

gerado = open('RNARafael.txt','w') 
gerado.write(rna)
gerado.close() 

