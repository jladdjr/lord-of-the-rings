#!/usr/bin/python

import unittest
import signal

import xmlrunner
from mock import (MagicMock, patch)

class GameTest(unittest.TestCase):
    """
    Tests game class.

    A few iterations:
    -testGame1: Command does not involve passage of time.
    -testGame2: Command does involve passage of time. Chance of battle = 0%.
    -testGame3: Command does involve passage of time. Chance of battle = 100%.
    """
    def testGame1(self):
        """
        Testing that helpCommand.execute.called when command does not
        involve passage of time. 
        """
        from game import Game
        g = Game()

        #Create mock objects
        helpCommand = MagicMock()
        helpCommand.execute = MagicMock()
        helpCommand._time = False
        battle = MagicMock()
        g._parser.getNextCommand = MagicMock(return_value=helpCommand)

        g._nextTurn()
        errorMsg = "battle should not have been called but was."
        self.assertFalse(battle.called, errorMsg)
        errorMsg = "Game._nextTurn() failed to execute command"
        self.assertTrue(helpCommand.execute.called, errorMsg)
        
    def testCase2(self):
        """
        Testing that helpCommand.execute.called when command involves
        a passing of time. Battle probability = 0%. 
        """
        from game import Game
        from space import Space
        from player import Player
        from battle_engine import battle
        
        g = Game()
        space = Space("Shire", "Home of the Russians", "Eregion", battleProbability = 0)
        player = Player("Russian", space)
        
        #Create mock objects
        helpCommand = MagicMock()
        helpCommand.execute = MagicMock()
        helpCommand._time = True
        battle = MagicMock()
        g._parser.getNextCommand = MagicMock(return_value=helpCommand)

        g._nextTurn()
        errorMsg = "battle should not have been called but was."
        self.assertFalse(battle.called, errorMsg)
        errorMsg = "Game._nextTurn() failed to execute command"
        self.assertTrue(helpCommand.execute.called, errorMsg)

    def testCase3(self):
        """
        Testing that helpCommand.execute.called when command involves
        a passing of time. Battle probability = 100%.
        """
        from game import Game
        from space import Space
        from player import Player
        from battle_engine import battle

        g = Game()
        space = Space("Shire", "Home of the Russians", "Eregion", battleProbability = 1)
        player = Player("Russian", space)
        
        #Create mock objects
        helpCommand = MagicMock()
        helpCommand.execute = MagicMock()
        helpCommand._time = True
        battle = MagicMock()
        g._parser.getNextCommand = MagicMock(return_value=helpCommand)

        g._nextTurn()
        errorMsg = "battle was supposed to have been called but was not."
        self.assertTrue(battle.called, errorMsg)
        errorMsg = "Game._nextTurn() failed to execute command"
        self.assertTrue(helpCommand.execute.called, errorMsg)
    
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
        p._commandRecognized = MagicMock(side_effect=[False, True])
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
        from items.item import Item
        
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

class ItemSetTest(unittest.TestCase):
    """
    Tests ItemSet class.
    """
    INITIAL_COUNT = 3
    INITIAL_WEIGHT = 4

    def setUp(self):
        from items.item import Item
        from items.item_set import ItemSet

        sword = Item("sword", "made by elves", 2)
        helmet = Item("helmet", "made by men", 1)
        potion = Item("potion", "restores health", 1)

        self._itemList = [sword, helmet, potion]
        self._items = ItemSet([sword, helmet, potion])

    def tearDown(self):
        self._itemList = self._items = None

    def testInitItemSet(self):
        errorMsg = "ItemSet object has more objects than it was given " \
                    "during initialization."
        self.assertEqual(len(self._items._items), ItemSetTest.INITIAL_COUNT, errorMsg)

        errorMsg = "ItemSet object does not include all objects given " \
                    "during initialization."
        for item in self._itemList:
            self.assertTrue(item in self._items._items, errorMsg)

    def testCountItems(self):
        expectedCount = ItemSetTest.INITIAL_COUNT
        actualCount = self._items.count()
        
        errorMsg = "Actual count and expected count different for ItemSet object."
        self.assertEqual(expectedCount, actualCount, errorMsg)

    def testAddRemoveContainsItems(self):
        from items.item import Item
        antidote = Item("antidote", "cures poison", 1)

        #Verify item not included in collection
        errorMsg = "ItemSet.containsItem() claimed to contain item not present."
        self.assertFalse(self._items.containsItem(antidote), errorMsg)

        #Add item
        self._items.addItem(antidote)

        errorMsg = "ItemSet.containsItem() failed to identify existing item." 
        self.assertTrue(self._items.containsItem(antidote), errorMsg)

        errorMsg = "ItemSet.containsItemWithName() failed to identify existing item."
        self.assertTrue(self._items.containsItemWithName("antidote"), errorMsg)

        #Remove item
        self._items.removeItem(antidote)

        errorMsg = "ItemSet.containsItem() claimed to contain item not present."
        self.assertFalse(self._items.containsItem(antidote), errorMsg)

    def testItemsWeight(self):
        from items.item import Item 

        errorMsg = "Initial weight of ItemSet object incorrect."
        expectedWeight = ItemSetTest.INITIAL_WEIGHT
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

        heavyRock = Item("heavy rock", "weighs a ton", 2000)

        #Add item
        self._items.addItem(heavyRock)

        errorMsg = "ItemSet.weight() reported incorrect weight." 
        expectedWeight += 2000
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

        #Remove item
        self._items.removeItem(heavyRock)

        expectedWeight -= 2000
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

    def testItemSetIter(self):
        #Verify iterator returns by ItemSet object visits the exact
        #collection of objects added to ItemSet

        #(Implicitly) use iterator in for loop
        for item in self._items:
            #Verify item returned is recognized
            errorMsg = "ItemSet iterator returned unrecognized object."
            self.assertTrue(item in self._itemList, errorMsg)

            #Remove item from original list of items
            self._itemList.remove(item)

        #Assert all items are accounted for
        errorMsg = "ItemSet object contained Item not added during initialization."
        self.assertEqual(len(self._itemList), 0, errorMsg)

class SpaceTest(unittest.TestCase):
    """
    Test for spaces.
    """
    def testItems(self):
        from space import Space
        from items.item import Item

        #Prepare items
        blade = Item("blade", "appears to be dull", 1)
        bow = Item("bow", "long bow", 2) 

        #Create space
        space = Space("shire", "Home of the Hobbits.", "Mordor")
        items = space.getItems()

        #Assert space initially empty
        errorMsg = "New space contains items; should be empty" 
        self.assertEqual(items.count(), 0, errorMsg)

        errorMsg = "Space claims to contain item even though it is empty."
        self.assertFalse(space.containsItem(blade), errorMsg)
        self.assertFalse(space.containsItem(bow), errorMsg)

        #Add blade
        space.addItem(blade)
        errorMsg = "Space failed to report that it contained item known to exist."
        self.assertTrue(space.containsItem(blade), errorMsg)

        #Add bow 
        space.addItem(bow)
        self.assertTrue(space.containsItem(bow), errorMsg)

        #Get room's items. Assert blade and bow exist
        items = space.getItems()
        self.assertEqual(items.count(), 2, "Room should contain exactly two items.")
        self.assertTrue(items.containsItem(blade), "Could not find blade in room's set of items.")
        self.assertTrue(items.containsItem(bow), "Could not find bow in room's set of items.")

        #Remove blade
        space.removeItem(blade)
        errorMsg = "Space claims to have item that was removed."
        self.assertFalse(space.containsItem(blade), errorMsg)
        errorMsg = "Space missing item that should still exist."
        self.assertTrue(space.containsItem(bow), errorMsg)

        #Get room's items. Assert only bow exists
        items = space.getItems()
        self.assertEqual(items.count(), 1, "Room should contain exactly one item.")
        self.assertFalse(items.containsItem(blade), 
                "Blade found in room (even though it was removed).")
        self.assertFalse(items.containsItemWithName("blade"), "Blade found in room (even though it was removed).")
        self.assertTrue(items.containsItem(bow), "Could not find bow in room's set of items.")

    def testRegion(self):
        from space import Space
        import constants

        space = Space("West Emnet", "Horses for riding", "Rohan")

        errorMsg = "space.getRegion() should return 'Rohan.'"
        self.assertEquals(space.getRegion(), "Rohan", errorMsg)

    def testCities(self):
        from space import Space
        from cities.city import City

        #Create city
        newYorkCity = City("New York City", "An enormous city", "Come test here")

        #Create space
        newYork = Space("New  York", "A huge space", "Welcome to our space", city = newYorkCity)

        #Assert city in space
        errorMsg = "space.getCity() should return newYorkCity but does not."
        self.assertEqual(newYork.getCity(), newYorkCity, errorMsg)

    def testUniquePlace(self):
        from space import Space
        from unique_place import UniquePlace

        #Create UniquePlace
        dmitriyHouse = UniquePlace("Dmitriy's House", "Lots of vodka", "[Knocks once.]")

        #Create space
        chocolateMountain = Space("Chocolate Mountain", "Chocolate rain here", "Welcome.", uniquePlace = dmitriyHouse)
        
        #Assert uniquePlace in space
        errorMsg = "space.getUniquePlace() should return dmitriyHouse but does not."
        self.assertEqual(chocolateMountain.getUniquePlace(), dmitriyHouse, errorMsg)
        
