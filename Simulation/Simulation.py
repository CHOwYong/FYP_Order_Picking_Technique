"""
Author : Tan Jian Xi
last modified: 11/10
last modified by: Tan Jian Xi
"""




#purpose of this class is to enable fixing of certain variables
#for example for all simulations use layout 1
#all simulations use only 2 workers etcetc
#we do this by having this being the main interface

#SO here we will be mass producing scenarios
#Then feeding it to the simulation running component

from Scenario import Scenario
from datetime import datetime
from SKUPlacement import WarehouseSKUIDGenerator
from Layout import layout
import random
from CSVWriter import writeNewCsv
import sys


def simulate(rangeRowsCols:int,maxNoSKUs:int,noIterations:int,noWorkers:int,filename:str,rangeRowColsFixed:int = 0,maxNoSkusFixed:int = 0,noWorkersFixed:int = 0) -> None:
    """
    Function that runs the simulation and writes output to a .csv file
    """
    if rangeRowsCols >= 10 or rangeRowsCols < 1:
        print("RangeRowsCols must be in range 1-9.")
        return 0
    
    if maxNoSKUs > 40 or maxNoSKUs < 1:
        print("Max no of Skus to be picked must be in range 1-40.")
        return 0

    if noIterations < 1:
        print("Number of iterations must be more than 0.")
        return 0

    skusPerAisle = 40 #Pre Assumption made during definition of warehouse.

    res = []

    
    for i in range(noIterations):
        print("Running Iteration",i + 1)

        seed = datetime.now().timestamp() + i
        
        rowsCols = 0
        if (rangeRowColsFixed):
            rowsCols = rangeRowsCols
        else:
            rowsCols = random.randint(1,rangeRowsCols)
        
        noSkus = 0
        if (maxNoSkusFixed):
            noSkus = maxNoSKUs
        else:
            noSkus = random.randint(1,maxNoSKUs)

        no_workers = 0
        if(noWorkersFixed):
            no_workers = noWorkers
        else:
            no_workers = random.randint(1,noWorkers)

        warehouseLayout = layout(no_of_sku_per_aisle = skusPerAisle,no_of_shelves=0,no_of_rows=rowsCols,no_of_columns=rowsCols)
        warehouseLayout.load()

        skuGenerator = WarehouseSKUIDGenerator(seed=seed,num_columns=warehouseLayout.no_of_columns,num_rows=warehouseLayout.no_of_rows,skus_per_aisle=skusPerAisle,num_of_items=noSkus)

        skuGenerator.generate_all_skus()
        skuList = skuGenerator.skus

        
        currentScenario = Scenario(layout=warehouseLayout,worker_no=no_workers,SKUlist=skuList)

        resRandom = currentScenario.simulate_random()
        resHeuristic = currentScenario.simulate_heuristic_s()
        
        
        resAStar = currentScenario.simulate_a_star()
        

        subres = [seed] + resRandom + resHeuristic + resAStar + [warehouseLayout.no_cross_aisles] + [no_workers] + [rowsCols] + [noSkus]
        res.append(subres)

    writeNewCsv(filename + ".csv",res)
    
    print("Results Have Been Written to " + filename + ".csv")


if __name__ == "__main__":
    #max no of SKUS is 40
    #max rows and cols is 9
    # simulate(9,40,500,4,"results")
    # simulate(9,40,500,4,"NoWorkersEffect",rangeRowColsFixed=1,maxNoSkusFixed=1)
    # simulate(9,40,500,1,"RangeColRowsEffect",noWorkersFixed=1,maxNoSkusFixed=1)
    # simulate(9,40,500,1,"MaxNoSkusEffect",noWorkersFixed=1,rangeRowColsFixed=1)
    print("----------------------------------------------------------------------------------------")
    print("Hi! Welcome to the warehouse simulation! To begin, please fill in the following prompts.")

    rangeRowCols = -1
    while True:
        rangeRowCols = int(input("Please enter an integer input in the range of 1 to 9 for how many Rows and Columns the warehouse can have!\n"))
        if rangeRowCols in range(0,10):
            break
        else:
            print("Number of Rows and Columns must be in range 1-9.\n")
    
    maxNoSkus = -1
    while True:
        maxNoSkus = int(input("Please enter an integer input in the range of 1 to 40 for how many SKU Orders can be given per scenario!\n"))
        if maxNoSkus in range(0,41):
            break
        else:
            print("Maximum number of SKU orders per scenario must be in range 1-40.\n")

    
    noWorkers = -1
    while True:
        noWorkers = int(input("Please enter a positive integer input larger than 0 for how many workers may be active in a scenario!\n"))
        if noWorkers >= 1:
            break
        else:
            print("Number of workers must be a positive integer larger than 0.\n")

    noIterations = -1
    while True:
        noIterations = int(input("Please enter a positive integer input larger than 0 for how many iterations should the simulation run!\n"))
        if noIterations >= 1:
            break
        else:
            print("No Iterations must be a positive integer larger than 0.\n")
    
    filename = input("Please enter a filename for the outputted .csv file! There is no need to include the .csv extension in the name.\n")
    
    rangeRowColsFixed = -1
    while True:
        rangeRowColsFixed = int(input("Please enter 1 if you want to fix the number of cols and rows for every iteration of the simulation, and 0 otherwise.\n"))
        if rangeRowColsFixed == 1 or rangeRowColsFixed == 0:
            break
        else:
            print("A value that was not 0 or 1 was given.\n")

    maxNoSkusFixed = -1
    while True:
        maxNoSkusFixed = int(input("Please enter 1 if you want to fix the number of SKU orders for every iteration of the simulation, and 0 otherwise.\n"))
        if maxNoSkusFixed == 1 or maxNoSkusFixed == 0:
            break
        else:
            print("A value that was not 0 or 1 was given.\n")

    noWorkersFixed = -1
    while True:
        noWorkersFixed = int(input("Please enter 1 if you want to fix the number of workers/pickers for every iteration of the simulation, and 0 otherwise.\n"))
        if noWorkersFixed == 1 or noWorkersFixed == 0:
            break
        else:
            print("A value that was not 0 or 1 was given.\n")


    simulate(rangeRowCols,maxNoSkus,noIterations,noWorkers,filename,rangeRowColsFixed,maxNoSkusFixed,noWorkersFixed)
    print("----------------------------------------------------------------------------------------")