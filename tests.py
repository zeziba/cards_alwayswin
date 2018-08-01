import unittest

import pd_main


class TestMethods(unittest.TestCase):
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(), ['Bust'])
        
    def test_pair(self):
        self.assertEqual(pd_main.dice_rules(), ['Pair'])
        
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(), ['Bust'])
        
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(), ['Bust'])
        
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(), ['Bust'])
        
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(), ['Bust'])
        
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(), ['Bust'])
        
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(), ['Bust'])
    
    def test_die(self):
        dice = pd_main.Dice()


if __name__ == '__main__':
unittest.main()
