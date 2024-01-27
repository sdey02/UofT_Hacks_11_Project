import cohere
from json import load

co = cohere.Client(load(open("config.json", "r"))["token"])

user_input = "Hello I am in a random country today. We are going to figure otu what country i am in by the acitivites that I do throughout the day. I am in Brazil for some coffee this morning. I want to see the birds in Rio De Janeiro."

location = co.generate(
  model='command',
  prompt=f'I am going to give you some text. I want you to output one line of information from it in the form "City, Country". {user_input}',
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')

location_data = format(location.generations[0].text)

caption_user_input = "Hello I am in a random country today. We are going to figure otu what country i am in by the acitivites that I do throughout the day. I am in Brazil for some coffee this morning. I want to see the birds in Rio De Janeiro."

caption = co.generate(
  model='command',
  prompt=f'I am going to give you some text describing the events that took place in a photo. Using that text, output only a short, catchy caption for the photo inside double quotes.{caption_user_input}',
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')

caption_data = format(caption.generations[0].text)

print(caption_data)