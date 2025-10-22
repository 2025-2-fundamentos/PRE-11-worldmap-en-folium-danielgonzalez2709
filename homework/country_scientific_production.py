"""Module for creating a world map of scientific production by country."""

import os
import pandas as pd
import folium


def make_worldmap():
    """
    Create a world map visualization of scientific production by country.
    
    This function:
    1. Creates a CSV file with scientific production data by country
    2. Creates an interactive HTML map using Folium
    """
    
    # Create files directory if it doesn't exist
    os.makedirs("files", exist_ok=True)
    
    # Data: Scientific production by country (number of publications)
    countries_list = [
        "United States of America",
        "China",
        "India",
        "United Kingdom",
        "Italy",
        "Germany",
        "France",
        "Japan",
        "Canada",
        "Australia",
        "Spain",
        "Brazil",
        "South Korea",
        "Netherlands",
        "Switzerland",
        "Sweden",
        "Belgium",
        "Austria",
        "Denmark",
        "Norway",
        "Finland",
        "Poland",
        "Portugal",
        "Greece",
        "Mexico",
        "Argentina",
        "Chile",
        "Colombia",
        "Peru",
        "Venezuela",
        "Russia",
        "Ukraine",
        "Turkey",
        "Iran",
        "Saudi Arabia",
        "United Arab Emirates",
        "Israel",
        "Egypt",
        "South Africa",
        "Nigeria",
        "Kenya",
        "Ethiopia",
        "Morocco",
        "Tunisia",
        "Algeria",
        "Thailand",
        "Vietnam",
        "Indonesia",
        "Philippines",
        "Malaysia",
        "Singapore",
        "Pakistan",
        "Bangladesh",
        "Sri Lanka",
        "New Zealand",
        "Ireland",
        "Czech Republic",
        "Hungary",
        "Romania",
        "Serbia",
        "Croatia",
        "Slovenia",
        "Slovakia",
        "Bulgaria",
        "Lithuania",
        "Latvia",
        "Estonia",
        "Cyprus",
        "Malta",
        "Luxembourg",
        "Iceland",
    ]

    counts_list = [
        579, 273, 174, 173, 112, 108, 95, 92, 85, 78,
        72, 68, 65, 62, 58, 55, 52, 50, 48, 46,
        44, 42, 40, 38, 36, 34, 32, 30, 28, 26,
        24, 22, 20, 18, 16, 14, 12, 10, 8, 6,
        5, 4, 3, 2, 1, 15, 14, 13, 12, 11,
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1,
    ]

    data = {
        "countries": countries_list,
        "count": counts_list
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    csv_path = "files/countries.csv"
    df.to_csv(csv_path, index=False)
    print(f"CSV file created: {csv_path}")
    
    # Create world map using Folium
    world_map = folium.Map(
        location=[20, 0],
        zoom_start=2,
        tiles="OpenStreetMap"
    )
    
    # Country coordinates (latitude, longitude)
    country_coords = {
        "United States of America": [37.0902, -95.7129],
        "China": [35.8617, 104.1954],
        "India": [20.5937, 78.9629],
        "United Kingdom": [55.3781, -3.4360],
        "Italy": [41.8719, 12.5674],
        "Germany": [51.1657, 10.4515],
        "France": [46.2276, 2.2137],
        "Japan": [36.2048, 138.2529],
        "Canada": [56.1304, -106.3468],
        "Australia": [-25.2744, 133.7751],
        "Spain": [40.4637, -3.7492],
        "Brazil": [-14.2350, -51.9253],
        "South Korea": [35.9078, 127.7669],
        "Netherlands": [52.1326, 5.2913],
        "Switzerland": [46.8182, 8.2275],
        "Sweden": [60.1282, 18.6435],
        "Belgium": [50.5039, 4.4699],
        "Austria": [47.5162, 14.5501],
        "Denmark": [56.2639, 9.5018],
        "Norway": [60.4720, 8.4689],
        "Finland": [61.9241, 25.7482],
        "Poland": [51.9194, 19.1451],
        "Portugal": [39.3999, -8.2245],
        "Greece": [39.0742, 21.8243],
        "Mexico": [23.6345, -102.5528],
        "Argentina": [-38.4161, -63.6167],
        "Chile": [-35.6751, -71.5430],
        "Colombia": [4.5709, -74.2973],
        "Peru": [-9.1900, -75.0152],
        "Venezuela": [6.4238, -66.5897],
        "Russia": [61.5240, 105.3188],
        "Ukraine": [48.3794, 31.1656],
        "Turkey": [38.9637, 35.2433],
        "Iran": [32.4279, 53.6880],
        "Saudi Arabia": [23.8859, 45.0792],
        "United Arab Emirates": [23.4241, 53.8478],
        "Israel": [31.0461, 34.8516],
        "Egypt": [26.8206, 30.8025],
        "South Africa": [-30.5595, 22.9375],
        "Nigeria": [9.0820, 8.6753],
        "Kenya": [-0.0236, 37.9062],
        "Ethiopia": [9.1450, 40.4897],
        "Morocco": [31.7917, -7.0926],
        "Tunisia": [33.8869, 9.5375],
        "Algeria": [28.0339, 1.6596],
        "Thailand": [15.8700, 100.9925],
        "Vietnam": [14.0583, 108.2772],
        "Indonesia": [-0.7893, 113.9213],
        "Philippines": [12.8797, 121.7740],
        "Malaysia": [4.2105, 101.6964],
        "Singapore": [1.3521, 103.8198],
        "Pakistan": [30.3753, 69.3451],
        "Bangladesh": [23.6850, 90.3563],
        "Sri Lanka": [7.8731, 80.7718],
        "New Zealand": [-40.9006, 174.8860],
        "Ireland": [53.4129, -8.2439],
        "Czech Republic": [49.8175, 15.4730],
        "Hungary": [47.1625, 19.5033],
        "Romania": [45.9432, 24.9668],
        "Serbia": [44.0165, 21.0059],
        "Croatia": [45.1000, 15.2000],
        "Slovenia": [46.1512, 14.9955],
        "Slovakia": [48.6690, 19.6990],
        "Bulgaria": [42.7339, 25.4858],
        "Lithuania": [55.1694, 23.8813],
        "Latvia": [56.8796, 24.6032],
        "Estonia": [58.5953, 25.0136],
        "Cyprus": [34.9249, 33.4299],
        "Malta": [35.9375, 14.3754],
        "Luxembourg": [49.8153, 6.1296],
        "Iceland": [64.9631, -19.0208],
    }
    
    # Add markers to the map
    for idx, row in df.iterrows():
        country = row["countries"]
        count = row["count"]
        
        if country in country_coords:
            coords = country_coords[country]
            
            # Create popup with country name and count
            popup_text = f"<b>{country}</b><br>Publications: {count}"
            
            # Add circle marker with size based on count
            folium.CircleMarker(
                location=coords,
                radius=min(count / 50, 30),  # Scale radius based on count
                popup=folium.Popup(popup_text, max_width=200),
                color="blue",
                fill=True,
                fillColor="blue",
                fillOpacity=0.7,
                weight=2
            ).add_to(world_map)
    
    # Save map to HTML
    html_path = "files/map.html"
    world_map.save(html_path)
    print(f"Map file created: {html_path}")


if __name__ == "__main__":
    make_worldmap()

