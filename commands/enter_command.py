#!/usr/bin/python

from command import Command
from cities.city import City

class EnterCommand(Command):
    """
    Allows player to enter a city/uniquePlace.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new enter command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player
        self._time = True

    def execute(self):
        """
        Allows player to enter a city or a uniquePlace.
        """
        name = self._player.getName()
        space = self._player.getLocation()
        
        possiblePlaces = []
        
        #If city in space...
        if space.getCity():
            city = space.getCity()
            #For single city
            if isinstance(city, City):
                cityName = city.getName()
                possiblePlaces.append(cityName)
            #For multiple cities
            elif isinstance(city, list):
                for specificCity in city:
                    cityName = specificCity.getName()
                    possiblePlaces.append(cityName)
        
        #If uniquePlace in space...
        if space.getUniquePlace():
            uniquePlace = space.getUniquePlace()
            uniquePlaceName = uniquePlace.getName()
            possiblePlaces.append(uniquePlaceName)
            
        #Sort possiblePlaces
        possiblePlaces.sort()

        #If zero possible places...
        if len(possiblePlaces) == 0:
            print "No possible destinations for player."
            return
        
        #User prompt
        print "%s may go to the following:" % self._player.getName()
        for possiblePlace in possiblePlaces:
            print "\t%s" % possiblePlace
            print ""

        choice = None
        while choice not in possiblePlaces:
            choice = raw_input("Where would you like to go? ")
            
            #If user choice is a city
            if space.getCity():
                if isinstance(city, City):
                    if city.returnCity(choice):
                        print ""
                        print city.getGreeting()
                        print ""
                        
                        #User prompt
                        print "The following may be entered in %s:" % city.getName()
                        buildings = city.getBuildings()
                        buildingsString = []
                        for building in buildings:
                            print "\t%s" % building.getName()
                            buildingsString.append(building.getName())
                        print ""
                        
                        #Select Building in City
                        choice = None
                        while choice not in buildingsString:
                            choice = raw_input("Where would you like to go? ")
                            if choice in buildingsString:
                                for building in buildings:
                                    if choice == building.getName():
                                        building.enter(self._player)

                                #User prompt if player wants to enter another building        
                                choice = None
                                possibleResponses = ["yes", "no"]
                                while choice not in possibleResponses:
                                    print ""
                                    choice = raw_input("Would you like to go somewhere else (yes/no)? ")
                                    if choice == "yes":
                                        print ""
                                        print "The following may be entered in %s:" % city.getName()
                                        for building in buildings:
                                            print "\t%s" % building.getName()
                                        print ""
                                        continue
                                    elif choice == "no":
                                        return
                                    else:
                                        print "Huh?"
                elif isinstance(city, list):
                    for specificCity in city:
                        if choice == specificCity.getName():
                            #User prompt
                            print "The following may be entered in %s:" % specificCity.getName()
                            buildings = specificCity.getBuildings()
                            buildingsString = []
                            for building in buildings:
                                print "\t%s" % building.getName()
                                buildingsString.append(building.getName())
                            print ""
                        
                            #Select Building in City
                            choice = None
                            while choice not in buildingsString:
                                choice = raw_input("Where would you like to go? ")
                                if choice in buildingsString:
                                    for building in buildings:
                                        if choice == building.getName():
                                            building.enter(self._player)

                                #User prompt if player wants to enter another building        
                                choice = None
                                possibleResponses = ["yes", "no"]
                                while choice not in possibleResponses:
                                    print ""
                                    choice = raw_input("Would you like to go somewhere else (yes/no)? ")
                                    if choice == "yes":
                                        print ""
                                        print "The following may be entered in %s:" % specificCity.getName()
                                        for building in buildings:
                                            print "\t%s" % building.getName()
                                        print ""
                                        continue
                                    elif choice == "no":
                                        return
                                    else:
                                        print "Huh?"

            #If user input is an unique place
            elif space.getUniquePlace():
                if uniquePlace.returnUniquePlace(choice):
                    print ""
                    print uniquePlace.getGreeting()
                    print ""
                    uniquePlace.enter()
                    return
