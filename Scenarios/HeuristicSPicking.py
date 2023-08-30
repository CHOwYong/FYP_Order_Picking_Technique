from Layout import *

def get_sku_list_rows(sku_list:list,layout:layout):
    no_rows = layout.no_cross_aisles + 1
    res = [[] for _ in range(no_rows)]

    for i in sku_list:
        row_no = int(str(i)[0])
        res[row_no-1].append(i)

    return res

def get_aisles(sku_list:list):
    aisles = []
    for i in range(len(sku_list)):
        sku_list[i] = str(sku_list[i])
      
    
    for sku in sku_list:
        sku_col = int(sku[1]) #column no
        sku_no  = int(sku[2:])
        if sku_no > 40:
            #means sku is on the right side of the aisle
            if sku_col + 1 not in aisles:
                aisles.append(sku_col + 1)
        else:
            if sku_col not in aisles:
                aisles.append(sku_col)

    return sorted(aisles)


def move_down_next_row(ended_at:int,sku_next_row:list):
    aisles_next_row = get_aisles(sku_list=sku_next_row)

    if abs(ended_at - aisles_next_row[0]) < abs(ended_at - aisles_next_row[-1]):
        return(2 + abs(ended_at - aisles_next_row[0]),aisles_next_row[0],"right")
    else:
        return(2 + abs(ended_at - aisles_next_row[-1]),aisles_next_row[-1],"left")


def heuristic_s_picking_row(sku_list:list,start_aisle:int,direction:str):
    sku_list = sorted(sku_list)
    total_dist = 0
    aisles = get_aisles(sku_list=sku_list)
    ended_at = None

    if direction == "left":
        end_aisle = aisles[0]
        ended_at = (int(str(sku_list[0])[0]),aisles[0])
    else:
        end_aisle = aisles[-1]
        ended_at = (int(str(sku_list[0])[0]),aisles[-1])

    if start_aisle != end_aisle:
        dist_horizontal = (abs(start_aisle - end_aisle) - 1)*2 + (abs(start_aisle - end_aisle))*2 #number of aisle to traverse + number of shelves passed
        dist_vertical = len(aisles)*40
        total_dist = total_dist + dist_horizontal + dist_vertical
    else:
        total_dist = 40


    if len(aisles)%2 == 0:
        total_dist += 40


    return (total_dist,ended_at)

def return_to_start(row_aisle:set):
    row = row_aisle[0]
    aisle = row_aisle[1]
    total_dist = 0

    if row_aisle != 1:
        dist_horizontal = (abs(aisle - 2))*2 + (abs(aisle-1)*2) #number of aisle to traverse + number of shelves passed
        dist_vertical = row*40
        total_dist = total_dist + dist_horizontal + dist_vertical
    else:
        total_dist = row*40 + (row - 1)*2
    
    return total_dist

def heuristic_s(layout:layout,sku_list)->int:
    sku_list_rows = get_sku_list_rows(sku_list=sku_list,layout=layout)

    start_aisle = 1 #STARTING POS
    direction = "right"
    total_dist = 0
    ended_at = None

    for row in sku_list_rows:
        if ended_at is not None:
            move_down_next_row_res = move_down_next_row(ended_at[1],row)
            total_dist += move_down_next_row_res[0]
            start_aisle = move_down_next_row_res[1]
            direction = move_down_next_row_res[2]

        dist_pick_row = heuristic_s_picking_row(row,start_aisle,direction)
        total_dist += dist_pick_row[0]
        ended_at = dist_pick_row[1]

    total_dist += return_to_start((ended_at[0],ended_at[1]))
    

    return total_dist

        


if __name__ == "__main__":
    skus = [1140,1141,1341,1440,2140,2141,2341,2440]
    layout = layout(80,4,1,4)
    # print(get_sku_list_rows(skus))
    # skus = [1140,1141,1341,1440]
    # print(get_aisles(sku_list=skus))
    # print(heuristic_s_picking_row(sku_list=skus,direction="left"))
    print(heuristic_s(layout=layout,sku_list=skus))
    pass
