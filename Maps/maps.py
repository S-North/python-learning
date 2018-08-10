import folium, pandas

# crate a map with location and zoom, export to test.html

map = folium.Map(location=[51.455, -0.03], zoom_start = 15)

print(map)
print(map.save('test.html'))

# new map with markers

map2 = map = folium.Map(location=[51.455, -0.03], zoom_start = 15, tiles = 'Stamen Terrain')

print(map2)
print(map2.save('test2.html'))

# map with diferent tile, popups & a click co-ords window
##
map3 = folium.Map(location = [51.455, -0.03], zoom_start = 15, tiles = 'stamenwatercolor') # lol @ watercolours
folium.Marker(location = [51.4551, -0.031], popup = 'I am so lost', icon = folium.Icon(icon = 'cloud')).add_to(map3)
folium.Marker(location = [51.455, -0.03], popup = 'But I can see you', icon = folium.Icon(color = 'green')).add_to(map3)
map3.add_child(folium.LatLngPopup())

print(map3)
print(map3.save('test3.html'))

## using pandas to read map data from a csv
##

map4 = folium.Map(location=[51.455, -0.03], zoom_start = 14, tiles = 'Stamen Terrain')
df = pandas.read_csv('locations.csv')

for lat,lon,name in zip(df['LAT'], df['LNG'], df['TEXT']):      # introducing the ZIP function
    folium.Marker(
        location=[lat, lon],
        popup = name,
        icon = folium.Icon(icon = 'cloud')
        ).add_to(map4)

print(map4.save('test4.html'))

## modifying markers with data
#

map4 = folium.Map(location=[51.455, -0.03], zoom_start = 14, tiles = 'Stamen Terrain')
df = pandas.read_csv('locations.csv')
print(df)

for lat, lon, name, allegiance, strength in zip(df['LAT'], df['LNG'], df['TEXT'], df['ALLEGIANCE'], df['STRENGTH']):
    folium.Marker(                          # introducing the ZIP function
        location=[lat, lon], popup = name, icon = folium.Icon
        (color = 'green' if allegiance == "Frogs" else 'blue',
        icon = 'cloud' if strength in range(20, 600) else 'home')
        ).add_to(map4)

print(map4.save('test4.html'))

# placing the data visualisations in a function
#

df = pandas.read_csv('locations.csv')
# take the average location
latmean = df['LAT'].mean()
lonmean = df['LNG'].mean()
# use the mean location to centre the map
map4 = folium.Map(location=[latmean, lonmean], zoom_start = 14, tiles = 'stamenwatercolor')

def strength_icon(strength):
    if strength in range(0, 4):
        icon = 'home'
    elif strength in range(5, 10):
        icon = 'flag'
    elif strength in range(11, 30):
        icon = 'bookmark'
    else:
        icon = 'star'
    return icon

for lat, lon, name, allegiance, strength in zip(df['LAT'], df['LNG'], df['TEXT'], df['ALLEGIANCE'], df['STRENGTH']):
    folium.Marker(                          # introducing the ZIP function
        location=[lat, lon], popup = name, icon = folium.Icon
        (color = 'green' if allegiance == "Frogs" else 'blue',
        #icon = 'flag')
        icon = strength_icon(strength))
        ).add_to(map4)

print(map4.save('test4.html'))