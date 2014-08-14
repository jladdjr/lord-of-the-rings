#!/usr/bin/python

from monsters.barrow_wight import BarrowWight
from monsters.goblin import Goblin
from monsters.great_goblin import GreatGoblin
from monsters.king_of_the_barrows import KingOfTheBarrows
from monsters.nazgul import Nazgul
from monsters.nazgul_ii import Nazgul_II
from monsters.nazgul_iii import Nazgul_III
from monsters.troll import Troll
from monsters.warg_rider import WargRider
from monsters.uruk_hai import UrukHai
from monsters.uruk_hai_archer import UrukHaiArcher
from monsters.elite_uruk_hai import EliteUrukHai
from monsters.dunlending import Dunlending
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.siege_works import SiegeWorks
from monsters.dragon_of_mordor import DragonOfMordor
from monsters.corsair_of_umbar import CorsairOfUmbar
from monsters.armored_mumakil import ArmoredMumakil
from monsters.black_numernorian import BlackNumernorian
from monsters.easterling_warrior import EasterlingWarrior
from monsters.sauroman import Sauroman
from monsters.mouth_of_sauron import MouthOfSauron
from monsters.witch_king import WitchKing
from monsters.shelob import Shelob
from monsters.balrog import Balrog
from monsters.orc_ii import Orc_II
from monsters.orc_archer_ii import OrcArcher_II
from monsters.troll_ii import Troll_II
from monsters.black_numernorian_ii import BlackNumernorian_II

"""
Constants used in Lord of the Rings.
"""
#Game constants
COMMAND_PROMPT           = "> "
CURRENCY                 = "rubles"
SPACES_WITH_UNIQUE_ITEMS = 4
ELVEN_RING_PROB          = .3

#Player initialization
class PlayerInitialization(object):
    """
    Constants used in player initialization.
    """
    EXPERIENCE    = 0
    LEVEL         = 1
    MONEY         = 20
    MAX_HP        = 20
    ATTACK        = 5
    WEIGHT_LIMIT  = 15
    WEAPON_ATTACK = 0
    ARMOR_DEFENSE = 0
    CHARM_ATTACK  = 0
    CHARM_DEFENSE = 0
    CHARM_HP      = 0

#Character stats constants
HP_STAT           = 1.2
ATTACK_STAT       = 1.2
MAX_LEVEL         = 20
WEIGHT_LIMIT_STAT = 1.15

#Player levels
"""
Keys are player levels; values are the experience required to obtain its paired
level.
"""
LEVEL_EXP_REQUIREMENT = {1: 0, 2: 20, 3: 44, 4: 72, 5: 105, 6: 144, 7: 190, 
8: 245, 9: 311, 10: 390, 11: 484, 12: 596, 13: 730, 14:890 , 15: 1082, 
16: 1312, 17: 1588, 18: 1919, 19: 2316, 20: 2792}

#Item stat constants 
SELL_LOSS_PERCENTAGE = .5
WEAPON_COST          = 1
ARMOR_COST           = 2

#Item type enumeration
class ItemType(object):
    """
    Enumerated typing for items. 
    """
    GENERIC = 1
    ARMOR   = 2
    WEAPON  = 3
    POTION  = 4
    CHARM   = 5

#Direction enumeration
class Direction(object):
    """
    The cardinal directions.
    """
    NORTH = 'north'
    SOUTH = 'south'
    EAST  = 'east'
    WEST  = 'west'

#Region type enumeration
class RegionType(object):
    """
    The region types in Middle Earth.
    """
    ERIADOR       = 1
    BARROW_DOWNS  = 2
    HIGH_PASS     = 3
    ENEDWAITH     = 4
    MORIA         = 5
    RHOVANION     = 6
    ROHAN         = 7
    GONDOR        = 8
    MORDOR        = 8

#Region base spawn
class RegionBaseSpawn(object):
    """
    Regional base spawn per random battle for space in region.
    """
    ERIADOR       = 1
    BARROW_DOWNS  = 4
    HIGH_PASS     = 0
    ENEDWAITH     = 6
    MORIA         = 5
    RHOVANION     = 6
    ROHAN         = 6
    GONDOR        = 8
    MORDOR        = 8

