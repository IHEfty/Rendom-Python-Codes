import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
import requests

key = "" #your OpenCage API key

def get_address_from_google_maps(lat, lng, google_maps_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={google_maps_key}"
    response = requests.get(url)
    result = response.json()
    
    if result['status'] == 'OK':
        return result['results'][0]['formatted_address']
    else:
        return "Address not found"

google_maps_key = "AIzaSyAOVYRIgupAurZup5y1PRh8Ismb1A3lLao" 

number = input("Please give your number: ")
try:
    new_number = phonenumbers.parse(number, "BD")
except phonenumbers.NumberParseException as e:
    print("Error parsing number:", e)
    exit(1)

location_description = geocoder.description_for_number(new_number, "en")
print("Location description:", location_description)

service_name = carrier.name_for_number(new_number, "en")
print("Service provider:", service_name)

geocoder_service = OpenCageGeocode(key)
result = geocoder_service.geocode(location_description)

if result:  
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    print("Latitude:", lat)
    print("Longitude:", lng)

    detailed_address = get_address_from_google_maps(lat, lng, google_maps_key)
    print("Detailed Address:", detailed_address)

    google_maps_url = f"https://www.google.com/maps/@{lat},{lng},15z"
    print("View location on Google Maps:", google_maps_url)

    my_map = folium.Map(location=[lat, lng], zoom_start=15)  
    folium.Marker([lat, lng], popup=detailed_address).add_to(my_map)

    my_map.save("location.html")
    print("Location tracking completed")
else:
    print("No location found for the given query.")
