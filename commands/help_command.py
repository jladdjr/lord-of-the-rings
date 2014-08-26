#!/usr/bin/python

from command import Command

class HelpCommand(Command):
    """
    Help command.
    """
    def __init__(self, name, explanation, commandWords):
        """
        Initializes help command.
        
        @param commandWords:        CommandWords used in game.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._commandWords = commandWords

    def execute(self):
        """
        Run Help command.
        """
        #Print header
        print "--------------------------------"
        print "Lord of the Rings Adventure Game"
        print "--------------------------------"
        print "The following commands may be used during the game:"
        print ""
        
        #Calculate some variables
        words = self._commandWords
        names = words.getCommandNames()
        
        lengthCommand = []
        for name in names:
            lengthCommand.append(len(name))
            
        minLength = min(lengthCommand)
        totalSpacing = 12
        
        #Print out command information
        for name in names:
            command = words.getCommand(name)
            explanation = command.getExplanation()
            whiteSpace = (12 - len(name)) * " "
            print "%s%s%s" % (name, whiteSpace, explanation)