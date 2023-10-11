"""
Author : Tan Jian Xi
last modified: 11/10
last modified by: Tan Jian Xi
"""



from Layout import layout
from HeuristicSPicking import heuristic_s
from AstarAlgorithm import a_star_algorithm
from RandomAlgorithm import RandomPicking
import math


#Use Scenario as the master class where all data is stored - including results, for analysis
class Scenario():

    def __init__(self, layout:layout, worker_no:int, SKUlist:list) -> None:
        self.layout = layout
        self.worker_no = worker_no
        self.SKUlist = SKUlist
        #under here add other stuff, such as time taken etc etc

        pass 
    pass

    def simulate_heuristic_s(self):
        """
        Returns [total_dist_travelled,time_taken]
        """
        if self.worker_no == 1:
            #dist travelled
            total_dist_travelled = heuristic_s(self.SKUlist,self.layout)

            #time to walk 1 m = 2.5s
            time_taken = total_dist_travelled*2.5


            return [total_dist_travelled,time_taken]
        else:
            chunks = [self.SKUlist[x:x+math.ceil(len(self.SKUlist)/self.worker_no)] for x in range(0, len(self.SKUlist), math.ceil(len(self.SKUlist)/self.worker_no))]
            total_dist_travelled = 0
            total_time_taken = 0
            for chunk in chunks:
                sub = heuristic_s(chunk,self.layout)
                total_dist_travelled += sub
                if sub*2.5 > total_time_taken:
                    total_time_taken = sub*2.5  
            return [total_dist_travelled,total_time_taken]

    
    def simulate_a_star(self):
        """
        Returns [total_dist_travelled,time_taken]
        """
        #dist travelled
        if self.worker_no == 1:
            try:
                total_dist_travelled = a_star_algorithm(self.layout,self.SKUlist)
            except Exception:
                return [-1,-1]
            
            #time to walk 1 m = 2.5s
            time_taken = total_dist_travelled*2.5

            return [total_dist_travelled,time_taken]
        else:
            chunks = [self.SKUlist[x:x+math.ceil(len(self.SKUlist)/self.worker_no)] for x in range(0, len(self.SKUlist), math.ceil(len(self.SKUlist)/self.worker_no))]
            total_dist_travelled = 0
            total_time_taken = 0

            for chunk in chunks:
                try:
                    
                    sub = a_star_algorithm(self.layout,chunk)
                    total_dist_travelled += sub
                    if sub*2.5 > total_time_taken:
                        total_time_taken = sub*2.5  
                except Exception:
                    return [-1,-1]
            return [total_dist_travelled,total_time_taken]

    
    def simulate_random(self):
        """
        Returns [total_dist_travelled,time_taken]
        """
        if self.worker_no == 1:
            #dist travelled
            total_dist_travelled = RandomPicking(self.SKUlist,self.layout)

            #time to walk 1 m = 2.5s
            time_taken = total_dist_travelled*2.5

            return [total_dist_travelled,time_taken]
        else:
            chunks = [self.SKUlist[x:x+math.ceil(len(self.SKUlist)/self.worker_no)] for x in range(0, len(self.SKUlist), math.ceil(len(self.SKUlist)/self.worker_no))]            
            total_dist_travelled = 0
            total_time_taken = 0
            for chunk in chunks:
                sub = RandomPicking(chunk,self.layout)
                total_dist_travelled += sub
                if sub*2.5 > total_time_taken:
                        total_time_taken = sub*2.5
            return [total_dist_travelled,total_time_taken]