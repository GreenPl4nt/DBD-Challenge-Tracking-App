import Character_extraction as ce
import Image_extraction as ie
import json

def save_file_creation(character_type:str, save_name:str):
    character_dict = {}

    if character_type == "Killer":
        character_list = ce.killer_list()
    elif character_type == "Survivor":
        character_list = ce.survivor_list()
    
    for i in character_list[:-1]:
        character_dict[i] = 0

    with open(f"./Saves/{save_name}.json", "w", encoding="utf-8") as f:
        json.dump(character_dict,f,indent=4)

save_file_creation("Survivor", "test save file")