class MovementTest(unittest.TestCase):
    """
    Tests the movement methods of space and movement commands.  
    """
    def testMovement(self):
        """
        General, encompassing test for movement, including movement commands.
        """
        from space import Space
        from player import Player
        from commands.north_command import NorthCommand
        from commands.south_command import SouthCommand
        from commands.west_command import WestCommand
        from commands.east_command import EastCommand
        from constants import Direction
        
        space = Space("Shire", "Home of the hobbits", "Mordor")
        player = Player("Russian", space)
        
        northCmd = NorthCommand("North", "Moves player north", player)
        southCmd = SouthCommand("South", "Moves player south", player)
        eastCmd = EastCommand("East", "Moves player east", player)
        westCmd = WestCommand("West", "Moves player west", player)
        
        #Non-movement case - ports not created
        errorMsg = "Player should still be in space but is not."

        northCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = space

        southCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = space

        eastCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = space

        westCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = Space

        #Create destinations and two-way ports
        north = Space("North Space", "Very cold", "Welcome")
        south = Space("South Space", "Very warm", "Welcome")
        east = Space("East Space", "Very mountainous", "Welcome")
        west = Space("West Space", "Coastal", "Welcome")

        space.createExit("north", north, outgoingOnly = False)
        space.createExit("south", south, outgoingOnly = False)
        space.createExit("east", east, outgoingOnly = False)
        space.createExit("west", west, outgoingOnly = False)

        #Test getExit() for destination spaces
        errorMsg = "getExit() test failed."
        self.assertEqual(north.getExit("south"), space, errorMsg)
        self.assertEqual(south.getExit("north"), space, errorMsg)
        self.assertEqual(east.getExit("west"), space, errorMsg)
        self.assertEqual(west.getExit("east"), space, errorMsg)

        #Test ports created using _isExit() for space
        errorMsg = "Ports are supposed to be created but are not - using _isExit()."
        self.assertEqual(space._isExit("north"), True, errorMsg)
        self.assertEqual(space._isExit("south"), True, errorMsg)
        self.assertEqual(space._isExit("east"), True, errorMsg)
        self.assertEqual(space._isExit("west"), True, errorMsg)

        #Test ports created without using direct access for Space
        errorMsg = "Ports are supposed to be created but were not - by direct attribute access."
        self.assertEqual(space._exits[Direction.NORTH], north, errorMsg)
        self.assertEqual(space._exits[Direction.SOUTH], south, errorMsg)
        self.assertEqual(space._exits[Direction.EAST], east, errorMsg)
        self.assertEqual(space._exits[Direction.WEST], west, errorMsg)

        #Test ports created without using direct access for destination Spaces
        errorMsg = "Ports are supposed to have been created but were not - by direct attribute access for destination spaces."
        self.assertEqual(north._exits[Direction.SOUTH], space, errorMsg)
        self.assertEqual(south._exits[Direction.NORTH], space, errorMsg)
        self.assertEqual(east._exits[Direction.WEST], space, errorMsg)
        self.assertEqual(west._exits[Direction.EAST], space, errorMsg)
                                      
        #Test two-way movement
        player._location = space
        northCmd.execute()
        errorMsg = "Player should be in north space but is not."
        self.assertEqual(player.getLocation(), north, errorMsg)
        southCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)

        player._location = space
        southCmd.execute()
        errorMsg = "Player should be in south space but is not."
        self.assertEqual(player.getLocation(), south, errorMsg)
        northCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)

        player._location = space
        eastCmd.execute()
        errorMsg = "Player should be in east space but is not."
        self.assertEqual(player.getLocation(), east, errorMsg)
        westCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)

        player._location = space
        westCmd.execute()
        errorMsg = "Player should be in west space but is not."
        self.assertEqual(player.getLocation(), west, errorMsg)
        eastCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)

        #Test clearExit() method
        errorMsg = "Port should have been cleared but was not."

        space.clearExit("north")
        self.assertTrue(space._exits[Direction.North], None, errorMsg)
                        
        space.clearExit("south")
        self.assertTrue(space._exits[Direction.South], None, errorMsg)
        
        space.clearExit("east")
        self.assertTrue(space._exits[Direction.East], None, errorMsg)
        
        space.clearExit("west")
        self.assertTrue(space._exits[Direction.West], None, errorMsg)

        #Test _isExit() method where there are no ports
        errorMsg = "_isExit() failed to return the correct port where no ports exist."
        self.assertTrue(space._isExit("north"), None, errorMsg)
        self.assertTrue(space._isExit("south"), None, errorMsg)
        self.assertTrue(space._isExit("east"), None, errorMsg)
        self.assertTrue(space._isExit("west"), None, errorMsg)

    def testMovement2(self):
        """
        Tests for one-way ports and one-way movement.
        """
        from space import Space
        from player import Player
        from commands.north_command import NorthCommand
        from commands.south_command import SouthCommand
        from commands.west_command import WestCommand
        from commands.east_command import EastCommand
        
        space = Space("Shire", "Home of the hobbits", "Mordor")
        player = Player("Russian", space)
        
        northCmd = NorthCommand("North", "Moves player north", player)
        southCmd = SouthCommand("South", "Moves player south", player)
        eastCmd = EastCommand("East", "Moves player east", player)
        westCmd = WestCommand("West", "Moves player west", player)
        
        north = Space("North Space", "Very cold", "Welcome")
        south = Space("South Space", "Very warm", "Welcome")
        east = Space("East Space", "Very mountainous", "Welcome")
        west = Space("West Space", "Coastal", "Welcome")
        
        #Create one-way ports
        space.createExit("north", north, outgoingOnly = True)
        space.createExit("south", south, outgoingOnly = True)
        space.createExit("east", east, outgoingOnly = True)
        space.createExit("west", west, outgoingOnly = True)

        #Test one-way movement
        player._location = space
        northCmd.execute()
        errorMsg = "Player should be in north space but is not."
        self.assertEqual(player.getLocation(), north, errorMsg)
        southCmd.execute()
        errorMsg = "Player should be in north space but is not."
        self.assertEqual(player.getLocation(), north, errorMsg)
        
        player._location = space
        southCmd.execute()
        errorMsg = "Player should be in south space but is not."
        self.assertEqual(player.getLocation(), south, errorMsg)
        northCmd.execute()
        errorMsg = "Player should be in south but is not."
        self.assertEqual(player.getLocation(), south, errorMsg)
        
        player._location = space
        eastCmd.execute()
        errorMsg = "Player should be in east space but is not."
        self.assertEqual(player.getLocation(), east, errorMsg)
        westCmd.execute()
        errorMsg = "Player should be in east but is not."
        self.assertEqual(player.getLocation(), east, errorMsg)
        
        player._location = space
        westCmd.execute()
        errorMsg = "Player should be in west space but is not."
        self.assertEqual(player.getLocation(), west, errorMsg)
        eastCmd.execute()
        errorMsg = "Player should be in west but is not."
        self.assertEqual(player.getLocation(), west, errorMsg)

class PickUpTest(unittest.TestCase):
    """
    Test PickUp class.
    """
    def testExecute(self):
        """
        Test case: player picks up an item that may be picked up.
        """
        from space import Space
        from player import Player
        from items.item import Item
        from commands.pick_up_command import PickUpCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        item = Item("Dagger", "A trusty blade", 2)
        pickUpCmd = PickUpCommand("pick up", "Picks up an object", player)
        
        space.addItem(item)

        #Test pre-test conditions
        self.assertTrue(space.containsItem(item), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(item), "Player inventory should not have item but does.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player equipment should not have item but does.")
            
        #Execute pickUpCmd and assert item in player inventory but not in space and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.pick_up_command.raw_input', create=True, new=rawInputMock):
            pickUpCmd.execute()
            
        self.assertFalse(space.containsItem(item), "Space should not have item but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(item), "Player should have item in inventory but does not.")

        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player should not have item in equipment but does.")
        
    def testExecute2(self):
        """
        Test case: player tries to pick up non-existent item.
        """
        from space import Space
        from player import Player
        from commands.pick_up_command import PickUpCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        pickUpCmd = PickUpCommand("pick up", "Picks up an object", player)

        #Test pre-test conditions
        self.assertEqual(space._items._items, [], "Space should have no items but does.")
        self.assertEqual(player._inventory._items, [], "player._inventory should have no items but does.")
        self.assertEqual(player._equipped._items, [], "player._equipped should have no items but does.")
            
        #Execute pickUpCmd and test that nothing has changed
        rawInputMock = MagicMock(return_value="Shiny Acorns")
        with patch('commands.pick_up_command.raw_input', create=True, new=rawInputMock):
            pickUpCmd.execute()
            
        self.assertEqual(space._items._items, [], "Space should have no items but does - post-test.")
        self.assertEqual(player._inventory._items, [], "player._inventory should have no items but does - post-test.")
        self.assertEqual(player._equipped._items, [], "player._equipped should have no items but does - post-test.")
        
class DropTest(unittest.TestCase):
    """
    Test Drop class.
    """
    def testExecute(self):
        """
        Test case where items in inventory and equipment.
        """
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield of Faith", "Quenches fiery darts", 2, 2, 2) 

        player.addToInventory(weapon)
        player.equip(weapon)
        player.addToInventory(armor)
        player.equip(armor)

        #Test pre-test conditions
        self.assertFalse(space.containsItem(weapon), "Space should not have weapon but does.")
        self.assertFalse(space.containsItem(armor), "Space should not have armor but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have weapon but does not.")
        self.assertTrue(inventory.containsItem(armor), "Inventory should have armor but does not.")

        equipped = player.getEquipped()
        self.assertTrue(equipped.containsItem(weapon), "Equipped should have weapon but does not.")
        self.assertTrue(equipped.containsItem(armor), "Equipped should have armor but does not.")

        #Assert item in space but not in player inventory and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        self.assertTrue(space.containsItemString("Dagger"), "Space should have weapon but does not.")
        self.assertTrue(space.containsItemString("Shield of Faith"), "Space should have armor but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have weapon but does.")
        self.assertFalse(inventory.containsItem(armor), "Inventory should not have armor but does.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipment should not have armor but does.")
        self.assertFalse(equipped.containsItem(armor), "Equipment should not have armor but does.")

    def testExecute2(self):
        """
        Test case where items in inventory but not in equipment.
        """
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield of Faith", "Quenches fiery darts", 2, 2, 2)

        player.addToInventory(weapon)
        player.addToInventory(armor)
        
        #Test pre-test conditions
        self.assertFalse(space.containsItem(weapon), "Space should not have weapon but does.")
        self.assertFalse(space.containsItem(armor), "Space should not have armor but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have weapon but does not.")
        self.assertTrue(inventory.containsItem(armor), "Inventory should have armor but does not.")

        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipped should not have weapon but does.")
        self.assertFalse(equipped.containsItem(armor), "Equipped should not have armor but does.")

        #Assert item in space but not in player inventory and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        self.assertTrue(space.containsItemString("Dagger"), "Space should have weapon but does not.")
        self.assertTrue(space.containsItemString("Shield of Faith"), "Space should have armor but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have weapon but does.")
        self.assertFalse(inventory.containsItem(armor), "Inventory should not have armor but does.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipment should not have weapon but does.")
        self.assertFalse(equipped.containsItem(armor), "Equipment should not have armor but does.")

    def testExecute3(self):
        """
        Test case for when player does not have item in either inventory or equipment.
        """
        from space import Space
        from player import Player
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        #Test pre-test conditions
        self.assertEqual(space._items._items, [], "Space should have no items but does.")
        self.assertEqual(player._inventory._items, [], "player._inventory should have no items but does.")
        self.assertEqual(player._equipped._items, [], "player._equipped should have no items but does.")

        #Attempt to drop item that does not exist
        rawInputMock = MagicMock(return_value="Melted Cheese")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        self.assertEqual(space._items._items, [], "Space should have no items but does - post-test.")
        self.assertEqual(player._inventory._items, [], "player._inventory should have no items but does - post-test.")
        self.assertEqual(player._equipped._items, [], "player._equipped should have no items but does - post-test.")

class EquipTest(unittest.TestCase):
    """
    Tests Equip Command.
    """
    def testPositiveCase(self):
        """
        Testcase: for equipping an item that may be equipped.
        """
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.equip_command import EquipCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "Very faithful", 2, 2, 2) 

        inventory = player.getInventory()
        inventory.addItem(weapon)
        inventory.addItem(armor)

        #Equipping equippable items
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
            
        equipped = player.getEquipped()

        self.assertTrue(inventory.containsItem(weapon), "Inventory should still have weapon but does not.")
        self.assertTrue(inventory.containsItem(armor), "Inventory should still have armor but does not.")
        
        self.assertTrue(equipped.containsItem(weapon), "Player failed to equip equipable weapon.")
        self.assertTrue(equipped.containsItem(armor), "Player failed to equip equipable armor.")
        
    def testNegativeCase1(self):
        """
        Attempting to equip items not in inventory.
        """
        from player import Player
        from space import Space
        from commands.equip_command import EquipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        #Trying to equip items not in inventory
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have weapon.")
        self.assertFalse(inventory.containsItem(armor), "Inventory should not have armor.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Weapon should not be in equipped.")
        self.assertFalse(equipped.containsItem(armor), "Armor should not be in equipped.")

    def testNegativeCase2(self):
        """
        Attempting to equip an item that may not be equipped.

        In this instance, item is of the Item class.
        """
        from player import Player
        from space import Space
        from items.item import Item
        from commands.equip_command import EquipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)
        
        item = Item("Charm", "Unknown effects", 1)
        
        inventory = player.getInventory()
        inventory.addItem(item)

        #Trying to equip item that cannot be equipped
        rawInputMock = MagicMock(return_value="Charm")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        self.assertTrue(inventory.containsItem(item), "Inventory should have item.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player equipped item of Item class.")

    def testNegativeCase3(self):
        """
        Attempting to equip items that are already equipped.
        """
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.equip_command import EquipCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2)

        inventory = player.getInventory()
        inventory.addItem(weapon)
        inventory.addItem(armor)
        
        equipped = player.getEquipped()
        equipped.addItem(weapon)
        equipped.addItem(armor)

        #Test - preconditions
        errorMsg = "Weapon and armor are supposed to be in inventory but are not."
        self.assertTrue(weapon in inventory._items, errorMsg)
        self.assertTrue(armor in inventory._items, errorMsg)
        errorMsg = "Inventory is supposed to have two items."
        self.assertEqual(player._inventory.conut(), 2, errorMsg)
        
        errorMsg = "Weapon is supposed to be in player._equipped but is not."
        self.assertTrue(weapon in player._equipped, errorMsg)
        errorMsg = "Armor is supposed to be in player._equipped but it is not."
        self.assertTrue(armor in player._equipped, errorMsg)
        errorMsg = "player._equipped is supposed to have two items but does not."
        self.assertEqual(player._equipped.count(), 2, errorMsg)

        #Equipping an item that is already equipped
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 
            
        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 

        #Test still only two equipped items
        errorMsg = "Weapon and armor are supposed to be in inventory but are not."
        self.assertTrue(weapon in player._inventory, errorMsg)
        self.assertTrue(armor in player._inventory, errorMsg)
        errorMsg = "Player inventory is only supposed to have two items."
        self.assertEqual(player.inventory.count(), 2, errorMsg)
            
        errorMsg = "Weapon is supposed to be in player._equipped but is not."
        self.assertTrue(weapon in player._equipped, errorMsg)
        errorMsg = "Armor is supposed to be in player._equipped but it is not."
        self.assertTrue(armor in player._equipped, errorMsg)
        errorMsg = "Player is supposed to have two equipped items but lists more."
        self.assertEqual(equipped.count(), 2, errorMsg)

    def testPlayerWeaponStats(self):
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from commands.equip_command import EquipCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        defaultAttack = player._attack
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)
        player.addToInventory(weapon)

        #Test preconditions
        errorMsg = "Weapon should be in player._inventory._items but is not."
        self.assertTrue(weapon in player._inventory._items, errorMsg)
        errorMsg = "Weapon shoud not be in player._equipped._items but is not."
        self.assertTrue(weapon not in player._equipped._items, errorMsg)

        #Equip weapon and check that _totalAttack and _weaponAttack update
        rawInputMock = MagicMock(return_value="Sword of the Spirit")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 

        errorMsg = "Weapon should be in player._inventory._items but is not."
        self.assertTrue(player._inventory.containsItem(weapon), errorMsg)
        errorMsg = "Weapon should be equipped but is not."
        self.assertTrue(player._equipped.containsItem(weapon), errorMsg)

        #Test for change
        errorMsg = "player._attack changed with weapon equip when it should not have."
        self.assertEqual(player._attack, defaultAttack, errorMsg)
        errorMsg = "player._weaponAttack not updated to correct value."
        self.assertEqual(player._weaponAttack, weapon._attack, errorMsg)
        errorMsg = "player._totalAttack not updated to correct value."
        self.assertEqual(player._totalAttack, defaultAttack + weapon._attack, errorMsg)

    def testPlayerArmorStats(self):
        from player import Player
        from space import Space
        from items.armor import Armor
        from commands.equip_command import EquipCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        armor = Armor("Shield of Faith", "For quenching fiery darts", 1, 1, 1)
        player.addToInventory(armor)

        #Test preconditions
        errorMsg = "Armor should be in player._inventory._items but is not."
        self.assertTrue(weapon in player._inventory._items, errorMsg)
        errorMsg = "Armor should not be in player._equipped._items but is not."
        self.assertTrue(weapon not in player._equipped._items, errorMsg)

        #Equip armor and check that player._defense updates
        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        errorMsg = "Armor should be in inventory but is not."
        self.assertTrue(player._inventory.containsItem(weapon), errorMsg)
        errorMsg = "Armor should be equipped but is not."
        self.assertTrue(player._equipped.containsItem(armor), errorMsg)
        
        #Test for change
        errorMsg = "player._armorDefense stat was not updated correctly."
        self.assertEqual(player._armorDefense, armor._defense, errorMsg)
                         
