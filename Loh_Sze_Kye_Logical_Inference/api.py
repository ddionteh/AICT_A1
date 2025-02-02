# HERE Traffic API, error 403 forbidden. Gonna create fake data instead.

import requests
import folium

# HERE API endpoint for traffic flow
url = "https://traffic.ls.hereapi.com/traffic/6.3/flow.json"

# Your HERE API key
api_key = ""

# Bounding box for Singapore
bbox = "1.4707,103.6048,1.1656,103.9912"

# Parameters for the API request
params = {
    "apiKey": api_key,
    "bbox": bbox,
    "responseattributes": "sh,fc"
}

# Make the API request
response = requests.get(url, params=params)

if response.status_code == 200:
    traffic_data = response.json()
    
    # Create a map centered on Singapore
    singapore_map = folium.Map(location=[1.3521, 103.8198], zoom_start=12)

    # Parse traffic flow data and add to the map
    for rw in traffic_data.get("RWS", []):
        for fi in rw.get("RW", [])[0].get("FIS", [])[0].get("FI", []):
            for shp in fi.get("SHP", []):
                coordinates = [(point.get("lat"), point.get("lon")) for point in shp.get("value", [])]
                folium.PolyLine(coordinates, color="red", weight=2.5, opacity=1).add_to(singapore_map)

    # Save the map to an HTML file
    singapore_map.save("singapore_traffic.html")
    print("Map saved to 'singapore_traffic.html'")
else:
    print(f"Error: {response.status_code} - {response.text}")