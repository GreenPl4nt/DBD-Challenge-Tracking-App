import customtkinter
import Character_extraction as ce
import Image_extraction as ie

#Complete sintetized functionality of frame for Killers and Survivors

class FunctionalGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, character:str, character_name:str):
        super().__init__(master)
        self.character_name = character_name
        self.character = character
        self.character_images = ie.extract_images(f"./Info/assets/Character assets/{character_name}",self.character)
        self.labels = []

        column = 0
        row = 0

        for i in self.character[:-1]:
            if self.character_name == "Killers":
                char_label = customtkinter.CTkLabel(self, text=f"The {self.character_name}")
            else:
                char_label = customtkinter.CTkLabel(self, text=character_name)
            char_button = customtkinter.CTkButton(self, image=self.character_images[i], text="", fg_color="transparent")
            char_button.grid(row=row+1, column=column, padx= 10, pady= (0,10))
            char_label.grid(row=row, column=column, padx= 10, pady= (0,10))
            
            if column == 3:
                row += 2
                column = 0
            else:
                column += 1 
            
            self.labels.append(char_label)
            
#Complete Window class sintetized for both Killers and Survivors

class FunctionalWindow(customtkinter.CTk):
    def __init__(self, char:str):
        super().__init__()
        self.char = char

        self.title(f"{self.char} Window")
        self.geometry("900x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        if self.char == "Survivors":
            self.funcgrid = FunctionalGrid(self, character=ce.survivor_list(), character_name=self.char)
        elif self.char == "Killers":
            self.funcgrid = FunctionalGrid(self, character=ce.killer_list(), character_name=self.char)

        self.funcgrid.grid(row= 0, column= 0, padx= 0, pady= (10,0), sticky="nsew")        

app = FunctionalWindow("Killers")

app.mainloop()