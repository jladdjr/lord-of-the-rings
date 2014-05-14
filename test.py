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
    Test for Space class.
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
        self.assertTrue(items.containsItem(bow), "Could not find bow in room's set of items.")

    def testCities(self):
        from space import Space
        from cities.city import City

        #Create city
        newYorkCity = City("City", "An enormous city", "Come test here")

        #Create space
        newYork = Space("Space", "A huge space", "Welcome to our space", city = newYorkCity)

        #Assert city in space
        errorMsg = "Space should contain city but does not."
        self.assertEqual(newYork.getCity(), newYorkCity, errorMsg)

    def testUniquePlace(self):
        from space import Space
        from unique_place import UniquePlace

        #Create UniquePlace
        dmitriyHouse = UniquePlace("Dmitriy's House", "Lots of vodka", "[knocks once]")

        #Create space
        chocolateMountain = Space("Chocolate Mountain", "Chocolate rain here", "Welcome", uniquePlace = dmitriyHouse)
        
        #Assert uniquePlace in space
        errorMsg = "Space should contain uniquePlace but does not."
        self.assertEqual(chocolateMountain.getUniquePlace(), dmitriyHouse, errorMsg)

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

        #Create two-way ports
        north = Space("North Space", "Very cold", "Welcome")
        south = Space("South Space", "Very warm", "Welcome")
        east = Space("East Space", "Very mountainous", "Welcome")
        west = Space("West Space", "Coastal", "Welcome")

        space.createExit("north", north, outgoingOnly = False)
        space.createExit("south", south, outgoingOnly = False)
        space.createExit("east", east, outgoingOnly = False)
        space.createExit("west", west, outgoingOnly = False)

        #Test getExit method for destination spaces
        errorMsg = "getExit() test failed."
        self.assertEqual(north.getExit("south"), space, errorMsg)
        self.assertEqual(south.getExit("north"), space, errorMsg)
        self.assertEqual(east.getExit("west"), space, errorMsg)
        self.assertEqual(west.getExit("east"), space, errorMsg)

        #Test ports created using _isExit() for space
        errorMsg = "Ports are supposed to be created but are not - tested using _isExit()."
        self.assertEqual(space._isExit("north"), True, errorMsg)
        self.assertEqual(space._isExit("south"), True, errorMsg)
        self.assertEqual(space._isExit("east"), True, errorMsg)
        self.assertEqual(space._isExit("west"), True, errorMsg)

        #Test ports created without using direct access for Space
        from constants import Direction
        errorMsg = "Ports are supposed to be created but are not - by direct attribute access."
        self.assertEqual(space._exits[Direction.North], north, errorMsg)
        self.assertEqual(space._exits[Direction.South], south, errorMsg)
        self.assertEqual(space._exits[Direction.East], east, errorMsg)
        self.assertEqual(space._exits[Direction.West], west, errorMsg)

        #Test ports created without using direct access for destination Spaces
        errorMsg = "Two-way ports were supposed to have been created but were not - by direct attribute access."
        self.assertEqual(north._exits[Direction.South], space, errorMsg)
        self.assertEqual(south._exits[Direction.North], space, errorMsg)
        self.assertEqual(east._exits[Direction.West], space, errorMsg)
        self.assertEqual(west._exits[Direction.East], space, errorMsg)
                                      
        #Test two-way movement
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
        player._location = space
        northCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)
        
        eastCmd.execute()
        errorMsg = "Player should be in east space but is not."
        self.assertEqual(player.getLocation(), east, errorMsg)
        player._location = space
        westCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)
        
        westCmd.execute()
        errorMsg = "Player should be in west space but is not."
        self.assertEqual(player.getLocation(), west, errorMsg)
        player._location = space
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

        #Test _isExit() method - where there are no ports
        errorMsg = "_isExit() failed to return the correct port - no ports exit."
        self.assertTrue(space._isExit("north"), None, errorMsg)
        self.assertTrue(space._isExit("south"), None, errorMsg)
        self.assertTrue(space._isExit("east"), None, errorMsg)
        self.assertTrue(space._isExit("west"), None, errorMsg)

    def testMovement2(self):
        """
        Smaller test for one-way ports and one-way movement.
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
        from space import Space
        from player import Player
        from items.item import Item
        from commands.pick_up_command import PickUpCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        item = Item("Dagger", "A trusty blade", 2)
        pickUpCmd = PickUpCommand("pick up", "Picks up an object", player)
        
        space.addItem(item)

        #Assert item in space but not in inventory and equipment
        self.assertTrue(space.containsItem(item), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(item), "Player should not have item but does in inventory.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player should not have item but does in equipment.")
            
        #Execute pickUpCmd and assert item in player inventory but not in space and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.pick_up_command.raw_input', create=True, new=rawInputMock):
            pickUpCmd.execute()
            
        self.assertFalse(space.containsItem(item), "Space should not have item but does.")

        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player should not have item in equipment.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(item), "Player should have item but does not.")
        
class DropTest(unittest.TestCase):
    """
    Test Drop class.
    """
    def testExecute(self):
        """
        Test for case: item in inventory and equipment.
        """
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)

        player.addToInventory(weapon)
        player.equip(weapon)

        #Asserts item in player inventory and equipped but not in space
        self.assertFalse(space.containsItem(weapon), "Space should not have item but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have item but does not.")

        equipped = player.getEquipped()
        self.assertTrue(equipped.containsItem(weapon), "Equipped should have item but does not.")

        #Assert item in space but not in player inventory and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        self.assertTrue(space.containsItemString("Dagger"), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have item but does.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipment should not have item but does.")

    def testExecute2(self):
        """
        Test for case: item in inventory and but not in equipment.
        """
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)

        player.addToInventory(weapon)
        
        #Asserts item in player inventory but not in equipped and space
        self.assertFalse(space.containsItem(weapon), "Space should not have item but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have item but does not.")

        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipped should not have item but does.")

        #Assert item in space but not in player inventory and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        self.assertTrue(space.containsItemString("Dagger"), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have item but does.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipment should not have item but does.")
        
class DescribeTest(unittest.TestCase):
    """
    Tests Describe class.
    """
    def testExecute(self):
        from player import Player
        from space import Space
        from commands.describe_command import DescribeCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        descCmd = DescribeCommand("describe", "Gives description of space", player)

        #Tests that execute returns space description
        #TODO: find a way to make sure that a print statement came out correctly.
        """
        self.assertEqual(descCmd.execute(), "Home of the Hobbits", \
            "Describe command gave incorrect description.")
        """

class EquipTest(unittest.TestCase):
    """
    Tests Equip Command.
    """
    def testExecute(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.equip_command import EquipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)
        
        #Trying to equip items not in inventory
        item = Item("Charm", "Unknown effects", 1)
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of Faith", 2, 2, 2)

        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Player equipped item not in inventory.")
        self.assertFalse(equipped.containsItem(armor), "Player equipped item not in inventory.")
        
        #Trying to equip item that cannot be equipped (e.g. item is not instance of Armor or Weapon)
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        item = Item("Charm", "Unknown effects", 1)

        inventory = player.getInventory()
        inventory.addItem(item)

        rawInputMock = MagicMock(return_value="Charm")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player equipped item of Item class.")

        #Equipping item that can be equipped
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2) 

        inventory = player.getInventory()
        inventory.addItem(weapon)
        inventory.addItem(armor)
        
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
            
        equipped = player.getEquipped()
        
        self.assertTrue(equipped.containsItem(weapon), "Player failed to equip equipable item.")
        self.assertTrue(equipped.containsItem(armor), "Player failed to equip equipable item.")
        
        #Equipping an item that is already equipped
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

        #Pretest
        self.assertEqual(equipped.count(), 2, "Player is supposed to have two equipped items but lists more.")
                        
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 
            
        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 

        #Test still only two equipped items
        self.assertEqual(equipped.count(), 2, "Player is supposed to have two equipped items but lists more.")

    def testExecutePlayerStatsWeapon(self):
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from commands.equip_command import EquipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)

        #Create defaults
        defaultAttack = player._level * constants.ATTACK_STAT

        rawInputMock = MagicMock(return_value="Sword of the Spirit")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 

        #Test for change
        errorMsg = "Player._attack changed with weapon equip when it should not have."
        self.assertEqual(player._attack, defaultAttack, errorMsg)
        errorMsg = "player._weaponAttack not updated to correct value."
        self.assertEqual(player._weaponAttack, weapon._attack, errorMsg)
        errorMsg = "Player._totalAttack not updated to correct value."
        self.assertEqual(player._totalAttack, defaultAttack + weapon._attack, errorMsg)

    def testExecutePlayerStatsArmor(self):
        from player import Player
        from space import Space
        from items.armor import Armor
        from commands.equip_command import EquipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        armor = Armor("Shield of Faith", "For quenching fiery darts", 1, 1, 1)

        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 

        #Test for change
        errorMsg = "Player._armorDefense stat was not updated correctly."
        self.assertEqual(player._armorDefense, armor._defense, errorMsg)
                         
class UnequipTest(unittest.TestCase):
    """
    Tests Unequip Command.
    """
    def testExecute(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand

        #Attempting to unequip item not currently equipped
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        item = Item("Charm", "Unknown effects", 1)
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2)

        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        ###TODO: FIND SOME WAY TO MAKE SURE THAT PRINT STATEMENT PRINTED
        
        #Attempting to unequip item that may be unequipped
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)

        player.equip(weapon)
        player.equip(armor)
        
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        equipped = player.getInventory()
        self.assertFalse(equipped.containsItem(weapon), "Failed to unequip item that it should have.")
        self.assertFalse(equipped.containsItem(armor), "Failed to unequip item that it should have.")

    def testExecutePlayerStatsWeapon(self):
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from commands.unequip_command import UnequipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("Unequip", "Unequips item in inventory to player", player)

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)

        #Setup
        player.equip(weapon)
        
        rawInputMock = MagicMock(return_value="Sword of the Spirit")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute() 

        #Test for change
        errorMsg = "player._weaponAttack should be zero but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "player._totalAttack should be attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)
        
    def testExecutePlayerStatsArmor(self):
        from player import Player
        from space import Space
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("Unequip", "Unequips item in inventory to player", player)

        armor = Armor("Shield of Faith", "For quenching fiery darts", 1, 1, 1)
        
        #Setup
        player.equip(armor)
        
        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute() 

        #Test for change
        errorMsg = "player._armorDefense should be zero after unequip but is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)

class UsePotionTest(unittest.TestCase):
    """
    Tests UsePotion command.
    """
    def testExecute(self):
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
        healing = 9
        expectedFinalHealth = 10
        
        potion = Potion("Enormous Potion", "So big", 1, healing, 10)
        player._inventory.addItem(potion)
        
        rawInputMock = MagicMock(return_value="Enormous Potion")
        with patch('commands.use_potion_command.raw_input', create = True, new = rawInputMock):
            usePotionCmd.execute()
            
        errorMsg = "Inventory still contains potion when it should not."
        self.assertFalse(inventory.containsItem(potion), errorMsg)
        errorMsg = "Player health not at correct amount."
        self.assertEqual(player._hp, expectedFinalHealth, errorMsg)
            
class WeaponTest(unittest.TestCase):
    """
    Tests Weapon class.
    """
    def testInit(self):
        from items.weapon import Weapon

        WEIGHT = 1
        ATTACK = 3
        COST = 1

        sword = Weapon("Sword", "A cheap sword", WEIGHT, ATTACK, COST)

        #Tests for correct initialization
        self.assertEqual(sword.getName(), "Sword", "Name did not initialize correctly.")
        self.assertEqual(sword.getDescription(), "A cheap sword", "Description did not initialize correctly.")
        self.assertEqual(sword.getWeight(), WEIGHT, "Weight did not initialize correctly.")
        self.assertEqual(sword.getAttack(), ATTACK, "Damage did not initialize correctly.")
        self.assertEqual(sword.getCost(), COST, "Cost did not initialize correctly.")

class ArmorTest(unittest.TestCase):
    """
    Tests Armor class.
    """
    def testInit(self):
        from items.armor import Armor

        WEIGHT = 2
        DEFENSE = 3
        COST = 1
        
        shield = Armor("Shield", "A cheap shield", WEIGHT, DEFENSE, COST)

        #Tests that shield initialized correctly
        self.assertEqual(shield.getName(), "Shield", "Name did not initialize correctly.")
        self.assertEqual(shield.getDescription(), "A cheap shield", "Description did not initialize correctly.")
        self.assertEqual(shield.getWeight(), WEIGHT, "Weight did not initialize correctly.")
        self.assertEqual(shield.getDefense(), DEFENSE, "Defense did not initialize correctly.")
        self.assertEqual(shield.getCost(), COST, "Cost did not initialize correctly.")

class Potion(unittest.TestCase):
    """
    Tests Potion class.
    """
    def testInit(self):
        from items.potion import Potion

        WEIGHT = 1
        HEALING = 10
        COST = 1

        potion = Potion("Potion", "A small potion", WEIGHT, HEALING, COST)
        
        #Tests for correct initialization
        self.assertEqual(potion.getName(), "Potion", "Name did not initialize correctly.")
        self.assertEqual(potion.getDescription(), "A small potion", "Description did not initialize correctly.")
        self.assertEqual(potion.getWeight(), WEIGHT, "Weight did not initialize correctly.")
        self.assertEqual(potion.getHealing(), HEALING, "Healing did not initialize correctly.")
        self.assertEqual(potion.getCost(), COST, "Cost did not initialize correctly.")

class PlayerTest(unittest.TestCase):
    """
    Tests Player class.
    """
    def testInit(self):
        from player import Player
        from space import Space
        from items.item_set import ItemSet
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        
        #Test for correct initialization
        self.assertEqual(player._name, "Frodo", "Player name did not initialize correctly.")
        self.assertEqual(player._location, space, "Player location did not initialize correctly.")
        self.assertEqual(player._money, constants.STARTING_MONEY, "Money did not initialize correctly.")
        
        emptyList = []
        self.assertEqual(player._inventory.getItems(), emptyList, "Player inventory was not initialized.")
        self.assertEqual(player._equipped.getItems(), emptyList, "Player equipped was not initialized.")
        
        self.assertEqual(player._experience, constants.STARTING_EXPERIENCE, "Player experience was not initialized.")
        self.assertEqual(player._level, constants.STARTING_LEVEL, "Player level was not initialized.")
        
        self.assertEqual(player._maxHp, constants.HP_STAT, "Player max Hp was not initialized.")
        self.assertEqual(player._hp, constants.HP_STAT, "Player Hp was not initialized.")
        self.assertEqual(player._attack, constants.ATTACK_STAT, "Player attack was not initialized.")

        self.assertEqual(player._weaponAttack, constants.STARTING_WEAPON_ATTACK, "Player attack bonus was not initialized.")
        self.assertEqual(player._armorDefense, constants.STARTING_ARMOR_DEFENSE, "Player defense bonus was not initialized.")
        self.assertEqual(player._totalAttack, player._attack + player._weaponAttack, "Player ._totalAttack did not initiate correctly.")
        
    def testAttack(self):
        from player import Player
        from space import Space
        from monsters.monster import Monster

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        MONSTER_HEALTH = 10
        monster = Monster("Orc", "An orc.", MONSTER_HEALTH, 1, 1)
        
        #Check monster health default state
        self.assertEqual(monster._hp, MONSTER_HEALTH, "Monster Hp did not initialize correctly.")
        
        #Player attacks monster
        player.attack(monster)
        
        actualHp = monster._hp
        expectedHp = 10 - (player._totalAttack)
        
        self.assertEqual(actualHp, expectedHp, "Monster attack failed to work correctly.")

    def testTakeDamage(self):
        from player import Player
        from space import Space
        from monsters.monster import Monster

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        
        #When attack is more than maxHp
        OVERKILL = player._maxHp + 10000

        player.takeAttack(OVERKILL)
        errorMsg = "Overkill testcase in testTakeDamage() failed."
        self.assertEqual(player._hp, 0, errorMsg)
        
        #When attack is less than maxHp
        player._hp = player._maxHp
        UNDERKILL = player._maxHp - 1

        player.takeAttack(UNDERKILL)
        errorMsg = "Underkill testcase in testTakeDamage() failed."
        self.assertEqual(player._hp, 1, errorMsg)

    def testTakeDamageArmor(self):
        from player import Player
        from space import Space
        from monsters.monster import Monster
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

        #Test starting experience
        errorMsg = "Player starting experienced failed to initialize correctly."
        self.assertEqual(player._experience, constants.STARTING_EXPERIENCE, errorMsg)

        #Test increaseExperience()
        player.increaseExperience(10000)
        
        errorMsg = "Player experience failed to increase."
        self.assertTrue(player._experience > constants.STARTING_EXPERIENCE, errorMsg)
        
    def _updateLevel(self):
        from player import Player
        from space import Space
        from math import floor
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        #Determine default player stats
        defaultLevel = self._level
        defaultMaxHp = self._maxHp
        defaultAttack = self._attack
        defaultTotalAttack = self._totalAttack

        #Increase player experience and run _updateLevel
        originalExperience = player._experience
        newExperience = 1000
        player._experience = newExperience + originalExperience
        player._updateLevel()

        #Test that stats have increased
        self.assertTrue(player._level > defaultLevel, "Player level did not increase.")
        self.assertTrue(player._maxHp > defaultMaxHp, "Player Hp did not increase.")
        self.assertTrue(player._attack > defaultAttack, "Player attack did not increase.")
        self.assertTrue(player._totalAttack > defaultTotalAttack, "Player totalAttack did not increase.")
        
        #Test for proper player stat change
        self.assertEqual(player._level, floor(player._experience/20) + 1, "Player level is incorrect.")
        self.assertEqual(player._maxHp, player._level * constants.HP_STAT, "Player Hp is incorrect.")
        self.assertEqual(player._attack, player._level * constants.ATTACK_STAT, "Player attack is incorrect.")
        self.assertEqual(player._totalAttack, player._attack + player._weaponAttack, "Player totalAttack is incorrect.")
        
    def testHeal(self):
        #Heal where healing amount is greater than total amount possible
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        attackAmount = 2
        healAmount = 3
        
        player.takeAttack(attackAmount)
        player.heal(healAmount)

        self.assertEqual(player._hp, player._maxHp, "Healing testcase #1 failed.")

        #Heal where healing amount is less than total amount possible
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        attackAmount = 3
        healAmount = 2
        difference = attackAmount - healAmount
        
        player.takeAttack(attackAmount)
        player.heal(healAmount)

        self.assertEqual(player._hp, player._maxHp - difference, "Healing testcase #2 failed.")
        
    def testEquipUnequip(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        newItem = Item("Chainik Reakettle", "Makes good tea", 1)
        newWeapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        newArmor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)
        
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)

        #Pretest player-specific items-based attributes
        errorMsg = "_weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "totalAttack should be simply attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)

        #Attempt to equip new items
        player.equip(newItem)
        self.assertFalse(newItem in player.getEquipped(), "Equipped %s and should not have." % newItem)
        player.equip(newWeapon)
        self.assertTrue(newWeapon in player.getEquipped(), "Failed to equip %s" % newWeapon)
        player.equip(newArmor)
        self.assertTrue(newArmor in player.getEquipped(), "Failed to equip %s" % newArmor)

        #Posttest player-specific items-based attributes
        errorMsg = "_weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, weapon.getAttack(), errorMsg)
        errorMsg = "_armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, armor.getDefenses(), errorMsg)
        errorMsg = "_totalAttack should have been updated but was not."
        self.assertEqual(player._totalAttack, player._attack + weapon.getAttack(), errorMsg)
        
        #Attempt to unequip items
        player.unequip(newWeapon)
        self.assertFalse(newWeapon in player.getEquipped(), "Failed to unequip %s" % newWeapon)
        player.unequip(newArmor)
        self.assertFalse(newArmor in player.getEquipped(), "Failed to unequip %s" % newArmor)

        #Check to see that item-specific attributes are reset to pre-equip figures
        errorMsg = "_weaponAttack should be 0 but it is not - unequip."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "armorDefense should be 0 but it is not - unequip."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "totalAttack should be simply attack but it is not - unequip."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)
        
    def addToInventory(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        newItem = Item("Chainik Reakettle", "Makes good tea", 1)
        newWeapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        newArmor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)

        #Test add items to inventory
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)
        errorMsg = "Failed to add in legimiate item to inventory"
        self.assertTrue(newItem in player._inventory, errorMsg)
        self.assertTrue(newWeapon in player._inventory, errorMsg)
        self.assertTrue(newArmor in player._inventory, errorMsg)
        
        #Test to add items already in inventory to inventory
        numberOfItems = len(player._inventory)
        
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)
        
        newNumberOfItems = len(player._inventory)
        errorMsg = "Number of items increased when it should not have."
        self.assertEqual(numberOfItems, newNumberOfItems, errorMsg)

    def removeFromInventory(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        newItem = Item("Chainik Reakettle", "Makes good tea", 1)
        newWeapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        newArmor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)

        #Test correct character initialization
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)
        errorMsg = "Failed to initialize test character correctly."
        self.assertTrue(newItem in player._inventory, errorMsg)
        self.assertTrue(newWeapon in player._inventory, errorMsg)
        self.assertTrue(newArmor in player._inventory, errorMsg)

        #Test removeFromInventory() default case
        player.removeFromInventory(newItem)
        player.removeFromInventory(newWeapon)
        player.removeFromInventory(newArmor)
        errorMsg = "Failed to remove item from inventory."
        self.assertFalse(newItem in player._inventory, errorMsg)
        self.assertFalse(newWeapon in player._inventory, errorMsg)
        self.assertFalse(newArmor in player._inventory, errorMsg)

        #Set things back up
        player._inventory = [newItem, newWeapon, newArmor]

        #Test that items are unequipped correctly
        player.removeFromInventory(newItem)
        player.removeFromInventory(newWeapon)
        player.removeFromInventory(newArmor)
        errorMsg = "Failed to remove item from equipped."
        self.assertFalse(newItem in player._equipped, errorMsg)
        self.assertFalse(newWeapon in player._equipped, errorMsg)
        self.assertFalse(newArmor in player._equipped, errorMsg)

        #Test that item-specific character attributes are reset to original values
        errorMsg = "_weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "_armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "_totalAttack should be player._attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)

    def canMoveDirection(self):
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

        #Test negative case - no ports created
        errorMsg = "player.canMoveDirection() negative case failed."
        self.assertFalse(player.canMoveNorth(), errorMsg)
        self.assertFalse(player.canMoveSouth(), errorMsg)
        self.assertFalse(player.canMoveEast(), errorMsg)
        self.assertFalse(player.canMoveWest(), errorMsg)

        #Test positive case - ports created
        space.createExit("north", north, outgoingOnly = False)
        space.createExit("south", south, outgoingOnly = False)
        space.createExit("east", east, outgoingOnly = False)
        space.createExit("west", west, outgoingOnly = False)

        #Test negative case - no ports created
        errorMsg = "player.canMoveDirection() positive case failed."
        self.assertTrue(player.canMoveNorth(), errorMsg)
        self.assertTrue(player.canMoveSouth(), errorMsg)
        self.assertTrue(player.canMoveEast(), errorMsg)
        self.assertTrue(player.canMoveWest(), errorMsg)
        
class InnTest(unittest.TestCase):
    """
    Tests the healing ability of Inn Object.
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
                
        #Player's health is lowest possible to be alive
        player._hp = 1
        #Player's money is equal to 10
        player._money = 10

        #Player chooses to stay at the inn
        rawInputMock = MagicMock(return_value=1)
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
        #Player's money should decrease by the cost of the inn, in our case 5
        self.assertEqual(player._money, 5, "Player's money not decreased by correct amount.")
        
        #Player's health should increase to maximum
        self.assertEqual(player._hp, player._maxHp, "Player's health not increased to full health.")
        
