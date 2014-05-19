#!/usr/bin/python

from command import Command
import constants

class QuitCommand(Command):
    """
    Quit command.
    """
    def __init__(self, name, explanation):
        """
        Initializes new quit command.

        @param name:          The name of the command.
        @param explanation:   Explanation of the Command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

    def execute(self):
        """
        Run Help command.
        """
        #Confirm quit
        response = raw_input( "Are you sure you want to quit? (yes/no): ")
        response = response.strip().lower()

        if 'yes' in response:
            print "Exiting...."
            exit(0)
