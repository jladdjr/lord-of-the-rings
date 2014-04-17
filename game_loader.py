#!/usr/bin/python

from space import Space
from cities.city import City
from cities.inn import Inn
from cities.square import Square
from cities.shop import Shop
from player import Player
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
from commands.check_inventory_command import CheckInventoryCommand
from commands.check_equipment_command import CheckEquipmentCommand
from commands.check_money_command import CheckMoneyCommand
from commands.check_stats_command import CheckStatsCommand
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand
import constants

def getWorld():
    #Hobbiton - The Shire
    #Inn
    description = "A place for strangers"
    greeting = "Welcome to our inn! I'm Sally of the Tokinsville Baggins Clan"
    sallyInn = Inn("Sally's Inn", description, greeting, 2)
    #Shop
    description = "Exotic selection by hobbit standards"
    greeting = "We have strange wares"
    sallyShop = Shop("Sally's Shop", description, greeting, 4, 3)
    #Square
    description = "Lots of hobbits, mostly gossip"
    greeting = "Did you hear the latest news on Lobelia Baggins?"
    talk = {"Lobelia Baggins": "Get lost!", "Naftel Took": "News has broken out that Lobelia is making an inquiry on Bag End", "Amaranth Brandybuck": "Nice weather isn't it?", "Balbo Baggins": "The word on the street is that Lobelia is trying to acquire the Baggins estate!", "Ferdinand Took": "I wonder when Gandalf will visit?"}
    hobbitonSquare = Square("Hobbiton Square", description, greeting, talk)
    #City
    description = """Hobbiton is a village in the central regions of the
    Shire within the borders of the Westfarthing. Hobbiton is located
    on both sides of the Water approximately a mile northwest of the
    neighboring village of Bywater.
    """
    hobbiton = City("Hobbiton", description, "Did you hear the latest news?", [sallyInn, sallyShop, hobbitonSquare])
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
    shire = Space("Shire", description, city = hobbiton)

    #tomBombadil = Place
    #The Old Forest
    description = """
    The Old Forest is one of the few surviving primordial forests
    which covered most of Eriador before the Second Age. The Old Forest
    has been known to play tricks on travelers in response to its
    massive deforestation. 
    """
    oldForest = Space("Old Forest", description)

    #weathertop = Place
    #The Weather Hills
    description = """
    Weather Hills was the name among Men for the north-south range of hills
    that lay in central Eriador and in ancient times marked part of the
    border between the lands of Arthedain and Rhudaur. Weathertop, or
    Amon Sûl, lays at the southern end of this range.
    """
    weatherHills = Space("Weather Hills", description)

    #Trollshaws
    description = """
    Trollshaws are the upland woods that lay to the west of Rivendell and
    the Rivers Hoarwell and Loudwater. They were the haunt of Trolls, three
    of which waylaid Bilbo and his companions during the Quest of Erebor.
    """
    trollshaws = Space("Trollshaws", description)

    #Misty Mountains - Rivendell
    #Inn
    description = "A relaxing stay in the scenic Misty Mountains!"
    greeting = "Welcome to Misty Mountain Inn! Let us host you tonight..."
    mistyInn = Inn("Misty Mountain Inn", description, greeting, 5) 
    #Shop
    description = "New Elvenware! Look like your favorite elf!"
    greeting = "Welcome to ElvenWares! Here we have the latest in elven gadgetry"
    elvenWares = Shop("ElvenWares", description, greeting, 4, 6)
    #Square
    description = "Hotshots only"
    greeting = "We've been waiting for your arrival..."
    talk = {"Elrond": "Don't you think about marrying my daughter", "Legolas": "What do you think about my hair?", "Aragorn": "Check out these knife tricks!", "Gimli": "I bet I can eat more hotdogs than you", "Gandalf": "Did you know I have the Ring of Fire?"}
    councilOfElrond = Square("Council of Elrond", description, greeting, talk)
    #City
    description = """
    Rivendell, also known as Imladris, is an Elven outpost in Middle-earth.
    It is also referred to as "The Last Homely House East of the Sea", a
    reference to Valinor, which is west of the Great Sea in Aman.
    """
    greeting = "Welcome to Rivendell! Glad the Nazgul didn't get you."
    rivendell = City("Rivendell", description, greeting, [mistyInn, elvenWares, councilOfElrond])
    #Misty Mountains
    description = """The Misty Mountains or Mountains of Mist is a great
    mountain range that lies between Eriador in the west and the Great
    River Anduin in the east. It runs 795 miles (1,280 kilometers) from
    Mount Gundabad in the far north to Methedras in the south.
    """
    mistyMountains = Space("Misty Mountains", description, city = rivendell)

    #High Pass - GoblinTown
    description = """Goblin-town is a Goblin dwelling which lies
    under the High Pass in the Misty Mountains and is ruled by the Great
    Goblin. Gullum's cave is deep beneath Goblin-town and is connected
    to the Goblins' tunnels.
    """
    greeting = ""
    goblinTown = City("Goblin Town", description, greeting)
    #High Pass
    description = """The High Pass is a pass over the Misty Mountains.
    On its western end is the refuge of Rivendell and from there the
    Great East Road climbs into the mountains until it reaches Goblin-town.
    """
    highPass = Space("High Pass", description, city = goblinTown)

    #Mirkwood - Elvenking's Halls
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """The Elvenking's Halls is the cave system in northern
    Mirkwood in which King Thranduil and many of the Elves of Mirkwood
    live.
    """
    greeting = ""
    elvenkingsHalls = City("Elvenking's Halls", description, greeting)
    #Mirkwood
    description = """Mirkwood or the Forest of Great Fear is a great
    forest in Rhovanion. Mirkwood is once called Greenwood the Great
    and later became the Wood of Greenleaves."""
    mirkwood = Space("Mirkwood", description, city = elvenkingsHalls)

    #Barrow Downs - Bree
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """Bree was settled in the early Third Age, in the
    realm Cardolan. Though the Princes of Cardolan claimed it, Bree
    continued to thrive without any central authority or government
    for many centuries. 
    """
    greeting = "Nazgul have been visiting the area at night!"
    bree = City("Bree", description, greeting)
    #Barrow Downs
    description = """Barrow-downs or Tyrn Gorthad is a series of low
    hills east of the Shire, behind the Old Forest and west of the
    village of Bree. Many of the hills are crowned with megaliths
    and barrows, whence its name.
    """
    barrowDowns = Space("Barrow Downs", description, city = bree)

    #Bruinen
    description = """Bruinen or Loudwater is a river in eastern Eriador.
    It began with two tributaries flowing from the western slopes of the
    Misty Mountains.
    """
    bruinen = Space("Bruinen", description)

    #tharbad = Place
    #Mitheithel
    description = """Mitheithel is the long river that rises in a place
    in the icy north of Middle-earth known by Men as Hoarwell.
    """
    mitheithel = Space("Mitheithel", description)

    #ostInEdhil = Place
    #Swanfleet
    description = """The Swanfleet or Nin-in-Eilph is a marshy area in
    eastern Eriador where the lower reaches of the Glanduin flows
    before it joins Mitheithel. Swanfleet is an inland delta.
    """
    swanfleet = Space("Swanfleet", description)
    
    #Dunland
    description = """Dunland is the land of the Dunlendings. Dunland means
    Hill Land in the language of neighbouring Rohan, whose people named it
    after arriving in nearby Calenardhon in the later Third Age. It is a
    land of the wild men.
    """
    dunland = Space("Mitheithel", description)

    #chamberOfMazarbul = Place
    #Moria - The Seventh Level
    description = """The Seventh Level of Moria or Khazad-dum is a level of
    chambers, corridors and rooms, being six levels above the Great Gates.
    The term level or levels in the ancient Dwarven kingdom generally refer
    to the eastern area of Moria, nearest the eastern gate which was most
    populated when Khazad-dum was a mighty city of the Dwarves.
    """
    greeting = ""
    theSeventhLevel = City("The Seventh Level", description, greeting)
    #Moria
    description = """Khazad-dum, (also known as Moria, The Black Chasm,
    The Black Pit, Dwarrowdelf, Hadhodrond, Casarrondo, and and Phurunargian)
    is the grandest and most famous of the mansions of the Dwarves. There,
    for many thousands of years, a thriving Dwarvish community created the
    greatest city ever known.
    """
    moria = Space("Moria", description, city = theSeventhLevel)

    #Lorien - Caras Galadhon
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """Caras Galadhon is a city located in Lorien. Its inhabitants
    dwell in large flets in the trees, reached by white ladders. On the top
    of the hill in the greatest of trees, are the house of Celeborn and Galadriel.
    """
    greeting = ""
    lorein = City("Lorein", description, greeting)
    #Lorien
    description = """Lothlorien is a kingdom of Silvan Elves on the
    eastern side of the Hithaeglir. It is considered one of the most
    beautiful places in Middle-earth and has the only mallorn-trees
    east of the sea.
    """
    lorien = Space("Lorien", description, city = lorein)

    #entmoot = Place
    #Fangorn
    description = """Fangorn Forest is a deep, dark woodland that grew
    beneath the southern tips of the Misty Mountains under the eastern flanks
    of that range. It gains notoriety for its Ents. The forest, known as
    Entwood in Rohan, was named after the oldest Ent, Fangorn.
    """
    fangorn = Space("Fangorn", description)

    #The Wold
    description = """The Wold is the northernmost and least populated part
    of Rohan, lying between Fangorn Forest and the Anduin, bordered to the
    north by the Limlight.

    Its main inhabitants were nomadic Men of Rohan who use the land to graze
    cattle. In recent years, these men have fled in response to frequent
    attacks by orcish raiders.
    """
    theWold = Space("The Wold", description)

    #Field of Celebrant
    description = """The Field of Celebrant lies between the Rivers Anduin
    and Limlight and southeast of Lothlorien. In T.A. 2510, the decisive
    Battle of the Field of Celebrant at which Eorl the Young rode from
    the north to the aid of Gondor occurred.
    """
    fieldOfCelebrant = Space("Field of Celebrant", description)

    #Calendardhon - Isenguard
    description = """Isengard ("Iron Fortress" or Angrenost in Sindarin) is
    a great fortress located within a valley at the southern end of the Misty
    Mountains near the Gap of Rohan. In the centre of the Ring of Isengard
    stands the stone tower of Orthanc.
    """
    greetings = ""
    isenguard = City("Isenguard", description, greetings)
    #Calenardhon
    description = """Calenardhon contains Isengard, a great fortress located
    within a valley at the southern end of the Misty Mountains near the Gap
    of Rohan.
    """   
    calenardhon = Space("Calenardhon", description)

    #Westfold - Helm's Deep
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """Helm's Deep is a large valley gorge in northwestern
    Ered Nimrais below the Thrihyrne. It is the name of the whole
    defensive system including its major defensive structure, the Hornburg.
    """
    greeting = ""
    helmsDeep = City("Helm's Deep", description, greeting)
    #Westfold
    description = """The Westfold is the western part of Rohan, close to
    the White Mountains and situated between the river Isen and the Folde.
    The North-South Road runs through the Westfold from the Fords of Isen
    to Edoras. Its strongpoint is Helm's Deep.
    """
    westfold = Space("Westfold", description, city = helmsDeep)

    #Westemnet
    description = """The Eastemnet is part of Rohan. It is an area of
    wide, grassy plains found east of the river Entwash.
    """ 
    westemnet = Space("West Emmet", description)

    #Eastemnet
    description = """The Eastemnet is part of Rohan. It contains
    wide, grassy plains and is east of the river Entwash and west of
    the Great River, Anduin.
    """ 
    eastemnet = Space("East Emmet", description)

    #Emyn Muil
    description = """Emyn Muil is a range of hills south of the Brown
    Lands and north of the Nindalf. The Anduin cuts through the hills
    and then pools in Nen Hithoel.
    """ 
    emynMuil = Space("Emyn Muil", description)

    #Eastfold - Edoras
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """Rohan's first capital was at Aldburg in the Folde
    until Eorl the Young's son Brego built Edoras. It is Rohan's
    only real city and holds the Golden Hall of Meduseld.
    """
    greeting = ""
    edoras = City("Edoras", description, greeting)
    #Eastfold - Aldburg
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """Aldburg was built by Eorl in the region known as the Folde,
    east of Edoras. The Kings of Rohan moved to Edoras after Brego, son of Eorl,
    completed the Golden Hall, but many centuries later there were still nobles
    living at Aldburg, including Eomer, son of Eomund.
    """
    greeting = ""
    aldburg = City("Aldburg", description, greeting)
    #Eastfold
    description = """Eastfold is a part of the realm of Rohan. Bounded
    by the Mering Stream and Snowbourn River, it contains the city of
    Edoras.
    """
    eastfold = Space("Eastfold", description, city = edoras)

    #Nindalf
    description = """The swamps of Nindalf or Wetwang lie to the south of
    Emyn Muil and east of the Great River Anduin and are fed by the great
    inland delta of Entwash. The Dead Marshes lie further east and may
    be an extension of Nindalf.
    """ 
    nindalf = Space("Nimdalf", description)

    #Valley of Udun - Dead Marshes
    description = """The Black Gate of Mordor is a gate built by Sauron
    to prevent invasion through the Pass of Cirith Gorgor, the gap between
    the Ered Lithui and the Ephel Duath.
    """
    greetings = ""
    morannon = City("Morannon", description, greetings)
    #Dead Marshes
    description = """The Dead Marshes are an area of swampland east by the
    Dagorlad plain, site of the ancient Battle of Dagorlad during the Last
    Alliance of Elves and Men.
    """ 
    deadMarshes = Space("Dead Marshes", description, city = morannon)

    #Valley of Udun - Isenmouthe
    description = """Isenmouthe or Carach Angren is a pass in the
    northeastern part of Mordor and guards the southern end of the valley,
    Udun.
    
    The pass is heavily guarded with Fortresses and watchtowers.
    """
    greetings = ""
    isenmouthe = City("Isenmouthe", description, greeting)
    #Valley of Udun
    description = """Udun is a depressed valley in northwestern Mordor.
    It lies between Cirith Gorgor and the Isenmouthe and is traversed
    by large armies of Sauron in times of war.
    """
    udun = Space("Udun", description, city = isenmouthe)
    
    #Cair Andros
    description = """Cair Andros, meaning "Ship of the Long-Foam," is an
    island in the river Anduin, resting nearly forty miles to the north
    of Osgiliath.  It is of paramount importance to Gondor because it
    prevents the enemy from crossing the river and entering into Anorien.
    """ 
    cairAndros = Space("Cair Andros", description, greeting)

    #Orodruin
    description = """Mount Doom, also known as Orodruin and Amon Amarth, is
    the volcano in Mordor where the One Ring was forged. It is the only place
    that the One Ring may be destroyed.
    """
    orodruin = Space("orodruin", description)

    #Anorien - Minas Tirith
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """Minas Tirith is a city of Gondor originally called Minas Anor.
    From T.A. 1640 onwards it became the capital of the South-kingdom and the seat of
    its Kings and ruling Stewards.
    """
    greeting = ""
    minasTirith = City("Minas Tirith", description, greeting)
    #Anorien
    description = """Anorien is the fiefdom of Gondor containing Minas Tirith, the
    capital of Gondor. Originally known as Minas Anor, it replaced the Osgiliath
    as capital of Gondor as Osgiliath was overun.
    """ 
    anorien = Space("Anorien", description, city = minasTirith)

    #argonath = Place
    #Anduin - Osgiliath
    """
    #Inn
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """Osgiliath was the ancient capital of the Kingdom of Gondor.
    Depopulated during the Third Age, it gradually fell into ruin. Osgiliath has
    strategic importance as a crossing point over the Anduin.
    """
    greeting = ""
    osgiliath = City("Osgiliath", description, greeting)
    #Anduin
    description = """Anduin is a river that crosses most of Middle-earth east
    of the Misty Mountains. Passing through many lands, it has many names:
    Langflood by the ancestors of the Rohirrim, the Great River of Wilderland in
    the Westron of Rivendell and the Shire, and simply the Great River in Gondor.
    """
    anduin = Space("Anduin", description, city = osgiliath)

    #Ephel Duath - Minas Morgul
    #City
    description = """Minas Morgul is a city-fortress in Mordor. Originally created
    as a Gondorian outpost and the sister city to Minas Anor, Minas Ithil safeguarded
    the eastern borders of the Kingdom of Gondor and the capital Osgiliath from
    the forces of Mordor during the early part of the Third Age.

    Minas Morgul is now home to the Nazgul and Cirith Ungol, a secret pass into
    Mordor.
    """
    greeting = ""
    minasMorgul = City("Minas Morgul", description, greeting)
    #Ephel Duath
    description = """The Ephel Dúath, or the Mountains of Shadow, are a range of
    mountains that guard Mordor's western and southern borders.
    """
    ephelDuath = Space("Ephel Duath", description, city = minasMorgul)

    #Cirith Ungol - Tower of Cirith Ungol
    description = """Gondor occupied the fortress until T.A. 1636 when the
    Great Plague killed large parts of Gondor's population. After the plague,
    Gondor never again manned the Tower of Cirith Ungol and evil was allowed
    to return to Mordor. Similar fates suffered the mountain fortress of Durthang
    in northwestern Mordor and the Towers of the Teeth at the Morannon.
    """
    greeting = ""
    towerOfCirithUngol = City("Tower of Cirith Ungol", description, greeting)
    #Cirith Ungol
    description = """Cirith Ungol is the pass through the western mountains of
    Mordor and the only way towards the land from the west. It is guarded by the
    Tower of Cirith Ungol, built by the Men of Gondor after the War of the Last
    Alliance of Elves and Men.
    """
    cirithUngol = Space("Cirith Ungol", description, city = towerOfCirithUngol)

    #Barad Dur
    description = """Barad-dur is the Dark Lord Sauron's sanctuary fortress
    in Mordor and serves as his base of operations. Over 1400 meters high
    and held together by dark magic, it is the largest fortress in
    Middle-earth.
    """
    greeting = ""
    baradDur = City("Barad Dur", description, greeting)
    #Plateau of Gorgoth
    description = """Plateau of Gorgoroth is a region in the northwestern region of
    Mordor. Gorgoroth is the location of the mines and forges which supplied Mordor's
    armies with weapons and armor.
    """
    plateauOfGorgoth = Space("Plateau of Gorgoth", description, city = baradDur)

    #Lossamarch - Pelargir
    #Inn
    """
    description = ""
    greeting = ""
     = Inn("", description, greeting, 5)
    #Shop
    description = ""
    greeting = ""
     = Shop("", description, greeting, 5, 4)
    #Square
    description = ""
    greeting = ""
    talk = {}
     = Square("", description, greeting, talk)
    """
    #City
    description = """One of the oldest cities in Middle Earth, Pelargir served
    as chief haven of the faithful as Numenorians migrated to Middle Earth to
    escape persecution. In later years, Pelargir served as chief port of Gondor.
    """
    greeting = ""
    pelargir = City("Pelargir", description, greeting)
    #Lossamarch
    description = """Lossarnach is a region and fiefdom in Southern Gondor. Known
    as the Vale of flowers, it is a fertile region lying south of the White Mountains.
    """ 
    lossamarch = Space("Lossamarch", description, city = pelargir)

    #Ithilien
    description = """Ithilien was the region and fiefdom of Gondor bordering Mordor.
    """ 
    ithilien = Space("Ithilien", description)

    #Connections: East-West
    shire.createExit("east", oldForest, outgoingOnly = False)
    oldForest.createExit("east", weatherHills, outgoingOnly = False)
    weatherHills.createExit("east", trollshaws, outgoingOnly = False)
    trollshaws.createExit("east", mistyMountains, outgoingOnly = False)
    mistyMountains.createExit("east", highPass, outgoingOnly = False)
    barrowDowns.createExit("east", bruinen, outgoingOnly = False)
    swanfleet.createExit("east", moria, outgoingOnly = False)
    moria.createExit("east", lorien, outgoingOnly = False)
    calenardhon.createExit("east", fangorn, outgoingOnly = False)
    fangorn.createExit("east", fieldOfCelebrant, outgoingOnly = False)
    fangorn.createExit("east", theWold, outgoingOnly = False)
    westfold.createExit("east", westemnet, outgoingOnly = False)
    westemnet.createExit("east", eastemnet, outgoingOnly = False)
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
    mitheithel.createExit("south", swanfleet, outgoingOnly = False)
    swanfleet.createExit("south", dunland, outgoingOnly = False)
    dunland.createExit("south", calenardhon, outgoingOnly = False)
    mirkwood.createExit("south", lorien, outgoingOnly = False)
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
    
    return shire
    
def getStartingInventory():
    """
    Generate's player's starting inventory.

    @return:   A list of the items.
    """
    weapon = Weapon("Rock", "Really heavy", 2, 1000, 1)
    armor = Armor("Leather Tunic", "Travel cloak", 3, 1, 1)
    potion = Potion("Vodka", "Good for health", 1, 1, 1)

    startingInventory = [weapon, armor, potion]
    
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

    checkInventoryCmd = CheckInventoryCommand("inventory", "Displays contents of inventory.", player)
    commandWords.addCommand("inventory", checkInventoryCmd)

    checkEquipmentCmd = CheckEquipmentCommand("equipment", "Displays current equipment and equipment stats.", player)
    commandWords.addCommand("equipment", checkEquipmentCmd)

    checkMoneyCmd = CheckMoneyCommand("money", "Displays player money", player)
    commandWords.addCommand("money", checkMoneyCmd)

    checkStatsCmd = CheckStatsCommand("stats", "Displays current character stats.", player)
    commandWords.addCommand("stats", checkStatsCmd)

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
