from Aisle import *
import Condition

class layout(Condition):
    
    no_of_sku_per_aisle = 0
    no_of_shelves = 0
    no_cross_aisles = 1
    no_of_columns = 1
    start_node = 0
    aisle_arr = None
    
    def __init__(self,random_gen:bool, no_of_sku_per_aisle:int, no_of_shelves:int, no_cross_aisles:int, no_of_columns:int) -> None:
        super(random_gen)
        self.no_of_sku_per_aisle = no_of_sku_per_aisle
        self.no_of_shelves = no_of_shelves
        self.no_cross_aisles = no_cross_aisles
        self.no_of_columns = no_of_columns
    
    #TODO implement different types of layouts
    #TODO allow selection of different layouts by choosing 1 for layout 1, 2 for layout 2 etc...
    #TODO allow for random selection of a layout

    def load(self): #Maybe switch this to load layout one, then have other functions for other layouts, then have a big load function that chooses what to load
        # Create a list of aisles
        aisle_arr = [None*self.no_of_columns]*self.no_cross_aisles
        
        for i in range(self.no_cross_aisles - 1):
            for j in range(self.no_of_columns - 1):
                start_sku = (i * 1000) + (j * 100) + 1
                end_sku = start_sku + self.no_of_sku_per_aisle - 1
                aisle_arr[i][j] = aisle(self.no_of_sku_per_aisle, self.no_of_shelves, start_sku, end_sku)

        self.aisle_arr = aisle_arr
        return self.aisle_arr
        

    