#!/usr/bin/python

class Command(object):
    """
    Parent class for all Command objects.
    """

    def __init__(self, name, explanation):
        """
        Initializes new command object.

        @param name:        Command name.
        @param explanation: Explanation of command.
        """
        self._name = name
        self._explanation = explanation

    def getName(self):
        """
        Returns command's name.
        """
        return self._name

    def getExplanation(self):
        """
        Returns command's explanation.
        """
        return self._explanation

    def execute(self):
        """
        Default execute method. By default,
        does nothing.

        This method should be overridden by child class.
        """
        pass
