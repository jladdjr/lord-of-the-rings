#!/usr/bin/python
#-*- coding: utf-8 -*-

from space import Space
from cities.city import City
from cities.inn import Inn
from cities.square import Square
from cities.shop import Shop
from unique_place import UniquePlace
from player import Player
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from commands.command_words import CommandWords
from commands.help_command import HelpCommand 
from commands.quit_command import QuitCommand
from commands.describe_command import DescribeCommand
from commands.drop_command import DropCommand
from commands.enter_command import EnterCommand
from commands.pick_up_command import PickUpCommand
from commands.equip_command import EquipCommand
from commands.unequip_command import UnequipCommand
from commands.use_potion_command import UsePotionCommand
from commands.check_inventory_command import CheckInventoryCommand
from commands.check_equipment_command import CheckEquipmentCommand
from commands.check_money_command import CheckMoneyCommand
from commands.check_stats_command import CheckStatsCommand
from commands.map_command import MapCommand
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand
from unique_places.tom_bombadil_house import TomBombadilHouse
from unique_places.weathertop import Weathertop
from unique_places.isenguard import Isenguard
from unique_places.tharbad import Tharbad
from unique_places.argonath import Argonath
from unique_places.ost_in_edhil import OstInEdhil
from unique_places.goblin_town import GoblinTown
from unique_places.minas_morgul import MinasMorgul
from unique_places.black_gate import BlackGate
from unique_places.isenmouthe import Isenmouthe
from unique_places.barad_dur import BaradDur
from unique_places.dol_guldur import DolGuldur
from unique_places.tower_of_cirith_ungol import TowerOfCirithUngol
from unique_places.moria import Moria
import items.unique_items
import constants

import random

