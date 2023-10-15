import unittest
from Layout import layout
from Scenario import Scenario


class TestScenario(unittest.TestCase):

    def test_initialize(self):
        layout1 = layout(80,81,9,9)
        noWorkers = 10
        skus = [1140,1141,1341,1440,2140,2141,2341,2440]
        testS = Scenario(layout1,noWorkers,skus)

        self.assertEqual(testS.layout,layout1)
        self.assertEqual(testS.worker_no,noWorkers)
        self.assertEqual(testS.SKUlist, skus)
    
    def test_heuristic(self):
        
        layout1 = layout(40,81,9,9)
        noWorkers = 1
        skus = [1140,2341,2440]
        testS1 = Scenario(layout1,noWorkers,skus)


        """
        Testing heuristic method when there is 1 worker
        """

        self.assertEqual(testS1.simulate_heuristic_s(),[184,460])

        

        noWorkers = 3
        testS2 = Scenario(layout1,noWorkers,skus)
        

        """
        Testing heuristic method when there is more than 1 worker
        """
        self.assertEqual(testS2.simulate_heuristic_s(),[448,460])
        

        noWorkers = 10
        testS3 = Scenario(layout1,noWorkers,skus)

        """
        Testing heuristic when no of workers exceeds no of skus
        """
        self.assertEqual(testS3.simulate_heuristic_s(),[448,460])
        

        pass

    def test_a_star(self):
        """
        Testing A Star method when there is 1 worker
        """
        layout1 = layout(40,81,9,9)
        noWorkers = 1
        skus = [1140,2440]
        layout1.load()
        testS1 = Scenario(layout1,noWorkers,skus)
        self.assertEqual(testS1.simulate_a_star(),[179,447.5])

        
        noWorkers = 2
        testS2 = Scenario(layout1,noWorkers,skus)
        """
        Testing A Star method when there is more than 1 worker
        """
        self.assertEqual(testS2.simulate_a_star(),[221,447.5])

        
        noWorkers = 10
        testS3 = Scenario(layout1,noWorkers,skus)
        """
        Testing A-star when no of workers exceeds no of skus
        """
        self.assertEqual(testS3.simulate_a_star(),[221,447.5])
        pass

if __name__ == "__main__":
    unittest.main()