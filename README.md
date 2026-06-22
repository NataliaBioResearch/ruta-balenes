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

🖼️ Vista prèvia del mapa
Aquesta és una captura del mapa interactiu generat pel projecte:

[Parece que el resultado no era seguro para mostrar. ¡Cambiemos de enfoque y probemos algo diferente!]

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
Rutes ordenades cronològicament

Colors únics per balena

Punts amb tooltip i popup

Llegenda automàtica

Capa base + capes alternatives (Toner, Watercolor, Positron, Dark Matter)

Control de capes

📜 Llicència
Aquest projecte es pot utilitzar amb finalitats educatives, científiques i divulgatives.
Si reutilitzes el codi, cita aquest repositori.

🌊 Autoria
Projecte creat per Gaia (NataliaBioResearch)  
Visualització de dades ambientals i ecologia marina.
