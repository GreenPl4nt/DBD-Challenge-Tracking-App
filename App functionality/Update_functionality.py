import customtkinter
import requests

GITHUB_API_LATEST = "https://api.github.com/repos/GreenPl4nt/DBD-Challenge-Tracking-App/releases/latest"

class update_checker(customtkinter.CTkToplevel):
    def __init__(self, master, state):
        super().__init__()
        self.transient(master)
        self.lift()
        self.geometry("250x100")
        # State is 0 means not being able to check an update
        if state == 0:
            self.title("Error")
            self.label = customtkinter.CTkLabel(self,text="Could Not Check For Updates")

        #State is 1 means an update was not found but the query was successfull
        elif state == 1:
            self.title("Up to date")
            self.label = customtkinter.CTkLabel(self,text="The app is up to date")

        #State is 2 means an update was found and is querying the user to update
        elif state == 2:
            self.title("Update Found")
            self.label = customtkinter.CTkLabel(self,text="A new update was found, press Ok to update")

        self.label.pack(padx=20,pady=20)


def open_top_level(master,state):
    if master.toplevel_window is None or not master.toplevel_window.winfo_exists():
        master.toplevel_window = update_checker(master,state)
        master.toplevel_window.focus()
    else:
        master.toplevel_window.focus()

def check_for_updates(master, version):
    try:
        response = requests.get(url=GITHUB_API_LATEST,timeout=5)
        response.raise_for_status()

        data = response.json()

        latest_version = data["tag_name"]

        if latest_version > version:
            open_top_level(master,2)
        else:
            open_top_level(master,1)
    except Exception as e:
        open_top_level(master,0)

