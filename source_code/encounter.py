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


'''


# -- 
# >> Imports
# --

import os
import sys
import json

from tkinter import * 
from tkinter.ttk import *

# To prevent circular imports, I can only import data in the other file, and only import ui into this file.
#from data import load_data, save_data
from ui import masterWindow, settingsPanel



masterWindow()
settingsPanel()

mainloop() 