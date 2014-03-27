#!/usr/bin/python

from building import Building

class Inn(Building):
    """
    Inns are instances of the Building object.
    Inns have a special method that allows player to heal.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes inn object.

        @param name:           The name of the inn.
        @param description:    A description of the inn.
        @param greetings:      The greetings the user gets as he enters a inn.
        @param cost:           The cost of using the inn.
        """
        Building.__init__(self, name, description, greetings)
        self._cost = cost
        
    def enterBuilding(self, player):
        """
        Player enters inn.
        """
        print self._greetings
        print "Cost to stay: %s." %self._cost

		#TODO: Use _heal method to heal player.
    
    def getCost(self):
        """
        Returns cost for using inn.
        
        @return:    Cost of using inn.
        """
        return self._cost

	def _heal(self, player):
		"""
		Heals a player.

		@param player:		The player.
		"""
		pass
