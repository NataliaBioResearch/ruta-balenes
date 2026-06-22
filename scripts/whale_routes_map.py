import pandas as pd
import folium
from shapely.geometry import Point, LineString
import geopandas as gpd
from folium.plugins import BeautifyIcon
import matplotlib.cm as cm
import matplotlib.colors as colors

# ---------------------------------------------------------
# 1) Carregar dades
# ---------------------------------------------------------

# Ruta relativa al CSV (posa el fitxer dins /data)
csv_filepath = "data/humpback_whales.csv"

# Carregar dades
whale_data = pd.read_csv(csv_filepath)

# Crear geometries
gdf = gpd.GeoDataFrame(
    whale_data,
    geometry=gpd.points_from_xy(
        whale_data['deploy-on-longitude'],
        whale_data['deploy-on-latitude']
    ),
    crs="EPSG:4326"
)

# ---------------------------------------------------------
# 2) Preparar colors per a cada balena
# ---------------------------------------------------------

whale_ids = gdf['animal-id'].unique()
cmap = cm.get_cmap('tab20', len(whale_ids))
whale_colors = {whale_id: colors.to_hex(cmap(i)) for i, whale_id in enumerate(whale_ids)}

# ---------------------------------------------------------
# 3) Crear mapa base
# ---------------------------------------------------------

m = folium.Map(
    location=[-25.0, 153.0],
    zoom_start=6,
    tiles='Stamen Terrain',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
)

# ---------------------------------------------------------
# 4) Afegir rutes i punts
# ---------------------------------------------------------

for whale_id in whale_ids:
    whale_df = gdf[gdf['animal-id'] == whale_id].sort_values("deploy-on-date")
    whale_color = whale_colors[whale_id]

    # Afegir línia si hi ha més d'un punt
    if len(whale_df) > 1:
        line = LineString(whale_df.geometry.tolist())
        folium.PolyLine(
            locations=[(coord.y, coord.x) for coord in line.coords],
            color=whale_color,
            weight=2.5,
            opacity=1
        ).add_to(m)

    # Afegir punts
    for _, row in whale_df.iterrows():
        icon = BeautifyIcon(
            icon='circle',
            border_color=whale_color,
            border_width=2,
            text_color=whale_color
        )
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"ID: {row['animal-id']}<br>Data: {row['deploy-on-date']}",
            tooltip=f"{row['animal-id']} ({row['deploy-on-date']})",
            icon=icon
        ).add_to(m)

# ---------------------------------------------------------
# 5) Llegenda
# ---------------------------------------------------------

legend_html = '''
<div style="position: fixed; 
     bottom: 50px; left: 50px; width: 200px; height: auto; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color:white; padding:10px;">
     <b>Colors de les balenes</b><br>
'''
for whale_id, color in whale_colors.items():
    legend_html += f'<i style="background:{color};width:10px;height:10px;display:inline-block;"></i> {whale_id}<br>'

legend_html += '</div>'
m.get_root().html.add_child(folium.Element(legend_html))

# ---------------------------------------------------------
# 6) Capes addicionals
# ---------------------------------------------------------

folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('Stamen Watercolor').add_to(m)
folium.TileLayer('cartodb positron').add_to(m)
folium.TileLayer('cartodb dark_matter').add_to(m)
folium.LayerControl().add_to(m)

# ---------------------------------------------------------
# 7) Desar resultat
# ---------------------------------------------------------

m.save('maps/whale_routes_map.html')

print("Mapa creat correctament a 'maps/whale_routes_map.html'")
