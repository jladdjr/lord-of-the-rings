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
sting = Weapon("Sting", "Elvish - made in Gondolin", 2, 10, 8)
theOneRing = Item("The One Ring", "Very important", 8, 75)
leatherCloak = Armor("Leather Cloak", "Travel Tunic", 4, 4, 1)
vodka = Potion("Vodka", "Good for health", 1, 1, 4)
startingInventory = [sting, theOneRing, leatherCloak, vodka]

#Hobbiton Square
walkingCane = Item("Walking Cane", "Dubiously helpful", 2, 1)
tea = Potion("Tea", "A delightful refreshment", 1, 0, 2)
newspaper = Item("The Shire Newspaper", "Mostly tabloids... about hobbits", 
0, 0)
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

#Shop weapons
#Eriador Shops - levels 1-6
walkingStick = Weapon("Walking Stick", "Offensive properties", 2, 2, 1)
gardenShovel = Weapon("Garden Shovel", 
    "The best weapon we could find...", 3, 3, 2)
gardenSythe = Weapon("Garden Sythe", "Very intimidating", 3, 5, 4)
shortSword = Weapon("Short Sword", "Hobbit-sized", 3, 6, 5)
hobbitElite = Weapon("Elite Hobbit Battle Gear", "Basically, rocks", 2, 8, 6)

eriadorWeaponsDist = {
    walkingStick: [0, 2],
    gardenShovel: [1, 3],
    gardenSythe: [3, 5],
    shortSword: [4, 5],
    hobbitElite: [4, 20]
}

#Rohan Shops - levels 8-12
ironSword = Weapon("Iron Sword", "Strange markings", 1, 1, 1)
mediumSword = Weapon("Medium Sword", "Battle tested", 1, 1, 1)
rohirricBow = Weapon("Rohirric Bow", "Historic embroidery", 1, 1, 1)
battleMace = Weapon("Battle Mace", "Classic for knights", 1, 1, 1)
battleLance = Weapon("Battle Lance", "Essential for knights", 1, 1, 1)

rohanWeaponsDist = {
    ironSword: [0 , 10],
    mediumSword: [10 , 14],
    rohirricBow: [10 , 20],
    battleMace: [9 , 12],
    battleLance: [8 , 20],
}

#Rhovanion Shops - levels 6-15
elvenTrainerBow = Weapon("Elven Trainer Bow", "For elf children", 1, 1, 1)
elvenBlade = Weapon("Elven Blade", "Glows as enemies near", 1, 1 , 1)
elvenBow = Weapon("Elven Bow", "Standard grade", 1, 1, 1)
doubleBlades = Weapon("Double Blades", "Slice and dice", 1, 1, 1)
eliteElvenSword = Weapon("Elite Elven Blade", "Powerful, magical properties", 
    1, 1, 1)
eliteElvenBow = Weapon("Elite Elven Longbow", "Made of mallorn", 1, 1, 1)

rhovanionWeaponsDist = {
    elvenTrainerBow: [0, 8],
    elvenBlade: [8, 10],
    elvenBow: [9, 11],
    doubleBlades: [10, 12],
    eliteElvenSword: [12, 20],
    eliteElvenBow: [12, 20],
}

#Gondor Shops - levels 12-20
soldersSword = Weapon("Soldier's Sword", "Standard grade", 1, 1, 1)
longSword = Weapon("Long Sword", "A Gondorian blade", 1, 1, 1)
compoundBow = Weapon("Compound Bow", "Extreme range", 1, 1, 1)
eliteLongSword = Weapon("Elite Long Sword", "A Numernorian blade", 1, 1, 1)
gondorianLongbow = Weapon("Gondorian Longbow", "Extreme range", 1, 1, 1)

gondorWeaponsDist = {
    soldersSword: [0, 14],
    longSword: [12, 15],
    compoundBow: [14, 16],
    eliteLongSword: [16, 20],
    gondorianLongbow: [16, 20],
}

