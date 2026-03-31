#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import sys
import numpy as np
import random

class Game_Engine:
    def __init__(self):
        self.on = True # turn this false to turn off the game
        self.player_name = ""
        self.power = 20
        self.alone = True # end game hehehe
        self.current_planet = "" 
        self.data_list = {}
        self.data_n = 1

    def Engine(self):
        self.Starting_Screen() #FOR THE LOVE OF GOD PLEASE ENABLE THIS LATER
        while self.on:
            self.Space()  
            choice = input("Terminal:").lower().strip()
            self.Space()  
            if choice in actions:
                actions[choice]()
            else:
                self.General_Error() # this block handles the entire game by keeping a loop of the terminal and picking actions from a dictionary
        

    def Engine_Stop(self):
        self.on = False # just a function to end the game

    def General_Error(self):
        print('Captain, I do not understand that command. Type "Commands" into the terminal for a list of commands.') # error if i need it

    def Starting_Screen(self):
        self.Play_Animation(5, "BOOTING...", "SUCCESS")
        self.Play_Animation(0.3, "ENABLING MOTION SENSORS...", "SUCCESS")
        self.Play_Animation(0.1, "CHECKING STATUS...", "SUCCESS")
        self.player_name = input("INPUT USERNAME: ")
        while self.player_name == "":
            self.player_name = input("Please enter a name.")
        self.Play_Animation(4, "LOADING ADMIN INTERFACE...", "FAILURE")
        self.Play_Animation(4, "LOADING DEFAULT INTERFACE...", "SUCCESS")
        print(f'Welcome aboard, captain {self.player_name}. Enter "Commands" into the terminal window to see a list of actions.')
        # this part is a bit messy, but necessary dialogue so i wouldnt have to use a separate file

    def Space(self):
        print("\n" + "-"*20 + "\n") # adds a neat space in the line

    def Database(self):
        print("SELECT THE SCAN RESULTS FROM DATABASE")
        for key in self.data_list:
            print(key)

    def Return(self):
        if self.power > 10:
            print("COMMAND UNAVAILABLE: SECURITY PROTOCOL ACTIVE")
            print("SECURITY PROTOCOL CANNOT BE OVERRIDEN, ENERGY REQUIREMENT - 10%")
            
        else:
            print("Initiating emergency return sequence...")
        
            self.Play_Animation(4, "Calculating Earth trajectory", "TRAJECTORY LOCKED")
            self.Play_Animation(6, "Warming up hyper-drive", "SPOOLING AT 100%")
            self.Play_Animation(8, "Initiating jump in 3... 2... 1...", "FATAL ERROR")
        
            self.Space()
            time.sleep(4)
        
            print("SECURITY OVERRIDE INITIATED.")
            time.sleep(4)
            print("ERROR: ANOMALY INSIDE AIRCRAFT.")
            time.sleep(4)
            print("Return sequence aborted. All non-essential systems locked.")
        
            self.alone = False

    def Pause(self):
        print("\n" + "-"*20)
        input(" >>> Press Enter to continue...")
        print("-"*20 + "\n") # added this for when i need to let the reader read

    def Commands(self):
        command_list = """
These are the available commands:
--------------------
GENERAL COMMANDS

help - Ships manual. MUST READ!
status - Shows ship diagnostics.
exit - Exits the terminal.
zoom - Opens a selection of planets to zoom on.
storage - Opens a list of processed scan data.

ACTION COMMANDS - USES ENERGY

Admin mode for now. Use "noob" to just fastly lower energy to look at return command.

scan - Record data of the currently selected planet.
return - Set spacecraft course back towards the colony.
"""
        print(command_list) # VERY IMPORTANT list of commands for the player

    def Help(self):
        message = """
Brave volunteer, we are very sorry for the situation you were put in. If we could avoid this we would, but you have to know
that there was no other choice. This old junk did not even have an operational system in place, so this terminal has
been programmed for your ease of use. Each item under the "Action" category uses energy, so make sure to use the
"status" command as frequently as possible to not get stranded. Keep in mind that the energy loss seems to be quite random. 
Once your energy reaches 10% the "return" command will be unlocked and you will be able to come home. Good luck.

THIS GAME IS COMPLETELY UNFINISHED STORY WISE, WHILE IT ALL THE COMMANDS WORK TO SOME EXTENT IT DOESNT LEAD TO AN "ENDING",
I WILL FINISH IT AFTER EXAMS. Currently the only planets you will be ablet to scan are Earth and Mars. You can use the command
"noob" till your energy is below 10 to see the vision for how the game was supposed to end.
"""
        print(message) # starting message left for the player

    def Energy_Loss(self):
        self.power = self.power - np.random.randint(3, 8) # energy loss will probably change later

    def Status(self):
        if self.alone:
            print("You are alone. The metal room around you hums with the")
            print("faint vibration of the ion-drive. Condensation drips")
            print("slowly from the overhead ventilation grate.")
            print("\n[ SENSORS ]")
            self.Play_Animation(1, "CHECKING ENERGY LEVELS", "Status loaded")
            print(f"ENERGY LEVELS - {self.power}")
            print("CONTINUING TO MONITOR") # status
        else:
            print("You are not alone.")

    def Zoom(self):
        if self.current_planet in planets:
            print(f"Please select a planet to zoom on. You are currently on planet {planets[self.current_planet]}:")
        else:
            print(f"You currently have no planet selected. Please make a selection from the list below.")
        selection = """
Mimas
Titan
Earth
Ceres
Mars
Rhea
Miranda
Oberon
"""
        print(selection)
        valid = True
        while valid:
            choice = input("Terminal:").lower().strip()
            self.Space()  
            if choice in planets:
                self.current_planet = choice
                self.Play_Animation(2, "Zooming...", f"The ship is now locked onto {planets[choice]}.")
                print("Use the zoom tool again if you wish to select a different planet.")
                valid = False
            else:
                print("The input was not recognized. Please select a planet.")
                self.Space()

    def Scan(self):
        if self.current_planet not in planets:
            print("No planet is currently selected. Please use the 'zoom' tool.")
            return

        planet_name = planets[self.current_planet]
        print(f"Initiating scan of {planet_name}. This will use energy.")
        
        if not self.Confirm():
            return
            
        self.Energy_Loss()

        available_scans = scan_database.get(self.current_planet)
        
        if not available_scans:
            print(f"Sensors cannot penetrate the atmosphere of {planet_name}. No data gathered.")
            return

        chosen_scan = random.choice(available_scans)
    
        for duration, start_msg, end_msg in chosen_scan["animations"]:
            self.Play_Animation(duration, start_msg, end_msg)
            
        log_entry = chosen_scan["log"]    
        self.data_list[f"data{self.data_n}"] = log_entry
        self.data_n += 1
        
        self.Space()
                
    def Play_Animation(self, duration, start_msg, end_msg, bar_length=20):
        steps = 100 
        sleep_time = duration / steps
    
        for i in range(steps + 1):
            percent = i / steps
            filled_length = int(bar_length * percent)
        
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
            status = f"\r{start_msg} |{bar}| {int(percent * 100)}%"
            sys.stdout.write(status.ljust(80))
            sys.stdout.flush()
        
            time.sleep(sleep_time)
    
        sys.stdout.write(f"\r{end_msg}".ljust(80) + "\n")
    
    def Confirm(self):
        while True:
            answer = input("Are you sure? (y/n): ").lower().strip()
            if answer in ['y', 'yes']:
                self.Play_Animation(1, "Loading command...", "Command loaded.")
                return True
            if answer in ['n', 'no']:
                print("Command canceled.")
                return False
            print("Please enter Yes or No.")

        

