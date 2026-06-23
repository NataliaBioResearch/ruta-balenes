# 🪸 Mapa interactiu de rutes de balenes geolocalitzades

## Projecte de visualització amb Python, GeoPandas i Folium

Aquest repositori conté un projecte complet per visualitzar les rutes de moviment de balenes *Megaptera novaeangliae* (balena geperuda) a la costa est d’Austràlia.

A partir d’un conjunt de dades amb coordenades GPS, el projecte genera un mapa interactiu amb:

- Punts de localització per a cada balena
- Rutes connectades en ordre temporal
- Colors diferenciats per individu
- Capes de mapa alternatives
- Llegenda automàtica

El resultat final és un fitxer HTML navegable i interactiu.

---

# 🎯 Objectiu del projecte

Aquest projecte té com a finalitat transformar dades de seguiment animal en una visualització geoespacial intuïtiva i interactiva.

Mitjançant eines de ciència de dades i sistemes d'informació geogràfica (SIG), es poden explorar patrons de moviment, migració i distribució espacial de les balenes geperudes al llarg de la costa est australiana.

Aquesta aproximació facilita tant l'anàlisi científica com la divulgació ambiental, permetent interpretar grans volums de dades de localització de manera visual.

---

# 🖼️ Vista prèvia del mapa

Aquesta és una captura del mapa interactiu generat pel projecte:

```markdown
![Mapa interactiu de rutes de balenes](maps/whale_routes_map.png)
```

![Mapa interactiu de rutes de balenes](maps/whale_routes_map.png)

> Assegura't que la imatge està desada a `maps/whale_routes_map.png`.

---

# ⚙️ Característiques tècniques

El flux de treball inclou:

- Importació i neteja de dades GPS
- Conversió de coordenades a objectes geoespacials
- Agrupació de registres per individu
- Ordenació temporal de les observacions
- Construcció automàtica de rutes mitjançant geometries `LineString`
- Generació d'un mapa interactiu multicapa
- Exportació final a format HTML

---

# 📁 Estructura del repositori

```text
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
```

---

# 🧪 Dades

Les dades utilitzades provenen del conjunt:

> Movements of Australia's east coast humpback whales

El fitxer CSV conté, entre d'altres:

| Camp | Descripció |
|--------|------------|
| `animal-id` | Identificador únic de cada balena |
| `deploy-on-date` | Data de la localització |
| `deploy-on-latitude` | Latitud |
| `deploy-on-longitude` | Longitud |

---

# 🗺️ Resultat

El mapa generat es desa automàticament a:

```text
maps/whale_routes_map.html
```

Pots obrir-lo amb qualsevol navegador web.

---

# 🐍 Com executar el projecte

## 1. Clona el repositori

```bash
git clone https://github.com/NataliaBioResearch/ruta-balenes.git
cd ruta-balenes
```

## 2. Instal·la les dependències

```bash
pip install -r requirements.txt
```

## 3. Executa l'script

```bash
python scripts/whale_routes_map.py
```

El mapa es generarà a:

```text
maps/whale_routes_map.html
```

---

# 🧠 Tecnologies utilitzades

- pandas
- geopandas
- shapely
- folium
- matplotlib

---

# 🎨 Funcionalitats del mapa

- Rutes ordenades cronològicament
- Colors únics per balena
- Punts amb tooltip i popup
- Llegenda automàtica
- Capa base + capes alternatives:
  - Toner
  - Watercolor
  - Positron
  - Dark Matter
- Control de capes

---

# 🚀 Possibles millores futures

Algunes extensions que es podrien incorporar són:

- Animació temporal dels desplaçaments
- Filtrat per períodes de temps
- Integració de dades oceanogràfiques (temperatura, corrents i profunditat)
- Estadístiques de distància recorreguda per individu
- Publicació del mapa com a aplicació web interactiva
- Integració amb dades en temps real procedents de dispositius de seguiment

---

# 🌍 Aplicacions

Aquest tipus de visualització pot ser útil en:

- Ecologia marina
- Conservació d'espècies migratòries
- Seguiment de fauna mitjançant telemetria
- Educació ambiental
- Divulgació científica
- Projectes de SIG i anàlisi espacial

---

# ⭐ Suport al projecte

Si aquest repositori t'ha resultat útil o interessant, pots donar-li una estrella a GitHub per ajudar a donar visibilitat al projecte.

Gràcies per visitar-lo i per l'interès en la conservació i l'estudi de la fauna marina.

---

# 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.11-blue)
![GeoPandas](https://img.shields.io/badge/GeoPandas-GIS-green)
![Folium](https://img.shields.io/badge/Folium-Maps-brightgreen)
![License](https://img.shields.io/badge/License-Educational-orange)

---

# 🌊 Autoria

**Gaia (NataliaBioResearch)**

Visualització de dades ambientals i ecologia marina.
