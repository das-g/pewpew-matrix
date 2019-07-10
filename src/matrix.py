import pew
from random import randrange, random, uniform

pew.init()
screen = pew.Pix()

def darken_screen():
    for x in range(screen.width):
        for y in range(screen.height):
            c = darken(screen.pixel(x, y))
            screen.pixel(x, y, c)

def darken(c):
    d = 1 if random() > .5 else 0
    return c - d if c > 0 else 0

class Blot:
    def __init__(self):
        self.x = randrange(screen.width)
        self.y = 0.0
        self.speed = uniform(0.2, 1.5)

    def step(self):
        self.y += self.speed
        if self.y > screen.height:
            blots.remove(self)
            blots.add(Blot())
            del(self)
            return
        screen.pixel(self.x, int(self.y), 3)

blots = set(Blot() for _ in range(8))

while True:
    darken_screen()
    for b in blots:
        b.step()
    pew.show(screen)