#Space spawn probability
class SpaceSpawnProb(object):
    """
    Used to store space spawn probabilities.
    """
    shire               = 0
    oldForest           = .7
    weatherHills        = .75
    trollshaws          = .85
    mistyMountainsNorth = .85
    highPass            = 0
    mirkwood            = .4
    southernMirkwood    = .9
    barrowDowns         = .85
    bruinen             = .75
    mitheithel          = .75
    swanfleet           = .75
    dunland             = .85
    mistyMountainsSouth = 0
    lorien              = .4
    fangorn             = .4
    theWold             = .4
    fieldOfCelebrant    = .25
    calenardhon         = .95
    westfold            = .85
    westemnet           = .8
    eastemnet           = .6
    emynMuil            = .4
    eastfold            = .5
    nindalf             = .8
    deadMarshes         = .5
    udun                = .95
    cairAndros          = .8
    orodruin            = .95
    anorien             = .75
    anduin              = .85
    ephelDuath          = .9
    cirithUngol         = .9
    plateauOfGorgoth    = .95
    lossamarch          = .6
    ithilien            = .85

#Space bonusDifficulty
class SpaceBonusDiff(object):
    """
    Used to store space bonus difficulty probabilities.
    """
    shire               = 0
    oldForest           = 0
    weatherHills        = 0
    trollshaws          = .2
    mistyMountainsNorth = 0
    highPass            = 0
    mirkwood            = 0
    southernMirkwood    = .2
    barrowDowns         = 0
    bruinen             = 0
    mitheithel          = .2
    swanfleet           = .2
    dunland             = 0
    mistyMountainsSouth = 0
    lorien              = 0
    fangorn             = 0
    theWold             = -.3
    fieldOfCelebrant    = -.3
    calenardhon         = .5
    westfold            = .3
    westemnet           = .15
    eastemnet           = 0
    emynMuil            = -.2
    eastfold            = 0
    nindalf             = -.2
    deadMarshes         = .2
    udun                = .3
    cairAndros          = .2
    orodruin            = .3
    anorien             = .3
    anduin              = 0
    ephelDuath          = .2
    cirithUngol         = .2
    plateauOfGorgoth    = .2
    lossamarch          = 0
    ithilien            = .2

#Monster names
class MonsterNames(object):
    """
    Contains the names of the monsters in LotR.
    """
    BarrowWight         = "Barrow Wight"
    Goblin              = "Goblin"
    GreatGoblin         = "Great Goblin"
    KingOfTheBarrows    = "King of the Barrows"
    Nazgul              = "Nazgul"
    Nazgul_II           = "Nazgul II"
    Nazgul_III          = "Nazgul III"
    Troll               = "Troll"
    WargRider           = "Warg Rider"
    UrukHai             = "Uruk Hai"
    UrukHaiArcher       = "Uruk Hai Archer"
    EliteUrukHai        = "Elite Uruk Hai"
    Dunlending          = "Dunlending"
    Orc                 = "Orc"
    OrcArcher           = "Orcish Archer"
    SiegeWorks          = "Siege Works"
    DragonOfMordor      = "Dragon of Mordor"
    CorsairOfUmbar      = "Corsair of Umbar"
    ArmoredMumakil      = "Armored Mumakil"
    BlackNumernorian    = "Black Numernorian"
    EasterlingWarrior   = "Easterling Warrior"
    Sauroman            = "Sauroman of Many Colors"
    MouthOfSauron       = "Mouth Of Sauron"
    WitchKing           = "Witch King"
    Shelob              = "Shelob"
    Balrog              = "Balrog"
    Orc_II              = "Orc II"
    OrcArcher_II        = "Orc Archer II"
    Troll_II            = "Troll II"
    BlackNumernorian_II = "Black Numernorian II"
    
