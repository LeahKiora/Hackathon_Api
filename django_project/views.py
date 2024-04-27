
import requests
from django.shortcuts import render 

def index(request):
  response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = response.json()
  fact = data['text']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']

  # This is the assignment for the Hackathon, 
  # Instructions: 
  # Use this API and randomize the students
  response2 = requests.get('https://freetestapi.com/api/v1/students') # Use this API
  data2 = response2.json()
  name = data2[0]['name']

  # response4 = requests.get('https://api.punkapi.com/v2/beers')
  # data4 = response4.json()
  # beer = data4[0]['text']

  response5 = requests.get('http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline')
  data5 = response5.json()
  product = data5[0]['name']

  response6 = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode')
  data6 = response6.json()
  joke = data6['setup']
  
  #i dont know why my code is not executing
  # response7 = requests.get('https://api.fisenko.net/v1/quotes/en?query=string&offset=0&limit=')
  # data7 = response7.json()
  # quote = data7[1]['quote']

  return render(request, 'templates/index.html', {'fact': fact, 'dog': dog,  'name': name, 'product': product, 'joke': joke})