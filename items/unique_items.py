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

#Hobbiton Square
walkingCane = Item("Walking Cane", "Dubiously helpful", 1)
tea = Potion("Tea", "A delightful refreshment", 1, 1, 1)
newspaper = Item("The Shire Newspaper", "Mostly tabloids... about hobbits", 1)
hobbitonSquareItems = {"Naftel Took": walkingCane, "Amaranth Brandybuck": [tea, newspaper]}

#Council of Elrond
legolasHair = Item("Legolas' Hair", "Industrial applications", 0)
mithrilVest = Armor("Mithril Vest", "Gift from Bilbo", 1, 5, 0)
anduril = Weapon("Anduril - The Flame of the West", "The sword once broken, now reforged", 2, 20, 50)
councilOfElrondItems = {"Elrond": [mithrilVest, anduril], "Legolas": legolasHair}

#The Pit
water = Potion("Water", "For sobering up", 1, 5, 1)
elvenRum = Potion("Elven Rum", "Bad for non-elves", 1, 5, -5)
thePitItems = {"Curufin": water, "Daeron": elvenRum}

#Elvenking's Throne
sweetNewElvenWare = Armor("Sweet New ElvenWare", "The latest from Mirkwood", 10, 5, 10)
elvenkingsThroneItems = {"Beleg": sweetNewElvenWare}

#Prancing Pony
tea = Potion("Tea", "Left by Dudo", 2, 2, 1)
bulletin = Item("Nazgul Bulletin", "The people of Bree are scared of Nazgul", 0)
prancingPonyItems = {"Harry Goatleaf": bulletin, "Dudo Baggins": tea}

#Galadriel's Mirror
elvenCloak = Armor("Elven Cloak", "Gifts from Galadriel", 0, 4, 25)
phialOfGaladriel = Item("Phial of Galadriel", "'May it be a light for you in dark places...'", 0)
galadrielsMirrorItems = {"Galadriel": [elvenCloak, phialOfGaladriel]}

#Helm's Deep Commons
vodka = Potion("Koskenkorva", "Rohirric Poisons", 1, 5, 0)
vodka2 = Potion("Luksusowa", "Budget Vodka", 1, 4, 0)
helmsDeepCommonsItems = {"Erkenbrand": vodka, "Gambling the Old": vodka2}

#Edoras Commons
tea = Potion("Tea", "For sharing stories over", 1, 5, 1)
tea2 = Potion("Soda", "'Risque' in this community", 1, 5, 1)
newspaper = Item("Newspaper", "Full of clippings. Mostly for reminiscing", 1)
edorasCommonsItems = {"Helm Gammerhand": tea, "Frealaf Hildeson": tea2, "Brytta Leofa": newspaper}

#Auburn Square Commons
russianTea = Potion("Russian Tea", "Very rare", 1, 5, 1)
freePizza = Potion("Free Pizza", "Tombstones though", 1, 10, 1)
chineseHandouts = Item("Chinese Handouts", "Poor quality", 1)
auburnSquareCommons = {"Dmitriy": russianTea, "Jim 'The Dear Ladd' Jr.": freePizza, "Chris 'Chocolate Rain' Wang": chineseHandouts}

#Market Square
fruitSamples = Potion("Fruit Samples", "Meagerly", 1, 2, 0)
foodHoards = Potion("Food Hoards", "It appears that some people are stocking up", 3, 10, 2)
negativeThinking = Item("Negative Thinking", "Not something you want", 15)
marketSquareItems = {"Calmacil": fruitSamples ,"Atanatar": foodHoards, "Castamir": negativeThinking}

#Tower of Echelion
palatir = Item("Palatir", "Strange orb-like thing", 10)
niceSword = Weapon("Nice Sword", "Very Nice!", 3, 15, 4)
towerOfEchelionItems = {"Denethor": palatir, "Prince Imrahil": niceSword}

#Beach
draagz = Item("Draagz", "Bad for health... and illegal", 15)
vodka = Potion("Vodka", "From the Gondorian heartland", 10, 5, 10)
flowersAndTrinkets = Potion("Flowers And Trinkets", "Massive mental health bonuses", 10, 5, 10)
beachItems = {"Gondorian bro #3": draagz, "Gondorian bro #2": flowersAndTrinkets}

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
tarhelmCrown = Armor("TarnHelm Crown", "Straight from Tristram", 2, 10, 10)
snowclash = Armor("Snowclash Battle Belt", "Straight from Tristram", 2, 10, 10)
razortail = Armor("Razortail Sharkskin", "Straight from Tristram", 2, 10, 10)
nightsmoke = Armor("Nightsmoke", "Straight from Tristram", 2, 10, 10)
peasantCrown = Armor("Peasant Crown", "Straight from Tristram", 2, 10, 10)
crownOfThieves = Armor("Crown of Thieves", "Straight from Tristram", 2, 10, 10)
harlequinCrestShako = Armor("Harlequin Crest Shako", "Straight from Tristram", 2, 10, 10)

findableUniques = [scepterOfAnnuminas, aeglos, glamdring, arglachel, angrist, anguirel, ananruth, belthronding,
                   dramborleg, grond, guthwine, herugrim, orchrist, ringil, crownOfElendil, ironCrown, helmOfHador,
                   tarhelmCrown, snowclash, razortail, nightsmoke, peasantCrown, crownOfThieves, harlequinCrestShako]