#Monster descriptions
class MonsterDescriptions(object):
    """
    Contains the descriptions of the monsters in LotR.
    """
    BarrowWight         = "A sad soul left haunting the Downs."
    Goblin              = "\"Give me all of your stuff!\""
    GreatGoblin         = "\"Give me ALL of your stuff!\""
    KingOfTheBarrows    = "An intense, evil spirit."
    Nazgul              = "\"AAAAEEEEEEEEEEE!!!\""
    Nazgul_II           = "Nazgul's older brother."
    Nazgul_III          = "Now with dragon mount!"
    Troll               = "\"Merrily I troll along.\""
    WargRider           = "Likes riding... wargs."
    UrukHai             = "\"You even lift bro?\""
    UrukHaiArcher       = "Lifts over long distances."
    EliteUrukHai        = "Bench press champion."
    Dunlending          = "The original people of Middle Earth."
    Orc                 = "Not very nice."
    OrcArcher           = "A total j@ck@$$."
    SiegeWorks          = "Completely useless in this situation."
    DragonOfMordor      = "Distant cousin of Dragonite."
    CorsairOfUmbar      = "Basically, pirates."
    ArmoredMumakil      = "Armored elephants mounted with archers."
    BlackNumernorian    = "Extremely powerful sorcerers."
    EasterlingWarrior   = "From China."
    Sauroman            = "Head of the White Council."
    MouthOfSauron       = "Chief Emissary of Sauron."
    WitchKing           = "Sauron's second in command."
    Shelob              = "Last Child of Ungoliant"
    Balrog              = "Durin's Bane"
    Orc_II              = "Orc's older brother."
    OrcArcher_II        = "Orc archer's older brother."
    Troll_II            = "Troll's older brother."
    BlackNumernorian_II = "Black numernorian's older brother."    
    
#Monster attack strings
class MonsterAttackStrings(object):
    """
    Contains the attack strings of the monsters in LotR. For instance,
    "Goblin *sliced and diced* %s for %s damage!"
    """
    BarrowWight         = "sang a sad song"
    Goblin              = "slice and diced"
    GreatGoblin         = "slice and diced"
    KingOfTheBarrows    = "sang a symphony of sadness"
    Nazgul              = "slashed you with a Morgul knife"
    Nazgul_II           = "slashed you with Scythe of Sorrow"
    Nazgul_III          = "fire-breathing dragoned you"
    Troll               = "slamed you with fists of malice"
    WargRider           = "trampled around"
    UrukHai             = "tried to out lift you"
    UrukHaiArcher       = "tried to out lift you"
    EliteUrukHai        = "tried to out lift you"
    Dunlending          = "hacked and slashed"
    Orc                 = "hacked"
    OrcArcher           = "shot fiery darts"
    SiegeWorks          = "did nothing"
    DragonOfMordor      = "used hyperbeam"
    CorsairOfUmbar      = "slashed"
    ArmoredMumakil      = "got pissed and started trampling around"
    BlackNumernorian    = "summon spiritual darkness"
    EasterlingWarrior   = "tried to avenge his ancestors"
    Sauroman            = "cast elemental spells"
    MouthOfSauron       = "slashed you with an enchanted blade"
    WitchKing           = "performed black magic"
    Shelob              = "stung you"
    Balrog              = "scourged you with whips of fire"
    Orc_II              = "hacked"
    OrcArcher_II        = "shot fiery darts"
    Troll_II            = "slamed you with fists of malice"
    BlackNumernorian_II = "summon spiritual darkness"
    
