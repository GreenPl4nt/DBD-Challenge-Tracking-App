import json

# Opening the Json with the character information
with open("./Info/data/Character info.json", "r", encoding="utf-8") as file:
    data = json.load(file)


#Opening exactly the whole Killer and perk list or the individual Killer names

def killers():
    killers = data["Killer"]
    return killers

def killer_list():
    list = []
    for key in killers():
        list.append(key)
    return list

#Opening exactly the whole Survivor and perk list or the individual survivor names

def survivors():
    survivors = data["Survivors"]
    return survivors

def survivor_list():
    list = []
    for key in survivors():
        list.append(key)
    return list

print(survivor_list())

