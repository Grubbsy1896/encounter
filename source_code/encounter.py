# --------------------
# Original Development Date: 1/17/2021
# Updates and Redesign Date: 3/31/2021
# 
# Encounter, is a program to track random encounters/soft resets for Badge Quests in Pokemon Games.
# 
# --------------------


'''

Credits 

https://icon-icons.com/search/icons/pokemon&page=1
https://pypi.org/project/pypresence/


'''


# -- 
# >> Imports
# --

import os
import sys
import json

from tkinter import * 
from tkinter.ttk import *
from pypresence import *
from time import time, sleep

# To prevent circular imports, I can only import data in the other file, and only import ui into this file.
#from data import load_data, save_data
from ui import masterWindow, settingsPanel, encounterData

global window
window = masterWindow()
settingsPanel()

client_id = '856919302481641482'  
RPC = Presence(client_id, pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop

start_time = time()
def updatePresence():
    global window 
    encountermode = encounterData()[0]

    encounters = encounterData()[1]

    # print(RPC.update(state="Playing", details="Join Now!",buttons=[{"label": "Discord", "url": "link"}]))
    print(RPC.update(
        state=f"in {encountermode}", 
        details="Shiny Hunting", 
        buttons=[{"label": f"{encounters} Encounters", "url": "https://github.com/Grubbsy1896/encounter"}], 
        large_image="slowpokeupsize", 
        large_text="EnCounter v1.0", 
        #small_image="zubathunt",        # Removed because the assets are hard coded.
        #small_text="Target: Zubat",     # You can customize your own here, make sure you make
        start = start_time,              # Your own discord app and go to the rich presence assets and upload there. 
        ))  # Set the presence           # Don't forget to update the ID and ANY relevant data.

    window.after(30000, updatePresence)

window.after(5000, updatePresence)
window.mainloop()

mainloop() 
