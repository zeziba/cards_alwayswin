import unittest

import pd_main


class TestMethods(unittest.TestCase):
    def test_bust(self):
        self.assertEqual(pd_main.dice_rules(hand=[5, 6, 3, 1, 4]), (['Bust'], 0))
        
    def test_pair(self):
        self.assertEqual(pd_main.dice_rules(hand=[5, 6, 3, 1, 1]), (['Pair'], 1))

    def test_two_pair(self):
        self.assertEqual(pd_main.dice_rules(hand=[5, 3, 3, 1, 1]), (['Two Pair'], 2))

    def test_three_kind(self):
        self.assertEqual(pd_main.dice_rules(hand=[5, 6, 1, 1, 1]), (['Three of a Kind'], 1))

    def test_straight(self):
        self.assertEqual(pd_main.dice_rules(hand=[1, 2, 3, 4, 5]), (['Straight'], 4))

    def test_full_house(self):
        self.assertEqual(pd_main.dice_rules(hand=[3, 3, 3, 6, 6]), (['Full House'], 5))

    def test_four_kind(self):
        self.assertEqual(pd_main.dice_rules(hand=[4, 4, 4, 4, 1]), (['Four of a Kind'], 1))

    def test_five_kind(self):
        self.assertEqual(pd_main.dice_rules(hand=[1, 1, 1, 1, 1]), (['Five of a kind'], 7))
    
    def test_die(self):
        dice = pd_main.Dice()
        self.assertAlmostEqual(dice(), 3, delta=3)

    def test_game_dice_generation(self):
        game = pd_main.PokeDiceGame()
        self.assertEqual(all(type(die) is pd_main.Dice for die in game.current_hand), True)

    def test_game(self):
        game = pd_main.PokeDiceGame()
        game.roll_hand()
        self.assertEqual(all(type(die) is int for die in game.current_hand), True)


if __name__ == '__main__':
    unittest.main()
