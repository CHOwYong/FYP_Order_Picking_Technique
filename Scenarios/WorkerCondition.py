import Condition
import random

#IN THIS CLASS, VALUES OF NONE INDICATE PLACEHOLDER/UNINITIALIZED VALUES


class WorkerCondition(Condition):
    def __init__(self, random_generation :bool, worker_num:int = None) -> None:
        super(random_generation)
        self.worker_number = worker_num
        pass

    def load(self):
        if (self.random_gen and self.worker_number is None):
            self.worker_number = random.randint(1,3)
        return self.worker_number

    pass