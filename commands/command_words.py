#!/usr/bin/python

class CommandWords(object):
    """
    Dictionary of all Command objects used in the game.
    """

    def __init__(self):
        """
        Initializes new dictionary of commands.
        """
        self._commandWords = {}

    def addCommand(self, name, command):
        """
        Adds command to dictionary of commands.

        @precondition:      name not already assigned mapped to command.

        @param name:        Name of command.
        @param command:     Command object.
        """
        #Does command already exist?
        if self.isCommand(name):
            errorMsg = "Cannot add '%s' to CommandWords; command name already in use." % \
                    name
            raise AssertionError(errorMsg)

        #Add command
        self._commandWords[name] = command

    def getCommand(self, name):
        """
        Retrieves a command by name.

        @precondition:      isCommand()

        @param name:        Name of command.
        @return:            Command object.
                            Returns None if command not found.
        """
        if self.isCommand(name): 
            return self._commandWords[name]
        return None

    def getCommandNames(self):
        """
        Returns list of all command names.

        @return:            List of all command names.
        """
        names = self._commandWords.keys()
        names.sort()

        return names

    def removeCommand(self, name):
        """
        Removes a command by name.

        @precondition:      isCommand()

        @param name:        Name of command.
        """
        if not self.isCommand(name):
            errorMsg = "Cannot remove '%s' from CommandWords; command not recognized."
            raise AssertionError(errorMsg)
        del self._commandWords[name]

    def isCommand(self, name):
        """
        Determines if command with a given name
        has been defined.

        @param name:    Name of command.
        @return:        True if command has been defined,
                        False otherwise.
        """
        exists = name in self._commandWords.keys()
        return exists
