# this is the widget which will hold the weather of the current location 
import customtkinter as ctk 
import urllib.request #used for the apis 
import threading # this library is very important for running many processes at the same time 

class Weather(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # Create a grid
        self.rowconfigure(0, weight = 2, uniform="hello") # the reason why I made it 2 is because I want this to hold the icon, which will take a lot of space
        self.rowconfigure((1,2), weight = 1, uniform="hello")
        self.columnconfigure(0, weight= 1, uniform= "hello")
        self.grid_propagate(False)
        
        # create a label for the app 
        self.header = ctk.CTkLabel(master, text = "Weather 🌤️", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.header.grid(row = 0, column = 0, sticky = "ne",  pady = 15, padx = 180)
        
        # Create the labels for the weather and location (placeholders for now, will be changed via the API)
        self.lbl_weather = ctk.CTkLabel(self, text = "Loading Weather...", font = ("Google Sans Flex", 15, "normal"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl_weather.grid(row = 1, column = 0, sticky = "n")
        
        self.lbl_location = ctk.CTkLabel(self, text = "Loading Location...", font = ("Google Sans Flex", 15, "normal"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl_location.grid(row = 2, column = 0, sticky = "n")
        
        # Create a label that will hold the "icon" (will just be an emoji! )
        self.img = ctk.CTkLabel(self, text = "", font = ("Google Sans Flex", 30, "normal"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.img.grid(row = 0, column = 0)
        
        # Use the threading to run this in hte background so that it does not crash everything! 
        # 