class MonsterDeathStrings(object):
    """
    Contains the death strings of the monsters in LotR. These strings
    are displayed as player kills monster.
    """
    BarrowWight         = "\"Good. I am going back to sleep now.\""
    Goblin              = "\"I'm going back home now.\""
    GreatGoblin         = "\"I'm going back home now too.\""
    KingOfTheBarrows    = "\"I am going back to sleep now.\""
    Nazgul              = "\"AAAAEEEEEEEEEEE!!!\""
    Nazgul_II           = "\"...AAAAEEEEEEEEEEE!!!\""
    Nazgul_III          = "\"....\""
    Troll               = "\"Merrily I troll away.\""
    WargRider           = "[Whimpers] ...My warg...."
    UrukHai             = "Well, back to the gym I guess...."
    UrukHaiArcher       = "Leg lifts and suicides here I come...."
    EliteUrukHai        = "[Walks back to the locker room depressed.]"
    Dunlending          = "\"Why the heck am I even here?\""
    Orc                 = "Orc was cut in two!"
    OrcArcher           = "Orcish Archer was slain!"
    SiegeWorks          = "...."
    DragonOfMordor      = "Dragon of Mordor was knocked out!"
    CorsairOfUmbar      = "Corsair of Umbar went back home."
    ArmoredMumakil      = "Armored Mumakil is going home to Africa now."
    BlackNumernorian    = "[Black Numernorian returned to the shadows.]"
    EasterlingWarrior   = "Easterling Warrior went back to China."
    Sauroman            = "\"Wizards reincarnate you know....\""
    MouthOfSauron       = "\"Rides off to fight another day.\""
    WitchKing           = "\"Hmm....\""
    Shelob              = "[Shelob retreats into the shadows.]"
    Balrog              = "[The Balrog retreats into the shadows.']"
    Orc_II              = "Orc was cut in two!"
    OrcArcher_II        = "Orcish Archer was slain!"
    Troll_II            = "\"Merrily I troll away.\""
    BlackNumernorian_II = "[Black Numernorian returned to the shadows.]"
    
#Region monster distribution
"""
A dictionary of dictionaries where the higher-level keys are regions. 
The inner set contains the monster class-probability pairs that are 
used as probability distribution functions for monster spawn.

monster_factory's getMonsters() generates a random number between [0, 1). If 
the randomly generated number falls within the range of each class, a monster 
of that class is spawned.
"""
REGIONAL_MONSTER_DISTRIBUTION = {
    RegionType.ERIADOR:      {Nazgul: [0, 1]},
    RegionType.BARROW_DOWNS: {BarrowWight: [0, .9], 
                              KingOfTheBarrows: [.9, 1]},
    RegionType.HIGH_PASS:    {Goblin: [0, 1]},
    RegionType.ENEDWAITH:    {WargRider: [0, .3], 
                              Dunlending: [.3, .6], 
                              UrukHai: [.6, .8], 
                              UrukHaiArcher: [.8, .9], 
                              EliteUrukHai: [.9, 1]},
     RegionType.MORIA:       {Orc: [0, .7], 
                              OrcArcher: [.7, .925], 
                              Troll: [.925, .98], 
                              Balrog: [.98, 1]},
     RegionType.RHOVANION:   {Orc: [0, .5], 
                              OrcArcher: [.5, .7], 
                              Nazgul_II: [.7, .85], 
                              BlackNumernorian: [.85, 1]},
     RegionType.ROHAN:       {UrukHai: [0, .5], 
                              UrukHaiArcher: [.5, .7], 
                              EliteUrukHai: [.7, .8], 
                              WargRider: [.8, 1]},
     RegionType.GONDOR:      {Orc: [0, .45], 
                              OrcArcher: [.5, .6],
                              EasterlingWarrior: [.6, .65],
                              Troll: [.65, .75], 
                              Nazgul_II: [.75, .775], 
                              DragonOfMordor: [.775, .8], 
                              CorsairOfUmbar: [.8, .85], 
                              ArmoredMumakil: [.85, .9], 
                              SiegeWorks: [.9, .95], 
                              BlackNumernorian: [.95, 1]},
     RegionType.MORDOR:      {Orc_II: [0, .5], 
                              OrcArcher_II: [.5, .65], 
                              Troll_II: [.65, .75], 
                              Nazgul_III: [.75, .85], 
                              DragonOfMordor: [.85, .9], 
                              BlackNumernorian_II: [.9, .95], 
                              SiegeWorks: [.95, 1]}
     }

