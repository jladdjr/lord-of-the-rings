#!/usr/bin/python

from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm

"""
A storing place for some of the unique items of the game.

For instance, "The One Ring."
"""
#Items - Story
#Starting Inventory
sting = Weapon("Sting", "Elvish - made in Gondolin", 2, 10, 10)
theOneRing = Charm("The One Ring", "Very important", 10, 0, 0, 10, 0)
leatherCloak = Armor("Leather Cloak", "Travel Tunic", 2, 2, 1)
vodka = Potion("Vodka", "Good for health", 1, 1, 5)
charm = Charm("A", "a", 0,0,0,0,0)
charm2 = Charm("B", "b", 0,0,0,0,0)
startingInventory = [sting, theOneRing, leatherCloak, vodka, charm, charm2]

#Hobbiton Square
walkingCane = Item("Walking Cane", "Dubiously helpful", 1, 1)
tea = Potion("Tea", "A delightful refreshment", 1, 1, 1)
newspaper = Item("The Shire Newspaper", "Mostly tabloids... about hobbits", 
1, 1)
hobbitonSquareItems = {"Naftel Took": walkingCane, 
"Amaranth Brandybuck": [tea, newspaper]}

#Council of Elrond
legolasHair = Item("Legolas' Hair", "Industrial applications", 0, 1)
mithrilVest = Armor("Mithril Vest", "Gift from Bilbo", 1, 5, 0)
anduril = Weapon("Anduril - The Flame of the West", 
"The sword once broken, now reforged", 2, 20, 50)
councilOfElrondItems = {"Elrond": [mithrilVest, anduril], 
"Legolas": legolasHair}

#The Pit
water = Potion("Water", "For sobering up", 1, 5, 1)
elvenRum = Potion("Elven Rum", "Toxic to all other species", 1, 5, -5)
thePitItems = {"Curufin": water, "Daeron": elvenRum}

#Elvenking's Throne
sweetNewElvenWare = Armor("Sweet New ElvenWare", 
"The latest from Mirkwood", 10, 5, 10)
elvenkingsThroneItems = {"Beleg": sweetNewElvenWare}

#Prancing Pony
tea = Potion("Tea", "Left by Dudo", 2, 2, 1)
bulletin = Item("Nazgul Bulletin", "Details Nazgul sightings", 0, 1)
prancingPonyItems = {"Harry Goatleaf": bulletin, "Dudo Baggins": tea}

#Galadriel's Mirror
elvenCloak = Armor("Elven Cloak", "Gifts from Galadriel", 0, 4, 25)
phialOfGaladriel = Item("Phial of Galadriel", 
"\"May it be a light for you in dark places\"", 0, 0)
galadrielsMirrorItems = {"Galadriel": [elvenCloak, phialOfGaladriel]}

#Helm's Deep Commons
vodka = Potion("Koskenkorva", "Rohirric Poisons", 1, 5, 0)
vodka2 = Potion("Luksusowa", "Budget Vodka", 1, 4, 0)
helmsDeepCommonsItems = {"Erkenbrand": vodka, "Gambling the Old": vodka2}

#Edoras Commons
tea = Potion("Tea", "For sharing stories over", 1, 5, 1)
tea2 = Potion("Tea", "Secret recipies", 1, 5, 1)
newspaper = Item("Newspaper Clippins", "Mostly for reminiscing", 1, 1)
edorasCommonsItems = {"Helm Gammerhand": tea, "Frealaf Hildeson": tea2, 
"Brytta Leofa": newspaper}

#Auburn Square Commons
russianTea = Potion("Russian Tea", "Only 30% alcohol by volume", 1, 5, 1)
freePizza = Potion("Free Pizza", "Tombstones though", 1, 10, 1)
chineseHandouts = Item("Chinese Handouts", "Poor quality", 1, 1)
auburnSquareCommons = {"Dmitriy": russianTea, "Jim": freePizza, 
"Chris": chineseHandouts}

#Market Square
fruitSamples = Potion("Fruit Samples", "Meagerly", 1, 2, 0)
foodHoards = Potion("Spare Food Hoards", "Generously given", 3, 10, 2)
negativeThinking = Charm("Negative Thinking", "Not something you want", 
10, 0, -10, -10, -10)
marketSquareItems = {"Calmacil": fruitSamples ,"Atanatar": foodHoards, 
"Castamir": negativeThinking}

#Tower of Echelion
palatir = Item("Palatir", "For seeing mysteries", 2, 1)
windbeam = Charm("Windbeam", "The Horn of Elendil", 1, 1, 1, 1, 1)
executorSword = Weapon("Executor Sword", "A gift from Prince Imrahil", 
3, 15, 4)
towerOfEchelionItems = {"Denethor": [palatir, windbeam], 
"Prince Imrahil": executorSword}

#Beach
draagz = Item("Draagz", "Bad for health", 15, 1)
vodka = Potion("Vodka", "From the Gondorian heartland", 10, 5, 10)
flowersAndTrinkets = Charm("Flowers And Trinkets", 
"Massive mental health bonuses", 10, 5, 10, 1, 1)
beachItems = {"Gondorian bro #3": [draagz, vodka], 
"Gondorian bro #2": flowersAndTrinkets}

