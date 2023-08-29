import random

class WarehouseSKUIDGenerator:
    def __init__(self, num_columns, num_rows, skus_per_aisle, num_of_items):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.skus_per_aisle = skus_per_aisle
        self.num_of_items = num_of_items



    def generate_all_skus(self): #TODO generate only a certain set of sku ids
        skus = []
        while len(skus) != self.num_of_items:
            col = random.randint(1,self.num_columns)
            row = random.randint(1,self.num_rows)
            num = random.randint(1,self.skus_per_aisle)
            sku_id = (col * 1000) + (row * 100) + (num)
            
            if (len(skus) == 0) or (sku_id not in skus):
                skus.append(sku_id) 
            else:
                continue

        return skus


# Example usage
num_columns = 5
num_rows = 1
skus_per_aisle = 80
num_of_items = 10

generator = WarehouseSKUIDGenerator(num_columns, num_rows, skus_per_aisle, num_of_items)
skus = generator.generate_all_skus()

for sku in skus:
    print(sku)
