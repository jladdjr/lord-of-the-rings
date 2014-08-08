#!/usr/bin/python

from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm
import constants

"""
A storing place for some of the unique items of the game.

For instance, "The One Ring."
"""
#Items - Story
#Starting Inventory
sting = Weapon("Sting", "Elvish - made in Gondolin", 2, 22, 8)
theOneRing = Item("The One Ring", "Very important", 6, 540)
leatherCloak = Armor("Leather Cloak", "Travel tunic", 3, 8, 1)
vodka = Potion("Vodka", "Good for health", 1, 4, 4)
startingInventory = [sting, theOneRing, leatherCloak, vodka]

#Hobbiton Square
walkingCane = Item("Walking Cane", "Dubiously helpful", 2, 2)
tea = Potion("Tea", "A delightful refreshment", 1, 1, 4)
newspaper = Item("The Shire Newspaper", "Mostly tabloids... about hobbits", 
0, 0)
hobbitonSquareItems = {"Naftel Took": walkingCane, 
"Amaranth Brandybuck": [tea, newspaper]}

#Council of Elrond
legolasHair = Item("Legolas' Hair", "Industrial applications", 0, 12)
mithrilVest = Armor("Mithril Vest", "Gift from Bilbo", 1, 102, 4)
anduril = Weapon("Anduril - The Flame of the West", 
"The sword once broken, now reforged", 2, 114, 22)
councilOfElrondItems = {"Elrond": anduril, "Legolas": legolasHair, "Bilbo": 
    mithrilVest}

#The Pit
water = Potion("Water", "For sobering up", 1, 4, 8)
elvenRum = Potion("Elven Rum", "Toxic to all other species", 1, 6, -5)
thePitItems = {"Curufin": water, "Daeron": elvenRum}

#Elvenking's Throne
sweetNewElvenWare = Armor("Sweet New ElvenWare", 
"The latest from Mirkwood", 4, 52, 3)
elvenkingsThroneItems = {"Beleg": sweetNewElvenWare}

#Prancing Pony
tea = Potion("Tea", "Left by Dudo", 1, 3, 1)
bulletin = Item("Nazgul Bulletin", "Details Nazgul sightings", 0, 0)
prancingPonyItems = {"Harry Goatleaf": bulletin, "Dudo Baggins": tea}

#Galadriel's Mirror
elvenCloak = Armor("Elven Cloak", "A gift from Galadriel", 4, 62, 3)
phialOfGaladriel = Item("Phial of Galadriel", 
"\"May it be a light for you in dark places\"", 1, 92)
galadrielsMirrorItems = {"Galadriel": [elvenCloak, phialOfGaladriel]}

#Helm's Deep Commons
vodka = Potion("Koskenkorva", "Rohirric Poisons", 1, 12, 32)
vodka2 = Potion("Luksusowa", "Budget Vodka", 1, 10, 24)
helmsDeepCommonsItems = {"Erkenbrand": vodka, "Gambling the Old": vodka2}

#Edoras Commons
tea = Potion("Tea", "For sharing stories over", 1, 16, 46)
tea2 = Potion("Tea", "Secret recipies", 1, 14, 42)
newspaper = Item("Newspaper Clippins", "Mostly for reminiscing", 1, 0)
edorasCommonsItems = {"Helm Gammerhand": tea, "Frealaf Hildeson": tea2, 
"Brytta Leofa": newspaper}

#Auburn Square Commons
russianTea = Potion("Russian Tea", "Only 30% alcohol by volume", 1, 8, 28)
freePizza = Potion("Free Pizza", "Tombstones though", 1, 16, 52)
chineseHandouts = Item("Chinese Handouts", "Poor quality", 14, 42)
auburnSquareCommons = {"Dmitriy": russianTea, "Jim": freePizza, 
"Chris": chineseHandouts}

#Market Square
fruitSamples = Potion("Fruit Samples", "Meagerly", 2, 18, 30)
foodHoards = Potion("Spare Food Hoards", "Generously given", 4, 42, 85)
negativeThinking = Charm("Negative Thinking", "Not something you want", 
35, 0, -15, -2, -40)
marketSquareItems = {"Calmacil": fruitSamples ,"Atanatar": foodHoards, 
"Castamir": negativeThinking}

