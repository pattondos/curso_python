import bs4, requests

url = "http://books.toscrape.com/catalogue/page-{}.html"
lista_titulos_libros_4 = []

for pagina in range(1, 51):
    
    paginacion = url.format(pagina)
    resultado = requests.get(paginacion)
    formato = bs4.BeautifulSoup(resultado.text, "lxml")
    
    libros = formato.select(".product_pod")
    for libro in libros:
        
        if (len(libro.select(".star-rating.Four")) != 0) or (len(libro.select(".star-rating.Five")) != 0):
            titulo_libro = libro.select("a")[1]["title"]
            
            lista_titulos_libros_4.append(titulo_libro)

for titulo in lista_titulos_libros_4:
    print(titulo)


