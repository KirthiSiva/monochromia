def dict_sort(self): 
    # clear the current used dict 
    all_to_do = {}
    
    for _ in self.checkboxes: 
        if _.get() == 1: # if the checkbox is filled 
            all_to_do[_] = True 
        else:
            all_to_do[_] = False 
    
    return all_to_do

print(dict_sort())
