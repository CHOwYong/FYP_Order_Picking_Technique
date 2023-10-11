"""
Author : OwYongCheeHao
last modified: 25/9
last modified by: OwYongCheeHao
"""
class sku:
    """
    This class is for making sku object/nodes for the network graph
    """
    # class attributes
    sku_no = None
    sku_neighbours = None
    sku_side = None # 0 means left and 1 means right
    
    # used for A* algo traverse
    total_dist = 0
    
    def __init__(self, no_of_sku, sku_side:int) -> None:
        self.sku_no = no_of_sku
        self.sku_neighbours = []
        self.sku_side = sku_side
        
    def add_neighbour(self, neighbour_sku) -> None:
        self.sku_neighbours.append(neighbour_sku)
    
    def get_neighbours(self) -> list:
        return self.sku_neighbours
    
    def get_sku_no(self):
        return self.sku_no
    
    def get_total_dist(self):
        return self.total_dist
        
    def update_total_dist(self,total_dist):
        self.total_dist = total_dist
    
    def __str__(self) -> str:
        return str(self.sku_no) + " " + str(self.sku_neighbours)
    
    