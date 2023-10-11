"""
Author : Tan Jian Xi
last modified: 20/9
last modified by: Tan Jian Xi
"""

import csv

"""
Information to be recorded:
-DIST TRAVELLED RANDOM
-TIME TAKEN RANDOM
-DIST TRAVELLED HEURISTIC
-TIME TAKEN HEURISTIC
-DIST TRAVELLED OPTIMAL
-TIME TAKEN OPTIMAL
-NO OF CROSS AISLES
-NO OF PICKERS
-GENERATION SEED(FOR SKU PLACEMENT)
"""
CSVHEADER = ["SEED","DIST TRAVELLED RANDOM","TIME TAKEN RANDOM","DIST TRAVELLED HEURISTIC","TIME TAKEN HEURISTIC","DIST TRAVELLED OPTIMAL","TIME TAKEN OPTIMAL","NO OF CROSS AISLES","NO OF PICKERS", "NO ROWS COLS","NO SKUS"]

def writeNewCsv(filename:str,data:list[list]) -> bool:
    fields = CSVHEADER

    with open(filename,"w",newline='') as csvfile:
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        
        # writing the data rows 
        csvwriter.writerows(data)
    
    return True


def appendCsv(filename:str,data:list[list]) -> bool:
    

    with open(filename,"a",newline='') as csvfile:
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the data rows 
        csvwriter.writerows(data)
    
    return True

    
