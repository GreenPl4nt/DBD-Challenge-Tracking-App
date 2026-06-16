import customtkinter
import Character_extraction as ce
import Image_extraction as ie

#Creates the scrollable frame with the killers of dbd

class Killergrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master,killers):
        super().__init__(master)
        self.killers = killers
        self.killer_images = ie.extract_images("./Info/assets/Character assets/Killers",self.killers)
        self.labels = []

        column = 0
        row = 0

        for killers in self.killers[:-1]:

            killerlabel = customtkinter.CTkLabel(self,text=f"The {killers}")
            killerbutton = customtkinter.CTkButton(self, image=self.killer_images[killers], text="", fg_color="transparent")
            killerbutton.grid(row=row+1,column=column, padx=10, pady=(0,10),)
            killerlabel.grid(row=row, column=column, padx= 10, pady=(0,10),)
            if column == 3:
                row += 2
                column = 0
            else:
                column += 1

            self.labels.append(killerlabel)
        


class Survivorgrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master,survivors):
        super().__init__(master)
        self.survivors = survivors
        self.survivor_images = ie.extract_images("./Info/assets/Character assets/Survivors",self.survivors)
        self.labels = []

        column = 0
        row = 0

        for survivors in self.survivors[:-1]:

            survivorlabel = customtkinter.CTkLabel(self,text=f"{survivors}")
            survivorbutton = customtkinter.CTkButton(self, image=self.survivor_images[survivors], text="", fg_color="transparent")
            survivorbutton.grid(row=row+1,column=column, padx=10, pady=(0,10),)
            survivorlabel.grid(row=row, column=column, padx= 10, pady=(0,10),)
            if column == 3:
                row += 2
                column = 0
            else:
                column += 1

            self.labels.append(survivorlabel)

        
#Creates the window for killers, might change to general funcionality that changes depending on what is pressed

class KillerWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Killer Window")
        self.geometry("900x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.killers = Killergrid(self,killers=ce.killer_list())
        self.killers.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        self.update_idletasks()


class SurvivorWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Survivor Window")
        self.geometry("900x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.survivors = Survivorgrid(self,survivors=ce.survivor_list())
        self.survivors.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        self.update_idletasks()

app = SurvivorWindow()

app.mainloop()