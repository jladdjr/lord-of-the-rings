#!/usr/bin/python

from unique_place import UniquePlace

class OstInEdhil(UniquePlace):
    """
    OstInEdhil is a unique place in Anduin. OstInEdhil was once a 
    great city that was inhabited by elves before Sauron destroyed
    it.

    If player visits OstInEdhil, he is healed.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Argonath.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
	@param greetings:	The greetings the user gets as he enters.        
	"""
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

    def enter(self, player):
        """
        Enter Ost-in-Edhil.

        @param player:  The current player.
        """
	healing = player.getMaxHp() - player.getHp()
		
	print self._greetings
	print ""
	print "You decide that this is a good place to spend the night."
	raw_input("Press enter to continue." )
	print ""
		
	player.heal(healing)
	print "%s was healed by %s!" % (player.getName(), healing)
	print ""
	
	print "You awaken refreshed and ready for a new day."
	print ""