def getWorld():
    #Shire - Hobbiton
    #Inn
    description = "A place for strangers."
    greeting = "Welcome to our inn! I'm Sally of the Tokinsville Baggins Clan."
    sallyInn = Inn("Sally's Inn", description, greeting, 5)
    #Shop
    description = "Exotic selection by hobbit standards."
    greeting = "We have strange wares."
    sallyShop = Shop("Sally's Shop", description, greeting, 4, 3)
    #Square
    description = "Lots of hobbits, mostly gossip."
    greeting = "Did you hear the latest news on Lobelia Baggins?"
    talk = {"Lobelia Baggins": "Get lost!", "Naftel Took": "Going adventuring are ya? Here's my walking cane.", "Amaranth Brandybuck": "Nice weather isn't it?", "Balbo Baggins": "The word on the street is that Lobelia is trying to acquire the Baggins estate!", "Ferdinand Took": "I wonder when Gandalf will visit?"}
    hobbitonSquare = Square("Hobbiton Square", description, greeting, talk, items.unique_items.hobbitonSquareItems)
    #City
    description = """Hobbiton is a village in the central regions of the
    Shire within the borders of the Westfarthing. Hobbiton is located
    on both sides of the Water approximately a mile northwest of the
    neighboring village of Bywater.
    """
    greeting = "'Have you heard the news?'"
    hobbiton = City("Hobbiton", description, greeting, [sallyInn, sallyShop, hobbitonSquare])
    #The Shire
    description = """
    The Shire is divided into four farthings, North, South, East and West;
    its chief town is Michel Delving on the White Downs in the
    Westfarthing. The Mayor of Michel Delving is the most important of
    the Shire-hobbits.

    The Shire is largely dependent on agriculture and its land is
    well-suited for farming. One of its chief products is Shire
    Leaf, grown especially in the warmer regions of the Southfarthing.
    """
    shire = Space("Shire", description, constants.RegionType.ERIADOR, city = hobbiton)

    #The Old Forest - Tom Bombadil's House
	#Unique Place
    description = "The house of a mysterious and powerful being, who dwells in the valley of Withywindle."
    greeting = """
    \"Old Tom Bombadil is a merry fellow;
    Bright blue his jacket is, and his boots are yellow.\"
    """
    tomBombadil = TomBombadilHouse("Tom Bombadil's House", description, greeting)
    #The Old Forest
    description = """
    The Old Forest is one of the few surviving primordial forests
    which covered most of Eriador before the Second Age. The Old Forest
    has been known to play tricks on travelers in response to its
    massive deforestation. 
    """
    oldForest = Space("Old Forest", description, constants.RegionType.ERIADOR, uniquePlace = tomBombadil)

    #The Weather Hills - Weathertop
    #Unique Place
    description = "Once a great watchtower, guarding the entire region."
    greeting = "The Weathertop ruins whisper of its former glory."
    weathertop = Weathertop("Weathertop", description, greeting)
    #The Weather Hills
    description = """
    Weather Hills is the name among Men for the range of hills
    that lay in central Eriador and in ancient times marked part of the
    border between the lands of Arthedain and Rhudaur. Weathertop, or
    Amon Sûl, lays at the southern end of this range.
    """
    weatherHills = Space("Weather Hills", description, constants.RegionType.ERIADOR, uniquePlace = weathertop)

    #Trollshaws
    description = """
    Trollshaws are the upland woods that lay to the west of Rivendell and
    the Rivers Hoarwell and Loudwater. They were the haunt of Trolls, three
    of which waylaid Bilbo and his companions during the Quest of Erebor.
    """
    trollshaws = Space("Trollshaws", description, constants.RegionType.ERIADOR)

    #Misty Mountains North - Rivendell
    #Inn
    description = "A relaxing stay in the scenic Misty Mountains!"
    greeting = "Welcome to Misty Mountain Inn! Let us host you tonight...."
    mistyInn = Inn("Misty Mountain Inn", description, greeting, 5) 
    #Shop
    description = "New Elvenware! Look like your favorite elf!"
    greeting = "Welcome to ElvenWares! Here we have the latest in elven gadgetry."
    elvenWares = Shop("ElvenWares", description, greeting, 5, 6)
    #Square
    description = "Hotshots only."
    greeting = "We've been waiting for your arrival...."
    talk = {"Elrond": "The sword that was broken... now reforged!", "Legolas": "What do you think about my hair?", "Aragorn": "Check out these knife tricks!", "Gimli": "I bet I can eat more hotdogs than you.", "Gandalf": "Did you know I have the Ring of Fire?"}
    councilOfElrond = Square("Council of Elrond", description, greeting, talk, items.unique_items.councilOfElrondItems)
    #City
    description = """
    Rivendell, also known as Imladris, is an Elven outpost in Middle-earth.
    It is also referred to as "The Last Homely House East of the Sea," a
    reference to Valinor, which is west of the Great Sea in Aman.
    """
    greeting = "Rivendell is a sight for sore eyes, truly a mountain paradise."
    rivendell = City("Rivendell", description, greeting, [mistyInn, elvenWares, councilOfElrond])
    #Misty Mountains North
    description = """The Misty Mountains or Mountains of Mist is a great
    mountain range that lies between Eriador in the west and the Great
    River Anduin in the east. It runs 795 miles (1,280 kilometers) from
    Mount Gundabad in the far north to Methedras in the south.
    """
    mistyMountainsNorth = Space("Misty Mountains", description, constants.RegionType.ERIADOR, city = rivendell)

    #High Pass - Goblintown
    #Unique Place
    description = """Goblin-town is a Goblin dwelling which lies
    under the High Pass in the Misty Mountains and is ruled by the Great
    Goblin. Gullum's cave is deep beneath Goblin-town and is connected
    to the Goblins' tunnels.
    """
    greeting = "\"What is better: subtlety or aggression?\""
    goblinTown = GoblinTown("Goblin Town", description, greeting)
    #High Pass
    description = """The High Pass is a pass over the Misty Mountains.
    On its western end is the refuge of Rivendell and from there the
    Great East Road climbs into the mountains until it reaches Goblin-town.
    """
    highPass = Space("High Pass", description, constants.RegionType.HIGH_PASS, uniquePlace = goblinTown)

    #Mirkwood - Elvenking's Halls
    #Inn
    description = "A woodland experience...."
    greeting = "Welcome to Sihirli Mutfak!"
    sihirliMutfak = Inn("Sihirli Mutfak", description, greeting, 5)
    #Shop
    description = "Your local ElvenWares!"
    greeting = "Great variety of elven gadgetry available!"
    elvenWares = Shop("ElvenWares", description, greeting, 7, 10)
    #Square
    description = "Drinks on Thrandruil!"
    greeting = "You arrive to find a mass of drunken elves."
    talk = {"Cananthir": "Gaaalaaaagh....", "Curufin": "Don't mind Canathir, he's had a rough life", "Daeron": "Let's drink to Legolas!", "Ecthelion": "Glaaaaaaack....", "Earwen": "[Ignores you.]"}
    thePit = Square("The Pit", description, greeting, talk, items.unique_items.thePitItems)
    #Square
    description = "Thrandruil's throne room."
    greeting = "What makes you think that you belong here?"
    talk = {"Thranduil": "Hmmph! I'm elvenking!", "Angrod": "Much gnashing of teeth here. You probably won't find what you're looking for.", "Aredhel": "Hmmph! Humans!", "Argon": "Hmmph! Didn't you know that you're wearing yesterday's ElvenWare?", "Beleg": "Hmmph! Dress in better ElvenWare!"}
    elvenkingsThrone = Square("Elvenking's Throne", description, greeting, talk, items.unique_items.elvenkingsThroneItems)
    #City
    description = """The Elvenking's Halls is the cave system in northern
    Mirkwood in which King Thranduil and many of the Elves of Mirkwood
    live.
    """
    greeting = "You arrive to find a bustling network of caves."
    elvenkingsHalls = City("Elvenking's Halls", description, greeting, [sihirliMutfak, elvenWares, thePit, elvenkingsThrone])
    #Mirkwood
    description = """Mirkwood or the Forest of Great Fear is a great
    forest in Rhovanion. Mirkwood is once called Greenwood the Great
    and later became the Wood of Greenleaves."""
    mirkwood = Space("Mirkwood", description, constants.RegionType.RHOVANION, city = elvenkingsHalls)

    #Southern Mirkwood - Dol Guldur
    #Unique Place
    description = "Hill fortress of Sauron."
    greeting = "You are overcome with an overwhelming sense of fear as you approach the citadel of Dol Guldur."
    dolGuldur = DolGuldur("Dol Guldur", description, greeting)
    #The Old Forest
    description = """
    During the time of the War of the Ring, Southern Mirkwood was
    occupied by Dol Guldur, Sauron's northern fortress. 
    """
    southernMirkwood = Space("Southern Mirkwood", description, constants.RegionType.RHOVANION, uniquePlace = dolGuldur)

    #Barrow Downs - Bree
    #Inn
    description = "A quiet inn, tucked away in the outskirts of Bree."
    greeting = "Hi I'm Linda, the innkeeper."
    lindasInn = Inn("Linda's Inn", description, greeting, 5)
    #Shop
    description = "COME GET YOUR ORC-KILLING GEAR HERE!"
    greeting = "HI I'M HANK!!! KILL ORCS!!!!!"
    hanksBattleGear = Shop("Hank's Battle Gear", description, greeting, 8, 4)
    #Square
    description = "A noisy hole in the wall known for quarrels."
    greeting = "You are greeted with silence. Two people stare at you briefly \nbefore turning back to their drinks."
    talk = {"Bill Ferny": "I hear there's been Nazgul in these parts.", "Harry Goatleaf": "The entire town is scared of Nazgul....", "Henry Thistlewool": "The shadow has descended upon these parts....", "Dudo Baggins": "What am I even doing here?", "Estella Brandybuck": "Time to go home I think...."}
    prancingPony = Square("Prancing Pony", description, greeting, talk, items.unique_items.prancingPonyItems)
    #City
    description = """Bree was settled in the early Third Age, in the
    realm Cardolan. Though the Princes of Cardolan claimed it, Bree
    continued to thrive without any central authority or government
    for many centuries. 
    """
    greeting = "Nazgul have been visiting the area at night!"
    bree = City("Bree", description, greeting, [lindasInn, hanksBattleGear, prancingPony])
    #Barrow Downs
    description = """Barrow-downs or Tyrn Gorthad is a series of low
    hills east of the Shire, behind the Old Forest and west of the
    village of Bree. Many of the hills are crowned with megaliths
    and barrows.
    """
    barrowDowns = Space("Barrow Downs", description, constants.RegionType.BARROW_DOWNS, city = bree)

    #Bruinen
    description = """Bruinen or Loudwater is a river in eastern Eriador.
    It begins with two tributaries flowing from the western slopes of the
    Misty Mountains.
    """
    bruinen = Space("Bruinen", description, constants.RegionType.ERIADOR)

    #Mitheithel - Tharbad
    #Unique Place
    description = "Once a fortified town on the River Greyflood, Tharbad now lies in ruins."
    greeting = "An eerie mist greets you as you enter the ruins of the once great Tharbad...."
    tharbad = Tharbad("Tharbad", description, greeting)
    #Mitheithel
    description = """Mitheithel is the long river that rises in a place
    in the icy north of Middle-earth called Hoarwell.
    """
    mitheithel = Space("Mitheithel", description, constants.RegionType.ERIADOR, uniquePlace = tharbad)

    #Swanfleet - Ost In Edhil
    #Unique Place
    description = """Once a great elven city, now destroyed by Sauron. The 
    Rings of Power were forged by Celebrimbor here."""
    greeting = """You arrive at a strange sight: the once great city of Ost
    In Edhil now an ancient ruin. Strange symbols cover the land."""
    ostInEdhil = OstInEdhil("Ost In Edhil", description, greeting)
    #Swanfleet
    description = """The Swanfleet or Nin-in-Eilph is a marshy area in
    eastern Eriador where the lower reaches of the Glanduin flows
    before it joins Mitheithel. Swanfleet is an inland delta.
    """
    swanfleet = Space("Swanfleet", description, constants.RegionType.ERIADOR, uniquePlace = ostInEdhil)
    
    #Dunland
    description = """Dunland is the land of the Dunlendings. Dunland means
    Hill Land in the language of neighbouring Rohan, whose people named it
    after arriving in nearby Calenardhon in the later Third Age. It is a
    land of wild men.
    """
    dunland = Space("Mitheithel", description, constants.RegionType.RHOVANION)

    #Misty Mountains South
    #Unique Place
    description = """Moria consists of an enormous underground complex in
    north-western Middle-earth, comprising a vast network of tunnels,
    chambers, mines and huge halls or mansions, that ran under and ultimately 
    through the Misty Mountains. 
    """
    greeting = """Welcome to the Mines of Moria, where an unspeakable evil
    lurks in the shadows.
    """
    moria = Moria("Moria", description, greeting)
    #Misty Mountains South
    description = """Khazad-dum, (also known as Moria, The Black Chasm,
    The Black Pit, Dwarrowdelf, Hadhodrond, Casarrondo, and Phurunargian)
    is the grandest and most famous of the mansions of the Dwarves. There,
    for many thousands of years, a thriving Dwarvish community created the
    greatest city ever known.
    """
    mistyMountainsSouth = Space("Misty Mountains", description, constants.RegionType.MORIA, uniquePlace = moria)

    #Lorien - Caras Galadhon
    #Inn
    description = "Nested between the rivers Anduin and Silverlode."
    greeting = "Elvenwaters is a truly beautiful inn, bathed in mist."
    elvenWaters = Inn("ElvenWaters Inn", description, greeting, 5)
    #Shop
    description = "ElvenWares! Lots of great elven gear!"
    greeting = "Welcome to ElvenWares! We have lots of rare collectibles!"
    elvenWares = Shop("ElvenWares", description, greeting, 7, 8)
    #Square
    description = "For prophesy as well as plain old-fashioned vanity."
    greeting = "A strange sight: Galadriel's mirror as well as Galadriel herself!"
    talk = {"Galadriel": "Check out this new ElvenWare! How do you think I look?"}
    galadrielsMirror = Square("Galadriel's Mirror", description, greeting, talk, items.unique_items.galadrielsMirrorItems)
    #City
    description = """Caras Galadhon is a city located in Lorien. Its inhabitants
    dwell in large flets in the trees, reachable by white ladders. On the top
    of the hill in the greatest of trees is the house of Celeborn and Galadriel.
    """
    greeting = "Welcome to Caras Galdhon! Celeborn and Galadriel reside here."
    carasGaladhon = City("Caras Galadhon", description, greeting, [elvenWaters, elvenWares, galadrielsMirror])
    #Lorien
    description = """Lothlorien is a kingdom of Silvan Elves on the
    eastern side of the Hithaeglir. It is considered one of the most
    beautiful places in Middle-earth and has the only mallorn-trees
    east of the sea.
    """
    lorien = Space("Lorien", description, constants.RegionType.RHOVANION, city = carasGaladhon)

    #Fangorn - Derningle
    #Unique Place
    description = "Derningle is the site of meeting for Fangorn's ents."
    greeting = "\"Welcome to the Entmoot! Don't be so hasty.\""
    derningle = UniquePlace("Derningle", description, greeting)
    #Fangorn
    description = """Fangorn Forest is a deep, dark woodland that grows
    beneath the southern tips of the Misty Mountains under the eastern flanks
    of that range. It gains notoriety for its Ents. The forest, known as
    Entwood in Rohan, was named after its oldest Ent, Fangorn.
    """
    fangorn = Space("Fangorn", description, constants.RegionType.ROHAN, uniquePlace = derningle)

    #The Wold
    description = """The Wold is the northernmost and least populated part
    of Rohan, lying between Fangorn Forest and the Anduin, bordered to the
    north by the Limlight.

    Its main inhabitants were nomadic Men of Rohan who use the land to graze
    cattle. In recent years, these men have fled in response to frequent
    attacks by orcish raiders.
    """
    theWold = Space("The Wold", description, constants.RegionType.MORDOR)

    #Field of Celebrant
    description = """The Field of Celebrant lies between the Rivers Anduin
    and Limlight and southeast of Lothlorien. In T.A. 2510, the decisive
    Battle of the Field of Celebrant where the men of Rohan rose up to
    aid Gondor happened here.
    """
    fieldOfCelebrant = Space("Field of Celebrant", description, constants.RegionType.MORDOR)

    #Calenardhon - Isenguard
    #Unique Place
    description = """Isengard ("Iron Fortress" or Angrenost in Sindarin) is
    a great fortress located within a valley at the southern end of the Misty
    Mountains near the Gap of Rohan. In the centre of the Ring of Isengard
    stands the stone tower of Orthanc.
    """
    greetings = "Charred skies greet you as you approach Isenguard...."
    isenguard = Isenguard("Isenguard", description, greetings)
    #Calenardhon
    description = """Calenardhon contains Isengard, a great fortress located
    within a valley at the southern end of the Misty Mountains near the Gap
    of Rohan.
    """   
    calenardhon = Space("Calenardhon", description, constants.RegionType.ENEDWAITH, uniquePlace = isenguard)

    #Westfold - Helm's Deep
    #Inn
    description = "Where people go to sober up."
    greeting = "[No one is there to greet you.]"
    sobrietyRoom = Inn("Sobriety Room", description, greeting, 0)
    #Shop
    description = "The Armory [read: booze shop]."
    greeting = "We got every poison under the sun...."
    theArmory = Shop("The Armory", description, greeting, 10, 8)
    #Square
    description = "Mass drunkenness."
    greeting = "Everyone is passed out."
    talk = {"Erkenbrand": "Ughhhhhhh....", "Gambling the Old": "Merrrrrrrrrrrrr...."}
    helmsDeepCommons = Square("Helms Deep Commons", description, greeting, talk, items.unique_items.helmsDeepCommonsItems)
    #City
    description = """Helm's Deep is a large valley gorge in northwestern
    Ered Nimrais below the Thrihyrne. It is the name of the whole
    defensive system including its major defensive structure, the Hornburg.
    """
    greeting = "Welcome to Helm's Deep! WHOOO!!! PARTY!"
    helmsDeep = City("Helm's Deep", description, greeting, [sobrietyRoom, theArmory, helmsDeepCommons])
    #Westfold
    description = """The Westfold is the western part of Rohan, close to
    the White Mountains and situated between the river Isen and the Folde.
    The North-South Road runs through the Westfold from the Fords of Isen
    to Edoras. Its strongpoint is Helm's Deep.
    """
    westfold = Space("Westfold", description, constants.RegionType.ROHAN, city = helmsDeep)

    #Westemnet
    description = """The Eastemnet is part of Rohan. It is an area of
    wide, grassy plains east of the Entwash River.
    """ 
    westemnet = Space("West Emmet", description, constants.RegionType.ROHAN)

    #Eastemnet
    description = """The Eastemnet is part of Rohan. It contains
    wide, grassy plains and is east of the Entwash and west of
    the Great River, Anduin.
    """ 
    eastemnet = Space("East Emmet", description, constants.RegionType.ROHAN)

    #Emyn Muil
    description = """Emyn Muil is a range of hills south of the Brown
    Lands and north of Nindalf. The Anduin cuts through these hills
    and pools in Nen Hithoel.
    """ 
    emynMuil = Space("Emyn Muil", description, constants.RegionType.MORDOR)

    #Eastfold - Edoras
    #Inn
    description = "Edoras' old folks' home."
    greeting = "Here sonnie, thanks for coming to visit."
    sunsetVillage = Inn("Sunset Village", description, greeting, 5)
    #Shop
    description = "Crafts and various collectibles."
    greeting = "We have items dating back from T.A. 1497!"
    twiceRemembered = Shop("Twice Remembered", description, greeting, 12, 8)
    #Square
    description = "Home of bingo and other festivities."
    greeting = "How are you sonnie?"
    talk = {"Helm Gammerhand": "What is this 'War of the Ring' you speak of?", "Brytta Leofa": "Back in my day, we fought against a guy named Morgoth. I bet you've never even heard of Morgoth.", "Morwen Steelsheen": "You youngsters are so impatient these days. Always rushing off into battles that you don't need to be involved in....", "Frealaf Hildeson": "I have no idea what you're talking about with this 'Sauron' business."}
    edorasCommons = Square("Edoras Commons", description, greeting, talk, items.unique_items.edorasCommonsItems)
    #City
    description = """Rohan's first capital was at Aldburg in the Folde
    until Eorl the Young's son Brego built Edoras. It is Rohan's
    only real city and holds the Golden Hall of Meduseld.
    """
    greeting = "Welcome to Edoras, Rohan's greatest retirement community!"
    edoras = City("Edoras", description, greeting, [sunsetVillage, twiceRemembered, edorasCommons])
    #Eastfold - Aldburg
    #Inn
    description = "Innkeeper is a man by the name of Seth."
    greeting = "Sleepytime for Seth. I'll see you guys later."
    sethsHostel = Inn("Seth's Hostel", description, greeting, 5)
    #Shop
    description = "Other dishes too."
    greeting = "Coooooookie crisp!"
    milesCookieFactory = Shop("Miles' Cookie Factory", description, greeting, 15, 4)
    #Square
    description = "For late-night programming, among other things."
    greeting = "What the heck is going on?"
    talk = {"Dmitriy": "The isomorphic properties of this list lends itself to three-tailed development.", "Jim 'The Dear Ladd' Jr.": "???", "Chris 'Chocolate Rain' Wang": "I am from China."}
    auburnSquare = Square("Auburn Square Commons", description, greeting, talk, items.unique_items.auburnSquareCommons)
    #City
    description = """Aldburg was built by Eorl in the region known as the Folde,
    east of Edoras. The Kings of Rohan moved to Edoras after Brego, son of Eorl,
    completed the Golden Hall.
    """
    greeting = "Welcome to Aldburg! Home of Jim Ladd Jr."
    aldburg = City("Aldburg", description, greeting, [sethsHostel, milesCookieFactory, auburnSquare])
    #Eastfold
    description = """Eastfold is a part of the realm of Rohan. Bounded
    by the Mering Stream and Snowbourn River, it contains the city of
    Edoras.
    """
    eastfold = Space("Eastfold", description, constants.RegionType.ROHAN, city = [edoras, aldburg])

    #Nindalf
    description = """The swamps of Nindalf or Wetwang lie to the south of
    Emyn Muil and east of the Great River Anduin and are fed by the great
    inland delta of Entwash. The Dead Marshes lie further east and are
    an extension of Nindalf.
    """ 
    nindalf = Space("Nimdalf", description, constants.RegionType.MORDOR)

    #Dead Marshes - Black Gate
    #Unique Place
    description = """The Black Gate of Mordor is a gate built by Sauron
    to prevent invasion through the Pass of Cirith Gorgor, the gap between
    the Ered Lithui and the Ephel Duath.
    """
    greetings = "\"May it be a light to you in dark places.\""
    blackGate = BlackGate("Black Gate", description, greetings)
    #Dead Marshes
    description = """The Dead Marshes are an area of swampland east of the
    Dagorlad plain. It is the site of the ancient Battle of Dagorlad.
    """
    deadMarshes = Space("Dead Marshes", description, constants.RegionType.MORDOR, uniquePlace = blackGate)

    #Valley of Udun - Isenmouthe
    #Unique Place
    description = """Isenmouthe or Carach Angren is a pass in the
    northeastern part of Mordor and guards the southern end of the valley,
    Udun.
    
    The pass is heavily guarded with Fortresses and watchtowers.
    """
    greetings = "\"One does not simply walk into Mordor II.\""
    isenmouthe = Isenmouthe("Isenmouthe", description, greeting)
    #Valley of Udun
    description = """Udun is a depressed valley in northwestern Mordor.
    It lies between Cirith Gorgor and Isenmouthe and is traversed
    by large armies of Sauron in times of war.
    """
    udun = Space("Udun", description, constants.RegionType.MORDOR, uniquePlace = isenmouthe)
    
    #Cair Andros
    description = """Cair Andros, meaning "Ship of the Long-Foam," is an
    island in the river Anduin, resting nearly forty miles to the north
    of Osgiliath.  It is of paramount importance to Gondor because it
    prevents the enemy from crossing the river and entering into Anorien.
    """ 
    cairAndros = Space("Cair Andros", description, constants.RegionType.GONDOR, greeting)

    #Orodruin
    description = """Mount Doom, also known as Orodruin and Amon Amarth, is
    the volcano in Mordor where the One Ring was forged. It is the only place
    that the One Ring may be destroyed.
    """
    orodruin = Space("Orodruin", description, constants.RegionType.MORDOR)

    #Anorien - Minas Tirith
    #Inn
    description = "Home of elite Gondorian healers."
    greeting = "Welcome to the Houses of Healing. What can I do for you?"
    housesOfHealing = Inn("Houses of Healing", description, greeting, 5)
    #Shop
    description = "An elite armory, used by the best Gondorian troops."
    greeting = "Welcome to the Smithy of Kings! We have forged legendary blades...."
    smithyOfKings = Shop("Smithy of Kings", description, greeting, 15, 12)
    #Square
    description = "Minas Tirith commons."
    greeting = "Welcome to our square. This place used to be a lot more lively."
    talk = {"Calmacil": "Would you like to buy some fruit?", "Castamir": "Everyone is afraid.", "Ciryandil": "Orcish raids have been increasing in the outlying lands....", "Minalcar": "I wonder what we can do with Mordor....", "Narmacil": "I wonder if the king will return", "Tarondor": "I hope Rohan will bring aid.", "Atanatar": "Word has it that Mordor is preparing to attack."}
    marketSquare = Square("Market Square", description, greeting, talk, items.unique_items.marketSquareItems)
    #Square
    description = "Home to Gondorian royalty."
    greeting = "Denethor would like to see you...."
    talk = {"Denethor": "You are the true king of Gondor.", "Faramir": "The lands recently stolen by Sauron should be retaken....", "Boromir": "Nice ring. Give it to me!", "Prince Imrahil": "Sauron plans on moving soon....", "Swan Knight": "The men are afraid. The land is covered in shadow...."}
    towerOfEcthelion = Square("Tower of Ecthelion", description, greeting, talk, items.unique_items.towerOfEchelionItems)
    #City
    description = """Minas Tirith is a city of Gondor originally called Minas Anor.
    From T.A. 1640 onwards it became the capital of the South-kingdom and the seat of
    its Kings and ruling Stewards.
    """
    greeting = "Welcome to the last stronghold of the West, Minas Tirith."
    minasTirith = City("Minas Tirith", description, greeting, [housesOfHealing, marketSquare, towerOfEcthelion, smithyOfKings])
    #Anorien
    description = """Anorien is the fiefdom of Gondor containing Minas Tirith, the
    capital of Gondor. Originally known as Minas Anor, it replaced Osgiliath
    as capital of Gondor as Osgiliath became lost to Sauron.
    """
    anorien = Space("Anorien", description, constants.RegionType.GONDOR, city = minasTirith)

    #Anduin - Argonath
    #Unique Place
    description = "Great for dates."
    greeting = "\"Welcome to Argonath! Stay within the designated areas and listen to your guide.\""
    argonath = Argonath("Argonath", description, greeting)
    #Anduin - Osgiliath
    #Inn
    description = "A place to rest in the midst of battle."
    greeting = "Your cot is on the top left."
    soldierBarracks = Inn("Soldier Barracks", description, greeting, 5)
    #Shop
    description = "Rapidly depleting inventories."
    greeting = "What would you like? We are running low on everything...."
    osgiliathArmory = Shop("Osgiliath Armory", description, greeting, 4, 15)
    #Square
    description = "Once a glorious square in the capital of Gondor."
    greeting = "You find the square in ruins and completely deserted."
    talk = {}
    osgiliathCommons = Square("Osgiliath Commons", description, greeting, talk)
    #City
    description = """Osgiliath was the ancient capital of the Kingdom of Gondor.
    Depopulated during the Third Age, it gradually fell into ruin. Osgiliath has
    strategic importance as a crossing point over the Anduin.
    """
    greeting = "AEIEEE!!! WE'RE UNDER SEIGE!"
    osgiliath = City("Osgiliath", description, greeting, [soldierBarracks, osgiliathArmory, osgiliathCommons])
    #Anduin
    description = """Anduin is a river that crosses most of Middle-earth east
    of the Misty Mountains. Passing through many lands, it has many names:
    Langflood by the ancestors of the Rohirrim, the Great River of Wilderland in
    the Westron of Rivendell and the Shire, and simply the Great River in Gondor.
    """
    anduin = Space("Anduin", description, constants.RegionType.GONDOR, city = osgiliath, uniquePlace = argonath)

    #Ephel Duath - Minas Morgul
    #Unique Place
    description = """Minas Morgul is a city-fortress in Mordor. Originally created
    as a Gondorian outpost and the sister city to Minas Anor, Minas Ithil safeguarded
    the eastern borders of the Kingdom of Gondor and its capital from the forces of
    Mordor during the early part of the Third Age.

    Minas Morgul is now home to the Nazgul.
    """
    greeting = "\"One does not simply walk into Mordor.\""
    minasMorgul = MinasMorgul("Minas Morgul", description, greeting)
    #Ephel Duath
    description = """The Ephel Dúath, or the Mountains of Shadow, are a range of
    mountains that guard Mordor's western and southern borders.
    """
    ephelDuath = Space("Ephel Duath", description, constants.RegionType.MORDOR, uniquePlace = minasMorgul)

    #Cirith Ungol - Tower of Cirith Ungol
    #Unique Place
    description = """Gondor occupied the fortress until T.A. 1636 when the
    Great Plague killed large parts of Gondor's population. After the plague,
    Gondor never again manned the Tower of Cirith Ungol and evil was allowed
    to return to Mordor. Similar fates suffered the mountain fortress of Durthang
    in northwestern Mordor and the Towers of the Teeth at Morannon.
    """
    greeting = "\"May it be a light to you in dark places.\""
    towerOfCirithUngol = TowerOfCirithUngol("Tower of Cirith Ungol", description, greeting)
    #Cirith Ungol
    description = """Cirith Ungol is the pass through the western mountains of
    Mordor and the only way towards the land from the west. It is guarded by the
    Tower of Cirith Ungol, built by the Men of Gondor after the War of the Last
    Alliance of Elves and Men.
    """
    cirithUngol = Space("Cirith Ungol", description, constants.RegionType.MORDOR, uniquePlace = towerOfCirithUngol)

    #Plateau of Gorgoth - Barad Dur
    #Unique Place
    description = """Barad-dur is the Dark Lord Sauron's sanctuary fortress
    in Mordor and serves as his base of operations. Over 1400 meters high
    and held together by dark magic, it is the largest fortress in
    Middle-earth.
    """
    greeting = """Rising black, blacker and darker than the vast shades amid which it stood,
    the cruel pinnacles and iron crown of the topmost tower of Barad-dur."""
    baradDur = BaradDur("Barad Dur", description, greeting)
    #Plateau of Gorgoth
    description = """Plateau of Gorgoroth is a region in the northwestern region of
    Mordor. Gorgoroth is the location of the mines and forges which supply Mordor's
    armies with weapons and armor.
    """
    plateauOfGorgoth = Space("Plateau of Gorgoth", description, constants.RegionType.MORDOR, uniquePlace = baradDur)

    #Lossamarch - Pelargir
    #Inn
    description = "Beach resort along Gondor's finest coast!"
    greeting = "Hey bro! Welcome to Sunnyside Inn!"
    sunnysideInn = Inn("Sunnyside Inn", description, greeting, 5)
    #Shop
    description = "Beach accessories and paraphernalia."
    greeting = "Hey dude, let's hit the beach later!"
    palmTreeHut = Shop("Palm Tree Hut", description, greeting, 6, 14)
    #Square
    description = "Class-three waves and hot chicks!"
    greeting = "\"Bro, did you see those waves?\""
    talk = {"Gondorian bro #1": "Bro, let's hit the beach!", "Gondorian bro #2": "Bro! Let's just chill for awhile... bro?", "Gondorian bro #3": "Bro! I hear there's going to be a party later tonight.", "Gondorian chick #1": "Bro, I have a boyfriend....", "Gondorian chick #2": "Bro, what are you doing later?"}
    beach = Square("Pelargir Beach", description, greeting, talk, items.unique_items.beachItems)
    #City
    description = """One of the oldest cities in Middle Earth, Pelargir served
    as chief haven of the faithful as Numenorians migrated to Middle Earth to
    escape persecution. In later years, Pelargir served as chief port of Gondor.
    """
    greeting = "Enjoy a relaxing stay at Pelargir, port city of Gondor."
    pelargir = City("Pelargir", description, greeting, [sunnysideInn, palmTreeHut, beach])
    #Lossamarch
    description = """Lossarnach is a region and fiefdom in Southern Gondor. Known
    as the Vale of flowers, it is a fertile region lying south of the White Mountains.
    """ 
    lossamarch = Space("Lossamarch", description, constants.RegionType.GONDOR, city = pelargir)

    #Ithilien
    description = """Ithilien iss the region and fiefdom of Gondor bordering Mordor
    from the southwest.
    """ 
    ithilien = Space("Ithilien", description, constants.RegionType.GONDOR)

    #Connections: East-West
    shire.createExit("east", oldForest, outgoingOnly = False)
    oldForest.createExit("east", weatherHills, outgoingOnly = False)
    weatherHills.createExit("east", trollshaws, outgoingOnly = False)
    trollshaws.createExit("east", mistyMountainsNorth, outgoingOnly = False)
    mistyMountainsNorth.createExit("east", highPass, outgoingOnly = False)
    barrowDowns.createExit("east", bruinen, outgoingOnly = False)
    swanfleet.createExit("east", mistyMountainsSouth, outgoingOnly = False)
    mistyMountainsSouth.createExit("east", lorien, outgoingOnly = False)
    calenardhon.createExit("east", fangorn, outgoingOnly = False)
    fangorn.createExit("east", fieldOfCelebrant, outgoingOnly = False)
    fangorn.createExit("east", theWold, outgoingOnly = False)
    westfold.createExit("east", westemnet, outgoingOnly = False)
    westemnet.createExit("east", eastemnet, outgoingOnly = False)
    southernMirkwood.createExit("east", lorien, outgoingOnly = False)
    eastemnet.createExit("east", emynMuil, outgoingOnly = False)
    eastfold.createExit("east", nindalf, outgoingOnly = False)
    nindalf.createExit("east", deadMarshes, outgoingOnly = False)
    deadMarshes.createExit("east", udun, outgoingOnly = False)
    anorien.createExit("east", anduin, outgoingOnly = False)
    anduin.createExit("east", ephelDuath, outgoingOnly = False)
    lossamarch.createExit("east", ithilien, outgoingOnly = False)
    ephelDuath.createExit("east", plateauOfGorgoth, outgoingOnly = False)
    cirithUngol.createExit("east", plateauOfGorgoth, outgoingOnly = False)
    orodruin.createExit("east", plateauOfGorgoth, outgoingOnly = False)

    #Connections: North-South
    oldForest.createExit("south", barrowDowns, outgoingOnly = False)
    weatherHills.createExit("south", barrowDowns, outgoingOnly = False)
    trollshaws.createExit("south", bruinen, outgoingOnly = False)
    bruinen.createExit("south", mitheithel, outgoingOnly = False)
    highPass.createExit("south", mirkwood, outgoingOnly = False)
    mirkwood.createExit("south", southernMirkwood, outgoingOnly = False)
    southernMirkwood.createExit("south", emynMuil, outgoingOnly = False)
    mitheithel.createExit("south", swanfleet, outgoingOnly = False)
    swanfleet.createExit("south", dunland, outgoingOnly = False)
    dunland.createExit("south", calenardhon, outgoingOnly = False)
    lorien.createExit("south", fieldOfCelebrant, outgoingOnly = False)
    fieldOfCelebrant.createExit("south", theWold, outgoingOnly = False)
    calenardhon.createExit("south", westfold, outgoingOnly = False)
    fangorn.createExit("south", westemnet, outgoingOnly = False)
    theWold.createExit("south", eastemnet, outgoingOnly = False)
    westemnet.createExit("south", eastfold, outgoingOnly = False)
    eastemnet.createExit("south", nindalf, outgoingOnly = False)
    nindalf.createExit("south", cairAndros, outgoingOnly = False)
    emynMuil.createExit("south", deadMarshes, outgoingOnly = False)
    udun.createExit("south", plateauOfGorgoth, outgoingOnly = False)
    cairAndros.createExit("south", anduin, outgoingOnly = False)
    cirithUngol.createExit("south", ephelDuath, outgoingOnly = False)
    anorien.createExit("south", lossamarch, outgoingOnly = False)
    anduin.createExit("south", ithilien, outgoingOnly = False)
    
    spaces = [shire, oldForest, weatherHills, trollshaws, mistyMountainsNorth, highPass, mirkwood, 
    southernMirkwood, bruinen, mitheithel, swanfleet, dunland, mistyMountainsSouth, lorien, fangorn,
    fieldOfCelebrant, calenardhon, westfold, westemnet, eastemnet, emynMuil, eastfold, nindalf,
    deadMarshes, udun, cairAndros, orodruin, anorien, anduin, ephelDuath, cirithUngol, plateauOfGorgoth,
    lossamarch, ithilien]
    
    #Add low-level findable unique items to spaces
    for space in range(constants.SPACES_WITH_UNIQUE_ITEMS):
        if items.unique_items.lowLevelFindableUniques:
            #Determine which unique item
            item = random.choice(items.unique_items.lowLevelFindableUniques)
            items.unique_items.lowLevelFindableUniques.remove(item)
            #Determine which space
            space = random.choice(spaces)
            #Add item to space
            space.addItem(item)
    
    #Add miscellaneous unique items to spaces
    for space in range(len(items.unique_items.elvenRings)):
        if items.unique_items.elvenRings:
            #Determine which unique item
            item = random.choice(items.unique_items.elvenRings)
            items.unique_items.elvenRings.remove(item)
            #Determine which space
            space = random.choice(spaces)
            #Add item to space
            space.addItem(item)
    
    #TODO: return this to shire. For testing purposes
    return weatherHills
    
