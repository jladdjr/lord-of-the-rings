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
        self._player = player
        cost = self.getCost()

        print ""
        print "- - - %s - - -" % self.getName()
        print self._greetings
        print "Cost to stay: %s." % cost

        #Determine player choice
        choice = None
        while choice != "no":
            print ""
            choice = raw_input("Would you like to stay for the night? Reponse: 'yes' or 'no.' ")
            
            #Heal option   
            if choice == "yes":
                #Money check and transfer
                if self._player.getMoney() >= cost:
                    self._player.decreaseMoney(cost)
                    #Actual healing operation
                    self._heal(self._player)
                    print "%s was healed at %s cost! %s has %s %s remaining." \
                          % (self._player.getName(), cost, self._player.getName(), self._player.getMoney(), constants.CURRENCY)
                    break
                #Not enough money
                else:
                    print "%s doesn't have enough money." % self._player.getName()
                    return
                
            #Non-use option
            elif choice == "no":
                print "Thanks for coming to %s." % self._name
                
            #For invalid input
            else:
                print "'What?'"
    
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
