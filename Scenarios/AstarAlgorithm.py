"""
Author : OwYongCheeHao
last modified: 3/10
last modified by: OwYongCheeHao
"""
#%%
from SKU import *
from Layout import *

def a_star_algorithm(layout:layout):
    pass

def g_cost(sku1:sku, sku2:sku):
    """
    This funtion takes 2 sku node and calculate accurate distance between them
    Basic Assumption, sku nodes given is always the neighbour of each other
    Args:
        sku1 (sku): first sku node (start)
        sku2 (sku): second sku node (destination)
    """
    sku1_no_str = str(sku1.get_sku_no())
    sku2_no_str = str(sku2.get_sku_no())
    sku1_no = sku1.get_sku_no()
    sku2_no = sku2.get_sku_no()
    

    # same column
    if sku1_no_str[0] == sku2_no_str[0]:
        # same row
        if sku1_no_str[1] == sku2_no_str[1]:
            # same side of the column (aisle)
            if sku1.sku_side == sku2.sku_side:
                dist = abs(sku1_no - sku2_no) # basically 1
            # different side of the column (aisle)
            else:
                dist = 2
        # different row
        else:
            dist = 2
    # different column
    else:
        # same row
        if sku1_no_str[1] == sku2_no_str[1]:
            dist = 2
    return dist


def h_cost(sku1:sku, sku2:sku,item_per_aisle:int):
    """
    The heuristic cost of traveling from sku1 node to sku2 node.  It is calculated by using manthaton distance.
    Basic assumption sku1 node is always the left of sku2 node and sku1 node is always above sku2 node.
    Meaning sku1 < sku2.  The order is important for easier calculation.
    Args:
        sku1 (sku): first sku node (start)
        sku2 (sku): second sku node (destination) 
    """
    # ordering by the property sku1 < sku2
    sku1_no = sku1.get_sku_no()
    sku2_no = sku2.get_sku_no()
    if sku1_no > sku2_no:
        temp = sku1
        sku1 = sku2
        sku2 = temp
    
    sku1_no_str = str(sku1.get_sku_no())
    sku2_no_str = str(sku2.get_sku_no())
    half_item = item_per_aisle // 2
    # print("Computing")
    # print("sku_number1:", sku1_no_str)
    # print("sku number2:", sku2_no_str)
    # print("item per aisle:",item_per_aisle)
    
    # __________________Y difference__________________
    # same row
    if sku1_no_str[1] == sku2_no_str[1]:
        y_dist = abs(int(sku1_no_str[2:]) - int(sku2_no_str[2:]))
    # different row
    else:
        y_dist = abs((half_item - int(sku1_no_str[2:])) + int(sku2_no_str[2:]))
        
        # add the row and walkway distance between them
        row_multiplier = abs(int(sku1_no_str[1]) - int(sku2_no_str[1]))
        y_dist += row_multiplier * 2
        
        # if there are aisle(s) inbetween them
        if row_multiplier > 1:
            y_dist += (row_multiplier - 1) * half_item # per item 1 meter apart
    
    # __________________X difference__________________
    x_temp = abs(sku1.sku_side - sku2.sku_side)
    # same col
    if sku1_no_str[1] == sku2_no_str[1]:
        x_dist = x_temp * 2
    else:
        if sku1.sku_side == 0 and x_temp == 0:
            x_dist = 2
        elif sku1.sku_side == 0 and x_temp == 1: # sku facing outwards
            x_dist = 4
        else: # sku facing inwards
            x_dist = 0
        
        # add the aisle and walkway distance between them
        col_multiplier = abs(int(sku1_no_str[0]) - int(sku2_no_str[0]))
        x_dist += col_multiplier * 2 # width of walkway
        
        if col_multiplier > 1:
            x_dist += (col_multiplier - 1) * 2 # width of colmun is 2 meter
    
    h_n = x_dist + y_dist
    # print("x distance:",x_dist)
    # print("y distance:",y_dist)
    return h_n

    
#%%
if __name__ == "__main__":
    
    ######## Test for h(n) correctness ########
    sku1 = sku(1105,0)
    sku2 = sku(2215,0)
    
    h_cost(sku1,sku2,50)
    h_cost(sku2,sku1,50) # test if the ordering is correct
    
    ######## Test for g(n) correctness ########
    sku1 = sku(1105,0)
    sku2 = sku(1106,0)
    
    g_n = g_cost(sku1,sku2) # expect answer is 1
    print(g_n)
    
    sku1 = sku(1105,0)
    sku2 = sku(1110,1)
    
    g_n = g_cost(sku1,sku2) # expect answer is 2
    print(g_n)
    

# %%
