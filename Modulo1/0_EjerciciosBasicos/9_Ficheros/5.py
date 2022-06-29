# Ejercicio 5
# Escribir un programa que abra el fichero 
# con información sobre el PIB per cápita 
# de los países de la Unión Europea 
# (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
# pregunte por las iniciales de un país y 
# muestre el PIB per cápita de ese país de todos 
# los años disponibles.


def parsear_pib(url):
   
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf-8').split('\n') 
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        años = datos.pop(0).split('\t')[1:]
        dict_pibs = {}
        for pais in datos:
            datos_pais = pais.split('\t')
            codigo_pais = datos_pais.pop(0)[-2:]
            dict_pais = {}
            for i in range(len(datos_pais)):
                dict_pais[años[i].strip()] = datos_pais[i].strip()
            dict_pibs[codigo_pais] = dict_pais
        return dict_pibs

def pib(pibs, pais = "ES"):
   

    print("Año\tPIB")
    for i, j in pibs[pais].items():
        print(i, '\t', j)

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
pib(parsear_pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)








