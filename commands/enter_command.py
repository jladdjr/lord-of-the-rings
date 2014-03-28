#!/usr/bin/python

from command import Command

class EnterCommand(Command):
    """
    Allows player to enter a building.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new enter command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Finish initializing help-specific settings
        self._player = player

    def execute(self):
        """
        Allows player to enter a building.
        """
        space = self._player.getLocation()
        city = space.getCity()
        buildings = city.getBuildings()

        buildingToEnter = raw_input("Where would you like to go? ")
        building = city.getBuildingString(buildingToEnter)
 
        if building:
            building.execute(self._player)
        else:
            print "Building does not exist."
