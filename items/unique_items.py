#!/usr/bin/python

from items.armor import Armor
from items.weapon import Weapon

"""
A list of unique items.

Example: Andúril, the Flame of the West. 
"""

#Should consider using the Factory design pattern to do this:
#http://en.wikipedia.org/wiki/Factory_(software_concept)

#Let's touch base and I can give you more details about what this
#would look like. -Jim

steelDagger = Weapon(3, "Steel Dagger", "A trusty blade", 2)
leatherCloak = Armor(2, "Leather Cloak", "A common leather cloak, used for long journeys.", 2)
