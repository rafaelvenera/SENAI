import sqlite3, csv

def dic(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

cx = sqlite3.connect("enem2016.db")
cx.row_factory = dic
       
cur = cx.cursor()
cur.execute('DROP TABLE IF EXISTS enem')
cur.execute(""" CREATE TABLE enem(NU_INSCRICAO TEXT, TP_STATUS_REDACAO INTEGER, NU_NOTA_REDACAO REAL, NU_NOTA_CN REAL, NU_NOTA_CH REAL, NU_NOTA_LC REAL, NU_NOTA_MT REAL,MEDIA_PONDERADA REAL, NU_IDADE INTEGER); """)
cx.commit()

with open('train.csv', newline='', encoding='utf-8') as arquivo:
    next(arquivo) #Pula primeira linha
    
    for linha in csv.reader(arquivo):
        nr_inscricao = linha[1]
        status_redacao = linha[110]
        idade = linha[7]

        if (linha[116] == ''):
            redacao    = 0
        else:
            redacao = linha[116]
        if (linha[97] == ''):
            natureza    = 0
        else:
            natureza = linha[97]
        if (linha[98] == ''):
            humana    = 0
        else:
            humana = linha[98]
        if (linha[99] == ''):
            codigo    = 0
        else:
            codigo = linha[99]
        if (linha[100] == ''):
            matematica    = 0
        else:
            matematica = linha[100]
        
        media = ((float(redacao) * 3) + (float(natureza) * 2) + (float(humana) * 1) + (float(codigo) * 1.5) + (float(matematica) * 3)) / (3 + 2 + 1 + 1.5 + 3)
        cur.execute("""INSERT INTO enem VALUES (?,?,?,?,?,?,?,?,?);""", (nr_inscricao, status_redacao, redacao, natureza, humana, codigo, matematica, media ,idade))          

cx.commit()

cur.execute(""" SELECT NU_INSCRICAO, MEDIA_PONDERADA as 'NOTA_FINAL' FROM enem where TP_STATUS_REDACAO = 1 and NU_NOTA_REDACAO > 0 and NU_NOTA_CN > 0 and NU_NOTA_CH > 0 and NU_NOTA_LC > 0 and NU_NOTA_MT > 0
                ORDER BY MEDIA_PONDERADA DESC, NU_IDADE DESC limit 20 """)

resultado = cur.fetchall()
    
d = {'token':'Rafael Diego Venera', 'email':'rafael_venera@estudante.sc.senai.br', 'answer':resultado}

print(d)

cx.commit()
cx.close()

