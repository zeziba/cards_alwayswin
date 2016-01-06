__author__ = 'Charles Engen'


"""
This module will simulate random chance using poker dice.

Using https://en.wikipedia.org/wiki/Poker_dice as a template for the probabilities
I have created a game that the house always wins. Currently there is only one roll
to determine if you have a winning hand. This decreases the chances of getting a five of a kind
dramatically.

Using this simple algorithm I have demonstrated that it is a simple matter of
generating something where the house will win frequently but there is enough incentive
for a player to keep hitting go again.

With the simple values returned with the hand, we can use the value returned to give
out prizes based on that value. With anything 3(Three of a kind) or lower only giving marginally
good prizes and the rest giving gifts that are magnitudes better than the last.
This ensures that there is always incentive to roll again but the odds of getting the best prizes
are marginal at best ensuring the player does not feel ripped off.
"""

from random import randint
from collections import Counter


def dice_rules(hand):
    multiples = {2: 'Pair', 3: 'Three of a Kind', 4: 'Four of a Kind', 5: 'Five of a kind'}
    full_house = ['Pair', 'Three of a Kind']
    _hand = [multiples[count] for hand_, count in Counter(hand).items() if count in multiples]

    hand_values = {
        'Five of a kind': 7,
        'Four of a Kind': 6,
        'Full House': 5,
        'Straight': 4,
        'Three of a Kind': 3,
        'Two Pair': 2,
        'Pair': 1,
        'Bust': 0
    }

    if 'Five of a kind' in _hand:
        return ['Five of a kind'], hand_values['Five of a kind']
    elif sorted(hand) in ([i for i in range(1, 6)], [i for i in range(2, 7)]):
        return ['Straight'], hand_values['Straight']
    elif ' '.join(sorted(_hand)) == ' '.join(sorted(full_house)):
        return ['Full House'], hand_values['Full House']
    elif _hand == ['Pair', 'Pair']:
        return ['Two Pair'], hand_values['Two Pair']
    else:
        return (_hand, hand_values['Pair']) if _hand else (['Bust'], hand_values['Bust'])


class Dice(object):

    def __init__(self, sides=6):
        self.sides = 6

    def __call__(self):
        return randint(1, self.sides)


class PokeDiceGame(object):

    def __init__(self):
        self.cup_of_dice = [Dice() for i in range(5)]
        self.current_hand = []

    def roll_hand(self):
        self.current_hand = []
        for die in self.cup_of_dice:
            self.current_hand.append(die())


if __name__ == '__main__':
    root = PokeDiceGame()
    print(dice_rules([1, 2, 3, 4, 5]))
    print(dice_rules([2, 3, 4, 5, 6]))
    while True:
        root.roll_hand()
        print(root.current_hand)
        print(dice_rules(root.current_hand))
        input("Hit enter to continue.")