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
import spacy

def test(caption):
    #* Cohere model extracts location from user input (Deprecated Switching to SpaCy to get location data)
    # location = co.generate(   
    #     model='command',
    #     prompt=f'I am going to give you some text. I want you to output one line of information from it in the form "City, Country". {user_input}',
    #     max_tokens=300,
    #     temperature=0.9,
    #     k=0,
    #     stop_sequences=[],
    #     return_likelihoods='NONE')

    # location_data = format(location.generations[0].text)

    #! spaCY extrats location data from sentance.
    nlp = spacy.load('en_core_web_sm')
    array = []

    doc = nlp(caption)
    for entity in doc.ents:
        if entity.label_ == 'GPE':
            array.append(entity.text)

    location = ", ".join(array)
    
    #! Cohere model generates a caption for photo.
    co = cohere.Client(load(open("keys/config.json", "r"))["token"]) #! Cohere API Key 

    caption = co.generate(
        model='command',
        prompt=f'I am going to give you some text describing the events that took place in a photo. Using that text, output only a short, catchy caption for the photo inside double quotes.{caption}',
        max_tokens=300,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    
    caption_data = format(caption.generations[0].text)

    #! Geopy longitude and lattitude conversion.
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    
    geolocator = Nominatim(user_agent="my_request")
    location_geopy = geolocator.geocode(location)
    latitude = location_geopy.latitude
    longitude = location_geopy.longitude
    

    return [caption_data, latitude, longitude]