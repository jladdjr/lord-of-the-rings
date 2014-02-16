#!/usr/bin/python

from parser import Parser
from commandwords import CommandWords
from helpcommand import HelpCommand 
from quitcommand import QuitCommand
from northcommand import NorthCommand
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
        
        northCmd = NorthCommand("north", 
                    "Moves the player to the space north of current space")
        self._commandWords.addCommand("north", northCmd)

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
            errorMsg = "Failed to receive command from parser."
            raise AssertionError(errorMsg)
