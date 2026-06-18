import customtkinter
import Character_extraction as ce
import Image_extraction as ie
import Save_state_manipulation as ssm
import Button_functionality as bf
from pathlib import Path

#Complete sintetized functionality of frame for Killers and Survivors

class FunctionalGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, characters:list, character_name:str,save_file_name:str):
        super().__init__(master)

        self.save_name = save_file_name
        self.font = customtkinter.CTkFont(family="Roboto", size=15, weight="bold")
        self.character_name = character_name
        self.character = characters
        cleaned_names = [characters.replace('"','') for characters in characters]
        self.character_images = ie.extract_images(f"./Info/assets/Character assets/{character_name}",cleaned_names)
        self.icons = ie.other_images(f"./Info/assets/icons/")
        self.save_state = ssm.check_character_state(character_name,save_file_name)
        self.labels = []
        self.buttons_dict = {}

        column = 0
        row = 0

        for i in self.character[:-1]:

            self.grid_columnconfigure(column, weight=1)
            cleaned_name = i.replace('"','')

            #Button functionality for Killers

            if self.character_name == "Killers":
                char_label = customtkinter.CTkLabel(self, text=f"The {i}")
                if self.save_state[i] == 0:
                    char_button = customtkinter.CTkButton(self, 
                                                          image=self.character_images[cleaned_name], 
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], off_img=self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
                elif self.save_state[i] == 1:
                    char_button = customtkinter.CTkButton(self,
                                                          image=self.icons["dead survivor"],
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], off_img=self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
            
            #Button functionality for survivors

            elif self.character_name == "Survivors":
                char_label = customtkinter.CTkLabel(self, text=i, font=self.font)
                if self.save_state[i] == 0:
                    char_button = customtkinter.CTkButton(self, 
                                                          image=self.character_images[cleaned_name], 
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], off_img=self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
                elif self.save_state[i] == 1:
                    char_button = customtkinter.CTkButton(self,
                                                          image=self.icons["dead survivor"],
                                                          text="", 
                                                          fg_color="transparent",
                                                          command=lambda cn=i, on_img=self.character_images[cleaned_name], off_img=self.icons["dead survivor"]: bf.switch_image(self,button=self.buttons_dict[cn],
                                                                                  save=save_file_name,
                                                                                  character=cn,
                                                                                  on_image=on_img,
                                                                                  off_image=off_img,
                                                                                  char_type=character_name))
      
            char_button.grid(row=row+1, column=column, padx= 10, pady= (0,10))
            char_label.grid(row=row, column=column, padx= 10, pady= (0,10))
            
            char_button.image = self.character_images[cleaned_name]
            self.buttons_dict[i] = char_button

            if column == 3:
                row += 2
                column = 0
            else:
                column += 1 
            
            self.labels.append(char_label)

#Main menu frame that allows for changing between the killers and survivors

class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        killerbutton = customtkinter.CTkButton(self, text="killers", command= lambda: master.switch_window(MakeAndChooseSaves(master,char_type="Killers")))
        survivorbutton = customtkinter.CTkButton(self, text="survivors", command= lambda: master.switch_window(MakeAndChooseSaves(master,char_type="Survivors")))

        killerbutton.grid(row=1,column=1, padx= 10, pady= (0,10))
        survivorbutton.grid(row=1,column=2, padx= 10, pady= (0,10))

class MakeAndChooseSaves(customtkinter.CTkFrame):
    def __init__(self, master, char_type:str):
        super().__init__(master)

        self.row = 1

        def create_savefile():
            save_name = self.create_text.get()
            ssm.save_file_creation(char_type,save_name=save_name)
            if char_type == "Killers": 
                save_button = customtkinter.CTkButton(self, 
                                                    text=f"{save_name}",
                                                    command= lambda save=save_name, : master.switch_window(FunctionalGrid(master, 
                                                                                                        characters=ce.killer_list(), 
                                                                                                        character_name=char_type,
                                                                                                        save_file_name= save)))
            elif char_type == "Survivors" : 
                save_button = customtkinter.CTkButton(self, 
                                                    text=f"{save_name}",
                                                    command= lambda save=save_name, : master.switch_window(FunctionalGrid(master, 
                                                                                                        characters=ce.survivor_list(), 
                                                                                                        character_name=char_type,
                                                                                                        save_file_name= save)))   
            save_button.grid(row=self.row,column=0,padx= 10, pady= (10,10),sticky="ew")

            self.row += 1


        self.grid_columnconfigure(0, weight=1)
        self.save_path = f"./Saves/{char_type}"

        dir_path = Path(self.save_path)
        files_list = [i for i in dir_path.iterdir() if i.is_file()]

        for i in files_list:

            self.grid_rowconfigure(self.row, weight=1)
            save_name = str(i).replace(f"Saves\\{char_type}\\","")
            save_name = save_name.replace(".json","")
            if char_type == "Killers": 
                save_button = customtkinter.CTkButton(self, 
                                                    text=f"{save_name}",
                                                    command= lambda save=save_name, : master.switch_window(FunctionalGrid(master, 
                                                                                                        characters=ce.killer_list(), 
                                                                                                        character_name=char_type,
                                                                                                        save_file_name= save)))
            elif char_type == "Survivors" : 
                save_button = customtkinter.CTkButton(self, 
                                                    text=f"{save_name}",
                                                    command= lambda save=save_name, : master.switch_window(FunctionalGrid(master, 
                                                                                                        characters=ce.survivor_list(), 
                                                                                                        character_name=char_type,
                                                                                                        save_file_name= save)))                
            save_button.grid(row=self.row,column=0,padx= 10, pady= (10,10),sticky="ew")
            self.row += 1





        self.controls_frame = customtkinter.CTkFrame(self)
        self.controls_frame.grid(row=0, columnspan=3, sticky="ew")
        self.controls_frame.grid_columnconfigure(0, weight=1)
        self.controls_frame.grid_columnconfigure(1, weight=0)
        self.controls_frame.grid_columnconfigure(2, weight=0)

        self.create_text = customtkinter.CTkEntry(self.controls_frame, placeholder_text="this is where you put your save file name")
        self.create_button = customtkinter.CTkButton(self.controls_frame, text="Create Save file", command= lambda: create_savefile())

        self.create_text.grid(row=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.create_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


#Main Window class 

class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("900x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.funcgrid = MainMenu(self) 
        self.funcgrid.grid(row= 0, column= 0, padx= 0, pady= (10,0), sticky="nsew")


    def switch_window(self, frame_class):


        if self.funcgrid is not None:
            self.funcgrid.destroy()
        self.funcgrid = frame_class
        self.funcgrid.grid(row= 0, column= 0, padx= 0, pady= (10,0), sticky="nsew")


app = MainApp()

app.mainloop()