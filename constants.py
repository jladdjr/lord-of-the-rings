#!/usr/bin/python

from monsters.barrow_wight import BarrowWight
from monsters.goblin import Goblin
from monsters.great_goblin import GreatGoblin
from monsters.king_of_the_barrows import KingOfTheBarrows
from monsters.nazgul import Nazgul
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

"""
Constants for Lord of the Rings.
"""

#Game constants
COMMAND_PROMPT = "> "
CURRENCY = "rubles"

#Character initialization
STARTING_EXPERIENCE = 0
STARTING_EQUIPMENT = []
STARTING_LEVEL = 1
STARTING_MONEY = 20
STARTING_WEAPON_ATTACK = 0
STARTING_ARMOR_DEFENSE = 0

#Character stats constants
HP_STAT = 20
ATTACK_STAT = 2
MAX_LEVEL = 20

#Item stat constants 
SELL_LOSS_PERCENTAGE = .5
WEAPON_COST = 1
ARMOR_COST = 2

#Item type enumeration
class ItemType(object):
    """
    When a new item is created, its type should
    be added here. (e.g. POTION = 1, WEAPON = 2, ARMOR = 3, etc.)
    """
    GENERIC = 1
    ARMOR   = 2
    WEAPON  = 3
    POTION  = 4

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
    MORDOR        = 9

#Region base spawn
class RegionBaseSpawn(object):
    """
    Regional base spawn per random battle for space in region.
    """
    ERIADOR       = 1
    BARROW_DOWNS  = 2
    HIGH_PASS     = 3
    ENEDWAITH     = 4
    MORIA         = 5
    RHOVANION     = 6
    ROHAN         = 7
    GONDOR        = 8
    MORDOR        = 9

#Monster names
class MonsterNames(object):
    """
    Names of monsters.
    """
    BarrowWight = "Barrow Wight"
    Goblin = "Goblin"
    GreatGoblin = "Great Goblin"
    KingOfTheBarrows = "King of the Barrows"
    Nazgul = "Nazgul"
    Troll = "Troll"
    WargRider = "Warg Rider"
    UrukHai = "Uruk Hai"
    UrukHaiArcher = "Uruk Hai Archer"
    EliteUrukHai = "Elite Uruk Hai"
    Dunlending = "Dunlending"
    Orc = "Orc"
    OrcArcher = "Orcish Archer"
    SiegeWorks = "Siege Works"
    DragonOfMordor = "Dragon of Mordor"
    CorsairOfUmbar = "Corsair of Umbar"
    ArmoredMumakil = "Armored Mumakil"
    BlackNumernorian = "Black Numernorian"
    EasterlingWarrior = "Easterling Warrior"
    Sauroman = "Sauroman of Many Colors"
    MouthOfSauron = "Mouth Of Sauron"
    WitchKing = "Witch King"
    Shelob = "Shelob"
    Balrog = "Balrog"
    
#Monster descriptions
class MonsterDescriptions(object):
    """
    Descriptions of monsters.
    """
    BarrowWight = "A sad soul left haunting the Downs."
    Goblin = "\"Give me all of your stuff!\""
    GreatGoblin = "\"Give me ALL of your stuff!\""
    KingOfTheBarrows = "An intense, evil spirit."
    Nazgul = "\"AAAAEEEEEEEEEEE!!!\""
    Troll = "\"Merrily I troll along.\""
    WargRider = "Likes riding... wargs."
    UrukHai = "\"You even lift bro?\""
    UrukHaiArcher = "Lifts over long distances."
    EliteUrukHai = "Bench press champion."
    Dunlending = "The original people of Middle Earth."
    Orc = "Not very nice."
    OrcArcher = "A total j@ck@$$."
    SiegeWorks = "Completely useless in this situation."
    DragonOfMordor = "Distant cousin of Dragonite."
    CorsairOfUmbar = "Basically, pirates."
    ArmoredMumakil = "Armored elephants mounted with archers."
    BlackNumernorian = "Extremely powerful sorcerers."
    EasterlingWarrior = "From China."
    Sauroman = "Head of the White Council."
    MouthOfSauron = "Chief Emissary of Sauron."
    WitchKing = "Sauron's second in command."
    Shelob = "Last Child of Ungoliant"
    Balrog = "Durin's Bane"
    
