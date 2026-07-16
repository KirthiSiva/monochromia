import customtkinter as ctk  
import tkinter.font as tkfont

class ToDoList(ctk.CTkScrollableFrame):
    def __init__(self, master, values, width = 200, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, scrollbar_fg_color = None, scrollbar_button_color = None, scrollbar_button_hover_color = None, label_fg_color = None, label_text_color = None, label_text = "", label_font = None, label_anchor = "center", orientation = "vertical"):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, scrollbar_fg_color, scrollbar_button_color, scrollbar_button_hover_color, label_fg_color, label_text_color, label_text, label_font, label_anchor, orientation)
       
        # create a grid for the checkboxes 
        self.grid_columnconfigure(0, weight = 1)
       
        # declare some variables for the checkboxes (to-do "items")
        self.values = values
        self.checkboxes = []
        
        # create a "strike through" font when it is completed
        base_font = ("Google Sans Flex", 20, "normal")
        self.stc = ctk.CTkFont(family=base_font[0], size=base_font[1], overstrike=True)
        
        # create a label for the to do list 
        self.header = ctk.CTkLabel(master, text = "To - Do", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.header.grid(row = 0, column = 2, sticky = "sw", padx = 230)
        
        # create a button on the to do list 
        self.button = ctk.CTkButton(master, text = "Add Items", font = ("Google Sans Flex", 18, "normal"), corner_radius = 100, text_color = "white", fg_color="black", bg_color="transparent")
        self.button.grid(row = 0, column = 2, sticky = "se", padx = 150, pady = 7)

        # add checkboxes 
        for i, value in enumerate(self.values):
            to_do_item = ctk.CTkCheckBox(self, text = value, font = ("Google Sans Flex", 18, "bold"), text_color = "white", command = self.on_completed, checkmark_color="black", fg_color= "white", hover_color="white")
            to_do_item.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(to_do_item)
    
    # function to form a dictionary of all the current items 
    # this is convient for constantly reprinting the list of to_do items! 
    def dict_sort(self): 
        # clear the current used dict 
        all_to_do = {}
        
        for _ in self.checkboxes: 
            if _.get() == 1: # if the checkbox is filled 
                all_to_do[_] = True 
            else:
               all_to_do[_] = False 
        
        return all_to_do
    
    # function used to get "completed" to do list items 
    def get(self): 
        checked_counter = 0
        for _ in self.checkboxes: 
            if _.get() == 1: # if the checkbox is filled 
                checked_counter += 1
                _.configure(text_color = "gray", font = self.stc)
            else:
               _.configure(text_color = "white", font = ("Google Sans Flex", 20, "bold")) 
        
        # return the value for the "on_completed" function 
        return checked_counter
            
    # this function will run when the checkbox is clicked
    # DIRECTLY updates fractal tree! 
    def on_completed(self): 
        #1: refresh the list 
        # the way that I want to achieve this is to add to a dictionary
        # dictionary used to diffrienciate between a 
        
        #2: Get the # of completed lists 
        
        # update tree/give tree update trigger 
    
    
    # refresh list function 
    
    # add new popup function (use input dialog)
    
    # add item function 
    
    
        