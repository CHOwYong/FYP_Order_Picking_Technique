class aisle:
    # class attributes
    no_of_sku = 0
    no_of_shelves = 0
    start_sku = 0
    end_sku = 0
    
    def __init__(self, no_of_sku:int, no_of_shelves:int, start_sku:int, end_sku:int) -> None:
        self.no_of_sku = no_of_sku
        self.no_of_shelves = no_of_shelves
        self.start_sku = start_sku
        self.end_sku = end_sku
    