import random

class WarehouseSKUGenerator:
    def __init__(self, num_columns, num_rows, skus_per_aisle):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.skus_per_aisle = skus_per_aisle

    def generate_sku_id(self, column, row, sku_number):
        column_str = str(column)
        row_str = str(row)
        sku_str = str(sku_number).zfill(2)
        return f"{column_str}{row_str}{sku_str}"

    def generate_all_skus(self):
        skus = []
        for col in range(1, self.num_columns + 1):
            for row in range(1, self.num_rows + 1):
                # start_sku = (col * 1000) + (row * 100)
                for sku_num in range(1, self.skus_per_aisle + 1):
                    skus.append(self.generate_sku_id(col, row, sku_num))
        return skus

# Example usage
num_columns = 2
num_rows = 2
skus_per_aisle = 20

generator = WarehouseSKUGenerator(num_columns, num_rows, skus_per_aisle)
skus = generator.generate_all_skus()

for sku in skus:
    print(sku)
