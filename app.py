import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
moves = open("./moves.json", encoding= "utf8")

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.

# Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

def languages():
    print("Choose a language:")
    print("1. English")
    print("2. Chinese")
    print("3. Japanese")
    print("4. French")
    language_choice = input("Enter your choice: ").strip()

    language = {
        "1": "english",
        "2": "chinese",
        "3": "japanese",
        "4": "french"
    }

    language = language.get(language_choice, "english")

    print(f"You chose {language}.")
    return
    

def getPoke():

       
        pokemon_name = input("Which pokemon are you looking for? ").strip()
       
        matches = []

        for pokemon in data:
            if not isinstance(pokemon, dict):
                continue
            names = pokemon.get("name", {})

            if languages == "french":
                name = names.get("french", "")
            elif languages == "english":
                name = names.get("english", "")
            elif languages == "chinese":
                name = names.get("chinese", "")
            elif languages == "japanese":
                name = names.get("japanese", "")
            else:
                continue

            if name.lower().startswith(pokemon_name.lower()):
                matches.append(name)

            
        

        if matches:
            print("Matches found:")
            for name in matches:
                print(name)
                
            print(f"No Pokémon found matching '{pokemon_name}'.")




def pokedex():
    languages()
    getPoke()
pokedex()

   