class ShopSellItems(unittest.TestCase):
    """
    Tests the ability to sell in the Shop Object:
    -Item should be removed from inventory, equipped
    -Player money should be increased by half of its value
    -Item should be added to shop wares at full original cost
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor

        testShop = Shop("Chris' testing shop", "Come test here", "Hi", 5, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
        
        #Create starting iventory
        COST = 1
        weapon = Weapon("Knife", "Jack of all trades", 3, 1, COST)
        armor = Armor("Leather Tunic", "Travel cloak", 3, 1, COST)

        #Add items to player's inventory
        inventory = player._inventory
        player.addToInventory(weapon)
        player.addToInventory(armor)
        self.assertTrue(inventory.containsItemWithName("Knife"), "Knife not added to inventory.")
        self.assertTrue(inventory.containsItemWithName("Leather Tunic"), "Leather Tunic not added to inventory.")

        #Equip items and test to see that items are equipped
        equipped = player.getEquipped()
        player.equip(weapon)
        player.equip(armor)
        errorMsg = "Player items were not equipped correctly."
        self.assertTrue(weapon in equipped, errorMsg)
        self.assertTrue(armor in equipped, errorMsg)
                        
        #Player chooses to: 3(sell items), to sell knife, yes, 5(Quit) the shop
        rawInputMock = MagicMock(side_effect = ["3", "Knife", "y", "5"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

        #Player chooses to: 3(sell items), to sell leather tunic, yes, 5(Quit) the shop
        rawInputMock = MagicMock(side_effect = ["3", "Leather Tunic", "y", "5"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
        
        #Player's money should increase by the half the cost of item. In our case, it should increase by 1
        self.assertEqual(player._money, 21, "Player's money not increased by correct amount. It is %s." % player._money)
        
        #Player's inventory should no longer include items
        self.assertFalse(inventory.containsItemWithName("Knife"), "Knife that was sold is still in inventory")
        self.assertFalse(inventory.containsItemWithName("Leather Tunic"), "Leather tunic that was sold is still in inventory")

        #Player equipped should no longer include items
        self.assertFalse(inventory.containsItemWithName("Knife"), "Knife that was sold is still in equipped")
        self.assertFalse(inventory.containsItemWithName("Leather Tunic"), "Leather tunic that was sold is still in equipped")

        #Items now appear in shop wares
        errorMsg = "Items are now supposed to be in shop inventory but are not."
        self.assertTrue(weapon in testShop._items, errorMsg)
        self.assertTrue(armor in testShop._items, errorMsg)

        #Item prices are normal prices, not sell value
        errorMsg = "Item costs were not set back to where they were supposed to be."
        for item in testShop._items:
            self.assertEqual(item._cost, COST, errorMsg) 
        
        #Player chooses to: gobbledigook, 5(Quit) the shop - context menus should not crash program
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "5"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

class ShopPurchaseItems(unittest.TestCase):
    """
    Tests the ability to purchase items in the Shop Object:
    1.) Purchasing an item player has money for
        - item in inventory, not in equipped, not in shop wares, money changed by correct amount
    2.) Failing to purchase an item player does not have money for
        - item not in inventory, not in equipped, in shop wares, money unchanged
    3.) Failing to purchase invalid item
        - item not in inventory, not in equipped, money unchanged
    4.) Purchased items are removed from shop inventory
    5.) Not crashing when user input is gobbledigook
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor
        from items.potion import Potion

        testShop = Shop("Chris' testing Shop", "Come test here", "Hi", 5, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
       
        #Our shop should currently have 5 items (this was designed when it was created)
        self.assertEqual(len(testShop._items), 5, "Our test shop was generated with the wrong number of items")
        errorMsg = "Items in shop inventory are of wrong type."
        for item in testShop._items:
            self.assertTrue(isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Potion), errorMsg)

        #Add Potion to Shop inventory with weight=1, healing=5, cost=3
        testPotion = Potion("Medium Potion of Healing", "A good concoction. Made by Master Wang.", 1, 5, 3)
        testShop._items.append(testPotion)
       
        #Player should start with 20 rubles
        self.assertEqual(player._money, 20, "Player does not start with 20 rubles")
       
        #Player chooses to: 4(purchase item), "Medium Potion of Healing"(purchase this specific item), 5(quit the shop)
        rawInputMock = MagicMock(side_effect = ["4", "Medium Potion of Healing", "5"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Player's money should decrease by the cost of medium potion, which is 3
        self.assertEqual(player._money, 17, "Player's money not decreased by correct amount. It is %s" % player._money)
       
        #Test item in inventory, not in equipped, not in shop wares
        errorMsg = "Medium Potion that was purchased was not added to inventory."
        self.assertTrue(player._inventory.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is still in shop wares."
        self.assertFalse(testPotion in testShop._items, errorMsg)
        
        #Add SuperDuperLegendary Potion to Shop inventory with weight=1, healing=35, cost=28
        testPotion2 = Potion("SuperDuperLegendary Potion of Healing", "A Wang concoction. Made by Master Wang.", 1, 35, 28)
        testShop._items.append(testPotion2)

        #Player chooses to: 4(purchase item), "SuperDuperLegendary Potion of Healing", 5(quit the shop)
        rawInputMock = MagicMock(side_effect = ["4", "SuperDuperLegendary Potion of Healing", "5"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Player's money should not decrease by the cost of SuperDuperLegendary Potion of Healing, which is 28
        errorMsg = "Player's money should not be decreased from 17. Player can't buy SuperDuperLegendary Potion. It is currently %s." % player._money
        self.assertEqual(player._money, 17, errorMsg)
       
        #Test item not in inventory, not in equipped, in shop wares
        errorMsg = "Medium Potion that was purchased was added to inventory."
        self.assertFalse(player._inventory.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is no longer in shop wares."
        self.assertTrue(testShop._items.containsItemWithName("Medium Potion of Healing"), errorMsg)

        #Player chooses to: 4(purchase item), input "Fake Item", 5(quit the shop)
        rawInputMock = MagicMock(side_effect = ["4", "Fake Item", "5"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Player's money should not change
        errorMsg = "Player's money should not be decreased when trying to purchase fake item. It is currently %s" % player._money
        self.assertEqual(player._money, 17, errorMsg)
       
        #Test item not in inventory, not in equipped, not in shop wares
        errorMsg = "Medium Potion that was purchased was added to inventory."
        self.assertFalse(player._inventory.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is in shop wares."
        self.assertFalse(testShop._items.containsItemWithName("Medium Potion of Healing"), errorMsg)
        
        #Player chooses to: gobbledigook, 5(Quit) the shop
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "5"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
            
        #TODO make test for verifying the stats of items in the shop, and put into 1 shop test class with multiple methods
            
class SquareDoesNotCrash(unittest.TestCase):
    """
    Tests the ability of Square Object.
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from cities.square import Square
        from cities.city import City

        testsquare = Square("Chris' testing Square", "testing square", "Come test here", {"Master Wang":"I am Master Wang, creator various things in this Lord of the Rings game", "Miles":"Hello, I am Miles, the cookie legend"})
        testcity = City("Test City", "testing city", "hello to testing city. see Chris' Square", testsquare)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testcity)
        player = Player("Frodo", space)
        
        #Player chooses to: 1(talk), to Master Wang, 1(talk), to Miles, 2(Leave) the square
        rawInputMock = MagicMock(side_effect = ["1", "Master Wang", "1", "Miles", "gobbledigook", "2"])
        
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testsquare.enter(player)
        
        #if the code gets here, then it hasn't crashed yet; test something arbitrary here, like player's money.
        self.assertEqual(player._money, 20, "Why does player's money not equal 20?")
        
class UniquePlace(unittest.TestCase):
    """
    Tests the ability of UniquePlace Object.
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from unique_place import UniquePlace

        testuniqueplace = UniquePlace("Chris' unique testing room", "Come test here", "Hi")
        space = Space("Shire", "Home of the Hobbits.", "Mordor", uniquePlace = testuniqueplace)
        player = Player("Frodo", space)
        
        #if the code gets here, then it hasn't crashed yet; test something arbitrary here, like player's money.
        self.assertEqual(player._money, 20, "Why does player's money not equal 20?")



if __name__ == '__main__':
    #Supress output from game with "buffer=true"
    unittest.main()
