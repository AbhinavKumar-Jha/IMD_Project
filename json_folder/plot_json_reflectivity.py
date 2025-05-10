import json
import folium

# 🔹 Step 1: Load JSON file
# with open("radar_points.json", "r") as f:
#     data = json.load(f)

with open("json_folder/radar_points.json", "r") as f:
    data = json.load(f)



# 🔹 Step 2: Define color function based on reflectivity
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

# 🔹 Step 3: Calculate center of map
latitudes = [p['latitude'] for p in data]
longitudes = [p['longitude'] for p in data]
map_center = [sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes)]

# 🔹 Step 4: Create base map
m = folium.Map(location=map_center, zoom_start=7, tiles="cartodbpositron")

# 🔹 Step 5: Add circle markers
for point in data:
    folium.CircleMarker(
        location=[point['latitude'], point['longitude']],
        radius=4 + (point['reflectivity'] / 10),  # Size based on reflectivity
        color=get_color(point['reflectivity']),
        fill=True,
        fill_color=get_color(point['reflectivity']),
        fill_opacity=0.8,
        tooltip=f"{point.get('location', 'Unknown')}: {point['reflectivity']} dBZ"
    ).add_to(m)

# 🔹 Step 6: Save map
m.save("reflectivity_map_from_json.html")
print("✅ Map created: reflectivity_map_from_json.html")
