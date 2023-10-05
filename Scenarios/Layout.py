"""
Author : OwYongCheeHao
last modified: 25/9
last modified by: OwYongCheeHao
"""
#%%
from Aisle import *

class layout():
    """
    This class creates a network graph of the warehouse Layout based on various parameters
    """
    no_of_sku_per_aisle = 0
    no_of_shelves = 0
    no_of_rows = 1
    no_of_columns = 1
    
    start_node = None
    aisle_arr = None
    
    def __init__(self, no_of_sku_per_aisle:int, no_of_shelves:int, no_of_rows:int, no_of_columns:int) -> None:
        self.no_of_sku_per_aisle = no_of_sku_per_aisle
        self.no_of_shelves = no_of_shelves
        self.no_of_rows = no_of_rows
        self.no_of_columns = no_of_columns
    
    #TODO implement different types of layouts
    #TODO allow selection of different layouts by choosing 1 for layout 1, 2 for layout 2 etc...
    #TODO allow for random selection of a layout

    def load(self): #Maybe switch this to load layout one, then have other functions for other layouts, then have a big load function that chooses what to load
        # Create a list of aisles
        aisle_arr = [[None for i in range(self.no_of_columns)] for j in range(self.no_of_rows)]
        
        for i in range(1, self.no_of_columns + 1):
            for j in range(1, self.no_of_rows + 1):
                aisle_arr[i-1][j-1] = aisle(self.no_of_sku_per_aisle, j, i)

        self.aisle_arr = aisle_arr
        
        if self.no_of_rows > 1:
            self.link_row_aisle()
        self.link_col_aisle()
        
        self.start_node = self.aisle_arr[0][0].temp_array_L[0]
        
        return self.aisle_arr
    

    def link_col_aisle(self):
        for row in range(self.no_of_rows):
            prev_col = None
            for col in range(self.no_of_columns):
                curr_col = self.aisle_arr[row][col]
                link_LR(prev_col, curr_col)
                prev_col = curr_col
    
    def link_row_aisle(self):
        for col in range(self.no_of_columns):
            prev_row = None
            for row in range(self.no_of_rows):
                curr_row = self.aisle_arr[row][col]
                link_TB(prev_row, curr_row)
                prev_row = curr_row
                
def link_LR(aisle1,aisle2):
    """
    This function links the left and right aisle together
    """
    if aisle1 != None:
        x = aisle1.half_no_of_sku
        for i in range (x):
            aisle1.temp_array_R[i].add_neighbour(aisle2.temp_array_L[i])
            aisle2.temp_array_L[i].add_neighbour(aisle1.temp_array_R[i])
            
def link_TB(aisle1, aisle2):
    """
    This function links the top and bottom aisle together
    """
    if aisle1 != None:
        aisle1.temp_array_R[-1].add_neighbour(aisle2.temp_array_R[0])
        aisle2.temp_array_R[0].add_neighbour(aisle1.temp_array_R[-1])
        aisle1.temp_array_L[-1].add_neighbour(aisle2.temp_array_L[0])
        aisle2.temp_array_L[0].add_neighbour(aisle1.temp_array_L[-1])
    
        
#%%
if __name__ == "__main__":

    ####### Testing for layout ########
    layout1 = layout(10,0,2,2)
    layout1.load()
    print(layout1.aisle_arr)
# %%
