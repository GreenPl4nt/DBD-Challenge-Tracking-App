import customtkinter
import Character_extraction as ce
import Image_extraction as ie

class Killergrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master,killers):
        super().__init__(master)
        self.killers = killers
        self.killer_images = ie.extract_images("./Info/assets/Character assets/Killers",self.killers)
        self.labels = []

        def fit_to_size(self,width,height):
            self._parent_canvas.configure(width=width, height=height)

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
        

class KillerWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.bind("<Configure>", _on_root_resize)

        self.title("Killer Window")
        self.geometry("900x800")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.killers = Killergrid(self,killers=ce.killer_list())
        self.killers.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        


app = KillerWindow()
app.mainloop()