#Isenguard
keysOfOrthanc = Item("Keys to Orthanc", 
"Two gigantic black keys needed to gain entry to the Tower of Orthanc", 1, 1)
palatir = Item("Palatir", "Stones of Seeing", 4, 1)
isenguardItems = [keysOfOrthanc, palatir]

#Elven Rings
narya = Charm("Nanya", "Elven Ring of Fire", 10, 10, 10, 10, 10)
nenya = Charm("Nenya", "Elven Ring of Water", 10, 10, 10, 10, 10)
vilya = Charm("Vilya", "Elven Ring of Air", 10, 10, 10, 10, 10)
elvenRings = [narya, nenya, vilya]

#Low-level unique weapons
guthwine = Weapon("Guthwine", "Eomer's sword. Stolen goods", 10, 10, 20)
herugrim = Weapon("Herugrim", 
"Theoden's sword. Will attract negative attention", 10, 10, 20)
orchrist = Weapon("Orcrist", "Sindarin: 'Goblin Cleaver", 10, 15, 20)

#Low-level unique armor 
tarhelmCrown = Armor("TarnHelm Crown", "Straight from Tristram", 2, 10, 10)
snowclash = Armor("Snowclash Battle Belt", "Straight from Tristram", 2, 10, 10)
razortail = Armor("Razortail Sharkskin", "Straight from Tristram", 2, 10, 10)
nightsmoke = Armor("Nightsmoke", "Straight from Tristram", 2, 10, 10)
peasantCrown = Armor("Peasant Crown", "Straight from Tristram", 2, 10, 10)
crownOfThieves = Armor("Crown of Thieves", "Straight from Tristram", 2, 10, 10)

#High-level unique weapons
glamdring = Weapon("Glamdring", "Sindarin: \"Foe Hammer\"", 4, 20, 15)
anglachel = Weapon("Anglachel", "Sindarin: \"Iron of the Flaming Star\"", 
3, 15, 25)
angrist = Weapon("Angrist", "Sindarian: \"Iron Cleaver\"", 4, 20, 25)
anguirel = Weapon("Anguriel", "Sindarian: \"Iron of Eternity\"", 4, 20, 25)
belthronding = Weapon("Belthronding", "A bow wielded by Beleg Cuthalion", 
4, 20, 25)
dramborleg = Weapon("Dramborleg", "Sindarian: \"Thudder Sharp\"", 4, 15, 20)

#High-level unique armor
helmOfHador = Armor("Helm of Hador", 
"A helmet owned by the Royal House of Hador", 2, 10, 30)
harlequinCrestShako = Armor("Harlequin Crest Shako", 
"Straight from Tristram", 2, 10, 10)

#Elite-level unique items
aeglos = Weapon("Aeglos", "A spear wielded by Gil-galad", 4, 20, 30)
ananruth = Weapon("Aranruth", "Sindarian: \"King's Ire\"", 4, 20, 25)
scepterOfAnnuminas = Weapon("Scepter of Annuminas", 
"Held by the Kings of Arnor", 3, 25, 30)
ringil = Weapon("Ringil", "Sindarin: \"Cold Spark\"", 10, 15, 20)
grond = Weapon("Grond", "Morgoth's Mace", 10, 80, 20)
crownOfElendil = Armor("Crown of Elendil", 
"A brilliant crown worn by the Kings of Gondor", 2, 10, 30)
ironCrown = Armor("Iron Crown", 
"Forged by Morgoth to hold the Silmaril", 2, 10, 30)

lowLevelFindableUniques = [guthwine, herugrim, orchrist, tarhelmCrown, 
snowclash, razortail, nightsmoke, peasantCrown, crownOfThieves]

highLevelFindableUniques = [glamdring, anglachel, angrist, anguirel, 
belthronding, dramborleg, helmOfHador, harlequinCrestShako]

eliteLevelFindableUniques = [aeglos, ananruth, ringil, scepterOfAnnuminas, 
grond, crownOfElendil, ironCrown]

"""
#Shop weapons
walkingStick = Weapon("Walking Stick", "Offensive properties", 1, 1, 1)
gardenShovel = Weapon("Garden Shoven", 
    "Hobbits are ill-equipped for combat", 1, 1, 1)
gardenSythe = Weapon("Garden Sythe", "Very intimidating", 1, 1, 1)
shortSword = Weapon("Short Sword", "Hobbit-sized", 1, 1, 1)

mediumSword = Weapon("Medium Sword", "A vestige of arnor", 1, 1, 1)
ironSword = Weapon("Iron Sword", "Has seen battle use", 1, 1, 1)
rohirricLance = Weapon("Rohirric Lance", "Battle worn", 1, 1, 1)
battleMace = Weapon("Battle Mace", "Rohirric in origin", 1, 1, 1)

elvenTrainerBow = Weapon("Elven Trainer Bow", "Made of yew", 1, 1, 1)
elvenBlade = Weapon("Elven Blade", "Glows as enemies near", 1, 1 , 1)
elvenBow = Weapon("Elven Bow", "Standard grade", 1, 1, 1)
longSword = Weapon("Long Sword", "A Gondorian blade", 1, 1, 1)
eliteLongSword = Weapon("Elite Long Sword", "A Numernorian blade", 1, 1, 1)
eliteElvenSword = Weapon("Elite Elven Sword", "A historic blade", 1, 1, 1)
eliteElvenBow = Weapon("Elite Elven Longbow", "Made of mallorn", 1, 1, 1)
"""