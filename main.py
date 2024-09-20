import phonenumbers
import opencage
import folium
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_number,"en")
print(location)

from phonenumbers import carrier
service_number = phonenumbers.parse(number , "RO")
print(carrier.name_for_number(service_number , "en"))

from opencage.geocoder import  OpenCageGeocode

key = '40417dfa6c1545b3a23c21b65c7fd9da'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat , lng], zoom_start= 9)
folium.Marker([lat , lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")