class UnequipTest(unittest.TestCase):
    """
    Tests Unequip Command.
    """
    def testPositiveCase(self):
        """
        Unequipping an unequippable item.
        """
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2)

        player.addToInventory(weapon)
        player.addToInventory(armor)
        player.equip(weapon)
        player.equip(armor)

        #Test preconditions
        errorMsg = "Weapon and Armor should be in inventory but are not."
        self.assertTrue(weapon in player._inventory._items, errorMsg)
        self.assertTrue(armor in player._inventory._items, errorMsg)

        errroMsg = "Weapon and Armor should be in equipped but are not."
        self.assertTrue(weapon in player._equipped._items, errorMsg)
        self.assertTrue(armor in player._equipped._items, errorMsg)
        
        #Attempting to unequip item not currently equipped
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()
        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        errorMsg = "Weapon and Armor should be in inventory but are not."
        self.assertTrue(weapon in player._inventory._items, errorMsg)
        self.assertTrue(armor in player._inventory._items, errorMsg)

        errorMsg = "Player should not have weapon in equipped."
        self.assertFalse(player._equipped.containsItem(weapon), errorMsg)
        errorMsg = "Player should not have armor in equipped."
        self.assertFalse(player._equipped.containsItem(armor), errorMsg)
        
    def testNegativeCase(self):
        """
        Attempting to unequip an item that is not currently equipped.
        Item is in inventory. 
        """
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2)

        player.addToInventory(weapon)
        player.addToInventory(armor)

        #Test preconditions
        errorMsg = "Weapon and Armor should be in inventory but are not."
        self.assertTrue(weapon in player._inventory._items, errorMsg)
        self.assertTrue(armor in player._inventory._items, errorMsg)
        
        #Attempting to unequip item not currently equipped
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()
        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        errorMsg = "Weapon and Armor should be in inventory but are not."
        self.assertTrue(weapon in player._inventory._items, errorMsg)
        self.assertTrue(armor in player._inventory._items, errorMsg)

        errorMsg = "Player should not have weapon in equipped but does."
        self.assertFalse(player._equipped.containsItem(weapon), errorMsg)
        errorMsg = "Player should not have armor in equipped but does."
        self.assertFalse(player._equipped.containsItem(armor), errorMsg)
        
    def testNegativeCase2(self):
        """
        Attempting to unequip an item that is not currently equipped.
        Item is not in inventory. 
        """
        from player import Player
        from space import Space
        from commands.unequip_command import UnequipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        #Test preconditions
        errorMsg = "Inventory should be empty."
        self.assertEqual(player._inventory.count(), 0, errorMsg)
        errorMsg = "Equipment should be empty."
        self.assertEqual(player._equipped.count(), 0, erroMsg)
        
        #Attempting to unequip item not currently equipped
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()
        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        errorMsg = "Inventory should still be empty."
        self.assertEqual(player._inventory.count(), 0, errorMsg)
        errorMsg = "Equipment should still be empty."
        self.assertEqual(player._equipped.count(), 0, erroMsg)
        
    def testPlayerWeaponStats(self):
        """
        Tests that player-specific attributes such as player._totalAttack
        and player._weaponAttack reset with unequip.
        """
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from commands.unequip_command import UnequipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("Unequip", "Unequips item in inventory to player", player)

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)
        player.addToInventory(weapon)
        player.equip(weapon)

        #Test preconditions
        errorMsg = "Weapon should be in inventory and equipped."
        self.assertTrue(weapon in player._inventory._items, errorMsg)
        self.assertTrue(armor in player._equipped._items, errorMsg)

        #Test player-specific attributes to change back to defaults
        rawInputMock = MagicMock(return_value="Sword of the Spirit")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute() 

        errorMsg = "player._weaponAttack should be zero but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "player._totalAttack should be player._attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)
        
    def testPlayerArmorStats(self):
        """
        Tests that player._defense resets with unequip.
        """
        from player import Player
        from space import Space
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("Unequip", "Unequips item in inventory to player", player)

        armor = Armor("Shield of Faith", "For quenching fiery darts", 1, 1, 1)
        player.addToInventory(armor)
        player.equip(armor)

        #Test preconditions
        errorMsg = "Armor should be in player inventory and equipped."
        self.assertTrue(armor in player._inventory._items, errorMsg)
        self.assertTrue(armor in player._equipped._items , errorMsg)

        #Test for change back to player defaults        
        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute() 

        errorMsg = "player._armorDefense should be zero after unequip."
        self.assertEqual(player._armorDefense, 0, errorMsg)

class UsePotionTest(unittest.TestCase):
    """
    Tests UsePotion command.
    """
    def testPostiveCase(self):
        """
        Player has potion and uses potion.
        """
        from commands.use_potion_command import UsePotionCommand
        from space import Space
        from player import Player
        from items.potion import Potion

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        inventory = player.getInventory()
        usePotionCmd = UsePotionCommand("use potion", "Uses potion in inventory.", player)
        
        player._maxHp = 20
        player._hp = 1
        healing = 10
        correctFinalHp = player._hp + healing
        
        potion = Potion("Enormous Potion", "So big", 1, healing, 10)
        player._inventory.addItem(potion)

        #Test preconditions
        errorMsg = "Potion should be in player._inventory but is not."
        self.assertTrue(potion in player._inventory._items, errorMsg)
        errorMsg = "player._hp should be 1 but is not."
        self.assertEqual(player._hp, 1, errorMsg)
        
        #Test for proper change in player._inventory and player._hp
        rawInputMock = MagicMock(return_value="Enormous Potion")
        with patch('commands.use_potion_command.raw_input', create = True, new = rawInputMock):
            usePotionCmd.execute()
            
        errorMsg = "Inventory still contains potion when it should not."
        self.assertFalse(inventory.containsItem(potion), errorMsg)
        errorMsg = "Player health not at correct amount."
        self.assertEqual(player._hp, correctFinalHp, errorMsg)

    def testNegativeCase(self):
        """
        Player has no potions in inventory.
        """
        from commands.use_potion_command import UsePotionCommand
        from space import Space
        from player import Player
        from items.potion import Potion
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        usePotionCmd = UsePotionCommand("use potion", "Uses potion in inventory.", player)
        
        player._maxHp = 20
        player._hp = 10
        startingHp = player._hp

        #Test preconditions
        errorMsg = "Player should have no potions."
        self.assertEqual(player._inventory._items, 0, errorMsg)
        errorMsg = "player._hp should be 10 but is not."
        self.assertEqual(player._hp, 10, errorMsg)

        #Tests that player._inventory._items and player._hp do not change
        rawInputMock = MagicMock(return_value="Enormous Potion")
        with patch('commands.use_potion_command.raw_input', create = True, new = rawInputMock):
            usePotionCmd.execute()
            
        errorMsg = "Inventory should still not have any potions."
        self.assertEqual(player._inventory._items, 0, errorMsg)
        errorMsg = "player._hp changed when it should not have."
        self.assertEqual(player._hp, startingHp, errorMsg)
        
class WeaponTest(unittest.TestCase):
    """
    Tests Weapon class.
    """
    def testWeapon(self):
        from items.weapon import Weapon

        sword = Weapon("Sword", "A cheap sword", 3, 2, 1)

        self.assertEqual(sword.getName(), "Sword", "Name did not initialize correctly.")
        self.assertEqual(sword.getDescription(), "A cheap sword", "Description did not initialize correctly.")
        self.assertEqual(sword.getWeight(), 3, "Weight did not initialize correctly.")
        self.assertEqual(sword.getAttack(), 2, "Damage did not initialize correctly.")
        self.assertEqual(sword.getCost(), 1, "Cost did not initialize correctly.")

