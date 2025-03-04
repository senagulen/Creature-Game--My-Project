from abc import ABC, abstractmethod
from enum import Enum
import random

"""
Weapon is an enum that controls the types and values of weapons that
creatures may possess. 
see: https://docs.python.org/3/library/enum.html
Each creature possesses one weapon.
The weapons have a value with the higher number more powerful than 
lower numbers.
When a creature A encounters creature B, their
weapons are compared. For each difference in weapons, the 
creature with the lesser weapon looses 10 life points.
For example, if creature A has magic as a weapon, and creature B
has arrow as a weapon, creature B will loose 10 life points.
If two creatures have the same weapon, no life points are lost,
but each creature will loose some of their special power.
The way each creature processes an encounter is determined by their 
update_life_level method.
"""


class Weapon (Enum):
    magic = 30
    arrow = 20
    club = 10


class Creature(ABC):
    """
    The abstract superclass that all creatures inherit from.
    """

    def __init__(self, id, name, weapon: Weapon, life_points=50):
        self.id = id
        self.name = name
        self.weapon = weapon
        self.life_points = life_points

    @abstractmethod
    def update_life_level(self, diff):
        self.life_points += diff

    @abstractmethod
    def is_alive(self) -> bool:
        return self.life_points > 0

    @abstractmethod
    def __str__(self):
        sstr = f'{"id:"} {self.id} {"name:"} {self.name} ' \
            f' {"life level:"} {self.life_points}' \
            f' {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()}'
        return (sstr)


class Conjurer(Creature):
    # TODO: constructor here
    def __init__(self, id, name, weapon, life_points=50, num_spells=5):
        super().__init__(id, name, weapon, life_points)
        self.num_spells = num_spells

    # TODO: implement this method:
    def update_life_level(self, diff):
        if diff > 0:
            self.life_points += diff
            self.num_spells += 1
        elif diff == 0:
            if self.num_spells > 0:
                self.num_spells -= 1
        else:
            if self.num_spells > 0:
                self.num_spells -= 1
            else:
                self.life_points -= abs(diff)
                if self.life_points < 0:
                    self.life_points = 0

    # TODO: implement this method: (DONE)

    def is_alive(self) -> bool:
        if self.life_points > 0:
            return True
        else:
            return False

    # TODO: implement this method: (DONE)
    def __str__(self):
        sstr = f'{"id:"} {self.id} {"name:"} {self.name} ' \
            f' {"life level:"} {self.life_points}' \
            f' {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()} ' \
            f'spells: {self.num_spells}'
        return (sstr)


class Elf(Creature):
    def __init__(self, id, name, weapon, life_points=50, mind_control=1.5):
        super().__init__(id, name, weapon, life_points)
        self.mind_control = mind_control

    # TODO: implement this method:
    def update_life_level(self, diff):
        if diff > 0:
            self.life_points += diff
            self.mind_control *= 1.25
        elif diff == 0:
            self.mind_control *= 0.75
        else:
            if self.mind_control > 0:
                self.mind_control *= 0.75
                self.life_points -= abs(diff) - 5
            else:
                self.life_points -= abs(diff)
    # TODO: implement this method:

    def is_alive(self) -> bool:
        if self.life_points > 0:
            return True
        return False

    # TODO: implement this method:
    def __str__(self):
        sstr = f'{"id:"} {self.id} {"name:"} {self.name} ' \
            f' {"life level:"} {self.life_points}' \
            f' {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()} ' \
            f'mind control: {self.mind_control}'
        return (sstr)


class Golem(Creature):
    def __init__(self, id, name, weapon, life_points=50, endurance=20):
        super().__init__(id, name, weapon, life_points)
        self.endurance = endurance

    # TODO: implement this method:
    def update_life_level(self, diff):
        if diff > 0:
            self.life_points += diff
            self.endurance *= 1.25
        elif diff == 0:
            self.endurance *= 0.5
        else:
            if self.endurance > 0:
                self.life_points -= abs(diff) - 5
                self.endurance *= 0.5
            else:
                self.life_points -= abs(diff)

    # TODO: implement this method:

    def is_alive(self) -> bool:
        if self.life_points > 0:
            return True
        return False

    # TODO: implement this method:
    def __str__(self):
        info_str = f'{"id:"} {self.id} {"name:"} {self.name} ' \
            f' {"life level:"} {self.life_points}' \
            f' {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()} ' \
            f'endurance: {self.endurance}'
        return (info_str)


# TODO: implement this function:
def do_engagement(creatureA: Creature, creatureB: Creature):
    if not creatureA.is_alive() or not creatureB.is_alive():
        return None

    if is_5percent_or_less():
        creatureA.life_points = 0
    fight = creatureA.weapon.value - creatureB.weapon.value
    creatureA.update_life_level(fight)
    creatureB.update_life_level(-fight)


# allow for a seed value to be set in the random number generator.

def set_seed(seed_val):
    random.seed(seed_val)


def is_5percent_or_less() -> bool:
    """
    True if a random number is generated with a 5%
    probability, False otherwise.
    """
    num = random.random()
    return (num <= 0.05)
def generate_id() -> str:
    lower = 111
    upper = 999
    return str(random.randint(lower, upper))
def print_all(list):
    for i in range(0, len(list)):
        print(list[i])

if __name__=="__main__":

  # some code to help test and debug your code:
  set_seed(123456)
  creatures = []
  # make some creatures for testing:
  elf1 = Elf(generate_id(), "Eowyn", Weapon.arrow)
  conj1 = Conjurer(generate_id(), "Gandalf", Weapon.magic)
  conj2 = Conjurer(generate_id(), "Morgana", Weapon.magic)
  gol1 = Golem(generate_id(), "Turf", Weapon.club)
  creatures.append(elf1)
  creatures.append(conj1)
  creatures.append(conj2)
  creatures.append(gol1)
  print_all(creatures)
  print(" ")
  #test Conjurer update_life_level method with point diff negative.
  conj1.update_life_level(-20)
  res = (conj1.life_points == 50)
  print("life points be 50"+res)
  res=(conj1.num_spells == 4)
  print("num spells be 4"+res)
  # using the debugger is really helpful.
  # write statements that test the update_life_level method for 
  # when the diff is positive, zero, and negative for all three classes.
  print(" ")
  # test do_engagement:
  # if is_5percent_or_less returns True, Gandalf points will be 0- and he dies.
  # Otherwise, the weapon diff is 10, so Gandalf gains 10 life points and adds one spell,
  # Eowyn looses 5 life points and mind control is now 1.125.
  print_all(creatures)
  # test the is_5percent_or_less function:
  count=0
  for i in range(1, 100):
    if is_5percent_or_less():
      count+=1
  r=(count>=2 and count<=8)
  # use the debugger and make some more test cases