#!/usr/bin/python

from parser import Parser
import game_loader
import random

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
        self._battleEngine = game_loader.battleEngine(self._player)

        #Creates parser
        self._parser = Parser(self._commandList)

    def play(self):
        """
        Executes main game loop.
        """
        message = """
 __                                  __                   ______        
|  \                                |  \                 /      \       
| $$        ______    ______    ____| $$        ______  |  $$$$$$\      
| $$       /      \  /      \  /      $$       /      \ | $$_  \$$      
| $$      |  $$$$$$\|  $$$$$$\|  $$$$$$$      |  $$$$$$\| $$ \          
| $$      | $$  | $$| $$   \$$| $$  | $$      | $$  | $$| $$$$          
| $$_____ | $$__/ $$| $$      | $$__| $$      | $$__/ $$| $$            
| $$     \ \$$    $$| $$       \$$    $$       \$$    $$| $$            
 \$$$$$$$$  \$$$$$$  \$$        \$$$$$$$        \$$$$$$  \$$            
                                                                        
                                                                        
                                                                        
                   ________  __                                         
                  |        \|  \                                        
                   \$$$$$$$$| $$____    ______                          
                     | $$   | $$    \  /      \                         
                     | $$   | $$$$$$$\|  $$$$$$\                        
                     | $$   | $$  | $$| $$    $$                        
                     | $$   | $$  | $$| $$$$$$$$                        
                     | $$   | $$  | $$ \$$     \                        
                      \$$    \$$   \$$  \$$$$$$$                        
                                                                        
                                                                        
                                                                        
             _______   __                                               
            |       \ |  \                                              
            | $$$$$$$\ \$$ _______    ______    _______                 
            | $$__| $$|  \|       \  /      \  /       \                
            | $$    $$| $$| $$$$$$$\|  $$$$$$\|  $$$$$$$                
            | $$$$$$$\| $$| $$  | $$| $$  | $$ \$$    \                 
            | $$  | $$| $$| $$  | $$| $$__| $$ _\$$$$$$\                
            | $$  | $$| $$| $$  | $$ \$$    $$|       $$                
             \$$   \$$ \$$ \$$   \$$ _\$$$$$$$ \$$$$$$$                 
                                    |  \__| $$                          
                                     \$$    $$                          
                                      \$$$$$$
        """
        print message
        print "An adventure game where Russian tries to take on the hoards of Mordor."
        print "A little help from Dear Ladd Jr., Miles, Seth, and C-$ on the way."
        print "...~Money~..."
        print ""
        print "(Type 'help' for a list of available commands)"
        print ""

        while(True):
            self._nextTurn()

    def _nextTurn(self):
        """
        Executes next turn and then determines whether a random battle should occur.
        """
        #Executes next command
        nextCommand = self._parser.getNextCommand()
        
        if nextCommand is not None:
            nextCommand.execute()
            print ""
        else:
            errorMsg = "Failed to receive command from parser."
            raise AssertionError(errorMsg)

        #For random battles
        currentLocation = self._player.getLocation()
        probabilityBattle = space.getProbabilityBattle()
        if random.random() < probabilityBattle:
            #Call on battleobject to resolve battle
            self._battleEngine(self._player)
        
