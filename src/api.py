import requests
from pydantic import BaseModel



class PokemonSchame(BaseModel): #contrato de dados, schema de dados, View
    name: str
    type: str


    class Config:
        from_atributees = True

def pegar_pokemon(id: int) -> PokemonSchame:

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data= response.json()

    data_types =  data['types']
    types_list =[]
    for type_info in data_types:
        types_list.append(type_info['type']['name'])


    types = ' , '.join(types_list)
    return PokemonSchame(name=data['name'] , type=types)


print(pegar_pokemon(12))
print(pegar_pokemon(25))

