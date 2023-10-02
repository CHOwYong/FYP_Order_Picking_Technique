"""
Author : Subhan Saadat Khan
last modified: 15/09
last modified by: Subhan Saadat Khan
"""

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
    sideSection = False
    sameRow = True
    sameColumn = True
    i = 1
    while(i < len(skuList)):
        next_sku = str(skuList[i])
        if int(next_sku[0]) != int(curr_sku[0]):
            sameColumn = False
            #distance of walking through columns
            distance += (abs(int(next_sku[0]) - int(curr_sku[0])) - 1)*(40) + abs(int(next_sku[0]) - int(curr_sku[0]))*(2)
            #distance of covered when returning from your current shelf
            if int(next_sku[0]) > int(curr_sku[0]):
                if int(curr_sku[2:]) > 40:
                    distance += 80 - int(curr_sku[2:]) 
                    distance += 2
                else:
                    distance += 40 - int(curr_sku[2:]) 
            else:
                if int(curr_sku[2:]) > 40:
                    distance += abs(40 - int(curr_sku[2:]))
                    distance += 2
                else:
                    distance += int(curr_sku[2:]) 
                Top = False

        if int(next_sku[1]) != int(curr_sku[1]):
            sameRow = False
            if sameColumn and (abs(int(next_sku[1]) - int(curr_sku[1])) == 1):
                    if (int(next_sku[2:])<40 and int(curr_sku[2:])>40) and (int(curr_sku[1]) < int(next_sku[1])):
                        print("hello")
                        val = abs(40 - int(curr_sku[2:]))
                        sideSection = True
                        distance += 2 + abs(val - int(next_sku[2:]))
                    if (int(next_sku[2:])>40 and int(curr_sku[2:])<40) and (int(curr_sku[1]) > int(next_sku[1])):
                        val = abs(40 - int(next_sku[2:]))
                        distance += 2 + abs(val - int(curr_sku[2:]))
                        sideSection = True
                    # distance += 2 + abs(int(curr_sku[2:]) - int(next_sku[2:]))

            if not sideSection:
                distance += abs(int(next_sku[1]) - int(curr_sku[1]))*(2+2)
                if int(next_sku[1]) < int(curr_sku[1]):
                    left = False
                    distance -= 2

                if sameColumn:
                    #distance of covered when returning from your current shelf
                    if int(next_sku[0]) > int(curr_sku[0]):
                        if int(curr_sku[2:]) > 40:
                            distance += 80 - int(curr_sku[2:]) 
                        else:
                            distance += 40 - int(curr_sku[2:])
                        # distance -= 2

                    else:
                        if int(curr_sku[2:]) > 40:
                            distance += abs(40 - int(curr_sku[2:]))
                        else:
                            distance += int(curr_sku[2:]) 
                        # distance -= 2
        
        if sameRow and sameColumn:
            nextDist = abs(int(next_sku[2:]) - int(curr_sku[2:]))
            #next is in section 1 and curr is in section 2
            if int(next_sku[2:])<40 and int(curr_sku[2:])>40:
                # distance += 80 - int(curr_sku[2:])
                distance += abs(40 - int(curr_sku[2:]))
                # distance += int(curr_sku[2:])
                left = False

            #next is in section 2 and curr is in section 1
            elif int(next_sku[2:])>40 and int(curr_sku[2:])<40:
                distance += int(curr_sku[2:])
            
            #both locations are in same section
            else:
                sameSection = True
                distance += nextDist

        elif sameRow and not sameColumn:
            pass


        
        skuFlag = bool(int(next_sku[2:]) > 40)

        if skuFlag and not sameSection and not sideSection:
            if Top and left:
                distance += 2 + abs(40 - int(next_sku[2:]))
            elif Top and left == False:
                distance += abs(40 - int(next_sku[2:]))
            elif Top == False and left:
                distance += 2 + abs(80 - int(next_sku[2:]))
            else:
                distance += abs(80 - int(next_sku[2:]))

        elif not skuFlag and not sameSection and not sideSection:
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
        sideSection = False
        i += 1

    return distance

def RandomPicking(skuList):
    dist = start_picking(skuList)
    totalDist = visit_next_sku(dist, skuList)
    return totalDist

if __name__ == "__main__":
    # skus = [3278,1268,2108]

    #same row but different column (top to bottom)
    # skus = [1223,3238] #shelf 1 #126
    # skus = [1223,3253] #shelf 2 #103

    #same row but different column (bottom to top)
    # skus = [3238,1223] #shelf 1 #225 
    # skus = [3238,1253] #shelf 2 #237

    #same column but different row (top to bottom)
    # skus = [3238,3338] #shelf 1 #206m
    # skus = [3238,3348] #shelf 2 #178m

    #same column but different row (bottom to top)
    # skus = [3338,3238] #shelf 1 #210
    # skus = [3438,3248] #shelf 2 #186

    # same column same row
    #same section
    # skus = [3217,3238] #126
    # skus = [3217,3248] #132
    # skus = [3248,3273] #123
    # skus = [3248,3217] #125

    #special case
    # skus = [3248,3317] #109
    # skus = [3223,3168] #118

    # tester
    # skus = [2356,3221,1106,3161,2131,3378]  #278
    # skus = [2356,3221]  #278
    
    print(RandomPicking(skus))
    pass
            

            
           





