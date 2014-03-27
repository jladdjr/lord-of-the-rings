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
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

    def execute(self):
        """
        Run Help command.
        """
        #Confirm quit
        response = raw_input( "Are you sure you want to quit? (y/n): ")
        response = response.strip().lower()

        if 'y' in response:
            print "Exiting.."
            exit(0)
