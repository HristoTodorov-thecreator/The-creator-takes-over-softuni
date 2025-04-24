from typing import List
from pokemon import Pokemon

class Trainer:

    def __init__(self,name):
        self.name = name
        self.t :List[Pokemon]= []


    def add_pokemon(self,pokemon: Pokemon):
        if pokemon in self.t:
            return f'This pokemon is already caught'

        self.t.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self,pokemon_name):
        for pokemon in self.t:
            if pokemon.name == pokemon_name:
                self.t.remove(pokemon)
                return f'You have released {pokemon_name}'



        return f'Pokemon is not caught'




    def trainer_data(self):

        pokemons_data = "\n".join([f'- {k.pokemon_details()}' for k in self.t])

        return f'Pokemon Trainer {self.name}\n' + \
            f'Pokemon count {len(self.t)}\n' + \
            f'{pokemons_data}'

