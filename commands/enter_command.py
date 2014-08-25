#!/usr/bin/python

from command import Command
from cities.city import City
from unique_place import UniquePlace
import battle_engine
import constants

import random

class EnterCommand(Command):
    """
    Allows player to enter a city or unique place.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes enter command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation, time = False)

        self._player = player
    
    def _displayPlacesToEnter(self):
        """
        Displays the possible places (Cities or UniquePlaces) that player may 
        enter.
        """
        playerName = self._player.getName()
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        #If there are no cities or unique places
        if not (city or uniquePlace):
            print "No place to enter."
        
        #Otherwise print the possible places to enter
        else:
            print "%s may enter the following:" % playerName
            if isinstance(city, City):
                print "\t-%s" % city.getName()
            elif isinstance(city, list):
                for eachCity in city:
                    print "\t-%s" % eachCity.getName()
            
            #Display uniquePlaces that player may enter
            if isinstance(uniquePlace, UniquePlace):
                print "\t-%s" % uniquePlace.getName()
            elif isinstance(uniquePlace, list):
                for eachUniquePlace in uniquePlace:
                    print "\t-%s" % eachUniquePlace.getName()
            print ""
        
    def _createDictionaryOfPlaces(self):
        """
        Creates a dictionary of the places that are within space. Key-
        definition pairs are object names and their corresponding 
        objects.
        """
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        dictionary = {}
        
        #Add cities to dictionary
        if isinstance(city, City):
            dictionary[city.getName()] = city
        elif isinstance(city, list):
            for eachCity in city:
                dictionary[eachCity.getName()] = eachCity
        
        #Add uniquePlaces to dictionary
        if isinstance(uniquePlace, UniquePlace):
            dictionary[uniquePlace.getName()] = uniquePlace
        elif isinstance(uniquePlace, list):
            for eachUniquePlace in uniquePlace:
                dictionary[eachUniquePlace.getName()] = eachUniquePlace
        
        return dictionary
    
    def execute(self):
        """
        Allows player to enter a city or uniquePlace.
        """
        #Show the places that player may enter
        self._displayPlacesToEnter()
        
        #Create a dictionary of places within space
        #Key-value pairs are names and their corresponding objects
        dictionary = self._createDictionaryOfPlaces()
        
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        #If there is no place to enter
        if not (city or uniquePlace):
            return
        
        #Entering the place that the player chooses to enter
        choice = raw_input("Which of these would you like to enter?\n")
        while (choice not in dictionary.keys()) or choice == "cancel":
            if choice == "cancel":
                break 
            print "\n\"Huh?\""
            print "Try again, or type \"cancel.\"\n"
            choice = raw_input("Where would you like to enter?\n")
        else:
            print "\n"
            self._battlePhase()
            dictionary[choice].enter(self._player)
            
    def _battlePhase(self):
        """
        Evaluates if a random battle will occur. If so, battle_engine.battle()
        is called to execute the battle.
        """
        currentLocation = self._player.getLocation()
        battleProbability = currentLocation.getBattleProbability()
        
        #Determines if random battle will occur
        if random.random() < battleProbability:
            #Call on battle to resolve battle
            battle_engine.battle(self._player, 
            constants.BattleEngineContext.RANDOM)