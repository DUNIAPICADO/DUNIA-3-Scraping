import requests
from bs4 import BeautifulSoup

# URL de la página principal de Wikipedia en español
url = 'https://es.wikipedia.org/wiki/Portada'

# Enviar una solicitud GET al sitio web
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar las secciones destacadas
    featured_sections = soup.find_all('div', class_='mp-upper')
    
    # Extraer y mostrar los títulos de los artículos destacados
    for section in featured_sections:
        # Encontrar los enlaces dentro del div
        links = section.find_all('a')
        for link in links:
            title = link.get('title')
            if title:
                print(f'Título: {title}')
else:
    print(f"Error al acceder al sitio web. Código de estado: {response.status_code}")
