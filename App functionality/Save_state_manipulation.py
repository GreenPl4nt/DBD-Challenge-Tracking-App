import Character_extraction as ce
import Image_extraction as ie
import json
import os
from pathlib import Path

save_folder = Path(os.getenv("LOCALAPPDATA")) / "DBD Challenge Tracking App" / "Saves"


def save_file_creation(character_type:str, save_name:str):
    character_dict = {}

    if character_type == "Killers":
        character_list = ce.killer_list()
    elif character_type == "Survivors":
        character_list = ce.survivor_list()
    
    for i in character_list[:-1]:
        character_dict[i] = 0

    with open(f"{save_folder}/{character_type}/{save_name}.json", "w", encoding="utf-8") as f:
        json.dump(character_dict,f,indent=4)

def modify_character_state(char_type:str,save_name:str,character:str,new_state:int):

    path = f'{save_folder}/{char_type}/{save_name}.json'

    with open(path,'r') as file:
        data = json.load(file)

    data[character] = new_state

    with open(path,'w') as file:
        json.dump(data, file, indent=4)


def check_character_state(char_type:str,save_name:str):
    path = f'{save_folder}/{char_type}/{save_name}.json'
    with open(path,'r') as file:
        data = json.load(file)
    return data

