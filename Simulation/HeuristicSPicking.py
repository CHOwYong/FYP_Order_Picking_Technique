"""
Author : Tan Jian Xi
last modified: 9/10
last modified by: Tan Jian Xi
"""

from Layout import *

def get_sku_list_rows(sku_list:list,layout:layout):
    no_rows = layout.no_of_rows
    res = [[] for _ in range(no_rows)]

    no_digits = len(str(layout.no_of_rows))

    for i in sku_list:
        row_no = int(str(i)[0:no_digits])
        res[row_no-1].append(i)

    return res

def get_aisles(sku_list:list,layout:layout):
    aisles = []
    for i in range(len(sku_list)):
        sku_list[i] = str(sku_list[i])
      
    no_digits = len(str(layout.no_of_rows))
    
    for sku in sku_list:
        sku_col = int(sku[no_digits:no_digits*2]) #column no
        sku_no  = int(sku[no_digits*2:])
        if sku_no > 40:
            #means sku is on the right side of the aisle
            if sku_col + 1 not in aisles:
                aisles.append(sku_col + 1)
        else:
            if sku_col not in aisles:
                aisles.append(sku_col)

    return sorted(aisles)


def move_down_next_row(ended_at:int,sku_next_row:list,layout:layout):
    aisles_next_row = get_aisles(sku_list=sku_next_row,layout=layout)

    if abs(ended_at - aisles_next_row[0]) < abs(ended_at - aisles_next_row[-1]):
        return(2,aisles_next_row[0],"right")
    else:
        return(2,aisles_next_row[-1],"left")


def heuristic_s_picking_row(sku_list:list,start_aisle:int,direction:str,layout:layout):
    sku_list = sorted(sku_list)
    total_dist = 0
    aisles = get_aisles(sku_list=sku_list,layout=layout)
    ended_at = None

    if direction == "left":
        end_aisle = aisles[0]
        ended_at = aisles[0]
    else:
        end_aisle = aisles[-1]
        ended_at = aisles[-1]

    if start_aisle != end_aisle:
        dist_horizontal = (abs(start_aisle - end_aisle) - 1)*2 + (abs(start_aisle - end_aisle))*2 #number of aisle to traverse + number of shelves passed
        dist_vertical = len(aisles)*40
        total_dist = total_dist + dist_horizontal + dist_vertical
    else:
        total_dist = 40


    if len(aisles)%2 == 0:
        total_dist += 40


    return (total_dist,ended_at)

def return_to_start(row:int, aisle:int):
    total_dist = 0

    if aisle != 1:
        dist_horizontal = (abs(aisle - 2))*2 + (abs(aisle-1)*2) #number of aisle to traverse + number of shelves passed
        dist_vertical = row*40 + (row-1)*2
        total_dist = total_dist + dist_horizontal + dist_vertical
    else:
        total_dist = row*40 + (row-1)*2
    
    return total_dist


def heuristic_s(sku_list, layout:layout):
    #get rows in warehouse
    rows = get_sku_list_rows(sku_list=sku_list,layout=layout)

    #end_row = last row with items
    last_row_with_items = None
    for i in range(len(rows)):
        if len(rows[i]) > 0:
            last_row_with_items = i + 1
    
    #previous aisle
    previous_aisle = None

    #total dist
    total_dist = 0

    #current_aisle
    current_aisle = 1

    #picker move in direction
    direction = "right"

    #CODE FOR TRAVERSING DOWN
    # for each row in warehouse[:end_row + 1]:
	# check if there are items to be picked from row
	# if yes:
	# 	if previous aisle is not None: which means that we have traversed a prior aisle 
	# 		get current aisles
	# 		total dist += get min(abs(previous aisle - aisles_leftmost),abs(previous aisle - aisles_rightmost))
			
	# 	pick from row
	# 	add to total distance
	# 	go down by 2(total_dist += 2)
	# 	set previous aisle as current aisle
	# if no:
	# 	go down by 42(total_dist += 42)
	# 	keep previous aisle as current aisle

    for row in rows[:last_row_with_items]:
        aisles_to_pick_from = get_aisles(row,layout=layout)
        if len(aisles_to_pick_from) > 0:
            if previous_aisle is not None:
                #calculate aisle shift
                diff_aisles = min(abs(previous_aisle - aisles_to_pick_from[0]),abs(previous_aisle - aisles_to_pick_from[-1]))
                total_dist += min(abs(diff_aisles-1),diff_aisles)*2 + diff_aisles*2

                #calculate move down
                moved_down = move_down_next_row(previous_aisle,row,layout=layout)
                total_dist += moved_down[0]
                current_aisle = moved_down[1]
                direction =  moved_down[2]

            elif previous_aisle is None and aisles_to_pick_from[0] != 1:
                diff_aisles = min(abs(1 - aisles_to_pick_from[0]),abs(1 - aisles_to_pick_from[-1]))
                total_dist += min(abs(diff_aisles-1),diff_aisles)*2 + diff_aisles*2


            picked_row = heuristic_s_picking_row(row,current_aisle,direction,layout)
            total_dist += picked_row[0]
            previous_aisle = current_aisle
        
        elif len(aisles_to_pick_from) == 0:
            total_dist += 42


            


    # #GOING BACK UP
    # total_dist += dist between current aisle and first aisle
    # total_dist += dist between end_row and first row
    total_dist += return_to_start(last_row_with_items,previous_aisle)
    # return total dist
    
    return total_dist
    pass

if __name__ == "__main__":
    # layout = layout(80,4,4,4)
    # skus = [1140,1141,1341,1440,2140,2141,2341,2440]
    # print(heuristic_s(layout=layout,sku_list=skus))
    # skus = [1140,3140]
    # print(heuristic_s(layout=layout,sku_list=skus))
    # skus = [1140,3141]
    # print(heuristic_s(layout=layout,sku_list=skus))
    # skus = [2140]
    # print(heuristic_s(layout=layout,sku_list=skus))
    # skus = [3141]
    # print(heuristic_s(layout=layout,sku_list=skus))
    # layout = layout(80,0,10,10)
    # skus = [101040]
    # print(heuristic_s(layout=layout,sku_list=skus))
    
    pass
