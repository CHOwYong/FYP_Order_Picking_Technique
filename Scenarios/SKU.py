

class sku:
    # class attributes
    sku_no = None
    sku_neighbours = None
    
    def __init__(self, no_of_sku:int) -> None:
        self.sku_no = no_of_sku
        self.sku_neighbours = []
        
    def add_neighbour(self, neighbour_sku:int) -> None:
        self.sku_neighbours.append(neighbour_sku)
    
    def get_neighbours(self) -> list:
        return self.sku_neighbours
    
    def get_sku_no(self) -> int:
        return self.sku_no
    
    def __str__(self) -> str:
        return str(self.sku_no) + " " + str(self.sku_neighbours)
    