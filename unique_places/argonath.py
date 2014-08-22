#!/usr/bin/python

from unique_place import UniquePlace
import constants

class Argonath(UniquePlace):
    """
    Argonath is a unique place in Anduin. The Argonath consists of two
    gigantic statues of Isildur and Elendil.

    If player visits Argonath, he is healed and gains experience.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Argonath.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

    def enter(self, player):
        """
        Argonath's action sequence.

        @param player:  The player object.
        """
        #Generate reward
        name = player.getName()
        playerExperience = player.getExperience()
        experienceIncrease = (playerExperience * 
            constants.ARGONATH_EXP_INCREASE)
        maxHp = player.getMaxHp()
            
        #Story
        print self._greetings
        print ""
        print ("As you gaze upon the kings of old, you think about the present"
            " age and its \ncurrent darkness.")
        raw_input("Press enter to continue. ")
        print ""
            
        #Player receives reward
        print ("You draw up deep reserves of strength within yourself to" 
            " finish the quest. \nMordor awaits.")
        print "\n%s gains %s experience.\n" % (name, experienceIncrease)
        player.increaseExperience(experienceIncrease)
        player.heal(maxHp)
        
        raw_input("Press enter to leave. ")
        print ""