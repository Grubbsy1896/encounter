import os
import sys
import json

from tkinter import * 
from tkinter.ttk import *

from data import load_data, save_data

from pypresence import *
import time, datetime, struct, asyncio
from time import time, sleep
import asyncio
#from encounter import encounters (Preventing Circular Imports)


# --
# >> Globals
# --

global encounters
encounters = load_data()

global encountermode
encountermode = ""

global buttons 
buttons = []

global ROOT_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# --
# >> Setting Up The Main Window
# --

def masterWindow():
    '''Setting up the Main Window where the counter is.'''
    global master 
    master = Tk() 
    master.geometry("250x250") 
    master.title("EnCounter")
    master.iconbitmap(f'{ROOT_DIR}/assets/icon.ico')


    label = Label(master,  
                text ="Grubbsy's EnCounter | V 1") 
    label.pack(pady = 10) 
    #labelTotal = Button(master, text="0")

    settingsButton = Button(master, text=f"Settings", width=50, command = lambda: settingsPanel())
    settingsButton.pack()

    global label2
    label2 = Label(master, text="\n Total Encounters: 0 \n")
    label2.pack()

    return master
# --
# >> Main window functions
# --
def change_label_number(button, num, encounter, encounter_type):
    global buttons
    global encountermode
    encountermode = encounter
    # This is the counter/ Number Handling
    # Grabbing the encountertotal as a variable to make it an easier to work with variable. 
    encountertotal = encounters[str(encounter)][str(encounter_type)]
    encountertotal += 1
    # Updating the button.
    buttons[button].config(text=f"{encounter_type}: {encountertotal}")
    # Updating the thing to save it. 
    encounters[str(encounter)][str(encounter_type)]  = encountertotal
    encounters['global']['total_encounters'] = get_total_encounters(encounter)
    
    save_data(encounters)

    #Outputting 
    global label2
    label2.config(text=f"\nTotal Encounters: {get_total_encounters(encounter)}\n ")
    print(f"Total Encounters: {encounters['global']['total_encounters']}.")


def load_buttons(encounter):
    global encounters
    for etype in encounters[encounter]:
        create_button(next_button_num(), encounter, etype)

def create_button(number, encounter, etype): # Number is the id of the button in the buttons list. 
    global buttons
    b = Button(master, text=f"{etype}: {encounters[encounter][etype]}", width=50, 
                command = lambda: change_label_number(number, 1, encounter, etype))
    buttons.append(b)
    b.pack()

def next_button_num():
    global buttons
    return len(buttons)

def get_total_encounters(encounter):
    if encounter in encounters:
        total = 0
        for e in  encounters[str(encounter)]:
            total += encounters[str(encounter)][e] 
        
        return total
    else:
        return 0

# --
# >> The Settings Panel
# --

def settingsPanel():
    '''Setting up the settings panel'''
    global panel
    global encounters
    # basic variables
    panel = Tk()
    panel.geometry("250x250")
    panel.title("EnCounter Settings")
    panel.iconbitmap(f'{ROOT_DIR}/assets/icon.ico')
    # Label
    label1 = Label(panel, text="Settings")
    label1.pack()

    

    OPTIONS = []
    for encounter_type in encounters:
        if encounter_type != "global":
            OPTIONS.append(encounter_type)



    global selectedEncounter
    selectedEncounter = StringVar(panel)
    selectedEncounter.set(OPTIONS[0])

    # A Dropdown for loading the encounters
    encounterDropDown = OptionMenu(panel, selectedEncounter, *OPTIONS)
    encounterDropDown.pack()

    # A button for applying the loading settings
    applyEncounter = Button(panel, text="Apply Encounter List", width=50, command = lambda: get_load_buttons())
    applyEncounter.pack()

    # SPACER
    spacer = Label(panel, text="")
    spacer.pack()

    # A Button for opening the encounters window
    viewencounterlist = Button(panel, text="View Encounters", width = 50,
                        command = lambda: encountersWindow())
    viewencounterlist.pack()

    # SPACER
    spacer2 = Label(panel, text="")
    spacer2.pack()

    # Delete Buttons Button (IS LAST)
    removeEncounters = Button(panel, text=f"Clear Encounter List", width=50, 
                command = lambda: delete_buttons())
    removeEncounters.pack()

    # SPACER
    spacer3 = Label(panel, text="")
    spacer3.pack()

    # Create Button and label
    createLabel = Label(panel, text="Create An Encounter")
    createLabel.pack()

    createButton = Button(panel, text="Open Creator", width=50, command = lambda: creatorWindow())
    createButton.pack()

# --
# >> Panel Functions
# --

def delete_buttons():
    global buttons 
    for b in buttons:
        b.pack_forget()

def get_load_buttons():
    global selectedEncounter
    global encounters
    delete_buttons()
    encounter = selectedEncounter.get()
    if str(encounter) in encounters:
        load_buttons(encounter)
    else:
        pass

# --
# >> Create Encounter Page
# --

def creatorWindow():
    global creator
    creator = Tk()
    creator.geometry("250x250")
    creator.title("EnCounter Creator")
    creator.iconbitmap(f'{ROOT_DIR}/assets/icon.ico')

    textlabel1 = Label(creator, text="Name of Encounter List:")
    textlabel1.pack()

    global title_entry
    title_entry=Entry(creator)
    title_entry.pack()

    textlabel2 = Label(creator, text="Encounters (Split Via Comma) \nEX: Zubat, Slowpoke, Magikarp")
    textlabel2.pack()

    global list_entry
    list_entry = Entry(creator)
    list_entry.pack()

    confirmcreate = Button(creator, text="Apply", width=50, command= lambda: create_encounter_button())
    confirmcreate.pack()

# - WILL NEED, TEXT ENTRY
# ONE FOR TITLE
# ONE FOR POKEMON IN IT

# --
# >> Create Encounter Functions
# --

def create_encounter_button():
    global title_entry
    global list_entry
    listentry = str(list_entry.get())
    elist = listentry.replace(" ", "")
    elist = elist.split(",")

    create_encounter(str(title_entry.get()), elist)



# Adding New Data to the counters
def create_encounter(encountername, namelist):
    global encounters
    encounters[str(encountername)] = {} 
    for name in namelist:
        encounters[str(encountername)][str(name)] = 0
    save_data(encounters)

# --
# >> View Encounters Page
# --

def encountersWindow():
    window = Tk()
    window.geometry("250x250")
    window.title("EnCounter List")
    window.iconbitmap(f'{ROOT_DIR}/assets/icon.ico')

    listtext = ""
    for encounter in encounters:
        listtext += f"{encounter}: \n"
        for e in encounters[encounter]:
            listtext += f"  - {e} {encounters[encounter][e]} \n"

    label = Label(window, text=listtext)
    label.pack()

def encounterData():
    global encountermode
    return [encountermode, get_total_encounters(encountermode)]

    