def getStartingInventory():
    """
    Generate's player's starting inventory.

    @return:   A list of the items.
    """
    startingInventory = items.unique_items.startingInventory
    
    return startingInventory

def getPlayer(world, startingInventory):
    """
    Create player and give player starting inventory and equipment.

    @return:     A fully-loaded player
    """
    player = Player("Russian", world)

    for item in startingInventory:
        player.addToInventory(item)
    for item in startingInventory:
        player.equip(item)
        
    return player
    
def getCommandList(player):
    """
    Generates the list of commands used in the game.

    @return:   The commandWords object, which stores the game's commands.
    """
    #Create commandWords object
    commandWords = CommandWords()
    
    #Commands
    helpCmd = HelpCommand("help", 
        "Provides help information for game.", commandWords)
    commandWords.addCommand("help", helpCmd)

    quitCmd = QuitCommand("quit", "Exits the game.")
    commandWords.addCommand("quit", quitCmd)
   
    dropCmd = DropCommand("drop", "Drops an item from inventory into local environment.", player)
    commandWords.addCommand("drop", dropCmd)

    enterCmd = EnterCommand("enter", "Allows player to enter a building.", player)
    commandWords.addCommand("enter", enterCmd)

    pickupCmd = PickUpCommand("pick up", "Picks up an item from a location and adds to inventory.", player)
    commandWords.addCommand("pick up", pickupCmd)

    equipCmd = EquipCommand("equip", "Equips item in inventory.", player)
    commandWords.addCommand("equip", equipCmd)

    unequipCmd = UnequipCommand("unequip", "Unequips item that is currently equipped.", player)
    commandWords.addCommand("unequip", unequipCmd)

    usePotionCmd = UsePotionCommand("use potion", "Uses potion in inventory.", player)
    commandWords.addCommand("use potion", usePotionCmd)

    checkInventoryCmd = CheckInventoryCommand("inventory", "Displays contents of inventory.", player)
    commandWords.addCommand("inventory", checkInventoryCmd)

    checkEquipmentCmd = CheckEquipmentCommand("equipment", "Displays current equipment and equipment stats.", player)
    commandWords.addCommand("equipment", checkEquipmentCmd)

    checkMoneyCmd = CheckMoneyCommand("money", "Displays player money", player)
    commandWords.addCommand("money", checkMoneyCmd)

    checkStatsCmd = CheckStatsCommand("stats", "Displays current character stats.", player)
    commandWords.addCommand("stats", checkStatsCmd)

    mapCmd = MapCommand("map", "Displays map of current location", player)
    commandWords.addCommand("map", mapCmd)

    northCmd = NorthCommand("north", 
                "Moves the player to the space north of current space", player)
    commandWords.addCommand("north", northCmd)
    
    southCmd = SouthCommand("south", 
                "Moves the player to the space south of current space", player)
    commandWords.addCommand("south", southCmd)
    
    eastCmd = EastCommand("east", 
                "Moves the player to the space east of current space", player)
    commandWords.addCommand("east", eastCmd)
    
    westCmd = WestCommand("west", 
                "Moves the player to the space west of current space", player)
    commandWords.addCommand("west", westCmd)
    
    descCmd = DescribeCommand("describe", "Gives description of current space", player)
    commandWords.addCommand("describe", descCmd)

    return commandWords
