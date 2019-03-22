import unittest
from test import fact,div
class test(unittest.TestCase):
    def test_fact(self):
        re=fact(5)
        self.assertEqual(re,120)
    def test_div(self):
        re=div(2)
        self.assertEqual(re,1)
if __name__=="__main__":
    unittest.main()