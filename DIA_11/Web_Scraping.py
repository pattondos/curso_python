import bs4, requests

url ="https://www.escueladirecta.com/p/excel-aplicado-al-analisis-financiero"
resultado = requests.get(url)

formato = bs4.BeautifulSoup(resultado.text, "lxml")

imagenes = formato.select(".img-responsive")[0]["src"]
print(imagenes)

imagen_1 = requests.get(imagenes)
archivo_imagen = open("descarga.jpg", "wb")
archivo_imagen.write(imagen_1.content)
archivo_imagen.close()    

