# this class is here for the automatic tab open slot.
# i will be using hte "web browser" module for this to work 
# i will also be using a json to SAVE the data from the web opener 
import webbrowser
import customtkinter as ctk 

# this class is for the buttons that will be held here. 
# These buttons will be used to edit the links of the tab
# set the urls as a deeper property of it that is not shown (unless using the window)
class AutoTabOpen(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 50, corner_radius = 100, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        # add a label 
        self.lbl = ctk.CTkLabel(master, text = "🚀 Quick Start", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 0, column = 1, sticky = "nw", padx = 120)

        # add a button that will instantly open up all the tabs 
        self.open_button = ctk.CTkButton(master, text = "Launch!", font = ("Google Sans Flex", 18, "normal"), corner_radius = 100, text_color = "white", fg_color="black", bg_color="transparent", command = self.open_all_pressed)
        self.open_button.grid(row = 0, column = 1, sticky = "ne", padx = 130, pady = 10)
        
        # create the grid system for this so that all the buttons look good 
        # make sure to set propogate grid as False this time 
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="hello")
        self.grid_propagate(False) 
    
    def open_all_pressed(self):
        pass