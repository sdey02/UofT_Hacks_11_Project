import cohere
from json import load
import geopy
from geopy.geocoders import Nominatim
import requests
import ssl
import certifi
import geopy.geocoders
import sys
import json


co = cohere.Client(load(open("keys/config.json", "r"))["token"]) #! Cohere API Key 

#! Cohere model extracts location from user input.
# location = co.generate(   
#     model='command',
#     prompt=f'I am going to give you some text. I want you to output one line of information from it in the form "City, Country". {user_input}',
#     max_tokens=300,
#     temperature=0.9,
#     k=0,
#     stop_sequences=[],
#     return_likelihoods='NONE')

# location_data = format(location.generations[0].text)

#! Cohere model generates a caption for photo.
# caption = co.generate(
#     model='command',
#     prompt=f'I am going to give you some text describing the events that took place in a photo. Using that text, output only a short, catchy caption for the photo inside double quotes.{user_input}',
#     max_tokens=300,
#     temperature=0.9,
#     k=0,
#     stop_sequences=[],
#     return_likelihoods='NONE')

# caption_data = format(caption.generations[0].text)

#! Geopy longitude and lattitude conversion.
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

# geolocator = Nominatim(user_agent="my_request")
# location_geopy = geolocator.geocode(location_data)
# latitude = location_geopy.latitude
# longitude = location_geopy.longitude

# print(latitude)
# print(longitude)

def test(caption):
    location = co.generate(   
        model='command',
        prompt=f'I am going to give you some text. I want you to output one line of information from it in the form "City, Country". {caption}',
        max_tokens=300,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    
    location_data = format(location.generations[0].text)
    
    caption = co.generate(
        model='command',
        prompt=f'I am going to give you some text describing the events that took place in a photo. Using that text, output only a short, catchy caption for the photo inside double quotes.{caption}',
        max_tokens=300,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    
    caption_data = format(caption.generations[0].text)
    
    geolocator = Nominatim(user_agent="my_request")
    location_geopy = geolocator.geocode(location_data)
    latitude = location_geopy.latitude
    longitude = location_geopy.longitude

    return (latitude, longitude, caption_data)