#Tower of Echelion
palatir = Item("Palatir", "For seeing mysteries", 6, 112)
windbeam = Charm("Windbeam", "Strengthens the hearts of men", 4, 116, 14, 1, 36)
executorSword = Weapon("Executor Sword", "A gift from Prince Imrahil", 
12, 112, 26)
towerOfEchelionItems = {"Denethor": [palatir, windbeam], 
"Prince Imrahil": executorSword}

#Beach
draagz = Item("Draagz", "Bad for health", 2, 76)
vodka = Potion("Vodka", "From the Gondorian heartland", 1, 52, 48)
flowersAndTrinkets = Charm("Flowers And Trinkets", "Mental health bonuses", 
    5, 72, 6, 0, 18)
beachItems = {"Gondorian bro #3": [draagz, vodka], 
"Gondorian bro #2": flowersAndTrinkets}

#Elven Rings
narya = Charm("Nanya", "Elven Ring of Fire", 0, 270, 100, 0, 0)
nenya = Charm("Nenya", "Elven Ring of Water", 0, 280, 0, 0, 500)
vilya = Charm("Vilya", "Elven Ring of Air", 0, 265, 0, 15, 0)
elvenRings = [narya, nenya, vilya]

#Shop weapons
#Eriador Shops
walkingStick = Weapon("Walking Stick", "Offensive properties", 2, 4, 1)
gardenShovel = Weapon("Garden Shovel", 
    "The best weapon we could find...", 3, 5, 2)
gardenSythe = Weapon("Garden Sythe", "Very intimidating", 3, 7, 4)
shortSword = Weapon("Short Sword", "Hobbit-sized", 3, 8, 5)
hobbitElite = Weapon("Elite Hobbit Battle Gear", "Basically, rocks", 2, 12, 6)

eriadorWeaponsDist = {
    walkingStick: [0, 2],
    gardenShovel: [0, 2],
    gardenSythe: [1, 4],
    shortSword: [2, 6],
    hobbitElite: [4, 20]
}

#Rohan Shops
ironSword = Weapon("Iron Sword", "Strange markings", 6, 18, 12)
mediumSword = Weapon("Medium Sword", "Battle tested", 8, 26, 14)
rohirricBow = Weapon("Rohirric Bow", "Historic embroidery", 10, 30, 16)
battleMace = Weapon("Battle Mace", "Classic for knights", 8, 42, 20)
battleLance = Weapon("Battle Lance", "Knight esesential", 14, 62, 26)

rohanWeaponsDist = {
    ironSword: [0, 8],
    mediumSword: [6, 10],
    rohirricBow: [7, 10],
    battleMace: [8, 12],
    battleLance: [10, 20],
}

#Rhovanion Shops
elvenTrainerBow = Weapon("Elven Trainer Bow", "For elf children", 6, 16, 8)
elvenBlade = Weapon("Elven Blade", "Glows as enemies near", 5, 24, 12)
elvenBow = Weapon("Elven Bow", "Standard grade", 6, 35, 16)
doubleBlades = Weapon("Double Blades", "Slice and dice", 6, 42, 18)
eliteElvenSword = Weapon("Elite Elven Blade", "Powerful, magical properties", 
    8, 118, 32)
eliteElvenBow = Weapon("Elite Elven Longbow", "Made of mallorn", 8, 112, 40)

rhovanionWeaponsDist = {
    elvenTrainerBow: [0, 8],
    elvenBlade: [6, 10],
    elvenBow: [7, 10],
    doubleBlades: [8, 12],
    eliteElvenSword: [12, 20],
    eliteElvenBow: [12, 20],
}

#Gondor Shops
soldiersSword = Weapon("Soldier's Sword", "Standard grade", 8, 30, 16)
longSword = Weapon("Long Sword", "A Gondorian blade", 12, 52, 20)
compoundBow = Weapon("Compound Bow", "Extreme range", 12, 56, 22)
eliteLongSword = Weapon("Elite Long Sword", "A Numernorian blade", 10, 112, 25)
gondorianLongbow = Weapon("Gondorian Longbow", "Extreme range", 14, 102, 30)

gondorWeaponsDist = {
    soldiersSword: [0, 12],
    longSword: [12, 15],
    compoundBow: [13, 16],
    eliteLongSword: [16, 20],
    gondorianLongbow: [16, 20],
}