#Shop armor
#Eriador Shops - levels 1-5
farmerShawl = Armor("Farmer's Shawls", "Protection from the sun", 4, 4, 1)
travelCloak = Armor("Travel Cloak", "A dark shroud", 3, 5, 1)
leatherCloak = Armor("Leather Cloak", "Stuffy", 5, 8, 2)

eriadorArmorDist = {
    farmerShawl: [0, 2],
    travelCloak: [2, 4],
    leatherCloak: [3, 20]
}

#Rohan Shops - levels 8-12
leatherArmor = Armor("Leather Armor", "Light and lithe", 1, 1, 1)
chainmail = Armor("Chainmail", "Took an incredibly long time to make", 1, 1, 1)
suitOfArmor = Armor("Suit of Armor", "To become a knight in shining armor", 
    1, 1, 1)
rohirricBreastplate = Armor("Rohirric Breastplate", "Aged with dignity", 
    1, 1, 1)
    
rohanArmorDist = {
    leatherArmor: [0, 12],
    chainmail: [8, 15],
    suitOfArmor: [13, 15],
    rohirricBreastplate: [14, 20]
}

#Rhovanion Shops - levels 6-15
workersGear = Armor("Worker's Gear", "Poor-elf's clothes", 1, 1, 1)
elvenWare = Armor("Elven Ware", "A time-tested classic", 1, 1, 1)
eliteElvenWare = Armor("Elite Elven Ware", "At a huge premium", 1, 1, 1)
velvetSuit = Armor("Velvet Suit", "Sex appeal", 1, 1, 1)

rhovanionArmorDist = {
    workersGear: [0, 9],
    elvenWare: [8, 12],
    eliteElvenWare: [12, 15],
    velvetSuit: [15, 20]
}

#Gondorian Shops - levels 12-20
standardSoldiersArmor = Armor("Standard Soldier's Armor", "Sells for a reason", 
    1, 1, 1)
platemail = Armor("Platemail", "Can take a wallop", 1, 1, 1)
magneticArmor = Armor("Magnetic Armor", "Repels attacks", 1, 1, 1)
eliteGondorianArmor = Armor("Elite Gondorian Armor", "Elite Platemail", 
    1, 1, 1)
    
gondorArmorDist = {
    standardSoldiersArmor: [0, 16],
    platemail: [14, 16],
    magneticArmor: [16, 20],
    eliteGondorianArmor: [18, 20]
}

#Shop potions
#Eriador shops
hobbitTea = Potion("Hobbit Tea", "Bay leaf", 1, 1, 2)
shireWater = Potion("Shire Water", "From the Brandywine", 1, 2, 4)
shireWater2 = Potion("Shire Water", "From the Shirebourne", 1, 2, 6)

eriadorPotionDist = {
    hobbitTea: [0, 2],
    shireWater: [2, 4],
    shireWater2: [4, 20]
}

#Rohan shops
adornWater = Potion("Adorn Water", "From the Adorn River", 1, 1, 1)
rohirricTea = Potion("Rohirric Tea", "Calming effects", 1, 1, 1)
fangornWater = Potion("Entwash Water", "Extreme restorative properties", 1, 1, 1)

rohanPotionDist = {
    adornWater: [0, 12],
    shireWater: [10, 12],
    shireWater2: [12, 20]
}

#Rhovanion shops
elvenTea = Potion("Elven Tea", "Magical effects", 1, 1, 1)
mirkwoodWater = Potion("Elven Water", "From the Misty Mountains", 1, 1, 1)
magicalElixir = Potion("Magical Elixir", "Has a strange glow", 1, 1, 1)

rhovanionPotionDist = {
    elvenTea: [0, 12],
    mirkwoodWater: [12, 14],
    magicalElixir: [14, 20]
}

#Gondor shops
anduinWater = Potion("Anduin Water", "All the way from the Anduin River", 1, 1, 1)
snowmelt = Potion("Snowmelt", "From the White Mountains", 1, 1, 1)
advancedElixir = Potion("Advanced Elixir", "From the Houses of Healing", 1, 1, 1)

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