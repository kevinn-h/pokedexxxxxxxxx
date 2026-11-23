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
""" def pokedex():
    for item in data:
        pokemon=item["name"]
        print(pokemon)
pokedex() """

i = 0
def languages():
    global language
    print("Choose your language.")
    print("1. English")
    print("2. Chinese")
    print("3. French")
    print("4. Japanese")
    language_choice = input("Enter your choice: ").strip()

    language = {
        "1": "english",
        "2": "chinese",
        "3": "french",
        "4": "japanese"
    }

    language = language.get(language_choice, "english")

    print(f"You chose {language}.")

    for item in data:
        pokemon=item["name"]
        print(pokemon[language])

languages()
def type():
    william = input("what type of pokemon are you looking for?")
    matching_pokemon = []
    for i in range(len(data)):
        if william.capitalize() in data[i]["type"]:
            matching_pokemon.append(data[i]["name"][language])
    if len(matching_pokemon) == 0:
        print(f"pokemon type {william} doesn't exist")
    else:
        print(matching_pokemon)

type()

def partial_name():
    found = False
    name = input("what pokemon are you looking for?")
    for i in range(len(data)):
        if name.lower() in data[i]["name"][language].lower():
            print(data[i]["name"][language])
            found = True
        

partial_name()
            
    

