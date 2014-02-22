#!/usr/bin/python

from parser import Parser
<<<<<<< HEAD
from commandwords import CommandWords
from helpcommand import HelpCommand 
from quitcommand import QuitCommand
from northcommand import NorthCommand
from southcommand import SouthCommand
from eastcommand import EastCommand
from westcommand import WestCommand
=======
from commands.commandwords import CommandWords
from commands.helpcommand import HelpCommand 
from commands.quitcommand import QuitCommand
>>>>>>> master
from player import Player

class Game(object):
    """
    Prepares and executes turn-based game.
    """

    def __init__(self):
        """
        Initializes new game.
        """
        #CommandWords
        self._commandWords = CommandWords()

        #Commands
        helpCmd = HelpCommand("help", 
                    "Provides help information for game.", self._commandWords)
        self._commandWords.addCommand("help", helpCmd)

        quitCmd = QuitCommand("quit", "Exits game")
        self._commandWords.addCommand("quit", quitCmd)
<<<<<<< HEAD
        
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
=======
>>>>>>> master

        #Parser
        self._parser = Parser(self._commandWords)

        #Player
        self._player = Player()

        #TODO: Create game board

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
<<<<<<< HEAD
            errorMsg = "Failed to receive command from parser."
=======
            errorMsg = "Failed to received command from parser."
>>>>>>> master
            raise AssertionError(errorMsg)
