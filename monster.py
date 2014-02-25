#!/usr/bin/python

class Monster(object):
    """
    A generic monster to be used as a parent for specific future monster classes.
    """

    def __init__(self, name, description, experience):
        """
        Initializes an item object.

        @param name:        Name of monster.
        @param description: Description of monster.
        @param experience:  Experienced gained for defeating monster.
        """
        if (not name) or (not description) or (not experience):
            raise AssertionError("Monster must have name, description, and experience.")
        if experience < 1:
            errorMsg = "Invalid experience for monster (%s); experience must be positive integer." % experience
            raise AssertionError(errorMsg)

        self._name = name
        self._description = description
        self.experience = experience

    def getName(self):
        """
        Gets monster name.

        @return: Monster's name.
        """
        return self._name

    def getDescription(self):
        """
        Gets monster's description.

        @return: Monster's description.
        """
        return self._description

    def getExperience(self):
        """
        Gets monster's experience.

        @return: Monster's experience.
        """
        return self._experience
