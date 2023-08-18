from SKU import sku
class aisle:
    # class attributes
    no_of_sku = None
    col_number = None
    row_number = None
    temp_array_L = None
    temp_array_R = None
    
    def __init__(self, no_of_sku:int, col_number:int, row_number:int) -> None:
        self.no_of_sku = no_of_sku
        self.col_number = col_number
        self.row_number = row_number
    
    def build(self):
        self.temp_array_L = []
        self.temp_array_R = []
        L_col_prev_node = None
        R_col_prev_node = None
        middle = self.no_of_sku // 2
        
        
        for i in range(1,self.no_of_sku+1): # it will loop from 1 to no_of_sku so that sku number will start from 1 instead of 0
            sku_no = self.col_number * 1000 + self.row_number * 100 + i
            # left column of aisle
            if i <= middle:
                sku_node = sku(sku_no)
                self.temp_array_L.append(sku_node)
                self.build_neighbours_up_down(L_col_prev_node,sku_node)
                L_col_prev_node = sku_node
            # right column of aisle
            else: 
                sku_node = sku(sku_no)
                self.temp_array_R.append(sku_node)
                self.build_neighbours_up_down(R_col_prev_node,sku_node)
                self.build_neighbours_left_right(self.temp_array_L[i-middle],sku_node)
                R_col_prev_node = sku_node
        
        
    
    def build_neighbours_left_right(self,prev_node:sku,curr_node:sku):
        if prev_node != None:
            prev_node.add_neighbour(curr_node.get_sku_no())
            curr_node.add_neighbour(prev_node.get_sku_no())
    
    def build_neighbours_up_down(self,prev_node:sku,curr_node:sku):
        if prev_node != None:
            prev_node.add_neighbour(curr_node.get_sku_no())
            curr_node.add_neighbour(prev_node.get_sku_no())
    