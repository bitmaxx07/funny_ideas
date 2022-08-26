"""
This script simulates the growth of a player's weight change in his career
"""
import math
import random


class Player:
    def __init__(self, name, weight, height, age):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age

    def calculate_bmi(self, weight, height):
        return weight / (math.sqrt(height / 100))

    def evaluate_growth(self):
        # height only increases before 22 yrs old
        if self.age > 22:
            flag = True
        # the increase of height before 22 is with probability 65% at 18, 40% at 19, 30% at 20, 20% at 21 and 10% at 22
        if self.age == 18:
            if random.randrange(0, 100) <= 65:
                self.height += random.randrange(1, 5)
        if self.age == 19:
            if random.randrange(0, 100) <= 40:
                self.height += random.randrange(1, 4)
        if self.age == 20:
            if random.randrange(0, 100) <= 30:
                self.height += random.randrange(1, 3)
        if self.age == 21:
            if random.randrange(0, 100) <= 20:
                self.height += random.randrange(1, 2)
        if self.age == 22:
            if random.randrange(0, 100) <= 10:
                self.height += + 1
        # if the player's BMI is already too large or too small, we should decrease the trend to change them
        if self.calculate_bmi(self.weight, self.height) < 18.5 or \
                self.calculate_bmi(self.weight, self.height) > 24.9:
            self.weight += random.randrange(-2, 2)
        else:
            self.weight += random.randrange(-5, 9)
        self.age += 1

    def print_info(self):
        print("name: " + self.name + ", height: " + str(self.height) + ", weight: " + str(self.weight) + ", age: "
              + str(self.age))


player = Player("Joe", 80, 180, 17)

for i in range(1, 10):
    player.evaluate_growth()
    player.print_info()
