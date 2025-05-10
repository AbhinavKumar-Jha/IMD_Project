# import matplotlib.pyplot as plt
# import pandas as pd

# # Define the data
# data = {
#     'latitude': [22.50821, 22.51071, 22.51007, 22.49501, 22.49483,
#                  22.47405, 22.47347, 22.47290, 22.49723, 22.49678],
#     'longitude': [88.41649, 88.40481, 88.40394, 88.36797, 88.36688,
#                   86.55335, 86.54366, 86.53397, 86.57138, 86.56168],
#     'reflectivity': [40.49275, 48, 43.08571, 50, 48.45,
#                      40.35714, 42.07143, 42.57143, 41.14130, 40.61956]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Plot
# plt.figure(figsize=(10, 6))
# scatter = plt.scatter(df['longitude'], df['latitude'], c=df['reflectivity'], cmap='viridis', s=100, edgecolor='k')
# plt.colorbar(scatter, label='Reflectivity (dBZ)')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Reflectivity over Latitude and Longitude')
# plt.grid(True)
# plt.tight_layout()
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
# df = pd.read_csv("radar_points.csv")

df = pd.read_csv("csv_folder/radar_points.csv")


# Check for missing values and drop them (optional but recommended)
df = df.dropna(subset=['latitude', 'longitude', 'reflectivity'])

# Create scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['longitude'], df['latitude'], 
                      c=df['reflectivity'], cmap='viridis', 
                      s=100, edgecolor='k')

# Add colorbar and labels
plt.colorbar(scatter, label='Reflectivity (dBZ)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Reflectivity over Latitude and Longitude')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()


