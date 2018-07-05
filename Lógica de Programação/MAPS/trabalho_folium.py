import pandas as pd
import folium
import geocoder
from folium.plugins import MarkerCluster

def pegaLatLog(cidade):
    g = geocoder.arcgis(cidade)
    return(g.latlng)

mapa = folium.Map(
    location=[-16.1237611, -59.9219642],
    zoom_start=4)

marcador = MarkerCluster().add_to(mapa)

csv = pd.read_csv('importar1.csv', encoding = 'latin-1', delimiter= ';')

crimes = csv[csv['CIDADE'] != '']
                 
for _, csv in crimes.iterrows():

    latlng = pegaLatLog(csv['CIDADE'] + ",SC")
   
    if csv['MV HOMICIDIO DOLOSO'] > 0:
        folium.Marker([latlng[0], latlng[1]],
                    popup='HOMICIDIO DOLOSO',
                    icon=folium.Icon(color='red'),
                   ).add_to(marcador)

    if csv['MV LATROCINIO'] > 0:
        folium.Marker([latlng[0], latlng[1]],
                    popup='LATROCINIO',
                    icon=folium.Icon(color='blue'),
                   ).add_to(marcador)

    if csv['VM LESAO CORPORAL SEGUIDA DE MORTE'] > 0:
        folium.Marker([latlng[0], latlng[1]],
                    popup='LESAO CORPORAL SEGUIDA DE MORTE',
                    icon=folium.Icon(color='black'),
                   ).add_to(marcador)

    if csv['VM HOMICIDIO EM DECORRENCIA DE ACAO DA POLICIA CIVIL'] > 0:
        folium.Marker([latlng[0], latlng[1]],
                    popup='HOMICIDIO EM DECORRENCIA DE ACAO DA POLICIA CIVIL',
                    icon=folium.Icon(color='pink'),
                   ).add_to(marcador)

    if csv['VM HOMICIDIO EM DECORRENCIA DE ACAO DA POLICIA MILITAR'] > 0:
        folium.Marker([latlng[0], latlng[1]],
                    popup='HOMICIDIO EM DECORRENCIA DE ACAO DA POLICIA MILITAR',
                    icon=folium.Icon(color='purple'),
                   ).add_to(marcador)

    if csv['VM POLICIAL CIVIL MORTO EM SERVIÇO'] > 0:
        folium.Marker([latlng[0], latlng[1]],
                    popup='POLICIAL CIVIL MORTO EM SERVIÇO',
                    icon=folium.Icon(color='white'),
                   ).add_to(marcador)

    if csv['VM POLICIAL MILITAR MORTO EM SERVICO'] > 0:
        folium.Marker([latlng[0], latlng[1]],
                    popup='POLICIAL MILITAR MORTO EM SERVICO',
                    icon=folium.Icon(color='black'),
                   ).add_to(marcador)


mapa.save('map.html')
    
          
