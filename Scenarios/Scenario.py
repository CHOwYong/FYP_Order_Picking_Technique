"""
Author : Tan Jian Xi
last modified: 16/9
last modified by: Tan Jian Xi
"""



from Layout import layout
from WorkerCondition import WorkerCondition
from HeuristicSPicking import heuristic_s
from csv import writer


#Use Scenario as the master class where all data is stored - including results, for analysis
class Scenario():

    def __init__(self, layout:layout, worker_condition:WorkerCondition, SKUlist:list) -> None:
        self.layout = layout
        self.worker_condition = worker_condition
        self.SKUlist = SKUlist
        #under here add other stuff, such as time taken etc etc

        pass 
    pass

    def simulate_heuristic_s(self):
        #dist travelled
        total_dist_travelled = heuristic_s(self.layout,self.SKUlist)

        #time to walk 1 m = 2.5s
        time_taken = total_dist_travelled*2.5

        #cross aisles
        no_cross_aisles = self.layout.no_cross_aisles

        #no workers
        no_workers = self.worker_condition.worker_number

        #picking method
        picking_method = "Heuristic S"

        return [picking_method,total_dist_travelled,time_taken,no_cross_aisles,no_workers]