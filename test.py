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

    def testItems(self):
        from space import Space
        from items.item import Item

        #Prepare items
        blade = Item("blade", "appears to be dull", 1)
        bow = Item("bow", "long bow", 2) 

        #Create space
        space = Space("shire", "Home of the Hobbits.")
        items = space.getItemSet()

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
        items = space.getItemSet()
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
        items = space.getItemSet()
        self.assertEqual(items.count(), 1, "Room should contain exactly one item.")
        self.assertFalse(items.containsItem(blade), 
                "Blade found in room (even though it was removed).")
        self.assertTrue(items.containsItem(bow), "Could not find bow in room's set of items.")
        
class PickUpTest(unittest.TestCase):
    """
    Test PickUp class.
    """
    def testExecute(self):
        from space import Space
        from player import Player
        from items.item import Item
        from commands.pick_up_command import PickUpCommand
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        item = Item("Dagger", "A trusty blade", 2)
        space.addItem(item)
        pickUpCmd = PickUpCommand("pick up", "Picks up an object", player)
        
        #Assert item in space but not in inventory
        self.assertTrue(space.containsItem(item), "Space should have item but does not.")
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(item), "Player should not have item but does.")
        
        rawInputMock = MagicMock(return_value="Dagger")
        
        with patch('commands.pick_up_command.raw_input', create=True, new=rawInputMock):
            pickUpCmd.execute()
            
        #Assert item in player inventory but not in space
        self.assertFalse(space.containsItem(item), "Space should not have item but does.")
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(item), "Player should have item but does not.")
        
class DropTest(unittest.TestCase):
    """
    Test Drop class.
    """
    def testExecute(self):
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from commands.drop_command import DropCommand
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        weapon = Weapon("Dagger", "A trusty blade", 2, 2)
        
        player.addInventory(weapon)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)

        #Asserts item in player inventory but not in space
        self.assertFalse(space.containsItem(weapon), "Space should not have item but does.")
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have item but does not.")

        rawInputMock = MagicMock(return_value="weapon")
        
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        #Assert item in space but not in player inventory
        """
        TODO: Look at space.containsItem method
        self.assertTrue(space.containsItem(weapon), "Space should have item but does not. Instead it has %s" %space.getItemSet())
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have item but does.")
        """
class DescribeTest(unittest.TestCase):
    """
    Tests Describe class.
    """
    def testExecute(self):
        from player import Player
        from space import Space
        from commands.command import Command
        from commands.describe_command import DescribeCommand
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        descCmd = DescribeCommand("describe", "Gives description of space", player)

        #Tests that execute returns space description
        #TODO: find a way to make sure that a print statement came out correctly.
        """
        self.assertEqual(descCmd.execute(), "Home of the Hobbits", \
            "Describe command gave incorrect description.)
        """
class ArmorTest(unittest.TestCase):
    """
    Tests Armor class.
    """
    def testInit(self):
        from items.armor import Armor
        
        shield = Armor("Shield", "A cheap shield", 2, 3)

        #Tests that shield initialized correctly
        self.assertEqual(shield.getName(), "Shield", "Name did not initialize correctly.")
        self.assertEqual(shield.getDescription(), "A cheap shield", "Description did not initialize correctly.")
        self.assertEqual(shield.getWeight(), 2, "Weight did not initialize correctly.")
        self.assertEqual(shield.getDefense(), 3, "Defense did not initialize correctly.")

class WeaponTest(unittest.TestCase):
    """
    Tests Weapon class.
    """
    def testInit(self):
        from items.weapon import Weapon

        sword = Weapon("Sword", "A cheap sword", 1, 3)

        #Tests for correct initialization
        self.assertEqual(sword.getName(), "Sword", "Name did not initialize correctly.")
        self.assertEqual(sword.getDescription(), "A cheap sword", "Description did not initialize correctly.")
        self.assertEqual(sword.getWeight(), 1, "Weight did not initialize correctly.")
        self.assertEqual(sword.getAttack(), 3, "Damage did not initialize correctly.")

