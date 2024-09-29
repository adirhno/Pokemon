import json
import requests

def fetch_pokemon(name):
   response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
   responseData = response.json()['species']
   print(f'{responseData['name']}')

   with open ('pokemons.json', 'r+') as dataFile:
    data = json.load(dataFile) 
    data.append(responseData)
    dataFile.seek(0)
    json.dump(data,dataFile, indent=4 )
    


def choose_random_pokemon():
   response = requests.get('https://pokeapi.co/api/v2/pokemon/')
   from random import randrange
   pokemon_choosen = response.json()['results'][randrange(10)]['name']
   return pokemon_choosen
   


# with open ('pokemons.json', 'w+') as dataFromJson:
#   json.dump(response.json()['results'][:5], dataFromJson,indent= 4 )


def load_json():
   with open ('pokemons.json', 'r+') as file:
    pokemons = json.load(file)
   return pokemons    


def find_pokemon(pokemon):
     pokemons = load_json()
     for i in range(len(pokemons)):
      if pokemons[i]['name'] == pokemon:
         print(pokemons[i]['name'])
         return
        
     fetch_pokemon(pokemon) 

       
      
def main():
   ans = input('would you like to draw a Pokémon?')
   while ans.lower() != 'yes' or ans.lower() != 'no':
    if ans.lower() == 'yes':      
      find_pokemon(choose_random_pokemon())
      break
    elif ans.lower() == 'no':
     print('its your loss ;)')
     break
    else:
     print('please enter a valid answer')
     ans = input('would you like to draw a Pokémon?')
   
main()



