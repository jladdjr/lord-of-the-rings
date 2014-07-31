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
theOneRing = Item("The One Ring", "Very important", 8, 420)
leatherCloak = Armor("Leather Cloak", "Travel tunic", 4, 12, 1)
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
mithrilVest = Armor("Mithril Vest", "Gift from Bilbo", 1, 86, 4)
anduril = Weapon("Anduril - The Flame of the West", 
"The sword once broken, now reforged", 2, 56, 22)
councilOfElrondItems = {"Elrond": [mithrilVest, anduril], 
"Legolas": legolasHair}

#The Pit
water = Potion("Water", "For sobering up", 1, 4, 8)
elvenRum = Potion("Elven Rum", "Toxic to all other species", 1, 6, -5)
thePitItems = {"Curufin": water, "Daeron": elvenRum}

#Elvenking's Throne
sweetNewElvenWare = Armor("Sweet New ElvenWare", 
"The latest from Mirkwood", 4, 52, 4)
elvenkingsThroneItems = {"Beleg": sweetNewElvenWare}

#Prancing Pony
tea = Potion("Tea", "Left by Dudo", 1, 3, 1)
bulletin = Item("Nazgul Bulletin", "Details Nazgul sightings", 0, 0)
prancingPonyItems = {"Harry Goatleaf": bulletin, "Dudo Baggins": tea}

#Galadriel's Mirror
elvenCloak = Armor("Elven Cloak", "A gift from Galadriel", 4, 62, 4)
phialOfGaladriel = Item("Phial of Galadriel", 
"\"May it be a light for you in dark places\"", 1, 106)
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
35, 0, -15, -15, -15)
marketSquareItems = {"Calmacil": fruitSamples ,"Atanatar": foodHoards, 
"Castamir": negativeThinking}

#Tower of Echelion
palatir = Item("Palatir", "For seeing mysteries", 6, 112)
windbeam = Charm("Windbeam", "Strengthens the hearts of men", 4, 116, 50, 10, 4)
executorSword = Weapon("Executor Sword", "A gift from Prince Imrahil", 
12, 142, 42)
towerOfEchelionItems = {"Denethor": [palatir, windbeam], 
"Prince Imrahil": executorSword}

#Beach
draagz = Item("Draagz", "Bad for health", 2, 76)
vodka = Potion("Vodka", "From the Gondorian heartland", 1, 52, 48)
flowersAndTrinkets = Charm("Flowers And Trinkets", "Mental health bonuses", 
    5, 84, 23, 4, 1)
beachItems = {"Gondorian bro #3": [draagz, vodka], 
"Gondorian bro #2": flowersAndTrinkets}

#Elven Rings
narya = Charm("Nanya", "Elven Ring of Fire", 0, 270, 100, 0, 0)
nenya = Charm("Nenya", "Elven Ring of Water", 0, 280, 0, 500, 0)
vilya = Charm("Vilya", "Elven Ring of Air", 0, 265, 0, 0, 10)
elvenRings = [narya, nenya, vilya]

#Shop weapons
#Eriador Shops - levels 1-6
walkingStick = Weapon("Walking Stick", "Offensive properties", 2, 4, 1)
gardenShovel = Weapon("Garden Shovel", 
    "The best weapon we could find...", 3, 5, 2)
gardenSythe = Weapon("Garden Sythe", "Very intimidating", 3, 7, 4)
shortSword = Weapon("Short Sword", "Hobbit-sized", 3, 8, 5)
hobbitElite = Weapon("Elite Hobbit Battle Gear", "Basically, rocks", 2, 12, 6)

eriadorWeaponsDist = {
    walkingStick: [0, 2],
    gardenShovel: [1, 3],
    gardenSythe: [3, 5],
    shortSword: [4, 5],
    hobbitElite: [4, 20]
}

#Rohan Shops - levels 8-12
ironSword = Weapon("Iron Sword", "Strange markings", 6, 16, 12)
mediumSword = Weapon("Medium Sword", "Battle tested", 8, 24, 15)
rohirricBow = Weapon("Rohirric Bow", "Historic embroidery", 10, 30, 18)
battleMace = Weapon("Battle Mace", "Classic for knights", 8, 32, 22)
battleLance = Weapon("Battle Lance", "Knight esesential", 14, 62, 26)

rohanWeaponsDist = {
    ironSword: [0 , 10],
    mediumSword: [10 , 14],
    rohirricBow: [10 , 20],
    battleMace: [9 , 12],
    battleLance: [8 , 20],
}

#Rhovanion Shops - levels 6-15
elvenTrainerBow = Weapon("Elven Trainer Bow", "For elf children", 6, 16, 8)
elvenBlade = Weapon("Elven Blade", "Glows as enemies near", 5, 24, 12)
elvenBow = Weapon("Elven Bow", "Standard grade", 6, 35, 16)
doubleBlades = Weapon("Double Blades", "Slice and dice", 6, 42, 18)
eliteElvenSword = Weapon("Elite Elven Blade", "Powerful, magical properties", 
    8, 118, 32)
eliteElvenBow = Weapon("Elite Elven Longbow", "Made of mallorn", 8, 112, 40)

