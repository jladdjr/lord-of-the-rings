#!/usr/bin/python

from cities.building import Building

class Inn(Building):
    """
    Squares are public spaces that allow players to interface with city folk.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes inn object.

        @param name:           The name of the inn.
        @param description:    A description of the inn.
        @param greetings:      The greetings the user gets as he enters a inn.
        """
        Building.__init__(self, name, description, greetings)
        
    def execute(self, player):
        """
        The events sequence upon player entering inn.
        """
        player = self._player
        
        print "- - - %s - - -" %self._name
        print self._greetings
        print "Cost to stay: %s." %self._cost

        choice = None
        while choice != 2:
            print
            """
            Here are your options:
            1) Heal
            2) Leave
            """
            if choice == 1:
                print "%s was healed at %s cost! %s has %s remaining." 
                self._heal(self._player)
                self._player.decreaseMoney(self._cost)
            elif choice == 2:
                print "Thanks for coming to %s" %self._name
            else:
                print "Invalid choice."
    
    def getCost(self):
        """
        Returns cost for using inn.
        
        @return:    Cost of using inn.
        """
        return self._cost

    def _heal(self, player):
	"""
	Heals player at a cost.

	@param player:	  The player object.
	"""
	maxHp = player.getMaxHp()
	hp = player.getHp()
	amountToHeal = maxHp - hp

	player.heal(amountToHeal)