class ArmorTest(unittest.TestCase):
    """
    Tests Armor class.
    """
    def testArmor(self):
        from items.armor import Armor
        
        shield = Armor("Shield", "A cheap shield", 3, 2, 1)

        #Tests that shield initialized correctly
        self.assertEqual(shield.getName(), "Shield", "Name did not initialize correctly.")
        self.assertEqual(shield.getDescription(), "A cheap shield", "Description did not initialize correctly.")
        self.assertEqual(shield.getWeight(), 3, "Weight did not initialize correctly.")
        self.assertEqual(shield.getDefense(), 2, "Defense did not initialize correctly.")
        self.assertEqual(shield.getCost(), 1, "Cost did not initialize correctly.")

class Potion(unittest.TestCase):
    """
    Tests Potion class.
    """
    def testPotion(self):
        from items.potion import Potion

        potion = Potion("Potion", "A small potion", 3, 2, 1)
        
        #Tests for correct initialization
        self.assertEqual(potion.getName(), "Potion", "Name did not initialize correctly.")
        self.assertEqual(potion.getDescription(), "A small potion", "Description did not initialize correctly.")
        self.assertEqual(potion.getWeight(), 3, "Weight did not initialize correctly.")
        self.assertEqual(potion.getHealing(), 2, "Healing did not initialize correctly.")
        self.assertEqual(potion.getCost(), 1, "Cost did not initialize correctly.")

class PlayerTest(unittest.TestCase):
    """
    Tests Player class.
    """
    def testInit(self):
        from player import Player
        from space import Space
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        errorMsg = "Frodo", "player._name did not initialize correctly."
        self.assertEqual(player._name, errorMsg)
        errorMsg = "player._location did not initialize correctly."
        self.assertEqual(player._location, space, errorMsg)
        errorMsg = "player._money did not initialize correctly."
        self.assertEqual(player._money, constants.STARTING_MONEY, errorMsg)
        
        emptyList = []
        errorMsg = "player._inventory was not initialized correctly."
        self.assertEqual(player._inventory.getItems(), emptyList, errorMsg)
        errorMsg = "player._equipped was not initialized correctly."
        self.assertEqual(player._equipped.getItems(), emptyList, errorMsg)

        errorMsg = "player._experience was not initialized correctly."
        self.assertEqual(player._experience, constants.STARTING_EXPERIENCE, errorMsg)
        errorMsg = "player._level was not initialized correctly."
        self.assertEqual(player._level, constants.STARTING_LEVEL, errorMsg)

        errorMsg = "Player was not created with full health."
        self.assertEqual(player._maxHp, constants.HP_STAT, errorMsg)
        errorMsg = "player._hp was not initialized correctly."
        self.assertEqual(player._hp, constants.HP_STAT, errorMsg)
        errorMsg = "player_attack was not initialized correctly."
        self.assertEqual(player._attack, constants.ATTACK_STAT, errorMsg)

        errorMsg = "player._weaponAttack was not initialized correctly."
        self.assertEqual(player._weaponAttack, constants.STARTING_WEAPON_ATTACK, errorMsg)
        errorMsg = "player._armorDefense was not initialized correctly."
        self.assertEqual(player._armorDefense, constants.STARTING_ARMOR_DEFENSE, errorMsg)
        errorMsg = "player._totalAttack did not initiate correctly."
        self.assertEqual(player._totalAttack, player._attack + player._weaponAttack, errorMsg)
        
    def testAttack(self):
        from player import Player
        from space import Space
        from monsters.monster import Monster
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        monster = MagicMock()
        monster.takeAttack = MagicMock()
        
        #Player attacks monster
        player.attack(monster)
        errorMsg = "Player did not attack monster."
        self.assertTrue(monster.takeAttack.called, errorMsg)

    def testTakeAttack(self):
        """
        Tests player.takeAttack when attack is more than
        player._hp.
        """
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        
        OVERKILL = player._maxHp + 10000

        player.takeAttack(OVERKILL)
        errorMsg = "player._hp should be 0 but is not."
        self.assertEqual(player._hp, 0, errorMsg)

    def testTakeAttack2(self):
        """
        Tests player.takeAttack when attack is less than
        player._hp
        """
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        
        UNDERKILL = player._maxHp - 1

        player.takeAttack(UNDERKILL)
        errorMsg = "player._hp should be 1 but is not."
        self.assertEqual(player._hp, 1, errorMsg)

    def takeAttack3(self):
        """
        Tests player.takeAttack when player is equipped with
        armor.
        """
        from player import Player
        from space import Space
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        armor = Armor("Shield of Faith", "Quenches fiery darts", 2, 2, 2)
        player.equip(armor)

        #Testcase - armorDefense is more than attack
        player._hp = 10
        player.takeAttack(1)
        errorMsg = "Testcase - armorDefense is more than attack failed."
        self.assertEqual(player._hp, 10, errorMsg)
        
        #Testcase - armorDefense is attack
        player._hp = 10
        player.takeAttack(2)
        errorMsg = "Testcase - armorDefense is attack failed."
        self.assertEqual(player._hp, 10, errorMsg)
        
        #Testcase - armorDefense is less than attack
        player._hp = 10
        player.takeAttack(3)
        errorMsg = "Testcase - armorDefense is less than attack failed."
        self.assertEqual(player._hp, 9, errorMsg)
        
    def testIncreaseExperience(self):
        from player import Player
        from space import Space
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        player._updateLevel() = MagicMock()

        #Test that player._experience increases correctly and that _updateLevel() is called
        player.increaseExperience(10000)
        
        errorMsg = "Player experience failed to increase."
        self.assertEqual(player._experience, constants.STARTING_EXPERIENCE + 10000, errorMsg)
        errorMsg = "player._updateLevel() was not called."
        self.assertTrue(player._updateLevel.called, errorMsg)
        
    def testUpdateLevel(self):
        from math import floor
        
        from player import Player
        from space import Space
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        #Determine default player stats
        defaultLevel = player._level
        defaultMaxHp = player._maxHp
        defaultAttack = player._attack
        defaultTotalAttack = player._totalAttack

        #Increase player experience and run player._updateLevel
        originalExperience = player._experience
        player._experience = 10000 + originalExperience
        player._updateLevel()

        #Test that stats have increased
        errorMsg = "Player level did not increase."
        self.assertTrue(player._level > defaultLevel, errorMsg)
        errorMsg = "Player Hp did not increase."
        self.assertTrue(player._maxHp > defaultMaxHp, errorMsg)
        errorMsg = "Player attack did not increase."
        self.assertTrue(player._attack > defaultAttack, errorMsg)
        errorMsg = "Player totalAttack did not increase."
        self.assertTrue(player._totalAttack > defaultTotalAttack, errorMsg)

        #Test for proper player stat change
        errorMsg = "Player level is incorrect."
        self.assertEqual(player._level, floor(player._experience/20) + 1, errorMsg)
        errorMsg = "Player Hp is incorrect."
        self.assertEqual(player._maxHp, player._level * constants.HP_STAT, errorMsg)
        errorMsg = "Player attack is incorrect."
        self.assertEqual(player._attack, player._level * constants.ATTACK_STAT, errorMsg)
        errorMsg = "Player totalAttack is incorrect."
        self.assertEqual(player._totalAttack, player._attack + player._weaponAttack, errorMsg)
        
    def testHeal(self):
        """
        Where healing amount is more than the amount possible. 
        """
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        player._maxHp = 10
        player._hp = 9
        healAmount = 1000
        
        player.heal(healAmount)

        self.assertEqual(player._hp, player._maxHp, "Healing test #1 failed.")

    def testHeal2(self):
        """
        Where healing amount is less than the amount possible.
        """
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        player._maxHp = 10
        player._hp = 8
        healAmount = 1
        expectedHp = player._hp + healAmount
        
        player.heal(healAmount)

        self.assertEqual(player._hp, expectedHp, "Healing test #2 failed.")
        
    def testEquip(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        item = Item("Chainik Reakettle", "Makes good tea", 1)
        weapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        armor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)
        
        player.addToInventory(item)
        player.addToInventory(weapon)
        player.addToInventory(armor)

        #Pretest player-specific items-based attributes
        errorMsg = "_weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "_armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "_totalAttack should be simply attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)

        #Attempt to equip items
        player.equip(item)
        self.assertFalse(item in player._equipped._items, "Equipped %s and should not have." % item)
        player.equip(weapon)
        self.assertTrue(weapon in player._equipped._items, "Failed to equip %s." % weapon)
        player.equip(armor)
        self.assertTrue(armor in player._equipped._items, "Failed to equip %s." % armor)

        #Test for change in player's items-specific attributes
        errorMsg = "player._weaponAttack should be newWeapon._attack but is not."
        self.assertEqual(player._weaponAttack, weapon._attack, errorMsg)
        errorMsg = "_armorDefense should be newArmor._defense but is not."
        self.assertEqual(player._armorDefense, armor._defense, errorMsg)
        errorMsg = "_totalAttack should have been updated but was not."
        self.assertEqual(player._totalAttack, player._attack + weapon._attack, errorMsg)

    def testUnequip(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        item = Item("Chainik Reakettle", "Makes good tea", 1)
        weapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        armor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)
        
        player.addToInventory(item)
        player.addToInventory(weapon)
        player.addToInventory(armor)

        player.equip(weapon)
        player.equip(armor)
        
        #Attempt to unequip items
        player.unequip(weapon)
        self.assertFalse(newWeapon in player._equipped._items, "Failed to unequip %s" % weapon)
        player.unequip(armor)
        self.assertFalse(newArmor in player._equipped._items, "Failed to unequip %s" % armor)

        #Check to see that item-specific attributes reset to defaults
        errorMsg = "player._weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "player._armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "totalAttack should be simply attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)
        
    def testAddToInventory(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        item = Item("Chainik Reakettle", "Makes good tea", 1)
        weapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        armor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)

        player.addToInventory(item)
        player.addToInventory(weapon)
        player.addToInventory(armor)
        
        #Test add items to inventory
        errorMsg = "Failed to add item to inventory."
        self.assertTrue(item in player._inventory, errorMsg)
        self.assertTrue(weapon in player._inventory, errorMsg)
        self.assertTrue(armor in player._inventory, errorMsg)
        
        #Negative case: adding items already in inventory to inventory
        numberOfItems = player._inventory.count()
        
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)
        newNumberOfItems = player._inventory.count()
        
        errorMsg = "Number of items increased when it should not have."
        self.assertEqual(numberOfItems, newNumberOfItems, errorMsg)

    def testRemoveFromInventory(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        from items.item_set import ItemSet
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        item = Item("Chainik Reakettle", "Makes good tea", 1)
        weapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        armor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)

        player.addToInventory(item)
        player.addToInventory(weapon)
        player.addToInventory(armor)

        player.equip(weapon)
        player.equip(armor)

        #Pretest: items in player._inventory        
        errorMsg = "Failed to initialize test character correctly."
        self.assertTrue(item in player._inventory, errorMsg)
        self.assertTrue(weapon in player._inventory, errorMsg)
        self.assertTrue(armor in player._inventory, errorMsg)

        #Testing player.removeFromInventory()
        player.removeFromInventory(item)
        player.removeFromInventory(weapon)
        player.removeFromInventory(armor)
        
        errorMsg = "Failed to remove item from inventory."
        self.assertFalse(item in player._inventory, errorMsg)
        self.assertFalse(weapon in player._inventory, errorMsg)
        self.assertFalse(armor in player._inventory, errorMsg)

        #Test that items get unequipped
        errorMsg = "Failed to remove item from equipped."
        self.assertFalse(weapon in player._equipped._items, errorMsg)
        self.assertFalse(armor in player._equipped._items, errorMsg)

        #Test that item-specific character attributes are reset to original values
        errorMsg = "player._weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "player._armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "player._totalAttack should be player._attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)

    def testCanMoveDirection(self):
        """
        Tests if canMoveDirection() methods work.
        """
        from player import Player
        from space import Space
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        north = Space("North Space", "Very cold", "Welcome")
        south = Space("South Space", "Very warm", "Welcome")
        east = Space("East Space", "Very mountainous", "Welcome")
        west = Space("West Space", "Coastal", "Welcome")

        #Pretest - no ports created
        errorMsg = "player.canMoveDirection() negative case failed."
        self.assertFalse(player.canMoveNorth(), errorMsg)
        self.assertFalse(player.canMoveSouth(), errorMsg)
        self.assertFalse(player.canMoveEast(), errorMsg)
        self.assertFalse(player.canMoveWest(), errorMsg)

        #Create ports 
        space.createExit("north", north, outgoingOnly = False)
        space.createExit("south", south, outgoingOnly = False)
        space.createExit("east", east, outgoingOnly = False)
        space.createExit("west", west, outgoingOnly = False)

        #Test that player-movement methods work
        errorMsg = "player.canMoveNorth() failed."
        self.assertTrue(player.canMoveNorth(), errorMsg)
        errorMsg = "player.canMoveSouth() failed."
        self.assertTrue(player.canMoveSouth(), errorMsg)
        errorMsg = "player.canMoveEast() failed."
        self.assertTrue(player.canMoveEast(), errorMsg)
        errorMsg = "player.canMoveWest() failed."
        self.assertTrue(player.canMoveWest(), errorMsg)