rhovanionWeaponsDist = {
    elvenTrainerBow: [0, 8],
    elvenBlade: [8, 10],
    elvenBow: [9, 11],
    doubleBlades: [10, 12],
    eliteElvenSword: [12, 20],
    eliteElvenBow: [12, 20],
}

#Gondor Shops - levels 12-20
soldersSword = Weapon("Soldier's Sword", "Standard grade", 8, 1, 1)
longSword = Weapon("Long Sword", "A Gondorian blade", 12, 1, 1)
compoundBow = Weapon("Compound Bow", "Extreme range", 12, 1, 1)
eliteLongSword = Weapon("Elite Long Sword", "A Numernorian blade", 10, 1, 1)
gondorianLongbow = Weapon("Gondorian Longbow", "Extreme range", 13, 1, 1)

gondorWeaponsDist = {
    soldersSword: [0, 14],
    longSword: [12, 15],
    compoundBow: [14, 16],
    eliteLongSword: [16, 20],
    gondorianLongbow: [16, 20],
}

#Shop armor
#Eriador Shops - levels 1-5
farmerShawl = Armor("Farmer's Shawls", "Protection from the sun", 4, 8, 1)
travelCloak = Armor("Travel Cloak", "A dark shroud", 3, 12, 1)
leatherCloak = Armor("Leather Cloak", "Stuffy", 5, 14, 2)

eriadorArmorDist = {
    farmerShawl: [0, 2],
    travelCloak: [2, 4],
    leatherCloak: [3, 20]
}

#Rohan Shops - levels 8-12
leatherArmor = Armor("Leather Armor", "Light and lithe", 6, 18, 3)
chainmail = Armor("Chainmail", "Took an incredibly long time to make", 10, 24, 4)
suitOfArmor = Armor("Suit of Armor", "To become a knight in shining armor", 
    25, 85, 6)
rohirricBreastplate = Armor("Rohirric Breastplate", "Aged with dignity", 
    16, 74, 5)
    
rohanArmorDist = {
    leatherArmor: [0, 12],
    chainmail: [8, 15],
    suitOfArmor: [13, 15],
    rohirricBreastplate: [14, 20]
}

#Rhovanion Shops - levels 6-15
workersGear = Armor("Worker's Gear", "Poor-elf's clothes", 6, 16, 2)
elvenWare = Armor("Elven Ware", "A time-tested classic", 4, 40, 4)
eliteElvenWare = Armor("Elite Elven Ware", "At a huge premium", 4, 152, 5)
velvetSuit = Armor("Velvet Suit", "Sex appeal", 6, 262, 8)

rhovanionArmorDist = {
    workersGear: [0, 9],
    elvenWare: [8, 12],
    eliteElvenWare: [12, 15],
    velvetSuit: [15, 20]
}

#Gondorian Shops - levels 12-20
standardSoldiersArmor = Armor("Standard Soldier's Armor", "Sells for a reason", 
    12, 56, 3)
platemail = Armor("Platemail", "Can take a wallop", 18, 64, 4)
magneticArmor = Armor("Magnetic Armor", "Repels attacks", 16, 124, 5)
eliteGondorianArmor = Armor("Elite Gondorian Armor", "Elite Platemail", 
    18, 142, 6)
    
gondorArmorDist = {
    standardSoldiersArmor: [0, 16],
    platemail: [14, 16],
    magneticArmor: [16, 20],
    eliteGondorianArmor: [18, 20]
}

#Shop potions
#Eriador shops
hobbitTea = Potion("Hobbit Tea", "Bay leaf", 1, 4, 4)
shireWater = Potion("Shire Water", "From the Brandywine", 1, 6, 6)
shireWater2 = Potion("Shire Water", "From the Shirebourne", 1, 8, 10)

eriadorPotionDist = {
    hobbitTea: [0, 2],
    shireWater: [2, 4],
    shireWater2: [4, 20]
}

#Rohan shops
adornWater = Potion("Adorn Water", "From the Adorn River", 1, 14, 16)
rohirricTea = Potion("Rohirric Tea", "Calming effects", 1, 18, 18)
fangornWater = Potion("Entwash Water", "Extreme restorative properties", 1, 48, 64)

rohanPotionDist = {
    adornWater: [0, 12],
    shireWater: [10, 12],
    shireWater2: [12, 20]
}

#Rhovanion shops
elvenTea = Potion("Elven Tea", "Magical effects", 1, 18, 16)
mirkwoodWater = Potion("Elven Water", "From the Misty Mountains", 1, 24, 24)
magicalElixir = Potion("Magical Elixir", "Has a strange glow", 2, 35, 45)

rhovanionPotionDist = {
    elvenTea: [0, 12],
    mirkwoodWater: [12, 14],
    magicalElixir: [14, 20]
}

#Gondor shops
anduinWater = Potion("Anduin Water", "All the way from the Anduin River", 1, 1, 72)
snowmelt = Potion("Snowmelt", "From the White Mountains", 1, 1, 82)
advancedElixir = Potion("Advanced Elixir", "From the Houses of Healing", 2, 1, 152)

gondorPotionDist = {
    anduinWater: [0, 12],
    snowmelt: [12, 15],
    magicalElixir: [14, 20]
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