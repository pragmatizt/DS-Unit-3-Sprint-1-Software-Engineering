# The only two modules we can use (that we haven't made)
# This code has been checked with pep8online.com/checkresult
import unittest
import random


class Product():

    def __init__(self, name=None, price=10, weight=20, flammability=0.5, identifier=1):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        self.stealability = self.price / self.weight
        if self.stealability < 0.5:
            print("Not so stealable...")
        else:
            print("Very stealable!")

    def explode(self):
        self.explode = self.flammability * self.weight
        if self.explode < 10:
            print("...fizzle.")
        if self.explode >= 10 < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")


class BoxingGlobe(Product):

    def __init__(self, name=None, price=10, weight=10, flammability=0.5, identifier=1):
        # From my understanding of super(), we restate what is inherited.
        # weight has a new definition (10) above; not included in super().
        super().__init__(name, price, flammability, identifier)

        self.weight = weight

    # This "overriding" concept is new; but fun reading about it.
    # Correct me if wrong, but I'm not even including code.
    # since it's a glove -- a simple print statement will do.
    def explode(self):
            print("... it's a glove")

    def punch(self):
        if self.weight < 5:
            print("*opponent shrugs punch off")
        if self.weight >= 5 < 15:
            print("Great punch, bro.")
        else:
            print("*opponent falls unconscious*")
