"""
Author : OwYongCheeHao
last modified: 7/10
last modified by: OwYongCheeHao
"""
#%%
from SKU import *
from Layout import *
from Heapq import *

def a_star_algorithm(layout:layout,sku_orderList):
    """
    A* algorithm functions that traverse the layout picking all items as optimally as possible and returns the distance travel.
    Args:
        layout (layout): layout object
        sku_orderList: list of sku numbers(int) 

    Returns:
        _type_: _description_
    """
    frontiers = PriorityQueue()
    item_per_aisle = layout.no_of_sku_per_aisle
    
    # add the starting node to the frontiers
    frontiers.push(layout.start_node,0)
    # make the sku list to temp nodes (instead of finding the nodes in layout)
    goals = make_node(sku_orderList,item_per_aisle)
    # visited nodes
    visited = []
    
    # main algorithm
    while frontiers.isEmpty() == False and len(goals) != 0:
        curr_node = frontiers.pop()
        visited.append(curr_node.get_sku_no())
        # print(curr_node.get_sku_no(), curr_node.get_total_dist())
        
        # if current node is the goal remove from goal list
        check, goals_list = is_goal(curr_node.get_sku_no(), goals)
        # print("is it goal:",check)
        # print("goal left:",goals_list)
        if check:
            print(curr_node.get_sku_no())
            goals = goals_list
            if len(goals) == 0:
                total_dist_travel = curr_node.get_total_dist()
                total_dist_travel += h_cost(layout.start_node,curr_node,item_per_aisle)
                return total_dist_travel
            else:
                frontiers = PriorityQueue()
                visited = []
        
        neighbour_list = curr_node.get_neighbours()
        
        # print("neighbour sku")
        for n in neighbour_list:
            n_sku_no = n.get_sku_no()
            # print(n_sku_no)
            if n_sku_no in visited:
                continue
            
            # calculate g(n) then add with old g(n) to target node
            gn = g_cost(curr_node,n)
            total_gn = curr_node.get_total_dist() + gn
            n.update_total_dist(total_gn)
        
            # calculate sum of h(n) to all goals
            hn = sum_h_cost(n,goals,item_per_aisle)
            
            # calculate f(n) = g(n) + h(n)
            fn = total_gn + hn
            
            # update the frontier
            frontiers.update(n,fn)
    
        
def is_goal(sku_no:int, goals:list):
    for i in range(len(goals)):
        if goals[i].get_sku_no() == sku_no:
            goals.pop(i)
            return True, goals
    return False, goals

def make_node(sku_list:list, item_per_aisle:int):
    list_sku = []
    half_item = item_per_aisle // 2
    for sku_no in sku_list:
        no = int(str(sku_no)[2:])
        if no <= half_item:
            temp = sku(sku_no,0)
        else:
            temp = sku(sku_no,1)
        list_sku.append(temp)
    return list_sku


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


def h_cost(sku1:sku, sku2:sku, item_per_aisle:int):
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
        # diff side of aisle
        if sku1.sku_side != sku2.sku_side:
            y_dist = abs(y_dist - half_item)
    # different row
    else:
        y_dist = abs((half_item - int(sku1_no_str[2:])) + int(sku2_no_str[2:]))        
        # diff side of aisle
        if sku1.sku_side != sku2.sku_side:
            y_dist = abs(y_dist - half_item)
        
        # add the row and walkway distance between them
        row_multiplier = abs(int(sku1_no_str[1]) - int(sku2_no_str[1]))
        y_dist += row_multiplier * 2
        
        # if there are aisle(s) inbetween them
        if row_multiplier > 1:
            y_dist += (row_multiplier - 1) * half_item # per item 1 meter apart
    
    # __________________X difference__________________
    x_temp = abs(sku1.sku_side - sku2.sku_side)
    # same col
    if sku1_no_str[0] == sku2_no_str[0]:
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


def sum_h_cost(sku1,sku_list,item_per_aisle):
    h = 0
    for goal in sku_list:
        h += h_cost(sku1,goal,item_per_aisle)
    return h

    
#%%
if __name__ == "__main__":
    
    
    # sku1 = sku(1105,0)
    # sku2 = sku(2205,0)
    # sku3 = sku(1106,0)
    # sku4 = sku(1110,1)
    # ######## Test for h(n) correctness ########  
    # sku1 = sku(1101,0)
    # sku2 = sku(1105,0)
    # h_cost(sku1,sku2,10) # expect x=0,y=4,total=4
    
    # sku1 = sku(1101,0)
    # sku2 = sku(1110,1)
    # h_cost(sku1,sku2,10) # expect x=2,y=4,total=6
    
    # sku1 = sku(1101,0)
    # sku2 = sku(2101,0)
    # h_cost(sku1,sku2,10) # expect x=4,y=0,total=4
    
    # sku1 = sku(1101,0)
    # sku2 = sku(2106,1)
    # h_cost(sku1,sku2,10) # expect x=6,y=0,total=6
    
    # sku1 = sku(1101,0)
    # sku2 = sku(2110,1)
    # h_cost(sku1,sku2,10) # expect x=6,y=4,total=10
    
    # sku1 = sku(1101,0)
    # sku2 = sku(1210,1)
    # h_cost(sku1,sku2,10) # expect x=2,y=11,total=13
    
    # ######## Test for g(n) correctness ########
    # g_n = g_cost(sku1,sku3) # expect answer is 1
    # print(g_n)
    
    # g_n = g_cost(sku1,sku4) # expect answer is 2
    # print(g_n)
    
    # ######## Testing for Heapq working correctly or not ########
    # test = PriorityQueue()
    # test.push(sku1,10)
    # test.push(sku2,2)
    # test.push(sku3,23)
    
    # test.update(sku1,50)
    
    # print(test.pop().get_sku_no())
    # print(test.pop().get_sku_no())

    # ####### Testing for layout ########
    # layout1 = layout(10,0,2,2)
    # layout1.load()
    # print(layout1.aisle_arr)
    
    # # ####### Testing for is goal ########
    # a = make_node([1105,1110],10)
    # b,c = is_goal(1106,a)
    
    ####### Testing A* algo ########
    layout_1 = layout(10,0,10,10)
    layout_1.load()
    dist = a_star_algorithm(layout_1,[2103,1110,1203,2210]) # optimal path is 34 but expect to be 47 instead

# %%
