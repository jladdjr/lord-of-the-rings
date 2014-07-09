#!/usr/bin/python

class Command(object):
    """
    Parent class for all Command objects.
    """
    def __init__(self, name, explanation, time = False):
        """
        Initializes new command object.

        @param name:          Command name.
        @param explanation:   Explanation of command.
        @param time:          True if time passes with command.
                              False otherwise.
        """
        self._name = name
        self._explanation = explanation
        self._time = time

    def getName(self):
        """
        Returns command's name.
        
        @return:    Command name.
        """
        return self._name

    def getExplanation(self):
        """
        Returns command's explanation.
        
        @return:    Command explanation.
        """
        return self._explanation

    def getTime(self):
        """
        Returns time attribute of command.

        @return:   Time attribute of command. Represents
                   whether time is passing with command
                   execution.
        """
        return self._time

    def execute(self):
        """
        Default execute method. By default,
        does nothing.

        This method should be overridden by child classes.
        """
        pass