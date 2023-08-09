import Condition

class WorkerCondition(Condition):
    def __init__(self, worker_num):
        self.worker_number = worker_num
        pass

    def load(self):
        pass

    pass