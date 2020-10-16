# Задание 2.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size, height):
        self.V = size
        self.H = height

    @abstractmethod
    def tissue_cons(self):
        pass

    @property
    def tissue_cons_all(self):
        return f'Общий расход ткани: {round((self.V / 6.5 + 0.5) + (2 * self.H + 0.3))}.'


class Coat(Clothes):

    def __init__(self, size, heigth):
        super().__init__(size, heigth)

    def tissue_cons(self):
        coat_tissue = round(self.V / 6.5 + 0.5)
        return f'Расход ткани на пальто: {coat_tissue}.'


class Suit(Clothes):

    def __init__(self, size, height):
        super().__init__(size, height)

    def tissue_cons(self):
        suit_tissue = round(2 * self.H + 0.3)
        return f'Расход ткани на костюм: {suit_tissue}.'


coat = Coat(80, 160)
suit = Suit(90, 170)
print(coat.tissue_cons())
print(suit.tissue_cons())
print(coat.tissue_cons_all)
print(suit.tissue_cons_all)
