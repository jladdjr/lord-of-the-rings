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
        
    #TODO: Rename to enterBuilder() or just enter()
    def execute(self, player):
        """
        The events sequence upon player entering inn.
        """

        #TODO: No need to create a _player attribute here;
        #      You can just use 'player' throughout the method.
        self._player = player

        #TODO: Add space after using % for string replacement
        print ""
        print "- - - %s - - -" % self._name
        print self._greetings + "."
        print "Cost to stay: %s." % self._cost

        #TODO: In all building classes, avoid using magic numbers. Use constants instead.
        #Determine player choice
        choice = None
        STAY = 1
        LEAVE = 2

        while choice != LEAVE:
            print """
            What would you like to do?:
            1) Stay
            2) Leave
            """
            choice = int(raw_input("Choice? "))

            #Heal option   
            if choice == STAY:
                #Checks that player has enough money
                if self._player.getMoney() >= self._cost:
                    self._player.decreaseMoney(self._cost)
                    #Actual healing operation
                    self._heal(self._player)
                    print "%s was healed at %s cost! %s has %s rubbles remaining." \
                          %(self._player.getName(), self._cost, self._player.getName(), self._player.getMoney())
                    break
                #TODO: Add else clause; if player doesn't have enough money, print a message to that effect so player
                #      knows why nothing happened.
                
            #Non-use option
            elif choice == LEAVE:
                print "Thanks for coming to %s." % self._name
                
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
