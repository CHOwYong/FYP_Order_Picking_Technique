"""
Author : Subhan Saadat Khan
last modified: 30/08
last modified by: OwYongCheeHao
"""

import random
import os
#%%
class WarehouseSKUIDGenerator:
    def __init__(self, seed, num_columns, num_rows, skus_per_aisle, num_of_items):
        self.seed = seed                        # to generate the same set of skus
        self.num_columns = num_columns          # number of columns in the warehouse
        self.num_rows = num_rows                # number of rows in the warehouse
        self.skus_per_aisle = skus_per_aisle    # number of skus per aisle
        self.num_of_items = num_of_items        # number of skus to generate (order list size)
        self.skus = []                          # list of skus generated


    def generate_all_skus(self): #TODO generate only a certain set of sku ids
        random.seed(self.seed)
        while len(self.skus) < self.num_of_items:
            col = random.randint(1,self.num_columns)
            row = random.randint(1,self.num_rows)
            num = random.randint(1,self.skus_per_aisle)
            sku_id = (col * 1000) + (row * 100) + (num)
            
            # only add unique skus to the list
            if (len(self.skus) == 0) or (sku_id not in self.skus):
                self.skus.append(sku_id)
            else:
                continue

    def writeToFile(self, filepath):
        with open(filepath, 'a') as file:  # Use 'a' mode to append to the file
            for sku in self.skus:
                file.write(f"{sku}\n")
    
#%%
# Example usage of the WarehouseSKUIDGenerator
seed = 1111
num_columns = 5
num_rows = 1
skus_per_aisle = 80
num_of_items = 10
num_sets = 5
output_folder = "D:\Monash\FYP Project\FIT3161-3162\Sku"  # Change this to your desired folder name
output_filename = "test.txt"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_filepath = os.path.join(output_folder, output_filename)

for i in range(num_sets):
    seed = seed + i + 2  # Increment seed for each set
    generator = WarehouseSKUIDGenerator(seed,num_columns, num_rows, skus_per_aisle, num_of_items)
    generator.generate_all_skus()
    generator.writeToFile(output_filepath)
# %%
