#purpose of this class is to enable fixing of certain variables
#for example for all simulations use layout 1
#all simulations use only 2 workers etcetc
#we do this by having this being the main interface

#SO here we will be mass producing scenarios
#Then feeding it to the simulation running component

from Scenario import Scenario
from csv import writer

class ScenarioFactory():
    def __init__(self) -> None:
        pass

    def simulate(self):
        pass