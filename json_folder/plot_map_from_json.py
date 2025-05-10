import json
import folium

# Step 1.1: Load JSON
# with open("radar_points.json", "r") as f:
#     data = json.load(f)

with open("json_folder/radar_points.json", "r") as f:
    data = json.load(f)

# Step 1.2: Compute map center
latitudes = [pt['latitude'] for pt in data]
longitudes = [pt['longitude'] for pt in data]
map_center = [sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes)]

# Step 1.3: Color mapping
def get_color(dBZ):
    if dBZ >= 60: return '#800026'
    elif dBZ >= 55: return '#BD0026'
    elif dBZ >= 50: return '#E31A1C'
    elif dBZ >= 45: return '#FC4E2A'
    elif dBZ >= 40: return '#FD8D3C'
    elif dBZ >= 35: return '#FEB24C'
    elif dBZ >= 30: return '#FED976'
    elif dBZ >= 25: return '#FFEDA0'
    elif dBZ >= 20: return '#D9F0A3'
    else: return '#A6D96A'

# Step 1.4: Create Folium map
m = folium.Map(location=map_center, zoom_start=7, tiles="cartodbpositron")

for pt in data:
    folium.CircleMarker(
        location=[pt['latitude'], pt['longitude']],
        radius=6,
        popup=f"Reflectivity: {pt['reflectivity']} dBZ",
        color=get_color(pt['reflectivity']),
        fill=True,
        fill_color=get_color(pt['reflectivity']),
        fill_opacity=0.8
    ).add_to(m)

# Step 1.5: Save map
m.save("reflectivity_map.html")
print("✅ reflectivity_map.html saved.")




