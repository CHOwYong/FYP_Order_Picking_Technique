#  [colum no], [row no], [no],[no}?

def start_picking(skuList):
    totalDistance = 0
    first_sku = str(skuList[0])
    col_num = int(first_sku[0])
    row_num = int(first_sku[1])
    sku_num = int(first_sku[2:])
    totalDistance = ((col_num-1)*40 + (col_num-1)*2) + ((row_num-1)*2 + (row_num-1)*2)
    if sku_num > 40:
        totalDistance += (2 + abs(40 - sku_num))
    else:
        totalDistance += sku_num
    return totalDistance

def visit_next_sku(distance, skuList):
    curr_sku = str(skuList[0])
    Top = True
    left = True
    sameSection = False
    sameRow = True
    sameColumn = True
    i = 1
    while(i < len(skuList)):
        next_sku = str(skuList[i])
        if int(next_sku[0]) != int(curr_sku[0]):
            sameColumn = False
            distance += (abs(int(next_sku[0]) - int(curr_sku[0])) - 1)*(40) + abs(int(next_sku[0]) - int(curr_sku[0]))*(2)
            if int(next_sku[0]) > int(curr_sku[0]):
                if int(curr_sku[2:]) > 40:
                    distance += 80 - int(curr_sku[2:]) 
                else:
                    distance += 40 - int(curr_sku[2:]) 
            else:
                if int(curr_sku[2:]) > 40:
                    distance += abs(40 - int(curr_sku[2:]))
                else:
                    distance += (curr_sku[2:]) 
                Top = False

        if int(next_sku[1]) != int(curr_sku[1]):
            sameRow = False
            distance += abs(int(next_sku[1]) - int(curr_sku[1]))*(2+2)
            if int(next_sku[1]) < int(curr_sku[1]):
                left = False
        
        if sameRow and sameColumn:
            nextDist = abs(int(next_sku[2:]) - int(curr_sku[2:]))
            if nextDist>=40 and int(curr_sku[2:]) > 40:
                # distance += 80 - int(curr_sku[2:])
                distance += abs(40 - int(curr_sku[2:]))
                left = False

            elif nextDist>=40 and int(curr_sku[2:]) < 40:
                distance += int(curr_sku[2:])
            
            elif nextDist<40:
                sameSection = True
                distance += nextDist

        elif sameRow and not sameColumn:
            pass


        
        skuFlag = bool(int(next_sku[2:]) > 40)

        if skuFlag and not sameSection:
            if Top and left:
                distance += 2 + abs(40 - int(next_sku[2:]))
            elif Top and left == False:
                distance += abs(40 - int(next_sku[2:]))
            elif Top == False and left:
                distance += 2 + abs(80 - int(next_sku[2:]))
            else:
                distance += abs(80 - int(next_sku[2:]))

        elif not skuFlag and not sameSection:
            if Top and left:
                distance += int(next_sku[2:])
            elif Top and left == False:
                distance += 2 + int(next_sku[2:])
            elif Top == False and left:
                distance += abs(40 - int(next_sku[2:]))
            else:
                distance += 2+ abs(40 - int(next_sku[2:]))

        curr_sku = next_sku
        Top = True
        left = True
        Top = True
        left = True
        sameSection = False
        i += 1

    return distance

def RandomPicking(skuList):
    dist = start_picking(skuList)
    totalDist = visit_next_sku(dist, skuList)
    return totalDist


if __name__ == "__main__":
    skus = [3278,1268,2108]
    # skus = [3278,3211]
    # skus = [3233,3278]
    print(RandomPicking(skus))
    pass
            

            
           