engine = Game_Engine()

actions = {
    "help": engine.Help,
    "exit": engine.Engine_Stop,
    "commands": engine.Commands,
    "status": engine.Status,
    "zoom": engine.Zoom,
    "scan": engine.Scan,
    "noob": engine.Energy_Loss,
    "return": engine.Return,
    "storage": engine.Database
}

planets = {
    "mimas": "Mimas",
    "titan": "Titan",
    "earth": "Earth",
    "ceres": "Ceres",
    "mars": "Mars",
    "rhea": "Rhea",
    "miranda": "Miranda",
    "oberon": "Oberon"
}

scan_database = {
    "earth": [ # This is list for earth
        {# first message
            "animations": [
                (5, "Scanning surface", "SURFACE SCANS: CANNOT BE RETRIEVED"),
                (1, "Searching for distress messages", "SIGNAL INFORMATION: ERROR"),
                (2, "Amplifying detected waves", "AMPLIFICATION: COMPLETE"),
                (3, "Processing information", "DATA UPLOADED TO THE DATABASE")
            ],
            "log": """
This is the data1 log from earth you will retrieve.
"""
        },
        {# second message
            "animations": [
                (5, "Scanning surface", "SURFACE SCANS: CANNOT BE RETRIEVED"),
                (1, "Searching for distress messages", "SIGNAL INFORMATION: ERROR"),
                (2, "Amplifying detected waves", "AMPLIFICATION: COMPLETE"),
                (3, "Processing information", "DATA UPLOADED TO THE DATABASE")
            ],
            "log": """
This is the data2 log from earth you will retrieve.
"""
        }
    ],
    "mars": [ # new list for mars
        {
            "animations": [
                (5, "Scanning surface", "SURFACE SCANS: CANNOT BE RETRIEVED"),
                (1, "Searching for distress messages", "SIGNAL INFORMATION: ERROR"),
                (2, "Amplifying detected waves", "AMPLIFICATION: COMPLETE"),
                (3, "Processing information", "DATA UPLOADED TO THE DATABASE")
            ],
            "log": """
This is the data log from mars you will retrieve.
"""
        }
    ]
}

engine.Engine()

