#!/usr/bin/python

import constants
from commands.command_words import CommandWords

class Parser(object):
    """
    Parses user input, searching for registered commands.
    """
    def __init__(self, commandWords):
        """
        Initializes parser.

        @param commandWords:     List of commands.
        """
        if not commandWords:
            errorMsg = "Parser must be initialized with CommandWords object."
            raise AssertionError(errorMsg)

        self._commandWords = commandWords

    def getNextCommand(self):
        """
        Retrieves next command from user.
        """
        userInput = raw_input(constants.COMMAND_PROMPT)
        userInput = userInput.strip().lower()

        while not self._commandRecognized(userInput):
            print "Command '%s' not recognized. Type 'help' for help." % userInput
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