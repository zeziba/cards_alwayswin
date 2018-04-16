import PIL
from PIL import Image


class Dice:

    def __init__(self, dice=6):
        self.dice = []
        self.dice_number = dice

    def load(self, location="./"):
        for i in range(1, self.dice_number + 1):
            self.dice.append(Image.open("die_{}.png".format(i)))

    def get(self, num):
        return self.dice[num - 1]
