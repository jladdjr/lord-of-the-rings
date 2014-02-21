#!/usr/bin/python
from item import Item
from armor import Armor
from weapons import Weapons
import constants

class steelDagger(Weapons):
    def __init__(self):
        Weapons.__init__(self, 3):
        Item.__init__("Steel Dagger", "A trusty blade", 2)

class leatherCloak(Armor):
    def __init__(self):
        Armor.__init__(self, 2):
        item.__init__("Leather cloak", "A common leather cloak, used for long journeys.", 2)

