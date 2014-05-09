#!/usr/bin/python

from parser import Parser
import game_loader
import battle_engine
import random

class Game(object):
    """
    Prepares and executes turn-based game.
    """
    def __init__(self):
        """
        Initializes new game.
        """
        print "Game loading...."
        #Initializes game objects
        self._world = game_loader.getWorld()
        startingInventory = game_loader.getStartingInventory()
        self._player = game_loader.getPlayer(self._world, startingInventory)
        self._commandList = game_loader.getCommandList(self._player)
        print "Loading complete."
        
        #Creates parser
        self._parser = Parser(self._commandList)

    def play(self):
        """
        Executes main game loop.
        """
        splashScreen = """
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
        print splashScreen
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
        Determines if a random battle should occur and then executes
        the random battle before executing player command. 
        """
        #Determines if random battle will occur
        currentLocation = self._player.getLocation()
        battleProbability = currentLocation.getBattleProbability()
        if random.random() < battleProbability:
            #Call on battleobject to resolve battle
            battle_engine.battle(self._player)
        
        #Executes next command
        nextCommand = self._parser.getNextCommand()
        
        if nextCommand is not None:
            nextCommand.execute()
            print ""
        else:
            errorMsg = "Failed to receive command from parser."
            raise AssertionError(errorMsg)
