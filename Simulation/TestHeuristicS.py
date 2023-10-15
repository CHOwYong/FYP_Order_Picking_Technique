import unittest
from Layout import layout
from HeuristicSPicking import *

class TestHeuristicS(unittest.TestCase):
    def test_heuristic_s(self):
        layout1 = layout(80,4,4,4)
        """
        Ensure that correct value is calculated when there are multiple
        skus of the same rows and same columns
        """
        skus = [1140,1141,1341,1440,2140,2141,2341,2440]
        self.assertEqual(heuristic_s(layout=layout1,sku_list=skus),354)

        """
        Ensure that algorithm works when skus to be picked are from rows
        not successive to each other
        """
        skus = [1140,3140]
        self.assertEqual(heuristic_s(layout=layout1,sku_list=skus),248)

        """
        Ensure that algorithm works when skus to be picked are from columns
        not successive to each other
        """
        skus = [1140,1340]
        self.assertEqual(heuristic_s(layout=layout1,sku_list=skus),172)

        """
        Ensure that algorithm works when skus to be picked are from rows
        not successive to each other and columns not sucessive to each other
        """
        skus = [1140,3141]
        self.assertEqual(heuristic_s(layout=layout1,sku_list=skus),252)

        """
        Ensure that algorithm works when skus to be picked do not start from
        the row of the starting point(row 1)
        """
        skus = [2140]
        self.assertEqual(heuristic_s(layout=layout1,sku_list=skus),164)

        """
        Ensure that algorithm works when skus to be picked do not start from
        the row and column of the starting point(row 1)
        """
        skus = [3141]
        self.assertEqual(heuristic_s(layout=layout1,sku_list=skus),252)

        layout2 = layout(80,100,10,10)
        """
        Ensure that algorithm works when skus to be picked have sku id that 
        is more that 4
        """
        skus = [101040]
        self.assertEqual(heuristic_s(layout=layout2,sku_list=skus),904)

    def test_get_sku_list_rows(self):
        layout1 = layout(80,4,4,4)
        skus = [1140,1141,1341,1440,2140,2141,2341,2440]
        self.assertEqual(get_sku_list_rows(skus,layout1),[[1140,1141,1341,1440],[2140,2141,2341,2440],[],[]])
        skus = []
        self.assertEqual(get_sku_list_rows(skus,layout1),[[],[],[],[]])
        skus = [1440]
        self.assertEqual(get_sku_list_rows(skus,layout1),[[1440],[],[],[]])
        skus = [2440]
        self.assertEqual(get_sku_list_rows(skus,layout1),[[],[2440],[],[]])
        skus = [3440]
        self.assertEqual(get_sku_list_rows(skus,layout1),[[],[],[3440],[]])
        skus = [4440]
        self.assertEqual(get_sku_list_rows(skus,layout1),[[],[],[],[4440]])

    def test_get_aisles(self):
        layout1 = layout(80,4,4,4)
        skus = [1140,1141,1341,1440,2140,2141,2341,2440]
        self.assertEqual(get_aisles(skus,layout1),[1,2,4])

    def test_return_to_start(self):
        self.assertEqual(return_to_start(row = 1,aisle = 1),40)
        self.assertEqual(return_to_start(row = 1,aisle = 2),42)
        self.assertEqual(return_to_start(row = 2,aisle = 1),82)
        self.assertEqual(return_to_start(row = 2,aisle = 2),84)
        self.assertEqual(return_to_start(row = 2,aisle = 3),88)
        self.assertEqual(return_to_start(row = 3,aisle = 3),130)
        pass






if __name__ == '__main__':
    unittest.main()