import customtkinter
from pathlib import Path
import Save_state_manipulation as ssm

class MakeAndChooseSaves(customtkinter.CTkFrame):
    def __init__(self, master, char_type:str):
        super().__init__(master)

        self.row = 0

        def create_savefile():
            save_name = create_text.get()
            ssm.save_file_creation(char_type,save_name=save_name)
            save_button = customtkinter.CTkButton(self, 
                                                  text=f"{save_name}")
            save_button.grid(row=self.row,column=0,padx= 10, pady= (10,10),sticky="ew")

            self.row += 1

   

        self.grid_columnconfigure(0, weight=1)
        self.save_path = f"./Saves/{char_type}"

        dir_path = Path(self.save_path)
        files_list = [i for i in dir_path.iterdir() if i.is_file()]

        for i in files_list:

            self.grid_rowconfigure(self.row, weight=1)
            save_name = str(i).replace(f"Saves\\{char_type}\\","")
            save_button = customtkinter.CTkButton(self, 
                                                  text=f"{save_name.replace(".json","")}")
            save_button.grid(row=self.row,column=0,padx= 10, pady= (10,10),sticky="ew")
            self.row += 1
        create_text = customtkinter.CTkEntry(master,placeholder_text="this is where you put your save file name")
        create_button = customtkinter.CTkButton(master,text="Create Save file", command= lambda: create_savefile())

        create_button.grid(row=self.row, column=1, padx= 10, pady= (10,10), sticky="ew")
        create_text.grid(row=self.row, column=0, padx= 10, pady= (10,10), sticky="ew")


            
class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("900x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.funcgrid = MakeAndChooseSaves(self, "Killers") 
        self.funcgrid.grid(row= 0, column= 0, padx= 100, pady= (100,20), sticky="nsew")

app = MainApp()

app.mainloop()

        
