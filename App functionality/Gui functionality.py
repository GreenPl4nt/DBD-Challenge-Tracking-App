import customtkinter
import Character_extraction as ce
import Image_extraction as ie


#Complete sintetized functionality of frame for Killers and Survivors

class FunctionalGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, characters:list, character_name:str):
        super().__init__(master)

        self.font = customtkinter.CTkFont(family="Roboto", size=15, weight="bold")
        self.character_name = character_name
        self.character = characters
        cleaned_names = [characters.replace('"','') for characters in characters]
        self.character_images = ie.extract_images(f"./Info/assets/Character assets/{character_name}",cleaned_names)
        self.labels = []

        column = 0
        row = 0

        for i in self.character[:-1]:
            if self.character_name == "Killers":
                char_label = customtkinter.CTkLabel(self, text=f"The {i}")
            else:
                char_label = customtkinter.CTkLabel(self, text=i, font=self.font)
            cleaned_name = i.replace('"','')
            char_button = customtkinter.CTkButton(self, image=self.character_images[cleaned_name], text="", fg_color="transparent")
            print(char_button)
            char_button.grid(row=row+1, column=column, padx= 10, pady= (0,10))
            char_label.grid(row=row, column=column, padx= 10, pady= (0,10))
            
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
        killerbutton = customtkinter.CTkButton(self, text="killers", command= lambda: master.switch_window(FunctionalGrid(master, characters=ce.killer_list(), character_name="Killers")))
        survivorbutton = customtkinter.CTkButton(self, text="survivors", command= lambda: master.switch_window(FunctionalGrid(master, characters=ce.survivor_list(), character_name="Survivors")))

        killerbutton.grid(row=1,column=1, padx= 10, pady= (0,10))
        survivorbutton.grid(row=1,column=2, padx= 10, pady= (0,10))
            
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