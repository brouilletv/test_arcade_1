"""
test
Vincent Brouillet
groupe: 405
20 cercle
"""


import arcade
import random as r

color_list = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
        self.number_circle = 0

    def on_draw(self):
        if self.number_circle >= 20:
            pass
        else:
            arcade.draw_circle_filled(r.randint(20, 620), r.randint(20, 460), 20, (r.choice(color_list)))
            self.number_circle += 1


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
