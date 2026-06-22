🪸 Mapa interactiu de rutes de balenes geolocalitzades
Projecte de visualització amb Python, GeoPandas i Folium
Aquest repositori conté un projecte complet per visualitzar les rutes de moviment de balenes Megaptera novaeangliae (balena geperuda) a la costa est d’Austràlia.

A partir d’un conjunt de dades amb coordenades GPS, el projecte genera un mapa interactiu amb:

punts de localització per a cada balena

rutes connectades en ordre temporal

colors diferenciats per individu

capes de mapa alternatives

llegenda automàtica

El resultat final és un fitxer HTML navegable i interactiu.

🎯 Objectiu del projecte
Aquest projecte té com a finalitat transformar dades de seguiment animal en una visualització geoespacial intuïtiva i interactiva. Mitjançant eines de ciència de dades i sistemes d'informació geogràfica (SIG), es poden explorar patrons de moviment, migració i distribució espacial de les balenes geperudes al llarg de la costa est australiana.

Aquesta aproximació facilita tant l'anàlisi científica com la divulgació ambiental, permetent interpretar grans volums de dades de localització de manera visual.

🖼️ Vista prèvia del mapa
Aquesta és una captura del mapa interactiu generat pel projecte:

[Parece que el resultado no era seguro para mostrar. ¡Cambiemos de enfoque y probemos algo diferente!]

(Assegura’t que la imatge està pujada a maps/whale_routes_map.png.)

⚙️ Característiques tècniques
El flux de treball inclou:

importació i neteja de dades GPS

conversió de coordenades a objectes geoespacials

agrupació de registres per individu

ordenació temporal de les observacions

construcció automàtica de rutes mitjançant geometries LineString

generació d'un mapa interactiu multicapa

exportació final a format HTML

📁 Estructura del repositori
Código
ruta-balenes/
├── data/
│   ├── humpback_whales.csv
│   └── .gitkeep
├── maps/
│   ├── whale_routes_map.html
│   ├── whale_routes_map.png
│   └── .gitkeep
├── scripts/
│   └── whale_routes_map.py
├── requirements.txt
└── README.md
🧪 Dades
Les dades utilitzades provenen del conjunt:
“Movements of Australia’s east coast humpback whales”

El CSV conté, entre d’altres:

animal-id — identificador únic de cada balena

deploy-on-date — data de la localització

deploy-on-latitude — latitud

deploy-on-longitude — longitud

🗺️ Resultat
El mapa generat es desa automàticament a:

Código
maps/whale_routes_map.html
Pots obrir-lo amb qualsevol navegador web.

🐍 Com executar el projecte
1) Clona el repositori
Código
git clone https://github.com/NataliaBioResearch/ruta-balenes.git
cd ruta-balenes
2) Instal·la les dependències
Código
pip install -r requirements.txt
3) Executa l’script
Código
python scripts/whale_routes_map.py
El mapa es generarà a maps/whale_routes_map.html.

🧠 Tecnologies utilitzades
pandas

geopandas

shapely

folium

matplotlib

🎨 Funcionalitats del mapa
rutes ordenades cronològicament

colors únics per balena

punts amb tooltip i popup

llegenda automàtica

capa base + capes alternatives (Toner, Watercolor, Positron, Dark Matter)

control de capes

🚀 Possibles millores futures
Algunes extensions que es podrien incorporar són:

animació temporal dels desplaçaments

filtrat per períodes de temps

integració de dades oceanogràfiques (temperatura, corrents, profunditat)

estadístiques de distància recorreguda per individu

publicació del mapa com a aplicació web interactiva

integració amb dades en temps real procedents de dispositius de seguiment

🌍 Aplicacions
Aquest tipus de visualització pot ser útil en:

ecologia marina

conservació d'espècies migratòries

seguiment de fauna mitjançant telemetria

educació ambiental

divulgació científica

projectes de SIG i anàlisi espacial

⭐ Suport al projecte
Si aquest repositori t'ha resultat útil o interessant, pots donar-li una estrella a GitHub per ajudar a donar visibilitat al projecte.

Gràcies per visitar-lo i per l'interès en la conservació i l'estudi de la fauna marina.

🏷️ Badges
https://img.shields.io/badge/Python-3.11-blue  
https://img.shields.io/badge/GeoPandas-GIS-green  
https://img.shields.io/badge/Folium-Maps-brightgreen  
https://img.shields.io/badge/License-Educational-orange

🌊 Autoria
Projecte creat per Gaia (NataliaBioResearch)  
Visualització de dades ambientals i ecologia marina.
