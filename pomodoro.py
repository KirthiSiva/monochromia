# this is the widget which will hold the timer for the current goal being achieved
import customtkinter as ctk 

# A pomodoro timer is a timer where you have 25 minutes of uninterupted work, followed by 5 minutes of breaks
# This keeps going as a cycle (I think technically it is supposed to take a larger break after 4 of these cycles, but I don't need that)
class Timer(ctk.CTkFrame):
    def __init__(self, master, width = 400, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        # create a label for the window 
        self.lbl = ctk.CTkLabel(master, text = "Pomodoro ⏳", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.lbl.grid(row = 2, column = 0, sticky = "ne", padx = 150, pady = 15)