#!/usr/bin/python

from unique_place import UniquePlace
from monsters.uruk_hai import UrukHai
from monsters.uruk_hai_archer import UrukHaiArcher
from monsters.elite_uruk_hai import EliteUrukHai
from monsters.sauroman import Sauroman
from battle_engine import battle
from items.unique_items import keysOfOrthanc
from items.unique_items import palatir
import constants

class Isenguard(UniquePlace):
    """
    Isenguard is a unique place in Calenardhon. It is Sauroman's fortress-city
    and base of operations.
    
    If a player visits Isenguard, he is given the opportunity to fight waves of
    enemies and gain some loot.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Isenguard.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

        #Create three waves of monsters
        self._wave = []
        self._wave2 = []
        self._wave3 = []

        #Create monster wave #1
        for monster in range(7):
            urukHai = UrukHai(constants.MONSTER_STATS[UrukHai])
            self._wave.append(urukHai)
        for monster in range(3):
            urukHaiArcher = UrukHaiArcher(constants.MONSTER_STATS[UrukHaiArcher])
            self._wave.append(urukHaiArcher)
        
        #Create monster wave #2
        for monster in range(10):
            eliteUrukHai = EliteUrukHai(constants.MONSTER_STATS[EliteUrukHai])
            self._wave2.append(eliteUrukHai)
        for monster in range(5):
            urukHaiArcher = UrukHaiArcher(constants.MONSTER_STATS[UrukHaiArcher])
            self._wave2.append(urukHaiArcher)

        #Create monster wave #3 - elite Uruk Hai have increased stats
        BONUS = 3
        increasedStats = []
        for stat in constants.MONSTER_STATS[EliteUrukHai]:
            increasedStats.append(stat * BONUS)
        for monster in range(2):
            eliteUrukHai = EliteUrukHai(increasedStats)
            self._wave3.append(eliteUrukHai)
        #Create Sauroman
        sauroman = Sauroman(constants.MONSTER_STATS[Sauroman])
        self._wave3.append(sauroman)

        #Spawn loot
        self._battleEarnings = keysOfOrthanc
        self._summitFindings = palatir
        
    def enter(self, player):
        """
        Action sequence for visiting Isenguard.

        @param player:  The current player.
        """
        print self._greetings
        print ""

        #Player goes through series of battles to take Isenguard
        self._battle(player)
        print ""

        #Player given option to summit Orthanc
        choice = self._summitPrompt()
        print ""
        
        #Carry out user-dependent script
        if choice == "yes":
            self._summitOrthanc(player)
        else:
            print "You continue on your journey."
        
    def _battle(self, player):
        """
        Battle sequence for Isenguard.

        @param player:  The current player.
        """
        #Wave 1
        print "Immediately as you approach the Ring of Isenguard, you are greeted with an a wave of Uruk...."
        raw_input("Press enter to continue. ")
        battle(player, constants.BattleEngineContext.STORY, self._wave)
        print ""
        
        #Wave 2
        print "As you gaze over bodies of your slain enemies, Sauroman the Great Wizard appears."
        raw_input("Press enter to continue. ")
        print ""
        
        print "Sauroman: \"You shouldn't have come, foolish one. Were you haughty enough to think that you could take the Orthanc?\""
        raw_input("Press enter to continue. ")
        battle(player, constants.BattleEngineContext.STORY, self._wave2)
        print ""
        
        #Wave 3
        print "Sauroman: \"You stupid fool....\""
        raw_input("Press enter to continue. ")
        battle(player, constants.BattleEngineContext.STORY, self._wave3)
        print ""

        #Victory sequence
        print "Isenguard has a new overseer this day."
        print ""
        
        #Give player loot
        if self._battleEarnings:
            print "You have gained the Keys of the Orthanc!"
            print ""
            player.addToInventory(keysOfOrthanc)
            self._battleEarnings = None
        
    def _summitPrompt(self):
        """
        Solicits user choice. Player given opportunity to summit the Orthanc 
        (Sauroman's Tower).

        @param player:  The current player.
        """
        choice = None
        acceptable = ["yes", "no"]
        print "Would you like to summit the Tower of Orthanc?"
        while choice not in acceptable:
            choice = raw_input("Choice: 'yes' or 'no.' ")
            
        return choice

    def _summitOrthanc(self, player):
        """
        Action sequence given that user has choicen to summit the Orthanc.

        @param player:  The current player.
        """
        #Summiting the Orthanc
        print "You take a brief residence in the Tower of Orthanc!"
        raw_input("Press enter to continue. ")
        print ""
        
        print "Here is your view:"
        print \
"""
  .       ..       .
    |\      ||      /|
    | \     ||     / |
    |  \    ||    /  |
    |  :\___JL___/   |
    |  :|##XLJ: :|   |
    '\ :|###||: X|  /'
      \:|###||:X#| /
       |==========|
        |###XXX;;|
        |##XX:: :|
        |##Xn:: :|
        |##XU:: :|
        |##XX:: :|
        |##XX:: :|
        |##XX:: :|
        |##XX:: n|
        |##XX:: U|
        |##XX:: :|
        |##XX:: :|
        |##XX:: :|
        |##Xn:: :|
        |##XU:: :|
        |##XX:: :|
        |##XX:: :|
        |##XX:: :|
        |##XX:: n|
        |##XX:: U|
"""
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        if self._summitFindings:
            print "You found Sauroman's Palatir!"
            player.addToInventory(palatir)
            self._summitFindings = None
        print ""

        #Story
        print "Congratulations on your victory!"
        print ""
        
