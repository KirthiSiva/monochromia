import customtkinter as ctk  

class ToDoList(ctk.CTkScrollableFrame):
    def __init__(self, master, values, width = 200, height = 200, corner_radius = 50, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, scrollbar_fg_color = None, scrollbar_button_color = None, scrollbar_button_hover_color = None, label_fg_color = None, label_text_color = None, label_text = "", label_font = None, label_anchor = "center", orientation = "vertical"):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, scrollbar_fg_color, scrollbar_button_color, scrollbar_button_hover_color, label_fg_color, label_text_color, label_text, label_font, label_anchor, orientation)
       
        # create a grid for the checkboxes 
        self.grid_columnconfigure(0, weight = 1)
       
        # declare some variables for the checkboxes (to-do "items")
        self.values = values
        self.checkboxes = []
        
        # create a label for the to do list 
        self.header = ctk.CTkLabel(master, text = "To - Do", font = ("Google Sans Flex", 30, "bold"), text_color = "white", fg_color="transparent", bg_color="transparent")
        self.header.grid(row = 0, column = 2, sticky = "sw", padx = 230)
        
        # create a button on the to do list 
        self.button = ctk.CTkButton(master, text = "Add Items", font = ("Google Sans Flex", 18, "normal"), corner_radius = 100, text_color = "white", fg_color="black", bg_color="transparent")
        self.button.grid(row = 0, column = 2, sticky = "se", padx = 150, pady = 7)

        # add checkboxes 
        for i, value in enumerate(self.values):
            to_do_item = ctk.CTkCheckBox(self, text = value)
            to_do_item.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(to_do_item)
            
        