#Monster base stats
"""
Monster base stats are the only paramater used in monster creation.
Stats are a 3-element list whose elements are: hp, attack, and
experience (in that order).
"""
MONSTER_STATS = {BarrowWight:          [18, 2, 6],
                 Goblin:               [28, 5, 12],
                 GreatGoblin:          [72, 8, 42],
                 KingOfTheBarrows:     [72, 4, 32],
                 Nazgul:               [44, 3, 12],
                 Nazgul_II:            [82, 10, 52],
                 Nazgul_III:           [240, 48, 120],
                 Troll:                [86, 8, 36],
                 WargRider:            [32, 5, 14],
                 UrukHai:              [54, 5, 18],
                 UrukHaiArcher:        [32, 6, 16],
                 EliteUrukHai:         [72, 8, 28],
                 Dunlending:           [26, 5, 12],
                 Orc:                  [26, 5, 12],
                 OrcArcher:            [22, 7, 16],
                 SiegeWorks:           [220, 0, 52],
                 DragonOfMordor:       [300, 67, 176],
                 CorsairOfUmbar:       [76, 12, 48],
                 ArmoredMumakil:       [264, 42, 96],
                 BlackNumernorian:     [66, 12, 48],
                 EasterlingWarrior:    [74, 8, 30],
                 Sauroman:             [342, 52, 170],
                 MouthOfSauron:        [480, 72, 250],
                 WitchKing:            [600, 84, 320],
                 Shelob:               [450, 70, 140],
                 Balrog:               [1840, 162, 860],
                 Orc_II:               [72, 10, 35],
                 OrcArcher_II:         [66, 12, 40],
                 Troll_II:             [166, 16, 80],
                 BlackNumernorian_II:  [152, 24, 92]}
    
#Battle engine context
class BattleEngineContext(object):
    """
    Constants used for BattleEngine mode determination.
    """
    RANDOM = 1
    STORY  = 2

#Battle engine     
class ItemFind(object):
    """
    Constants used for determining whether player has found items as a result 
    of battle.
    """
    lowLevel   = [100, 5000, 300]
    highLevel  = [350, 5000, 600]
    eliteLevel = [500, 5000, 1000]
    
#Battle engine constants
class BattleEngine(object):
    """
    Constants for battle engine.
    """
    RUN_PROBABILITY_SUCCESS = 1
    STANDARD_DEVIATION      = 3
    MONEY_CONSTANT          = 3

#Shop factory probability constants
class ShopFactoryConstants(object):
    """
    Constants used in shop factory item type generation.
    """
    WEAPON_UPPER_LIMIT = .25
    ARMOR_UPPER_LIMIT  = .5
    POTION_UPPER_LIMIT = .975
    STANDARD_DEVIATION = 2.5
    QUALITY_MINIMUM    = 0
    QUALITY_MAXIMUM    = 20
    UNIQUE_QUALITY_REQ = 10

#Unique Place constants
"""
Constants used for unique places.
"""
WEATHERTOP_BATTLE_PROB = .5
WEATHERTOP_WITCH_KING_PROB = .125
THARBAD_BATTLE_PROB = .2
THARBAD_ITEM_FIND_PROB = .5
ARGONATH_EXP_INCREASE = .1
DERINGLE_EXP_INCREASE = .05
GOBLIN_TOWN_EVASION_PROB = .4
DOL_GULDUR_WITCH_KING_PROB = .125
CIRITH_UNGOL_EVASION_PROB = .4
CIRITH_UNGOL_SHELOB_PROB = .4
MORIA_ITEM_FIND_PROB = .3
MORIA_LOW_RISK_UPPER_LIMIT = 1
MORIA_MED_RISK_UPPER_LIMIT = 3
MORIA_LOW_RISK_SNEAK_UPPER_LIMIT = .65
MORIA_LOW_RISK_NEUTRAL_UPPER_LIMIT = .9
MORIA_MED_RISK_SNEAK_UPPER_LIMIT = .3
MORIA_MED_RISK_NEUTRAL_UPPER_LIMIT = .7
MORIA_HIGH_RISK_NEUTRAL_UPPER_LIMIT = .2