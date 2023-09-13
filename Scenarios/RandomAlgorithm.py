
def start_picking(skuList):
    totalDistance = 0
    first_sku = str(skuList[0])
    col_num = int(first_sku[0])
    row_num = int(first_sku[1])
    sku_num = int(first_sku[2:])
    totalDistance = ((col_num-1)*40 + (col_num-1)*2) + ((row_num-1)*2 + (row_num-1)*2)
    if sku_num > 40:
        totalDistance += (2 + sku_num)
    else:
        totalDistance += sku_num
    return totalDistance

def visit_next_sku(distance, skuList):
    curr_sku = str(skuList[0])
    i = 1
    while(i < len(skuList)):
        next_sku = str(skuList[i])
        if int(next_sku[0]) != int(curr_sku[0]):
            distance += abs(next_sku[0] - curr_sku[0])*(40+2)
        if int(next_sku[1]) != int(curr_sku[1]):
            distance += abs(next_sku[0] - curr_sku[0])*(40+2)




