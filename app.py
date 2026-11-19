import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.

# Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
def get_choice(z):
    while True:
        user_input = input("enter the pokemon you were looking for:")
        if user_input == 0:
            print("try again")
        else: 
            matches = [item for item in z if item.lower() == user_input.lower()]
            if matches:
                return matches[0]
            else:
                print("invalid try again.")


def languages():
    print("Choose your language.")
    print("1. English")
    print("2. Chinese")
    print("3. French")
    print("4. Japanese")
    language_choice = input("Enter your choice: ").strip()

    language = {
        "1": "english",
        "2": "chinese",
        "3": "japanese",
        "4": "french"
    }

    language = language.get(language_choice, "english")

    print(f"You chose {language}.")

    for item in data:
        pokemon=item["name"]
        print(pokemon[language])

    
    
def find_by_type():
    search_type = input("What type of Pokemon are you looking for? ")
    

    for pokemon in data:
        pokemon_types = pokemon["type"]
        print(pokemon_types[search_type])

find_by_type()
