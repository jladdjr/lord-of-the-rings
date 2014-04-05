#!/usr/bin/python

from cities.building import Building

class Inn(Building):
    """
    Inns are buildings that allow player to heal.
    """
    def __init__(self, name, description, greetings, cost):
        """
        Initializes inn object.

        @param name:           The name of the inn.
        @param description:    A description of the inn.
        @param greetings:      The greetings the user gets as he enters a inn.
        @param cost:           The cost of using the inn.
        """
        Building.__init__(self, name, description, greetings)
        self._cost = cost
        
    def execute(self, player):
        """
        The events sequence upon player entering inn.
        """
        self._player = player

        print ""
        print "- - - %s - - -" %self._name
        print self._greetings + "."
        print "Cost to stay: %s." %self._cost

        #Determine player choice
        choice = None
        while choice != 2:
            print """
            What would you like to do?:
            1) Stay
            2) Leave
            """
            choice = int(raw_input("Choice? "))

            #Heal option   
            if choice == 1:
                #Checks that player has enough money
                if self._player.getMoney() >= self._cost:
                    self._player.decreaseMoney(self._cost)
                    #Actual healing operation
                    self._heal(self._player)
                    print "%s was healed at %s cost! %s has %s rubles remaining." \
                          %(self._player.getName(), self._cost, self._player.getName(), self._player.getMoney())
                    break
                
            #Non-use option
            elif choice == 2:
                print "Thanks for coming to %s." %self._name
                
            #For invalid input
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