#Monster attack strings
class MonsterAttackStrings(object):
    """
    Attack strings for monsters.
    """
    BarrowWight = "sang a sad song"
    Goblin = "slice and diced"
    GreatGoblin = "slice and diced"
    KingOfTheBarrows = "sang a symphony of sadness"
    Nazgul = "slashed you with a Morgul knife"
    Troll = "slamed you with fists of malice"
    WargRider = "trampled around"
    UrukHai = "tried to out lift you"
    UrukHaiArcher = "tried to out lift you"
    EliteUrukHai = "tried to out lift you"
    Dunlending = "hacked and slashed"
    Orc = "hacked"
    OrcArcher = "shot fiery darts"
    SiegeWorks = "did nothing"
    DragonOfMordor = "used hyperbeam"
    CorsairOfUmbar = "slashed"
    ArmoredMumakil = "got pissed and started trampling around"
    BlackNumernorian = "summon spiritual darkness"
    EasterlingWarrior = "tried to avenge his ancestors"
    Sauroman = "cast elemental spells"
    MouthOfSauron = "slashed you with an enchanted blade"
    WitchKing = "performed black magic"
    Shelob = "stung you"
    Balrog = "scourged you with whips of fire"
    
class MonsterDeathStrings(object):
    """
    Death strings for monsters.
    """
    BarrowWight = "\"Good. I am going back to sleep now.\""
    Goblin = "\"I'm going back home now.\""
    GreatGoblin = "\"I'm going back home now too.\""
    KingOfTheBarrows = "\"I am going back to sleep now.\""
    Nazgul = "\"AAAAEEEEEEEEEEE!!!\""
    Troll = "\"Merrily I troll away.\""
    WargRider = "[Whimpers] ...My warg...."
    UrukHai = "Well, back to the gym I guess...."
    UrukHaiArcher = "Leg lifts and suicides here I come...."
    EliteUrukHai = "[Walks back to the locker room depressed.]"
    Dunlending = "\"Why the heck am I even here?\""
    Orc = "Orc was cut in two!"
    OrcArcher = "Orcish Archer was slain!"
    SiegeWorks = "...."
    DragonOfMordor = "Dragon of Mordor was knocked out!"
    CorsairOfUmbar = "Corsair of Umbar went back home."
    ArmoredMumakil = "Armored Mumakil is going home to Africa now."
    BlackNumernorian = "[Black Numernorian returned to the shadows.]"
    EasterlingWarrior = "Easterling Warrior went back to China."
    Sauroman = "Sauroman the Great Wizard was slain!"
    MouthOfSauron = "\"Rides off to fight another day.\""
    WitchKing = "\"Hmm....\""
    Shelob = "[Shelob retreats into the shadows.]"
    Balrog = "[The Balrog retreats into the shadows.']"
    
