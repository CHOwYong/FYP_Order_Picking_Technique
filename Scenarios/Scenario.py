from Layout import layout
from WorkerCondition import WorkerCondition


#Use Scenario as the master class where all data is stored - including results, for analysis
class Scenario():

    def __init__(self, layout:layout, worker_condition:WorkerCondition) -> None:
        self.layout = layout
        self.worker_condition = worker_condition
        #under here add other stuff, such as time taken etc etc

        pass 
    pass