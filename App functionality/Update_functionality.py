import customtkinter
import requests
import os
import subprocess
import sys
import tempfile
import threading
from packaging.version import Version
from pathlib import Path


GITHUB_API_LATEST = "https://api.github.com/repos/GreenPl4nt/DBD-Challenge-Tracking-App/releases/latest"

class update_checker(customtkinter.CTkToplevel):
    def __init__(self, master, state, data=None):
        super().__init__()

        self.transient(master)
        self.lift()
        self.geometry("300x100")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.data = data

        self.closebutton = customtkinter.CTkButton(self, text= "Close", command= lambda: close_pop_up(master))
        self.closebutton.grid(row=2, column= 2)

        # State is 0 means not being able to check an update
        if state == 0:
            self.title("Error")
            self.label = customtkinter.CTkLabel(self,text="Could Not Check For Updates", anchor="center")

        #State is 1 means an update was not found but the query was successfull
        elif state == 1:
            self.title("Up to date")
            self.label = customtkinter.CTkLabel(self,text="The app is up to date")

        #State is 2 means an update was found and is querying the user to update
        elif state == 2:
            self.title("Update Found")
            self.label = customtkinter.CTkLabel(self,text="A new update was found, press Ok to update")
            self.updatebutton = customtkinter.CTkButton(self, text="Ok", command= lambda: threading.Thread(
                                                                                                            target=cause_download, 
                                                                                                            data=(self,self.data), 
                                                                                                            daemon=True
                                                                                                            ).start())
            self.updatebutton.grid(row=2, column=1)

        self.label.configure(anchor="center", justify="center")
        self.label.grid(row= 0, column= 0, padx=20, pady=20, sticky="ew")


def open_top_level(master,state,data = None):

    information = data

    if master.toplevel_window is None or not master.toplevel_window.winfo_exists():
        master.toplevel_window = update_checker(master,state,information)
        master.toplevel_window.focus()
    else:
        master.toplevel_window.focus()

def check_for_updates(master, version):
    try:
        response = requests.get(url=GITHUB_API_LATEST,timeout=5)
        response.raise_for_status()

        data = response.json()

        latest_version = data["tag_name"]

        if Version(latest_version.lstrip("v")) > Version(version.lstrip("v")):
            open_top_level(master,2,data)

        else:
            open_top_level(master,1,data)

    except Exception as e:

        open_top_level(master,0)

def pick_installer_asset(release_data):
    for i in release_data.get("assets", []):
        name = i.get("name", "").lower()
        if name.endswith(".exe"):
            return i        
    return None


def download_asset(url,filename):
    temporal = Path(tempfile.gettempdir()) / filename
    with requests.get(url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(temporal,"wb") as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
    return temporal

def launch_installer(installer_path, silent=False):
    if silent:
        subprocess.Popen([str(installer_path),"/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART"])
    else:
        if sys.platform.startswith("win"):
            os.startfile(str(installer_path))
        else:
            subprocess.Popen([str(installer_path)])

def cause_download(popup,data):
    popup.updatebutton.configure(state="disable")
    asset = pick_installer_asset(data)
    installer_path = download_asset(asset["browser_download_url"], asset["name"])
    launch_installer(installer_path, silent=True)
    popup.master.destroy()

def close_pop_up(master):
    tw = getattr(master, "toplevel_window", None)
    if tw and tw.winfo_exists():
        try:
            tw.destroy()
        finally:
            master.toplevel_window = None
