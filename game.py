#!/usr/bin/python

from parser import Parser
from commands.command_words import CommandWords
from commands.help_command import HelpCommand 
from commands.quit_command import QuitCommand
from commands.drop_command import DropCommand
from commands.pick_up_command import PickUpCommand
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand
from commands.attack_command import AttackCommand


from player import Player
from worldmap import WorldMap

class Game(object):
    """
    Prepares and executes turn-based game.
    """

    def __init__(self):
        """
        Initializes new game.
        """

        #World Map
        self._worldMap = WorldMap()

        #Player
        self._startingLocation = self._worldMap._shire
        self._player = Player("Frodo", self._startingLocation)
        
        #CommandWords
        self._commandWords = CommandWords()

        #Commands
        helpCmd = HelpCommand("help", 
                    "Provides help information for game.", self._commandWords)
        self._commandWords.addCommand("help", helpCmd)

        quitCmd = QuitCommand("quit", "Exits the game.")
        self._commandWords.addCommand("quit", quitCmd)
        
        dropCmd = DropCommand("drop", "Drops an item from inventory into local environment.", self._player)
        self._commandWords.addCommand("drop", dropCmd)

        pickupCmd = PickUpCommand("pick up", "Picks up an item from a location and adds to inventory.", self._player)
        self._commandWords.addCommand("pick up", pickupCmd)

        attackCmd = AttackCommand("attack", "Allows a character to attack a target.", self._player, None)
        self._commandWords.addCommand("attack", attackCmd)
  
        northCmd = NorthCommand("north", 
                    "Moves the player to the space north of current space")
        self._commandWords.addCommand("north", northCmd)
        
        southCmd = SouthCommand("south", 
                    "Moves the player to the space south of current space")
        self._commandWords.addCommand("south", southCmd)
        
        eastCmd = EastCommand("east", 
                    "Moves the player to the space east of current space")
        self._commandWords.addCommand("east", eastCmd)
        
        westCmd = WestCommand("west", 
                    "Moves the player to the space west of current space")
        self._commandWords.addCommand("west", westCmd)
        
        descCmd = DescribeCommand("describe", 
                    "Gives description of current space", self._player)
        self._commandWords.addCommand("describe", descCmd)

        #Parser
        self._parser = Parser(self._commandWords)

    def play(self):
        """
        Executes main game loop.
        """
        print "Welcome to Lord of the Rings Adventure Game!"
        print "(Type 'help' for a list of available commands)"
        print ""

        while(True):
            self._nextTurn()

    def _nextTurn(self):
        """
        Executes next turn.
        """
        nextCommand = self._parser.getNextCommand()
        
        if nextCommand is not None:
            nextCommand.execute()
            print ""
        else:
            errorMsg = "Failed to receive command from parser."
            raise AssertionError(errorMsg)
