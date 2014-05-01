#!/usr/bin/python

from constants import ItemType
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion

"""
The unique items of the game. For instance, "The One Ring."
"""

#Items - Story
#Starting
sting = Weapon("Sting", "Elvish - made in Gondolin", 1, 5, 2)
theOneRing = Item("The One Ring", "'...and in the darkness bind them'", 5)
leatherCloak = Armor("Leather Cloak", "Travel Tunic", 1, 2, 1)
vodka = Potion("Vodka", "Good for health", 1, 1, 1)
startingInventory = [sting, theOneRing, leatherCloak, vodka]

#Rivendell
mithrilVest = Armor("Mithril Vest", "Gift from Bilbo", 1, 5, 0)
shardsOfNarsil = Item("Shards of Narsil", "The sword that Isildur used to cut the One Ring from Sauron", 2)

#Lorien
elvenCloak = Armor("Elven Cloak", "Gifts from Galadriel", 0, 4, 25)
phialOfGaladriel = Item("Phial of Galadriel", "'May it be a light for you in dark places...'", 0)

#Minas Tirith
anduril = Weapon("Anduril - The Flame of the West", "The sword once broken, now reforged", 2, 20, 50)

#Miscellaneous
keysOfOrthanc = Item("Keys to Orthanc", "Two gigantic black keys needed to gain entry to the Tower of Orthanc", 1)
windbeam = Item("Windbeam", "The Horn of Elendil", 1)
palatir = Item("Palatir", "Stones of Seeing", 4)
narya = Item("Nanya", "Elven Ring of Fire", 0)
nenya = Item("Nenya", "Elven Ring of Water", 0)
vilya = Item("Vilya", "Elven Ring of Air", 0)

#General unique weapons
scepterOfAnnuminas = Weapon("Scepter of Annuminas", "Held by the Kings of Arnor", 3, 25, 30)
aeglos = Weapon("Aeglos", "A spear wielded by Gil-galad", 4, 20, 30)
glamdring = Weapon("Glamdring", "Sindarin: 'Foe Hammer'", 4, 20, 15)
arglachel = Weapon("Anglachel", "Sindarin: 'Iron of the Flaming Star'", 3, 15, 25)
angrist = Weapon("Angrist", "Sindarian: 'Iron Cleaver'", 4, 20, 25)
anguirel = Weapon("Anguriel", "Sindarian: 'Iron of Eternity'", 4, 20, 25)
ananruth = Weapon("Aranruth", "Sindarian: 'King's Ire'", 4, 20, 25)
belthronding = Weapon("Belthronding", "A bow wielded by Beleg Cuthalion", 4, 20, 25)
dramborleg = Weapon("Dramborleg", "Sindarian: Thudder Sharp", 4, 15, 20)
grond = Weapon("Grond", "Morgoth's Mace", 10, 80, 20)
guthwine = Weapon("Guthwine", "Eomer's sword. Where did you get it?", 10, 10, 20)
herugrim = Weapon("Herugrim", "Theoden's sword. Where did this come from?", 10, 10, 20)
orchrist = Weapon("Orcrist", "Sindarin: 'Goblin Cleaver", 10, 15, 20)
ringil = Weapon("Ringil", "Sindarin: 'Cold Spark'", 10, 15, 20)

#General unique armor 
crownOfElendil = Armor("Crown of Elendil", "A brilliant crown worn by the Kings of Gondor", 2, 10, 30)
ironCrown = Armor("Iron Crown", "Forged by Morgoth to hold the Silmaril", 2, 10, 30)
helmOfHador = Armor("Helm of Hador", "A helmet owned by the Royal House of Hador", 2, 10, 30)
