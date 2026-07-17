#libraries to inport 
# The reason why I chose a fractal for the "growth" is to add a cool touch to the entire project! 
import customtkinter as ctk 

class Fractal(ctk.CTkCanvas): 
    def __init__(self, master, width=800, height = 800, **kwargs):
        super().__init__(self, master, width=width, height = height, bg = "black", highlightthickness = 0, **kwargs)
        
        # declare sme of the variables 
        self.width = width
        self.height = height 
        
        # current completion progress placeholder 
        self.progress = 0 
        
        # draw the initial (empty) fractal 
        self.draw_fractal() 
        
    # this is the function which will actually be updating how extended/retracted the pattenr will be 
    def update_progress(self, completed, total): 
        pass
       
        
        
        