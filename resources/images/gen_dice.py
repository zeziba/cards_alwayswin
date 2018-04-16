import PIL
from PIL import Image, ImageDraw, ImageFont
from os import path


class Die:

    def __init__(self, width=120, height=120, sides=6):
        self.card = (width, height)
        for i in range(1, sides + 1):
            self.gen_die("{}".format(i), "die_{}".format(i))

    @property
    def width(self):
        return self.card[0]

    @property
    def height(self):
        return self.card[1]

    def gen_die(self, text, die_name, color=(0, 0, 0), font_color=(255, 255, 255)):
        img = Image.new('RGB', (self.width, self.height), color=color)
        fnt = ImageFont.load_default().font
        d = ImageDraw.Draw(img)
        d.text((self.width // 2, self.height // 2), text=text, font=fnt, fill=font_color)

        img.save("{}.png".format(die_name))


if __name__ == "__main__":
    dies = Die()
