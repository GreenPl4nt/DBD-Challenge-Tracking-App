import customtkinter
from PIL import Image

#Creates an image, might make it so that the images scale with the window size

def other_images(path:str):
     icons = ["dead survivor"]
     img_dict = {}
     for i in icons:
          image = customtkinter.CTkImage(light_image= Image.open(f"{path}/{i}.png"),
                                        size=(242,242))
          img_dict[i] = image

     return img_dict

def extract_images(path:str,clist:list):
    img_dict = {}
    for i in clist [:-1]:
         image = customtkinter.CTkImage(light_image= Image.open(f"{path}/{i}.png"),
                                        size=(242,242))
         img_dict[i] = image
    return img_dict