#Shop armor
#Eriador Shops
farmerShawl = Armor("Farmer's Shawls", "Protection from the sun", 4, 8, 1)
travelCloak = Armor("Travel Cloak", "A dark shroud", 3, 12, 1)
leatherCloak = Armor("Leather Cloak", "Stuffy", 5, 14, 2)

eriadorArmorDist = {
    farmerShawl: [0, 2],
    travelCloak: [2, 4],
    leatherCloak: [4, 20]
}

#Rohan Shops
leatherArmor = Armor("Leather Armor", "Light and lithe", 6, 18, 2)
chainmail = Armor("Chainmail", "Took an incredibly long time to make", 10, 24, 4)
suitOfArmor = Armor("Suit of Armor", "To become a knight in shining armor", 
    25, 85, 6)
rohirricBreastplate = Armor("Rohirric Breastplate", "Aged with dignity", 
    16, 74, 5)
    
rohanArmorDist = {
    leatherArmor: [0, 7],
    chainmail: [8, 12],
    suitOfArmor: [10, 14],
    rohirricBreastplate: [12, 20]
}

#Rhovanion Shops
workersGear = Armor("Worker's Gear", "Poor-elf's clothes", 6, 14, 2)
elvenWare = Armor("Elven Ware", "A time-tested classic", 4, 40, 3)
eliteElvenWare = Armor("Elite ElvenWare", "At a huge premium", 4, 152, 5)
velvetSuit = Armor("Velvet Suit", "Sex appeal", 6, 262, 8)

rhovanionArmorDist = {
    workersGear: [0, 6],
    elvenWare: [6, 10],
    eliteElvenWare: [9, 15],
    velvetSuit: [12, 20]
}

#Gondorian Shops
standardSoldiersArmor = Armor("Standard Soldier's Armor", "Sells for a reason", 
    12, 56, 3)
platemail = Armor("Platemail", "Can take a wallop", 18, 84, 4)
magneticArmor = Armor("Magnetic Armor", "Repels attacks", 16, 124, 5)
eliteGondorianArmor = Armor("Elite Gondorian Armor", "Elite Platemail", 
    18, 142, 6)
    
gondorArmorDist = {
    standardSoldiersArmor: [0, 12],
    platemail: [12, 16],
    magneticArmor: [16, 20],
    eliteGondorianArmor: [17, 20]
}

#Shop potions
#Eriador shops
hobbitTea = Potion("Hobbit Tea", "Bay leaf", 1, 4, 4)
shireWater = Potion("Shire Water", "From the Brandywine", 1, 6, 6)
shireWater2 = Potion("Shire Water", "From the Shirebourne", 1, 8, 10)

eriadorPotionDist = {
    hobbitTea: [0, 2],
    shireWater: [2, 4],
    shireWater2: [2, 20]
}

#Rohan shops
adornWater = Potion("Adorn Water", "From the Adorn River", 1, 14, 22)
rohirricTea = Potion("Rohirric Tea", "Calming effects", 1, 24, 30)
fangornWater = Potion("Entwash Water", "Extreme restorative properties", 1, 48, 64)

rohanPotionDist = {
    adornWater: [0, 6],
    rohirricTea: [6, 10],
    fangornWater: [10, 20]
}

#Rhovanion shops
elvenTea = Potion("Elven Tea", "Magical effects", 1, 18, 16)
mirkwoodWater = Potion("Elven Water", "From the Misty Mountains", 1, 24, 24)
magicalElixir = Potion("Magical Elixir", "Has a strange glow", 2, 60, 50)

rhovanionPotionDist = {
    elvenTea: [0, 10],
    mirkwoodWater: [8, 12],
    magicalElixir: [12, 20]
}

#Gondor shops
anduinWater = Potion("Anduin Water", "All the way from the Anduin River", 1, 52, 72)
snowmelt = Potion("Snowmelt", "From the White Mountains", 1, 64, 82)
advancedElixir = Potion("Advanced Elixir", "From the Houses of Healing", 2, 102, 152)

gondorPotionDist = {
    anduinWater: [0, 12],
    snowmelt: [10, 15],
    advancedElixir: [14, 20]
}

