#!/usr/bin/python

import space_dictionary

class Space(object):
    """
    A given location on the map. Connects with other spaces
    to form larger geographic areas.
    """
    #name is the name of the object. this gets overwritten each time a space is created.
    self.name = 'space'
    def __init__(self):
        self._directions = space_dictionary.dictionary[name]
        print self._directions



def chris_room(Space):
    self.name = 'chris_room'
    #make sure to define the space name before the __init__ statement!!!
    Space.__init__(self)
    self.description = 'This is a description of this room, including what you are encountering when you enter it'