class InnTest(unittest.TestCase):
    """
    Tests Inn objects.

    Iterations:
    -For when player chooses to stay at inn and has money to do so.
    -For when player chooses to stay at inn and does not have money to do so.
    -For when player chooses not to stay at inn.
    -For invalid user input.
    """
    def testPositiveCase(self):
        """
        For when player chooses to stay at Inn and has enough money to do so.
        """
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
                
        player._hp = 1
        player._money = 10

        #Player chooses to stay at the inn
        rawInputMock = MagicMock(side_effect = ["yes"])
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
        #Test that player._money and player._hp are updated to correct values
        self.assertEqual(player._money, 5, "Player's money not decreased by correct amount.")
        self.assertEqual(player._hp, player._maxHp, "Player's health not increased to full health.")
        
    def testNegativeCase2(self):
        """
        For when player chooses to stay at Inn and does not have enough money to do so.
        """
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
                
        player._hp = 1
        player._money = 2

        #Player chooses to stay at the inn
        rawInputMock = MagicMock(side_effect = ["yes"])
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
        #Test that player._money and player._hp do not change
        self.assertEqual(player._money, 2, "Player money changed when it should not have.")
        self.assertEqual(player._hp, 1, "Player's health changed when it should not have.")

    def testNegativeCase3(self):
        """
        For when player chooses not to stay at the inn.
        """
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
                
        player._hp = 1
        player._money = 10

        #Player chooses not to stay at the inn
        rawInputMock = MagicMock(side_effect = ["no"])
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
        #Test that player._money and player._hp do not change
        self.assertEqual(player._money, 10, "Player money changed when it should not have.")
        self.assertEqual(player._hp, 1, "Player's health changed when it should not have.")
        
    def testNegativeCase4(self):
        """
        For invalid user input.
        """
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
        
        #For invalid user input
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "gobbledigook", "gobbledigook", "no"])
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
class ShopSellItems(unittest.TestCase):
    """
    Tests Shop's ability to sell items.
    """
    def testPositiveCase(self):
        """
        Player sells three items.
        
        Components:
        -Items should be removed from player._inventory and player._equipped
        -player._money should be increased by half of the value of the items
        -Items should be added to shop wares at full cost
        """
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor
        from items.potion import Potion

        testShop = Shop("Chris' Testing Shop", "Come test here", "Hi", 5, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)

        testShop._items = []
        
        #Create starting inventory and equipment
        weapon = Weapon("Knife", "Jack of all trades", 3, 1, 1)
        armor = Armor("Leather Tunic", "Travel cloak", 3, 1, 1)
        potion = Potion("Potion", "Vodka", 3, 1, 1)

        inventory = player._inventory
        player.addToInventory(weapon)
        player.addToInventory(armor)
        player.addToInventory(potion)

        equipped = player.getEquipped()
        player.equip(weapon)
        player.equip(armor)

        #Test that that items are in player._inventory and player._equipped
        self.assertTrue(inventory.containsItemWithName("Knife"), "Knife not added to inventory.")
        self.assertTrue(inventory.containsItemWithName("Leather Tunic"), "Leather Tunic not added to inventory.")
        self.assertTrue(inventory.containsItemWithName("Potion"), "Potion not added to inventory.")
    
        errorMsg = "Player items were not equipped correctly."
        self.assertTrue(equipped.containsItem(weapon), errorMsg)
        self.assertTrue(equipped.containsItem(armor), errorMsg)
                        
        #Player chooses to sell items
        rawInputMock = MagicMock(side_effect = ["sell", "Knife", "yes", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
        rawInputMock = MagicMock(side_effect = ["sell", "Leather Tunic", "yes", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
        rawInputMock = MagicMock(side_effect = ["sell", "Potion", "yes", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
        
        #Test items no longer in player._inventory and player._equipped
        errorMsg = "Knife that was sold is still in inventory"
        self.assertFalse(inventory.containsItemWithName("Knife"), errorMsg)
        errorMsg = "Leather tunic that was sold is still in inventory"
        self.assertFalse(inventory.containsItemWithName("Leather Tunic"), errorMsg)
        errorMsg = "Potion that was sold is still in inventory"
        self.assertFalse(inventory.containsItemWithName("Potion"), errorMsg)

        errorMsg = "Knife that was sold is still in equipped"
        self.assertFalse(equipped.containsItemWithName("Knife"), errorMsg)
        errorMsg = "Leather tunic that was sold is still in equipped"
        self.assertFalse(equipped.containsItemWithName("Leather Tunic"), errorMsg)

        #Test that items now appear in shop wares
        errorMsg = "Items are now supposed to be in shop inventory but are not."
        self.assertTrue(weapon in testShop._items, errorMsg)
        self.assertTrue(armor in testShop._items, errorMsg)
        self.assertTrue(potion in testShop._items, errorMsg)

        #New shop wares' prices are set to full cost
        errorMsg = "Item costs not set back to full amount."
        for item in testShop._items:
            self.assertEqual(item._cost, 1, errorMsg)

        #Player's money should increase by the half the cost of the items - 1.5 in our case
        errorMsg = "Player's money not increased to correct amount. It is %s." % player._money)
        self.assertEqual(player._money, 21.5, errorMsg)

    def testNegativeCase(self):
        """
        Testing that Shop can handle invalid user input.
        """
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.item import Item
        
        testShop = Shop("Chris' Testing Shop", "Come test here", "Hi", 5, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)

        goldNugget = Item("Gold Nugget", "Potentially cheese!", 1)
        player.addToInventory(goldNugget)

        #Test preconditions
        errorMsg = "goldNugget is supposed to be in player._inventory."
        self.assertTrue(goldNugget in player._inventory._items, errorMsg)

        #Player attempts to sell an invalid item
        rawInputMock = MagicMock(side_effect = ["sell", "gobbledigook", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

        #Player gives invalid input when prompted to confirm item sell
        rawInputMock = MagicMock(side_effect = ["sell", "Gold Nugget", "gobbledigook", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
            
class ShopPurchaseItems(unittest.TestCase):
    """
    Tests Shop's ability to allow for item purchases. 
    """
    def testPositiveCase(self):
        """
        Player purchases three items.

        Testing:
        -Items in inventory
        -Items not in equipped
        -Items not in shop wares
        -player._money updated correctly
        """
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor
        from items.potion import Potion

        testShop = Shop("Chris' Testing Shop", "Come test here", "Hi", 0, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)

        player._money = 20
        
        testWeapon = Potion("Knife", "Russian", 1, 1, 1)
        testArmor = Potion("Shield of Faith", "Also Russian", 1, 1, 1)
        testPotion = Potion("Medium Potion of Healing", "A good concoction. Made by Master Wang.", 1, 5, 3)
        testShop._items.append(testWeapon)
        testShop._items.append(testArmor)
        testShop._items.append(testPotion)

        #Test preconditions
        errorMsg = "Player does not start with 20 rubles."
        self.assertEqual(player._money, 20, errorMsg)
        errorMsg = "Our test shop was generated with the wrong number of items."
        self.assertEqual(len(testShop._items), 3, errorMsg)
        errorMsg = "Items in shop inventory are of the wrong type."
        for item in testShop._items:
            self.assertTrue(isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Potion), errorMsg)

        #Player purchases items
        rawInputMock = MagicMock(side_effect = ["purchase", "Knife", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
        rawInputMock = MagicMock(side_effect = ["purchase", "Shield of Faith", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
        rawInputMock = MagicMock(side_effect = ["purchase", "Medium Potion of Healing", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Test items in inventory
        errorMsg = "Knife that was purchased was not added to inventory."
        self.assertTrue(player._inventory.containsItemWithName("Knife"), errorMsg)
        errorMsg = "Shield of Faith that was purchased was not added to inventory."
        self.assertTrue(player._inventory.containsItemWithName("Shield of Faith"), errorMsg)
        errorMsg = "Medium Potion that was purchased was not added to inventory."
        self.assertTrue(player._inventory.containsItemWithName("Medium Potion of Healing"), errorMsg)

        #Test items not in equipped
        errorMsg = "Knife that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Knife"), errorMsg)
        errorMsg = "Shield of Faith that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Shield of Faith"), errorMsg)
        errorMsg = "Medium Potion that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Medium Potion of Healing"), errorMsg)
        
        #Test items not in shop wares
        errorMsg = "Knife that was purchased is still in shop wares."
        self.assertFalse(testPotion in testShop._items, errorMsg)
        errorMsg = "Shield of Faith that was purchased is still in shop wares."
        self.assertFalse(testPotion in testShop._items, errorMsg)
        errorMsg = "Medium Potion that was purchased is still in shop wares."
        self.assertFalse(testPotion in testShop._items, errorMsg)

        #player._money should decrease by the cost of the purchases, which is 5
        errorMsg = "player._money not decreased by correct amount."
        self.assertEqual(player._money, 15, errorMsg)
        
    def testNegativeCase(self):
        """
        Player attempts to purchase an item that is too expensive.

        Testing:
        -Item not in inventory
        -Item not in equipped
        -Item in shop wares
        -player._money unchanged
        """
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.potion import Potion

        testShop = Shop("Chris' Testing Shop", "Come test here", "Hi", 0, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)

        player._money = 20    

        testPotion = Potion("SuperDuperLegendary Potion", "A Wang concoction. Made by Master Wang.", 1, 35, 1000)
        testShop._items.append(potion)
        
        #Test preconditions
        errorMsg = "Player does not start with 20 rubles."
        self.assertEqual(player._money, 20, errorMsg)
        errorMsg = "Our test shop was generated with the wrong number of items."
        self.assertEqual(len(testShop._items), 1, errorMsg)
        errorMsg = "SuperDuperLegendary Potion not in testShop._items."
        self.assertTrue(testPotion in testShop._items, errorMsg)
        
        #Player attempts to purchase potion
        rawInputMock = MagicMock(side_effect = ["purchase", "SuperDuperLegendary Potion of Healing", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

        #Test potion not in inventory, not in equipped, in shop wares
        errorMsg = "SuperDuperLegendary Potion of Healing that was purchased was added to inventory."
        self.assertFalse(player._inventory.containsItemWithName("SuperDuperLegendary Potion of Healing"), errorMsg)
        errorMsg = "SuperDuperLegendary Potion of Healing that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("SuperDuperLegendary Potion of Healing"), errorMsg)
        errorMsg = "SuperDuperLegendary Potion of Healing that was purchased is no longer in shop wares."
        self.assertTrue(testPotion2 in testShop._items, errorMsg)
        
        #player._money should be unchanged
        errorMsg = "player._money changed when it was not supposed to."
        self.assertEqual(player._money, 20, errorMsg)

    def testNegativeCase2(self):
        """
        Player attempts to purchase an item that does not exist.

        Testing:
        -Inventory unchanged
        -Equipment unchanged
        -Shop wares unchanged
        -player._money unchanged
        """
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.potion import Potion

        testShop = Shop("Chris' Testing Shop", "Come test here", "Hi", 0, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)

        player._money = 20    

        #Test preconditions
        errorMsg = "Player does not start with 20 rubles."
        self.assertEqual(player._money, 20, errorMsg)
        errorMsg = "Player inventory should be empty."
        self.assertEqual(len(player._inventory._items), 0, errorMsg)
        errorMsg = "Player equipment should be empty."
        self.assertEqual(len(player._inventory._items), 0, errorMsg)
        errorMsg = "Our test shop was generated with the wrong number of items."
        self.assertEqual(len(testShop._items), 0, errorMsg)

        #Player attempts to purchase a non-existent item
        rawInputMock = MagicMock(side_effect = ["purchase", "gobbledigook", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

        #Inventory, equipment, and shop wares should be unchanged
        errorMsg = "Player inventory changed when it should not have."
        self.assertEqual(len(player._inventory._items), 0, errorMsg)
        errorMsg = "Player equipment changed when it should not have."
        self.assertEqual(len(player._equipment._items), 0, errorMsg)
        errorMsg = "Shop wares changed when it should not have."
        self.assertEqual(len(testShop._items), 0, errorMsg)
         
        #player._money should not change
        errorMsg = "Player's money incorrectly decreased when purchasing invalid item."
        self.assertEqual(player._money, 15, errorMsg)
                            
class Square(unittest.TestCase):
    """
    Tests square buildings.
    """
    def PositiveCase(self):
        """
        Player talks to various people in Square.

        Testing:
        -Person has several items to give (Master Wang).
        -Person has one item to give (Miles).
        -Person has no items to give (Putin).
        """
        from player import Player
        from space import Space
        from cities.square import Square
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor
        from items.potion import Potion
        from items.item import Item

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)
        armor = Armor("Shield of Faith", "Quenches fiery darts", 1, 1, 1)
        potion = Potion("Leaves from Tree of Life", "For healing the nations", 1, 1, 1)
        cookies = Item("Miles' Famous Cookies", "Gross this time", 1)
        
        talk = {"Master Wang": "I am Master Wang, creator various things in this Lord of the Rings game", "Miles": "Hello, I am Miles, the cookie legend", "Putin": "Oppression, engage...."}
        items = {"Master Wang": [weapon, armor, potion], "Miles": cookies}
        testSquare = Square("Chris' Testing Square", "Testing Square", "Come test here", talk, items)
        
        testCity = City("Test City", "Testing city", "Hello to Test City. See Chris' Square", testSquare)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
        
        #Test: talking to Master Wang (several items to give)
        rawInputMock = MagicMock(side_effect = ["Master Wang", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)

        #Check that Master Wang's items are now in inventory
        errorMsg = "Weapon is supposed to be in inventory but is not."
        self.assertTrue(weapon in inventory, errorMsg)
        errorMsg = "Armor is supposed to be in inventory but is not."
        self.assertTrue(armor in inventory, errorMsg)
        errorMsg = "Potion is supposed to be in inventory but is not."
        self.assertTrue(potion in inventory, errorMsg)

        #Check that items are no longer in square._items
        errorMsg = "Weapon is not supposed to be in testSquare._items but is."
        self.assertFalse(weapon in testSquare._items, errorMsg)
        errorMsg = "Armor is not supposed to be in testSquare._items but is."
        self.assertFalse(armor in testSquare._items, errorMsg)
        errorMsg = "Potion is not supposed to be in testSquare._items but is."
        self.assertFalse(potion in testSquare._items, errorMsg)
        
        #Test: talking to Miles (one item to give)
        rawInputMock = MagicMock(side_effect = ["Miles", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)

        #Check that item associated with Miles is now in inventory
        errorMsg = "Cookies is supposed to be in inventory but is not."
        self.assertTrue(cookies in inventory, errorMsg)

        #Check that item is no longer in square._items
        errorMsg = "Cookies is not supposed to be in testSquare._items but is."
        self.assertFalse(cookies in testSquare._items, errorMsg)

        #Test: talking to Putin (no items to give)
        rawInputMock = MagicMock(side_effect = ["Putin", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)
            
    def NegativeCase(self):
        """
        Player attempts to talk to invalid person.
        """
        from player import Player
        from space import Space
        from cities.square import Square
        from cities.city import City
        
        talk = {}
        items = {}
        testSquare = Square("Chris' Testing Square", "Testing Square", "Come test here", talk, items)
        
        testCity = City("Test City", "Testing city", "Hello to Test City. See Chris' Square", testSquare)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
        
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)
            
class City(unittest.TestCase):
    """
    Tests City's ability to handle a series of commands.

    The series of commands:
    -Player enters City, enters Inn, leaves Inn, leaves City.
    -Player enters City, enters Shop, leaves Shop, leaves City.
    -Player enters City, enters Square, leaves Square.
    -Player "gobbledigooks", leave City.
    """
    def testCity(self):
        from player import Player
        from space import Space
        from cities.city import City
        from cities.inn import Inn
        from cities.shop import Shop
        from cities.square import Square
        
        testInn = Inn("Seth N' Breakfast Test Inn", "Testing inn", "Come test here", 3)
        testShop = Shop("Pookie Tea Shop", "Full of chi hua-huas", "Moofey, moofey meep", 5, 5)
        testSquare = Square("Chocolate Mountain", "Origin of Chocolate Rain", "Meepey, meepey moof")
        testCity = City("TestCity", "Chris' unique testing city", "Come test here", buildings = [testInn, testShop, testSquare])
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)

        #Test that City can handle a series of commands
        cityInputMock = MagicMock(side_effect = ["Seth N' Breakfast Test Inn", "leave city", "Pookie Tea Shop",
            "leave city", "Chocolate Mountain", "gobbledigook", "leave city"])
        innInputMock = MagicMock(side_effect = ["no"])
        shopInputMock = MagicMock(side_effect = ["quit"])
        squareInputMock = MagicMock(side_effect = ["quit"])
        
        with patch('cities.city.raw_input', create = True, new = cityInputMock):
            with patch('cities.inn.raw_input', create = True, new = innInputMock):
                testCity.enter(player)
            with patch('cities.shop.raw_input', create = True, new = shopInputMock):
                testCity.enter(player)
            with patch('cities.square.raw_input', create = True, new = squareInputMock):
                testCity.enter(player)
        
class UniquePlace(unittest.TestCase):
    """
    Tests for correct UniquePlace initialization.
    """
    def testInit(self):
        from unique_place import UniquePlace

        testUniquePlace = UniquePlace("Chris' Unique Testing Room", "Come test here", "Here's some chocolate for coming")

        errorMsg = "testUniquePlace._name was not initialized correctly."
        self.assertEqual(testUniquePlace._name, "Chris' Unique Testing Room", errorMsg)
        errorMsg = "testUniquePlace._description was not initialized correctly."
        self.assertEqual(testUniquePlace._description, "Come test here", errorMsg)
        errorMsg = "testUniquePlace._greetings was not initialized correctly."
        self.assertEqual(testUniquePlace._greetings, "Here's some chocolate for coming", errorMsg)

class EnterCommand(unittest.TestCase):
    """
    Tests for Enter Command. In these tests, player enters
    different combinations of places.

    Iterations:
    -testPositiveCase:     one city and one unique place to enter.
    -testPositiveCase2:    multiple cities and one unique place to enter.
    -testPositiveCase3:    one city and multiple cities to enter.
    -testPositiveCase4:    multiple cities and multiple unique places to enter.
    -testNegativeCase:     no destinations to enter.
    -testNegativeCase2:    places to enter, invalid user input.
    """
    def testPositiveCase(self):
        """
        One city and one unique place to enter.

        Player chooses to:
        -Enter City, leave City
        -Enter UniquePlace
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testUniquePlace = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity, uniquePlace = testUniquePlace)
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)
        
        #Testing enter command's ability to execute a series of commands
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Master Wang's Magical Testing Place"])
        cityInputMock = MagicMock(side_effect = ["leave city"])
        
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()

    def testPositiveCase2(self):
        """
        Multiple cities and one unique place to enter.

        Player choses to:
        -Enter City, leave City
        -Enter City, leave City
        -Enter City, leave City
        -Enter UniquePlace
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity1 = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testCity2 = City("Seth's Sans-Shabbiness Shack Sh-City", "Seth's unique testing city", "Come test here")
        testCity3 = City("Miles' Magical Cookie Jail City", "Miles' unique testing city", "Come test here")
        testUniquePlace = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor",
            city = [testCity1, testCity2, testCity3], uniquePlace = testUniquePlace)
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)

        #Testing enter command's ability to execute a series of commands
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Seth's Sans-Shabbiness Shack Sh-City", 
            "Miles' Magical Cookie Jail City", "Master Wang's Magical Testing Place"])
        cityInputMock = MagicMock(side_effect = ["leave city", "leave city", "leave city"])
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()

    def testPositiveCase3(self):
        """
        One city and multiple cities to enter.

        Player choses to:
        -Enter City, leave City
        -Enter UniquePlace
        -Enter UniquePlace
        -Enter UniquePlace
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testUniquePlace1 = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        testUniquePlace2 = UniquePlace("Jim's Magic Castle of Time-Shifting", "Many different colours", "What time is it?")
        testUniquePlace3 = UniquePlace("Russian Armadillo Mound", "Where Texas meets Russia", "I'm confused.")
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor",
            city = testCity, uniquePlace = [testUniquePlace1, testUniquePlace2, testUniquePlace3])
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)

        #Testing enter command's ability to execute a series of commands
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Master Wang's Magical Testing Place", 
            "Jim's Magic Castle of Time-Shifting", "Russian Armadillo Mound"])
        cityInputMock = MagicMock(side_effect = ["leave city"])
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()

    def testPositiveCase4(self):
        """
        Multiple cities and multiple unique places to enter.

        Player choses to:
        -Enter City, leave City
        -Enter City, leave City
        -Enter City, leave City
        -Enter UniquePlace
        -Enter UniquePlace
        -Enter UniquePlace
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity1 = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testCity2 = City("Seth's Sans-Shabbiness Shack Sh-City", "Seth's unique testing city", "Come test here")
        testCity3 = City("Miles' Magical Cookie Jail City", "Miles' unique testing city", "Come test here")
        testUniquePlace1 = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        testUniquePlace2 = UniquePlace("Jim's Magic Castle of Time-Shifting", "Many different colours", "What time is it?")
        testUniquePlace3 = UniquePlace("Russian Armadillo Mound", "Where Texas meets Russia", "I'm confused.")
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor",
            city = [testCity1, testCity2, testCity3], uniquePlace = [testUniquePlace1, testUniquePlace2, testUniquePlace3])
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)

        #Testing enter command's ability to execute a series of commands
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Seth's Sans-Shabbiness Shack Sh-City", 
            "Miles' Magical Cookie Jail City", "Master Wang's Magical Testing Place",
            "Jim's Magic Castle of Time-Shifting", "Russian Armadillo Mound"])
        cityInputMock = MagicMock(side_effect = ["leave city", "leave city", "leave city"])
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()
                
    def testNegativeCase(self):
        """
        Trying to enter when there are no possible destinations.
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)

        rawInputMock = MagicMock(side_effect = ["enter"])
        with patch('commands.enter_command.raw_input', create = True, new = rawInputMock):
            enterCmd.execute()
            
    def testNegativeCase2(self):
        """
        Trying to enter where there are valid destinations but
        user gives inputs a place that does not exist.
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from cities.city import City
        from space import Space

        testCity = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        space = Space("Shire", "Home of the Hobbits.", "Mordor", testCity)
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)

        rawInputMock = MagicMock(side_effect = ["enter", "gobbledigook", "stop"])
        with patch('commands.enter_command.raw_input', create = True, new = rawInputMock):
            enterCmd.execute()

class DescribeCommand(unittest.TestCase):
    """
    Tests Describe Command.
    
    Three cases:
    -Works with space and no cities/unique places.
    -Works with one city and one unique place.
    -Works with multiple cities and multiple unique places.
    """
    def testCase1(self):
        from space import Space
        from commands.describe_command import DescribeCommand
        from player import Player
        from space import Space
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("The Bagginses", space)
        describeCmd = DescribeCommand("Test Describe Command", "Tests Describing", player)
        
        describeCmd.execute()
    
    def testCase2(self):
        from space import Space
        from commands.describe_command import DescribeCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity = City("Master Wang's Oriental Fun City", "Chris's testing city", "Come test here")
        testUniquePlace = UniquePlace("The UniquePlace of Testing", "Weird things sometimes happen when you test.", "Welcome to UniquePlace of Testing.")
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity, uniquePlace = testUniquePlace)
        player = Player("The Bagginses", space)
        describeCmd = DescribeCommand("Test Describe Command", "Tests Describing", player)
        
        describeCmd.execute()

    def testCase3(self):
        from space import Space
        from commands.describe_command import DescribeCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity1 = City("Master Wang's Oriental Fun City", "Chris' unique testing city", "Come test here")
        testCity2 = City("Chocolate Mountain", "Next to Vanilla Mountain", "Hi I'm Jim")
        testUniquePlace1 = UniquePlace("The UniquePlace of Testing", "Weird things sometimes happen when you test.", "Welcome to UniquePlace of Testing.")
        testUniquePlace2 = UniquePlace("Ukraine", "Not in great shape", "Welcome to Ukraine")
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = [testCity1, testCity2], uniquePlace = [testUniquePlace1, testUniquePlace2])
        player = Player("The Bagginses", space)
        describeCmd = DescribeCommand("Test Describe Command", "Tests Describing", player)
        
        describeCmd.execute()

class monster(unittest.TestCase):
    """
    Tests Monster class.
    """
    def testMonster(self):
        from monsters.monster import Monster

        monster = Monster("Jack", "@$$", [10, 5, 7], "Moof", "Meep")

        #Test monster initialized correctly
        errorMsg = "monster._name should be 'Jack'"
        self.assertEqual(monster._name, "Jack", errorMsg)
        errorMsg = "monster._description should be '@$$'"
        self.assertEqual(monster._description, "@$$", errorMsg)
        errorMsg = "monster._hp should be 10"
        self.assertEqual(monster._hp, 10, errorMsg)
        errorMsg = "monster._attack should be 5"
        self.assertEqual(monster._attack, 5, errorMsg)
        errorMsg = "monster._experience should be 7"
        self.assertEqual(monster._experience, 7, errorMsg)
        errorMsg = "monster._attackString sound be 'Moof'"
        self.assertEqual(monster._attackString, "Moof", errorMsg)
        errorMsg = "monster._deathString should be 'Meep'"
        self.assertEqual(monster._deathString, "Meep", errorMsg)
        
        #Test monster.attack()
        player = MagicMock()
        player.takeAttack = MagicMock()
        
        monster.attack(player)
        errorMsg = "monster.attack() failed to carry attack to player."
        player.takeAttack.assert_called_with(5)

        #Test monster.takeAttack() - attack is less than total hp
        monster.takeAttack(3)
        errorMsg = "monster.takeAttack() testcase #1 failed."
        self.assertEqual(monster._hp, 7, errorMsg)

        #Test monster.takeAttack() - attack is more than total hp
        monster.takeAttack(1000)
        errorMsg = "monster.takeAttack() testcase #2 failed"
        self.assertEqual(monster._hp, 0, errorMsg)

class monsterFactory(unittest.TestCase):
    """
    Tests monster factory.

    Pieces:
    -Tests default monster creation, that monsters are in fact created.
    -Testing difficulty feature - that default stats are implemented when
    difficulty set to zero. 
    -Testing difficulty feature - that monster stats increase as
    percentage over default. For instance, difficulty = 1 should result
    in monsters with 200% base monster stats.
    -Testing difficulty feature - that default monster spawn occurs when
    difficulty is set to zero.
    -Testing difficulty feature - that monster spawn increases as a percentage
    over default. For instance, difficulty = 1 should result in a 100% increase
    in monster spawn over base.
    -Testing that regional spawns work: that monster spawn reflects
    regional monster distributions held in constants. 

    Note params for getMonster: getMonsters(number, region, difficulty).
    """
    def testDefaultMonsterCreation(self):
        #Tests default monster creation, that monsters are in fact created.
        from factories.monster_factory import getMonsters
        from monsters.monster import Monster
        import constants
        
        monsters = getMonsters(3, constants.RegionType.ERIADOR, 0)
        errorMsg = "Nothing was created in initial monster creation test. %s" %monsters
        self.assertEqual(len(monsters), 0, errorMsg)
        
        for monster in monsters:
            errorMsg = "getMonsters did not spawn Monster objects."
            self.assertTrue(isinstance(monster, Monster), errorMsg)

    def testDefaultStatGeneration(self):
        #Testing difficulty feature - that default stats are implemented when
        #difficulty set to zero.
        """
        Mocked up monster spawn distribution of ERIADOR such that Trolls are spawned
        100% of the time. getMonsters is to spawn three Trolls using the newly mocked
        up monster distribution.
        """
        from factories.monster_factory import getMonsters
        from monsters.troll import Troll
        import constants
        
        constants.RegionMonsterDistribution = MagicMock(ERIADOR = {Troll: 1})
        monsters = getMonsters(3, 1, 0)
        for monster in monsters:
            errorMsg = "monster._hp was not initiated correctly."
            self.assertEqual(monster._hp, constants.MONSTER_STATS[Troll][0], errorMsg)
            errorMsg = "monster._attack was not initiated correctly."
            self.assertEqual(monster._attack, constants.MONSTER_STATS[Troll][1], errorMsg)
            errorMsg = "monster._experience was not initiated correctly."
            self.assertEqual(monster._attack, constants.MONSTER_STATS[Troll][2], errorMsg)
            
    def testDifficultyBonusStats(self):
        #-Testing difficulty feature - that monster stats increase as
        #percentage over default. For instance, difficulty = 1 should result
        #in monsters with 200% base monster stats.
        """
        Mocked up monster distribution of ERIADOR such that Trolls are spawned 100%
        of the time. getMonsters is to spawn Trolls with 200% base stats. 
        """
        from factories.monster_factory import getMonsters
        from monsters.troll import Troll
        import constants
        
        constants.RegionMonsterDistribution = MagicMock(ERIADOR = {Troll: 1})
        monsters = getMonsters(3, 1, 1)
        for monster in monsters:
            errorMsg = "monster._hp was not initiated correctly."
            self.assertEqual(monster._hp, 2 * constants.MONSTER_STATS[Troll][0], errorMsg)
            errorMsg = "monster._attack was not initiated correctly."
            self.assertEqual(monster._attack, 2 * constants.MONSTER_STATS[Troll][1], errorMsg)
            errorMsg = "monster._experience was not initiated correctly."
            self.assertEqual(monster._attack, 2 * constants.MONSTER_STATS[Troll][2], errorMsg)
            
    def testDefaultSpawnNumber(self):    
        #-Testing difficulty feature - that default monster spawn occurs when
        #difficulty is set to zero.
        """
        Params: number = 3, region = 1 (ERIADOR), difficulty = 0.
        """
        from factories.monster_factory import getMonsters
        import constants
        
        monsters = getMonsters(3, constants.RegionType.ERIADOR, 0)
        
        errorMsg = "getMonsters did not spawn three monsters. %s" %monsters
        self.assertEqual(len(monsters), 3, errorMsg)

    def testRegionalSpawn(self):
        #-Testing that regional spawns work: that monster spawn reflects
        #regional monster distributions held in constants. 
        """
        Tests that monsters of each type in a region's distribution
        spawn, given a large enough sample size.

        TODO: this still doesn't work. only one monster type spawned.
        """
        from factories.monster_factory import getMonsters
        from monsters.troll import Troll
        from monsters.nazgul import Nazgul
        from monsters.goblin import Goblin
        from monsters.great_goblin import GreatGoblin
        import constants
            
        constants.RegionMonsterDistribution = MagicMock(ERIADOR = {Troll: .5,
            Nazgul: 1})
        monstersEriador = getMonsters(5000, constants.RegionType.ERIADOR, 0)

        #Checking to see that Nazgul and Trolls are spawned
        numberNazgul = 0
        numberTroll = 0
        for monster in monstersEriador:
            if isinstance(monster, Nazgul):
                numberNazgul += 1
            elif isinstance(monster, Troll):
                numberTroll += 1
            else:
                raise AssertionError("Invalid monster type.")

        errorMsg = "Did not spawn five thousand monsters - Eriador"
        self.assertEqual(len(monstersEriador), 5000, errorMsg)
        errorMsg = "No nazgul spawned."
        self.assertTrue(numberNazgul != 0, errorMsg)
        errorMsg = "No trolls spawned."
        self.assertTrue(numberTroll != 0, errorMsg)

        #Checking to see that Goblin and GreatGoblin are spawned
        constants.RegionMonsterDistribution = MagicMock(HIGH_PASS = {Goblin: .5,
            GreatGoblin: 1})
        monstersHighPass = getMonsters(5000, constants.RegionType.HIGH_PASS, 0)
        print monstersEriador
        print monstersHighPass
        numberGoblin = 0
        numberGreatGoblin = 0
        for monster in monstersHighPass:
            if isinstance(monster, Goblin):
                numberGoblin += 1
            elif isinstance(monster, GreatGoblin):
                numberGreatGoblin += 1
            else:
                raise AssertionError("Invalid monster type.")
            
        errorMsg = "Did not spawn five thousand monsters - High Pass"
        self.assertEqual(len(monstersHighPass), 5000, errorMsg)
        errorMsg = "No goblins spawned."
        self.assertTrue(numberGoblin != 0, errorMsg)
        errorMsg = "No great goblins spawned."
        self.assertTrue(numberGreatGoblin != 0, errorMsg)
    
class battleEngine(unittest.TestCase):
    """
    Tests battleEngine.
    """
    def testRegionSpawn(self):
        """
        Tests that the right number of monsters is handed to monster_factory.getMonsters.
        
        Formula is: number = (1 + bonusDifficulty) * constants.RegionBaseSpawn.REGION
        """
        from space import Space
        from player import Player
        from battle_engine import battle
        from factories.monster_factory import getMonsters
        import constants

        space = Space("Shire", "Home of the hobbits", constants.RegionType.ERIADOR, battleBonusDifficulty = .5)
        player = Player("Russian", space)
        constants.RegionBaseSpawn.ERIADOR = MagicMock(return_value=2)
        getMonsters = MagicMock()

        battle(player)
        getMonsters.assert_called_once_with(3, constants.RegionType.ERIADOR, .5)

    def testPlayerAttackPhase1(self):
        """
        Tests playerAttackPhase.

        Iteration1: attacking a monster that doesn't exist should not result in
        any change to monsters.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import battle
        from battle_engine import playerAttackPhase
        import constants

        space = Space("Shire", "Full of Russians", constants.RegionType.ERIADOR)
        player = Player("Russian", space)
        bonusDifficulty = 0

        constants.RUN_PROBABILITY_SUCCESS = MagicMock(return_value=1)
        
        monster1 = MagicMock()
        monster1._takeAttack = MagicMock()
        monster1._name = "Jerk1"
        monster1._experience = 10
        monster1._hp = 10
        monster2 = MagicMock()
        monster2._takeAttack = MagicMock()
        monster2._name = "Jerk2"
        monster2._experience = 10
        monster2._hp = 10
        monster3 = MagicMock()
        monster3._takeAttack = MagicMock()
        monster3._name = "Jerk3"
        monster3._experience = 10
        monster3._hp = 10
        monsters = [monster1, monster2, monster3]
        
        battleInputMock = MagicMock(side_effect = ["attack", "run"])
        attackInputMock = MagicMock(side_effect = ["Non-Existent Jerk"])                                 
        with patch('battle_engine.raw_input', create = True, new = battleInputMock):
            with patch('battle_engine.playerAttackPhase.raw_input', create = True, new = attackInputMock):
                battle(player)

        errorMsg = "Testcase - attacking an invalid monster failed."
        self.assertFalse(monster1.called, errorMsg)
        self.assertFalse(monster2.called, errorMsg)
        self.assertFalse(monster3.called, errorMsg)
        
    def testPlayerAttackPhase2(self):
        """
        Tests playerAttackPhase.

        Iteration2: attacking a valid monster.

        Components:
        -Player attacks correct monster.
        -Player only attacks player-specified monster.
        -Monster attacked for correct amount of damage.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 1
        bonusDifficulty = 0
        
        monster1 = Monster("Jerk", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monster2 = MagicMock()
        monster2._takeAttack = MagicMock()
        monster2._name = "Jerk2"
        monster2._experience = 10
        monster2._hp = 10
        monster3 = MagicMock()
        monster3._takeAttack = MagicMock()
        monster3._name = "Jerk3"
        monster3._experience = 10
        monster3._hp = 10
        monsters = [monster1, monster2, monster3]

        rawInputMock = MagicMock(return_value="Jerk")
        with patch('battle_engine.raw_input', create=True, new=rawInputMock):
            playerAttackPhase(player, monsters, bonusDifficulty)

        monster1.takeAttack.called_with(player._totalAttack)

        #Player only attacks player-specified monster
        errorMsg = "Test: valid monster attack - wrong monster got attacked."
        self.assertFalse(monster2.called, errorMsg)
        self.assertFalse(monster3.called, errorMsg)

        #Monster attacked for correct amount of damage
        correctHealth = monster1._stats[0] - player._totalAttack
        errorMsg = "monster1 health was not set to correct amount after attack."
        self.assertEqual(monster1._hp, correctHealth, errorMsg)

    def testPlayerAttackPhase3(self):
        """
        Tests playerAttackPhase.

        Iteration3: a player attack that results in death of monster should
        remove monster from monsters.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 100
        bonusDifficulty = 0
        
        monster1 = Monster("Jerk", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monsters = [monster1]

        rawInputMock = MagicMock(return_value="Jerk")
        with patch('battle_engine.raw_input', create=True, new=rawInputMock):
            playerAttackPhase(player, monsters, bonusDifficulty)

        errorMsg = "monster1 should have been removed from monsters but was not."
        self.assertTrue(monster1 not in monsters, errorMsg)

    def testPlayerAttackPhase4(self):
        """
        Tests playerAttackPhase.

        Iteration4: a player attack that does not result in the death of monster
        should not remove monster from monsters.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 0
        bonusDifficulty = 0
        
        monster1 = Monster("Jerk", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monsters = [monster1]

        rawInputMock = MagicMock(return_value="Jerk")
        with patch('battle_engine.raw_input', create=True, new=rawInputMock):
            playerAttackPhase(player, monsters, bonusDifficulty)

        errorMsg = "monster1 should not have been removed from monsters but was."
        self.assertTrue(monster1 in monsters, errorMsg)

    def testPlayerAttackPhase5(self):
        """
        Tests playerAttackPhase.

        Iteration5: single monster death should result in earnings generation.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 100
        bonusDifficulty = 0
        
        monster1 = Monster("Jerk", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monsters = [monster1]

        rawInputMock = MagicMock(return_value="Jerk")
        with patch('battle_engine.raw_input', create=True, new=rawInputMock):
            playerAttackPhase(player, monsters, bonusDifficulty)

        errorMsg = "Money was not returned correctly - single monster death."
        self.assertEqual(money, 5, errorMsg)
        errorMsg = "Experience was not returned correctly - single monster death."
        self.assertEqual(experience, 5, errorMsg)

    def testPlayerAttackPhase6(self):
        """
        Tests playerAttackPhase.

        Iteration6: tests multiple monster death earnings generation.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import battle
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 100
        bonusDifficulty = 0
        
        monster1 = Monster("Jerk", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monster2 = Monster("Jerk2", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monster3 = Monster("Jerk3", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monsters = [monster1, monster2, monster3]

        battleInputMock = MagicMock(side_effect = ["attack", "attack", "attack"])
        attackInputMock = MagicMock(side_effect = ["Jerk", "Jerk2", "Jerk3"])
                                                   
        with patch('battle_engine.raw_input', create = True, new = battleInputMock):
            with patch('battle_engine.raw_input', create = True, new = attackInputMock):
                battle(player)

        errorMsg = "Money was not returned correctly - multiple monster death."
        self.assertEqual(money, 15, errorMsg)
        errorMsg = "Experience was not returned correctly - multiple monster death."
        self.assertEqual(experience, 15, errorMsg)

    def testPlayerAttackPhase7(self):
        """
        Tests playerAttackPhase.

        Iteration7: tests single monster death earnings generation with
        non-zero bonusDifficulty.

        bonusDifficulty increases earnings as a percentage over default.
        For instance, bonusDifficulty = 1 results in 200% earnings.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 100
        bonusDifficulty = 1
        
        monster1 = Monster("Jerk", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monsters = [monster1]

        rawInputMock = MagicMock(return_value="Jerk")
        with patch('battle_engine.raw_input', create=True, new=rawInputMock):
            playerAttackPhase(player, monsters, bonusDifficulty)

        errorMsg = "Money was not returned correctly - single monster death with bonus difficulty."
        self.assertEqual(money, 10, errorMsg)
        errorMsg = "Experience was not returned correctly - single monster death with bonus difficulty."
        self.assertEqual(experience, 10, errorMsg)

    def testPlayerAttackPhase8(self):
        """
        Tests playerAttackPhase.

        Iteration8: tests multiple monster death earnings generation with
        non-zero bonusDifficulty.

        bonusDifficulty increases earnings as a percentage over default.
        For instance, bonusDifficulty = 1 results in 200% earnings.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 100
        bonusDifficulty = 1
        
        monster1 = Monster("Jerk", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monster2 = Monster("Jerk2", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monster3 = Monster("Jerk3", "Total J@ck@$$", [5, 5, 5], "Moof", "Meep")
        monsters = [monster1, monster2, monster3]

        battleInputMock = MagicMock(side_effect = ["attack", "attack", "attack"])
        attackInputMock = MagicMock(side_effect = ["Jerk", "Jerk2", "Jerk3"])
                                                   
        with patch('battle_engine.raw_input', create = True, new = battleInputMock):
            with patch('battle_engine.raw_input', create = True, new = attackInputMock):
                battle(player)

        errorMsg = "Money was not returned correctly - multiple monster death with bonus difficulty."
        self.assertEqual(money, 30, errorMsg)
        errorMsg = "Experience was not returned correctly - multiple monster death with bonus difficulty."
        self.assertEqual(experience, 30, errorMsg)

    def testPlayerAttackPhase9(self):
        """
        Tests playerAttackPhase.

        Iteration9: for instances where several monsters have the same name, successive attacks
        result in attacking the same monster when attacks do not result in death blows. 
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import playerAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = Player("Russian", space)
        player._attack = 0
        bonusDifficulty = 1
        
        monster1 = MagicMock()
        monster1._takeAttack = MagicMock()
        monster1._name = "Jerk"
        monster1._experience = 10
        monster1._hp = 10
        monster2 = MagicMock()
        monster2._takeAttack = MagicMock()
        monster2._name = "Jerk"
        monster2._experience = 10
        monster2._hp = 10
        monster3 = MagicMock()
        monster3._takeAttack = MagicMock()
        monster3._name = "Jerk"
        monster3._experience = 10
        monster3._hp = 10
        monsters = [monster1, monster2, monster3]

        battleInputMock = MagicMock(side_effect = ["attack", "attack", "attack"])
        attackInputMock = MagicMock(side_effect = ["Jerk", "Jerk", "Jerk"])
                                                   
        with patch('battle_engine.raw_input', create = True, new = battleInputMock):
            with patch('battle_engine.raw_input', create = True, new = attackInputMock):
                battle(player)

        #Test that only one monster attacked
        errorMsg = "monster1 was supposed to be called but was not."
        self.assertTrue(monster1.called(), errorMsg)
        errorMsg = "Other monsters were not supposed to have been attacked but were."
        self.assertFalse(monster2.called(), errorMsg)
        self.assertFalse(monster3.called(), errorMsg)

    def testMonsterAttackPhase(self):
        """
        Tests that each monster gets to attack player.
        """
        from space import Space
        from player import Player
        from monsters.monster import Monster
        from battle_engine import monsterAttackPhase

        space = Space("Shire", "Full of Russians", "Eregion")
        player = MagicMock()
        player.takeAttack = MagicMock
        player._hp = 500
        player._maxHp = 500
        
        monster1 = MagicMock()
        monster1._attack = 5
        monsters = [monster1]

        #Calculate total damage
        totalDamage = 0
        for monster in monsters:
            totalDamage += monster._attack
        
        monsterAttackPhase(player, monsters)

        #Check that each player attacked player
        for monster in monsters:
            monster.attack.called_once_with(monster._attack)
            player.takeAttack.assert_called_with(monster._attack)

        #Check that player._hp is updated accordingly
        errorMsg = "player._hp was not updated correctly."
        self.assertEqual(player._hp, player._maxHp - totalDamage, errorMsg)

    def testEndSequence(self):
        """
        Tests that player money and experience increase by appropriate amounts.
        """
        from player import Player
        from space import Space
        from battle_engine import endSequence

        space = Space("Shire", "Home of chocolate bunnies", "Bun-Bun Mountain")
        player = Player("Russian", space)
        player._updateLevel = MagicMock()
        
        #0th element: money; 1st element: experience
        earnings = [30, 10]

        #Create defaults
        startingMoney = player._money
        startingExperience = player._experience

        #Test that player stats are updated and that player._updateLevel is called
        endSequence(player, earnings)
        errorMsg = "player._money was not updated to the correct value."
        self.assertEqual(player._money, startingMoney + 30, errorMsg)
        errorMsg = "player._experience was not updated to the correct value."
        self.assertEqual(player._experience, startingExperience + 10, errorMsg)
        player._updateLevel.called_once_with(10)
        
def handle_pdb(signal, frame):
    """
    Signal handler method that invokes pdb.

    @param signal:      Signal
    @param frame:       Frame
    """
    import pdb
    pdb.Pdb().set_trace(frame)

if __name__ == '__main__':
    #Add signal handler that invokes PDG
    signal.signal(signal.SIGINT, handle_pdb)

    #Supress output from game with "buffer=true"
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
