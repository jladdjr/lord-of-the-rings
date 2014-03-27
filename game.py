#!/usr/bin/python

from parser import Parser
import game_loader

class Game(object):
    """
    Prepares and executes turn-based game.
    """
    def __init__(self):
        """
        Initializes new game.
        """
        #Initializes game objects
        self._world = game_loader.getWorld()
        startingInventory = game_loader.getStartingInventory()
        self._player = game_loader.getPlayer(self._world, startingInventory)
        self._commandList = game_loader.getCommandList(self._player)

        #Creates parser
        self._parser = Parser(self._commandList)

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
