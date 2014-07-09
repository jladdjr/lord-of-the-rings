#!/usr/bin/python

from cities.building import Building
import constants

class Inn(Building):
    """
    Inns inherit from Building.
    
    Inns are buildings that allow player to heal for a price.
    """
    def __init__(self, name, description, greetings, cost):
        """
        Initializes the inn.

        @param name:           The name of the inn.
        @param description:    The description of the inn.
        @param greetings:      The greetings the user gets as he enters the inn.
        @param cost:           The cost of using the inn.
        """
        Building.__init__(self, name, description, greetings)
        
        self._cost = cost
        
    def enter(self, player):
        """
        The action sequence upon player entering inn.
        
        @param player:     The player object.
        """
        cost = self.getCost()

        print ""
        print "- - - %s - - -" % self.getName()
        print self._greetings
        print "Cost to stay: %s." % cost

        #Determine player choice
        choice = None
        while choice != "no":
            print ""
            choice = raw_input("Would you like to stay for the night? Response: 'yes' or 'no.' ")
            
            #Heal option   
            if choice == "yes":
                #Money check and transfer
                if player.getMoney() >= cost:
                    player.decreaseMoney(cost)
                    #Actual healing operation
                    self._heal(player)
                    print "%s was healed at %s cost! %s has %s %s remaining." \
                          % (player.getName(), cost, player.getName(), player.getMoney(), constants.CURRENCY)
                    break
                #Not enough money
                else:
                    print "%s doesn't have enough money." % player.getName()
                    return
                
            #Non-use option
            elif choice == "no":
                print "Thanks for coming to %s." % self._name
                
            #For invalid input
            else:
                print "'What?'"
    
    def getCost(self):
        """
        Returns inn cost.
        
        @return:    Cost of using inn.
        """
        return self._cost

    def _heal(self, player):
        """
        Heals player to maxHp.

        @param player:    The player object.
        """
        maxHp = player.getMaxHp()
        hp = player.getHp()
        amountToHeal = maxHp - hp

        player.heal(amountToHeal)