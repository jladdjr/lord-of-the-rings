#!/usr/bin/python

from command import Command

class HelpCommand(Command):
    """
    Help command.
    """
    def __init__(self, name, explanation, commandWords):
        """
        Initializes new help command.
        
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

        #Print help for each defined command
        words = self._commandWords

        names = words.getCommandNames() 
        for name in names:
            command = words.getCommand(name)
            explanation = command.getExplanation()
            print "%s\t\t\t%s" % (name, explanation)