#Region monster distribution
"""
A dictionary of dictionaries where the higher-level pairs are region-distribution pairs.
The inner set contains the class-probability pairs that are used as probability
distribution functions for monster spawn.

monster_factory's getMonsters() generates a random number between [0, 1). If the
randomly generated number falls within the range of each class, a monster of that class
is spawned.
"""
REGIONAL_MONSTER_DISTRIBUTION = {RegionType.ERIADOR : {Nazgul: [0, 1]},
                                 RegionType.BARROW_DOWNS : {BarrowWight: [0, .85], KingOfTheBarrows: [.85, 1]},
                                 RegionType.HIGH_PASS : {Goblin: [0, 1]},
                                 RegionType.ENEDWAITH : {WargRider: [0, .3], Dunlending: [.3, .6], UrukHai: [.6, .8], UrukHaiArcher: [.8, .9], EliteUrukHai: [.9, 1]},
                                 RegionType.MORIA : {Orc: [0, .6], OrcArcher: [.6, .85], Troll: [.85, 1]},
                                 RegionType.RHOVANION : {Orc: [0, .5], OrcArcher: [.5, .7], Nazgul: [.7, .85], BlackNumernorian: [.85, 1]},
                                 RegionType.ROHAN : {UrukHai: [0, .5], UrukHaiArcher: [.5, .7], EliteUrukHai: [.7, .8], WargRider: [.8, 1]},
                                 RegionType.GONDOR : {Orc: [0, .5], OrcArcher: [.5, .65], Troll: [.65, .75], Nazgul: [.75, .775], DragonOfMordor: [.775, .8], CorsairOfUmbar: [.8, .85], ArmoredMumakil: [.85, .9], SiegeWorks: [.9, .95], BlackNumernorian: [.95, 1]},
                                 RegionType.MORDOR : {Orc: [0, .5], OrcArcher: [.5, .65], Troll: [.65, .75], Nazgul: [.75, .85], DragonOfMordor: [.85, .9], BlackNumernorian: [.9, .95], SiegeWorks: [.95, 1]}}

#Monster base stats
"""
Monster base stats. Stats are a 3-element list whose elements
are: hp, attack, and experience in that order. 
"""
MONSTER_STATS = {BarrowWight:       [1, 1, 1],
                 Goblin:            [1, 1, 1],
                 GreatGoblin:       [1, 1, 1],
                 KingOfTheBarrows:  [1, 1, 1],
                 Nazgul:            [1, 1, 1],
                 Troll:             [1, 1, 1],
                 WargRider:         [1, 1, 1],       
                 UrukHai:           [1, 1, 1],
                 UrukHaiArcher:     [1, 1, 1],
                 EliteUrukHai:      [1, 1, 1],
                 Dunlending:        [1, 1, 1],
                 Orc:               [1, 1, 1],
                 OrcArcher:         [1, 1, 1],
                 SiegeWorks:        [1, 1, 1],
                 DragonOfMordor:    [1, 1, 1],
                 CorsairOfUmbar:    [1, 1, 1],
                 ArmoredMumakil:    [1, 1, 1],
                 BlackNumernorian:  [1, 1, 1],
                 EasterlingWarrior: [1, 1, 1],
                 Sauroman:          [1, 1, 1],
                 MouthOfSauron:     [1, 1, 1],
                 WitchKing:         [1, 1, 1],
                 Shelob:            [1, 1, 1],
                 Balrog:            [1, 1, 1]}

#Battle engine context
class BattleEngineContext(object):
    """
    BattleEngine has a parameter that determines if the
    battle is treated as a random battle or if the battle
    is treated as a story/boss battle.
    """
    RANDOM = 1
    STORY  = 2

#Battle engine constants
RUN_PROBABILITY_SUCCESS = 1
BATTLE_EARNINGS = 4

#Shop factory probability constants
class ShopFactoryConstants(object):
    """
    Constants used in shop factory. 
    """
    WEAPON_UPPER = .3
    ARMOR_LOWER = .3
    ARMOR_UPPER = .6
    POTION_LOWER = .6
    POTION_UPPER = .975

#Unique Place constants
class UniquePlaceConstants(object):
    """
    Constants used in unique places.
    """
    WeathertopBattleProb = .3
    WeathertopWitchKingProb = .125
    TharbadBattleProb = .2
    TharbadItemFindProb = .5
    ArgonathExperienceIncrease = .1
    DeringleExperienceIncrease = .05
    GoblinTownCaveEvasion = .4
    DolGuldurWitchKingProb = .125
    CirithUngolSneakProb = .4
    CirithUngolDarknessBonus = 5
