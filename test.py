#!/usr/bin/python

import unittest
from mock import (MagicMock, patch)

class GameTest(unittest.TestCase):
    """
    Tests Game class.
    """

    def testNextTurn(self):
        from game import Game
        g = Game()

        #Create mock objects
        helpCommand = MagicMock()
        helpCommand.execute = MagicMock()
        g._parser.getNextCommand = MagicMock(return_value=helpCommand)

        g._nextTurn()
        self.assertTrue(helpCommand.execute.called, "Game._nextTurn() failed to execute command")


class ParserTest(unittest.TestCase):
    """
    Tests Parser class.
    """

    def testGetNextCommand(self):
        from parser import Parser
        commandWords = MagicMock()
        p = Parser(commandWords)

        #Create mock objects
        #raw_input = MagicMock(side_effect=["unrecognized command", "good command"])
        p._commandRecognized = MagicMock(side_effect=[False,True])
        fakeCommand = MagicMock()
        p._commandWords.getCommand = MagicMock(return_value=fakeCommand) 

        #Patch raw_input and call getNextCommand()
        rawInputMock = MagicMock(side_effect=["unrecognized cmd", "valid cmd"])
        with patch('parser.raw_input', create=True, new=rawInputMock):
            command = p.getNextCommand()

        #Assert calls made
        errorMsg = "Expected raw_input to be called twice."
        self.assertEqual(rawInputMock.call_count, 2, errorMsg)
        errorMsg = "Expected Parser._commandRecognized() to be called twice."
        self.assertEqual(p._commandRecognized.call_count, 2, errorMsg)
        errorMsg = "Parser.getNextCommand() did not respond expected command."
        self.assertEqual(command, fakeCommand, errorMsg)

    def testCommandRecognized(self):
        from parser import Parser
        commandWords = MagicMock()
        commandWords.isCommand = MagicMock(return_value=True)
        p = Parser(commandWords)

        result = p._commandRecognized("valid command")

        errorMsg = "Expected Parser._commandRecognized() to return True."
        self.assertTrue(result, errorMsg) 


class ItemTest(unittest.TestCase):
    """
    Tests Item class.
    """

    def testItem(self):
        from item import Item
        name = "Generic item"
        description = "Generic description"
        weight = 9

        item = Item(name, description, weight)

        errorMsg = "Expected item name to be '%s'." % name
        self.assertEqual(item.getName(), name, errorMsg)
        errorMsg = "Expected item description to be '%s'." % description 
        self.assertEqual(item.getDescription(), description, errorMsg)
        errorMsg = "Expected item weight to be '%s'." % weight 
        self.assertEqual(item.getWeight(), weight, errorMsg)


class ItemsTest(unittest.TestCase):
    """
    Tests Items class.
    """

    INITIAL_COUNT = 3
    INITIAL_WEIGHT = 4

    def setUp(self):
        from item import Item
        from items import Items

        sword = Item("sword", "made by elves", 2)
        helmet = Item("helmet", "made by men", 1)
        potion = Item("potion", "restores health", 1)

        self._itemList = [sword, helmet, potion]
        self._items = Items([sword, helmet, potion])

    def tearDown(self):
        self._itemList = self._items = None

    def testInitItems(self):
        errorMsg = "Items object has more objects than it was given " \
                    "during initialization."
        self.assertEqual(len(self._items._items), ItemsTest.INITIAL_COUNT, errorMsg)

        errorMsg = "Items object does not include all objects given " \
                    "during initialization."
        for item in self._itemList:
            self.assertTrue(item in self._items._items, errorMsg)

    def testCountItems(self):
        expectedCount = ItemsTest.INITIAL_COUNT
        actualCount = self._items.count()
        
        errorMsg = "Actual count and expected count different for Items object."
        self.assertEqual(expectedCount, actualCount, errorMsg)

    def testAddRemoveContainsItems(self):
        from item import Item
        antidote = Item("antidote", "cures poison", 1)

        #Verify item not included in collection
        errorMsg = "Items.containsItem() claimed to contain item not present."
        self.assertFalse(self._items.containsItem(antidote), errorMsg)

        #Add item
        self._items.addItem(antidote)

        errorMsg = "Items.containsItem() failed to identify existing item." 
        self.assertTrue(self._items.containsItem(antidote), errorMsg)

        #Remove item
        self._items.removeItem(antidote)

        errorMsg = "Items.containsItem() claimed to contain item not present."
        self.assertFalse(self._items.containsItem(antidote), errorMsg)

    def testItemsWeight(self):
        from item import Item 

        errorMsg = "Initial weight of Items object incorrect."
        expectedWeight = ItemsTest.INITIAL_WEIGHT
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

        heavyRock = Item("heavy rock", "weighs a ton", 2000)

        #Add item
        self._items.addItem(heavyRock)

        errorMsg = "Items.weight() reported incorrect weight." 
        expectedWeight += 2000
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

        #Remove item
        self._items.removeItem(heavyRock)

        expectedWeight -= 2000
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)


    def testItemsIter(self):
        #Verify iterator returns by Items object visits the exact
        #collection of objects added to Items

        #(Implicitly) use iterator in for loop
        for item in self._items:
            #Verify item returned is recognized
            errorMsg = "Items iterator returned unrecognized object."
            self.assertTrue(item in self._itemList, errorMsg)

            #Remove item from original list of items
            self._itemList.remove(item)

        #Assert all items are accounted for
        errorMsg = "Items object contained Item not added during initialization."
        self.assertEqual(len(self._itemList), 0, errorMsg)

if __name__ == '__main__':
    #Supress output from game with "buffer=true"
    unittest.main(buffer=True)
