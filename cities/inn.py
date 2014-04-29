#!/usr/bin/python

from cities.building import Building
import constants

class Inn(Building):
    """
    Inns are buildings that allow player to heal for a cost.
    """
    def __init__(self, name, description, greetings, cost):
        """
        Initializes inn object.

        @param name:           The name of the inn.
        @param description:    A description of the inn.
        @param greetings:      The greetings the user gets as he enters the inn.
        @param cost:           The cost of using the inn.
        """
        Building.__init__(self, name, description, greetings)
        self._cost = cost
        
    def enter(self, player):
        """
        The events sequence upon player entering inn.
        """

        #TODO: No need to create a _player attribute here;
        #      You can just use 'player' throughout the method.
        self._player = player
        cost = self.getCost()

        print ""
        print "- - - %s - - -" % self.getName()
        print self._greetings
        print "Cost to stay: %s." % cost

        #Determine player choice
        STAY = 1
        LEAVE = 2
        
        choice = None
        while choice != LEAVE:
            print """
            Would you like to stay for the night?:
            1) Stay
            2) Leave
            """
            choice = int(raw_input("Choice? "))

            #Heal option   
            if choice == STAY:
                #Money check and transfer
                if self._player.getMoney() >= cost:
                    self._player.decreaseMoney(cost)
                    #Actual healing operation
                    self._heal(self._player)
                    print "%s was healed at %s cost! %s has %s %s remaining." \
                          % (self._player.getName(), cost, self._player.getName(), self._player.getMoney(), constants.CURRENCY)
                    break
                else:
                    print "%s have enough money." % self._player.getName()
                
            #Non-use option
            elif choice == LEAVE:
                print "Thanks for coming to %s." % self._name
                
            #For invalid input
            else:
                print "What?"
    
    def getCost(self):
        """
        Returns cost for using inn.
        
        @return:    Cost of using inn.
        """
        return self._cost

    def _heal(self, player):
        """
        Heals player to maxHp.

        @param player:	  The player object.
        """
        maxHp = player.getMaxHp()
        hp = player.getHp()
        amountToHeal = maxHp - hp

        player.heal(amountToHeal)