#Total shop weapons distributions
shopWeaponDist = {
    constants.RegionType.ERIADOR: eriadorWeaponsDist,
    constants.RegionType.RHOVANION: rhovanionWeaponsDist,
    constants.RegionType.ROHAN: rohanWeaponsDist,
    constants.RegionType.GONDOR: gondorWeaponsDist}

#Total shop armor distributions
shopArmorDist = {
    constants.RegionType.ERIADOR: eriadorArmorDist,
    constants.RegionType.RHOVANION: rhovanionArmorDist,
    constants.RegionType.ROHAN: rohanArmorDist,
    constants.RegionType.GONDOR: gondorArmorDist}
    
#Total shop potion distributions
shopPotionDist = {
    constants.RegionType.ERIADOR: eriadorPotionDist,
    constants.RegionType.RHOVANION: rhovanionPotionDist,
    constants.RegionType.ROHAN: rohanPotionDist,
    constants.RegionType.GONDOR: gondorPotionDist}
    
#Low-level unique weapons
guthwine = Weapon("Guthwine", "Eomer's sword. Stolen goods", 8, 142, 22)
herugrim = Weapon("Herugrim", 
"Theoden's sword. Will attract negative attention", 8, 136, 26)
orchrist = Weapon("Orcrist", "Sindarin: 'Goblin Cleaver", 15, 160, 24)

#Low-level unique armor
tarhelmCrown = Armor("Tarnhelm Crown", "Straight from Tristram", 6, 86, 3)
snowclash = Armor("Snowclash Battle Belt", "Straight from Tristram", 5, 92, 4)
razortail = Armor("Razortail Sharkskin", "Straight from Tristram", 8, 102, 4)
nightsmoke = Armor("Nightsmoke", "Straight from Tristram", 4, 114, 5)
peasantCrown = Armor("Peasant Crown", "Straight from Tristram", 4, 85, 4)
crownOfThieves = Armor("Crown of Thieves", "Straight from Tristram", 5, 76, 3)

#High-level unique weapons
glamdring = Weapon("Glamdring", "Foe Hammer", 6, 162, 72)
anglachel = Weapon("Anglachel", "Iron of the Flaming Star", 6, 170, 76)
angrist = Weapon("Angrist", "Iron Cleaver", 5, 174, 80)
anguirel = Weapon("Anguriel", "Iron of Eternity", 6, 172, 82)
belthronding = Weapon("Belthronding", "A bow wielded by Beleg Cuthalion", 
5, 176, 76)
dramborleg = Weapon("Dramborleg", "Thudder Sharp", 6, 160, 78)
scepterOfAnnuminas = Weapon("Scepter of Annuminas", 
"Held by the Kings of Arnor", 6, 232, 96)

#High-level unique armor
helmOfHador = Armor("Helm of Hador", 
"A helmet owned by the Royal House of Hador", 5, 140, 12)
harlequinCrestShako = Armor("Harlequin Crest Shako", 
"Straight from Tristram", 6, 162, 10)
templarsMight = Armor("Templar's Might", "Straight from Tristram", 6, 152, 12)
tyraelsMight = Armor("Tyrael's Might", "Straight from Tristram", 6, 170, 14)

#Elite-level unique items
aeglos = Weapon("Aeglos", "A spear wielded by Gil-galad", 6, 220, 152)
ananruth = Weapon("Aranruth", "King's Ire", 5, 242, 146)
ringil = Weapon("Ringil", "Cold Spark", 8, 248, 156)
grond = Weapon("Grond", "Morgoth's Mace", 30, 653, 340)
crownOfElendil = Armor("Crown of Elendil", 
    "A brilliant crown worn by the Kings of Gondor", 6, 220, 16)
ironCrown = Armor("Iron Crown", "Forged by Morgoth to hold the Silmaril", 
    10, 316, 22)

lowLevelFindableUniques = [guthwine, herugrim, orchrist, tarhelmCrown, 
    snowclash, razortail, nightsmoke, peasantCrown, crownOfThieves]

highLevelFindableUniques = [glamdring, anglachel, angrist, anguirel, 
    belthronding, dramborleg, scepterOfAnnuminas, helmOfHador, 
    harlequinCrestShako, templarsMight, tyraelsMight]

eliteLevelFindableUniques = [aeglos, ananruth, ringil, grond, crownOfElendil, 
    ironCrown]