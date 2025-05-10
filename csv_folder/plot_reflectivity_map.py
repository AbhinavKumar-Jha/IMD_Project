# import pandas as pd
# import folium

# # Load data
# df = pd.read_csv("radar_points.csv")
# df = df.dropna(subset=['latitude', 'longitude', 'reflectivity'])

# # Define reflectivity to color function
# def get_color(dBZ):
#     if dBZ >= 55: return "#800026"
#     elif dBZ >= 50: return "#BD0026"
#     elif dBZ >= 45: return "#E31A1C"
#     elif dBZ >= 40: return "#FC4E2A"
#     elif dBZ >= 35: return "#FD8D3C"
#     elif dBZ >= 30: return "#FEB24C"
#     elif dBZ >= 25: return "#FED976"
#     else: return "#FFEDA0"

# # Create map centered on average location
# map_center = [df['latitude'].mean(), df['longitude'].mean()]
# m = folium.Map(location=map_center, zoom_start=7, tiles="cartodbpositron")

# # Add points
# for _, row in df.iterrows():
#     folium.CircleMarker(
#         location=[row['latitude'], row['longitude']],
#         radius=6,
#         popup=f"{row['reflectivity']} dBZ",
#         color=get_color(row['reflectivity']),
#         fill=True,
#         fill_color=get_color(row['reflectivity']),
#         fill_opacity=0.8
#     ).add_to(m)

# # Save map
# m.save("reflectivity_map.html")
# print("✅ Map saved as reflectivity_map.html")





# import pandas as pd
# import folium

# # Load CSV
# df = pd.read_csv("radar_points.csv")
# df = df.dropna(subset=['latitude', 'longitude', 'reflectivity'])

# # Reflectivity to color mapping
# def get_color(dBZ):
#     if dBZ >= 60: return '#800026'  # dark red
#     elif dBZ >= 55: return '#BD0026'
#     elif dBZ >= 50: return '#E31A1C'
#     elif dBZ >= 45: return '#FC4E2A'
#     elif dBZ >= 40: return '#FD8D3C'
#     elif dBZ >= 35: return '#FEB24C'
#     elif dBZ >= 30: return '#FED976'
#     elif dBZ >= 25: return '#FFEDA0'
#     elif dBZ >= 20: return '#D9F0A3'
#     else: return '#A6D96A'  # light green

# # Create map
# map_center = [df['latitude'].mean(), df['longitude'].mean()]
# m = folium.Map(location=map_center, zoom_start=7, tiles="cartodbpositron")

# # Add points with dynamic color
# for _, row in df.iterrows():
#     folium.CircleMarker(
#         location=[row['latitude'], row['longitude']],
#         radius=6,
#         popup=f"Reflectivity: {row['reflectivity']} dBZ",
#         color=get_color(row['reflectivity']),
#         fill=True,
#         fill_color=get_color(row['reflectivity']),
#         fill_opacity=0.8
#     ).add_to(m)

# # Save
# m.save("reflectivity_map.html")
# print("✅ Reflectivity map saved as reflectivity_map.html")




import pandas as pd
import folium
from branca.element import Template, MacroElement

# Load CSV
# df = pd.read_csv("radar_points.csv")

df = pd.read_csv("csv_folder/radar_points.csv")

df = df.dropna(subset=['latitude', 'longitude', 'reflectivity'])

# Reflectivity to color mapping
def get_color(dBZ):
    if dBZ >= 60: return '#800026'  # dark red
    elif dBZ >= 55: return '#BD0026'
    elif dBZ >= 50: return '#E31A1C'
    elif dBZ >= 45: return '#FC4E2A'
    elif dBZ >= 40: return '#FD8D3C'
    elif dBZ >= 35: return '#FEB24C'
    elif dBZ >= 30: return '#FED976'
    elif dBZ >= 25: return '#FFEDA0'
    elif dBZ >= 20: return '#D9F0A3'
    else: return '#A6D96A'  # light green

# Create map
map_center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=7, tiles="cartodbpositron")

# Add points with dynamic color
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=6,
        popup=f"Reflectivity: {row['reflectivity']} dBZ",
        color=get_color(row['reflectivity']),
        fill=True,
        fill_color=get_color(row['reflectivity']),
        fill_opacity=0.8
    ).add_to(m)



# Add Legend
legend_html = """
{% macro html(this, kwargs) %}
<div style='
    position: fixed; 
    bottom: 30px; left: 10px; width: 180px; height: auto; 
    background-color: white; 
    border:2px solid grey; 
    z-index:9999; 
    font-size:14px;
    padding: 10px;
'>
<b>Reflectivity (dBZ)</b><br>
<i style="background:#800026;width:20px;height:10px;display:inline-block;"></i> ≥ 60<br>
<i style="background:#BD0026;width:20px;height:10px;display:inline-block;"></i> 55–59<br>
<i style="background:#E31A1C;width:20px;height:10px;display:inline-block;"></i> 50–54<br>
<i style="background:#FC4E2A;width:20px;height:10px;display:inline-block;"></i> 45–49<br>
<i style="background:#FD8D3C;width:20px;height:10px;display:inline-block;"></i> 40–44<br>
<i style="background:#FEB24C;width:20px;height:10px;display:inline-block;"></i> 35–39<br>
<i style="background:#FED976;width:20px;height:10px;display:inline-block;"></i> 30–34<br>
<i style="background:#FFEDA0;width:20px;height:10px;display:inline-block;"></i> 25–29<br>
<i style="background:#D9F0A3;width:20px;height:10px;display:inline-block;"></i> 20–24<br>
<i style="background:#A6D96A;width:20px;height:10px;display:inline-block;"></i> < 20<br>
</div>
{% endmacro %}
"""

legend = MacroElement()
legend._template = Template(legend_html)
m.get_root().add_child(legend)

# Save
m.save("reflectivity_map.html")
print("✅ Reflectivity map with legend saved as reflectivity_map.html")