class Potion(unittest.TestCase):
    """
    Tests Potion class.
    """
    def testInit(self):
        from items.potion import Potion

        potion = Potion("Potion", "A small potion", 1, 10)
        
        #Tests for correct initialization
        self.assertEqual(potion.getName(), "Potion", "Name did not initialize correctly.")
        self.assertEqual(potion.getDescription(), "A small potion", "Description did not initialize correctly.")
        self.assertEqual(potion.getWeight(), 1, "Weight did not initialize correctly.")
        self.assertEqual(potion.getHealing(), 10, "Healing did not initialize correctly.")

class PlayerTest(unittest.TestCase):
    """
    Tests Player class.
    """
    def testInit(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.item_set import ItemSet
        from items.weapon import Weapon
        from items.armor import Armor
        from stats import Stats
        from items.starting_inventory import startingInventory
        import constants

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        blade = Item("Blade", "Appears to be dull", 1)
        
        #Test for correct initialization
        self.assertEqual(player._inventory, player.getInventory(), "Starting inventory was not initialized correctly.")
        self.assertEqual(player._level, 1, "Player level was not initialized correctly. it was %s" %player._level)
        self.assertEqual(player._hp, constants.HP_STAT * player._level, "Player HP was not initialized correctly.")
        self.assertEqual(player._attack, constants.ATTACK_STAT * player._level, "Player damage was not initialized correctly.")

    def testAttack(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.item_set import ItemSet
        from items.weapon import Weapon
        from items.armor import Armor
        from stats import Stats
        from monsters.monster import Monster
        from items.starting_inventory import startingInventory
        import constants

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        monster = Monster("Orc", "An orc.", 10, 1, 1)
        
        #Check monster is undamaged
        self.assertEqual(monster.getHp(), 10, "Monster HP did not initialize correctly.")

        player.attack(monster)
        
        #Player attacks monster
        actualHp = monster.getHp()
        expectedHp = 10 - (player._attack + player._weaponAttack) 
        self.assertEqual(actualHp, expectedHp, "Monster attack failed.")

    def testTakeDamage(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.item_set import ItemSet
        from items.weapon import Weapon
        from items.armor import Armor
        from stats import Stats
        from monsters.monster import Monster
        from items.starting_inventory import startingInventory
        import constants

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        monster = Monster("Orc", "An orc.", 10, 1, 1)

        originalHp = player.getHp()
        monster.attack(player)
        
        #Test player's takeAttack method
        newHp = player.getHp()
        self.assertTrue(originalHp > newHp, "Player takeAttack failed.")

    """
    # TODO: Update this test after adding Hp, Damage, etc. features to Player class.

    def testLevelUp(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.item_set import ItemSet
        from items.weapon import Weapon
        from items.armor import Armor
        from stats import Stats
        from monsters.monster import Monster
        from starting_inventory import startingInventory
        import constants

        space = Space()
        player = Player("Frodo", space)

        originalLevel = player.getLevel()
        originalHp = player.getHp()
        originalDamage = player.getDamage()
        player.increaseExperience(1000)

        newLevel = player.getLevel()
        self.assertTrue(newLevel > originalLevel, "Player did not level up.")
        self.assertTrue(newHp > originalHp, "Player HP did not increase.")
        self.assertTrue(newDamage > originalDamage, "Player damage did not increase.")
    """
        
    def testEquipUnequip(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        from stats import Stats
        from items.starting_inventory import startingInventory
        import constants
        
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)

        newItem = Item("Chainik Reakettle", "Makes good tea", 1)
        newWeapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3)
        newArmor = Armor("Cookies of Miles", "Defends against sadness", 2, 4)
        
        player.addInventory(newItem)
        player.addInventory(newWeapon)
        player.addInventory(newArmor)

        #Attempt to equip new items
        player.equip(newItem)
        self.assertFalse(newItem in player.getEquipped(), "Equipped %s and should not have." % (newItem))
        player.equip(newWeapon)
        self.assertTrue(newWeapon in player.getEquipped(), "Failed to equip %s" % (newWeapon))
        player.equip(newArmor)
        self.assertTrue(newArmor in player.getEquipped(), "Failed to equip %s" % (newArmor))
        
        #Attempt to unequip items
        player.unequip(newWeapon)
        self.assertFalse(newWeapon in player.getEquipped(), "Failed to unequip %s" % (newWeapon))
        player.unequip(newArmor)
        self.assertFalse(newArmor in player.getEquipped(), "Failed to unequip %s" % (newArmor))
        
if __name__ == '__main__':
    #Supress output from game with "buffer=true"
    unittest.main()
