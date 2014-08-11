#!/usr/bin/python

import random
import sys

import game_loader
import battle_engine
from parser import Parser
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand
from commands.enter_command import EnterCommand
from items.unique_items import theOneRing
import constants

class Game(object):
    """
    Prepares and executes turn-based game.
    """
    def __init__(self):
        """
        Initializes game.
        """
        print "...Game Loading..."
        print "..."
        
        #Initializes game objects
        self._world = game_loader.getWorld()
        self._shire = self._world[0]
        self._orodruin = self._world[26]
        
        startingInventory = game_loader.getStartingInventory()
        self._player = game_loader.getPlayer(self._shire, startingInventory)
        self._commandList = game_loader.getCommandList(self._player)
        
        print "..."
        print "$$$Loading Complete$$$"
        
        #Creates parser
        self._parser = Parser(self._commandList)

    def play(self):
        """
        Executes main game loop.
        """
        splashScreen = """
        """
        print splashScreen
        print ("An adventure game where Russian tries to take on the hoards of" 
        " Mordor.")
        print ("A little help from Dear Ladd Jr., Miles, Seth, and C-$ along" 
        " the way.")
        print "...~Money~..."
        print ""
        print "(Type 'help' for a list of available commands)"
        print ""

        while(True):
            self._nextTurn()

    def _nextTurn(self):
        """
        Gets nextCommand from player. If nextCommand may be executed
        successfully and involves a passing of time, there is a chance that a 
        random battle will occur after nextCommand is executed.
        
        Commands with a chance of unsuccessful execution: the four movement 
        commands and enter command.
        """
        #Executes next command
        nextCommand = self._parser.getNextCommand()
        
        if nextCommand is not None:
            #Check command execution
            if self._executionCheck(nextCommand):
                #Then execute nextCommand
                nextCommand.execute()
                #If passing of time... chance a random battle will occur
                if nextCommand.getTime():
                    self._battlePhase()
            print ""
            
        else:
            errorMsg = "Failed to receive command from parser."
            raise AssertionError(errorMsg)
        
        #If player has won the game
        if self._winningConditions():
            print ("Congratulations! %s has saved Middle Earth!" 
            % self._player.getName())
            raw_input("Press enter to exit. ")
            sys.exit()
            
    def _executionCheck(self, nextCommand):
        """
        Checks if the user's command may be carried out. This only applies to 
        the four movement commands and enter command.
        
        This method is intended to prevent random battles from occuring in 
        instances where the command cannot be executed.
        
        @return:              True if command will be executed successfully and 
                              False otherwise.
        """
        space = self._player.getLocation()
        
        #Check movement commands
        if isinstance(nextCommand, NorthCommand):
            if not self._player.canMoveNorth():
                print "Cannot move north."
                return False
        elif isinstance(nextCommand, SouthCommand):
            if not self._player.canMoveSouth():
                print "Cannot move south."
                return False
        elif isinstance(nextCommand, EastCommand):
            if not self._player.canMoveEast():
                print "Cannot move east."
                return False
        elif isinstance(nextCommand, WestCommand):
            if not self._player.canMoveWest():
                print "Cannot move west."
                return False
        elif isinstance(nextCommand, EnterCommand):
            if not space.getCity() and not space.getUniquePlace():
                print "No place to enter."
                return False
        
        return True

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
    
    def _winningConditions(self):
        """
        Evaluates if player has won the game. Criteria for winning the game is 
        that the OneRing has been dropped in the space, orodruin (Mount Doom). 
        """
        if self._orodruin.containsItem(theOneRing):
            return True
        else:
            return False