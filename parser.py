#!/usr/bin/python

import constants
from commandwords import CommandWords

class Parser(object):
    """
    Parses user input, searching for registered commands.
    """

    def __init__(self, commandWords=None):
        """
        Initializes new parser.

        @param commandWords:     List of commands.
        """
        self._commandWords = commandWords

    def getNextCommand(self):
        """
        Retrieves next command from user.
        """
        userInput = raw_input(constants.COMMAND_PROMPT)
        userInput = userInput.strip().lower()

        while not self._commandRecognized(userInput):
            print "Command not recognized. Type 'help' for help."
            print ""

            userInput = raw_input(constants.COMMAND_PROMPT)
            userInput = userInput.strip().lower()

        command = self._commandWords.getCommand(userInput)
        return command

    def _commandRecognized(self, name):
        """
        Helper method to determine if user
        specified known command.

        @param name:        Command's name 
        @return:            True if recognized, False otherwise.
        """
        #Make sure name is not None
        if not name:
            return False

        recognized = self._commandWords.isCommand(name)
        return recognized
