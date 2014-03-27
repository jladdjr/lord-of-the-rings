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
        pickUpCmd = PickUpCommand("pick up", "Picks up an object", player)
        
        space.addItem(item)

        #Assert item in space but not in inventory and not in equipment
        self.assertTrue(space.containsItem(item), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(item), "Player should not have item but does in inventory.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player should not have item but does in equipment.")
            
        #Assert item in player inventory but not in space and not in equipment
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
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2)

        player.addInventory(weapon)
        player.addEquipped(weapon)

        #Asserts item in player inventory but not in space
        self.assertFalse(space.containsItem(weapon), "Space should not have item but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have item but does not.")

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
        
        space = Space("Shire", "Home of the Hobbits.")
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
        from commands.equip_command import EquipCommand

        #Tests default states
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)

        #Trying to equip item not in inventory
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        item = Item("Charm", "Unknown effects", 1)
        weapon = Weapon("Dagger", "A trusty blade", 2, 2)

        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Player equipped item not in inventory.")
        
        #Trying to equip item that cannot be equipped (e.g. item is not instance of Armor or Weapon)
        space = Space("Shire", "Home of the Hobbits.")
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
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2)

        inventory = player.getInventory()
        inventory.addItem(weapon)
        
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
            
        equipped = player.getEquipped()
        
        self.assertTrue(equipped.containsItem(weapon), "Player failed to equip equipable item.")
        
        #Equipping an item that is already equipped
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2)

        inventory = player.getInventory()
        inventory.addItem(weapon)
        
        equipped = player.getEquipped()
        equipped.addItem(weapon)
        
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 
            
        numberInInventory = 0
        numberInEquipped = 0
        for item in inventory._items:
            if item == weapon:
                numberInInventory += 1
        for item in equipped._items:
            if item == weapon:
                numberInEquipped += 1
            
        self.assertEqual(inventory.count(), 1, "Equipping an item that is already equipped failed -- inventory problem.")
        self.assertEqual(equipped.count(), 1, "Equipping an item that is already equipped failed -- equipment problem.")
        
class UnequipTest(unittest.TestCase):
    """
    Tests Unequip Command.
    """
    def testExecute(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from commands.unequip_command import UnequipCommand

        #Attempting to unequip item not currently equipped
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        item = Item("Charm", "Unknown effects", 1)
        weapon = Weapon("Dagger", "A trusty blade", 2, 2)

        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        ###TODO: FIND SOME WAY TO MAKE SURE THAT PRINT STATEMENT PRINTED
        
        #Attempting to unequip item that may be unequipped
        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2)

        player.equip(weapon)

        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        equipped = player.getInventory()
        self.assertFalse(equipped.containsItem(weapon), "Failed to unequip item that it should have.")
            
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
        from items.item_set import ItemSet
        import constants

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        
        #Test for correct initialization
        self.assertEqual(player._name, "Frodo", "Player name did not initialize correctly.")
        self.assertEqual(player._location, space, "Player location did not initialize correctly.")
        
        emptyList = []
        self.assertEqual(player._inventory.getItems(), emptyList, "Player inventory was not initialized.%s")
        self.assertEqual(player._equipped.getItems(), emptyList, "Player equipped was not initialized.")
        
        self.assertEqual(player._experience, constants.STARTING_EXPERIENCE, "Player experience was not initialized.")
        self.assertEqual(player._level, constants.STARTING_LEVEL, "Player level was not initialized.")
        
        self.assertEqual(player._maxHp, constants.HP_STAT, "Player max Hp was not initialized.")
        self.assertEqual(player._hp, constants.HP_STAT, "Player Hp was not initialized.")
        self.assertEqual(player._attack, constants.ATTACK_STAT, "Player attack was not initialized.")

        self.assertEqual(player._weaponAttack, 0, "Player attack bonus was not initialized.")
        self.assertEqual(player._armorDefense, 0, "Player defense bonus was not initialized.")
                         
    def testAttack(self):
        from player import Player
        from space import Space
        from monsters.monster import Monster

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        monster = Monster("Orc", "An orc.", 10, 1, 1)
        
        #Check monster health default state
        self.assertEqual(monster._hp, 10, "Monster Hp did not initialize correctly.")
        
        #Player attacks monster
        player.attack(monster)
        actualHp = monster._hp
        expectedHp = 10 - (player._attack + player._weaponAttack) 
        self.assertEqual(actualHp, expectedHp, "Monster attack failed to work correctly.")

    def testTakeDamage(self):
        from player import Player
        from space import Space
        from monsters.monster import Monster

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)
        monster = Monster("Orc", "An orc.", 10, 1, 1)
        monsterAttack = monster._attack
        
        #Test to see if Hp decreases after monster attack
        originalHp = player._hp
        monster.attack(player)
        newHp = player._hp
        self.assertTrue(newHp == originalHp - monsterAttack, "Player takeAttack method failed.")

    def testLevelUp(self):
        from player import Player
        from space import Space
<<<<<<< HEAD
        from math import floor
        import constants

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)

        #Increase player experience, run _updateLevel, and test if stats change to where they're intended
        originalExperience = player._experience
        experienceIncrease = 1000
        
        player._experience = originalExperience + experienceIncrease
        player._updateLevel()

        self.assertEqual(player._experience, originalExperience + experienceIncrease, "Player experience did not increase.")
        self.assertEqual(player._level, floor(player._experience/20) + 1, "Player did not level up.")
        self.assertEqual(player._maxHp, player._level * constants.HP_STAT, "Player Hp did not increase.")
        self.assertEqual(player._attack, player._level * constants.ATTACK_STAT, "Player damage did not increase.")
=======
        from items.item import Item
        from items.item_set import ItemSet
        from items.weapon import Weapon
        from items.armor import Armor
        from stats import Stats
        from monsters.monster import Monster
        import constants

        space = Space("shire", "Frodo's home")
        player = Player("Frodo", space)

        originalLevel = player.getLevel()
        originalHp = player.getHp()
        originalDamage = player.getAttack()
        originalExperience = player.getExperience()
        
        player.increaseExperience(1000)
        
        newLevel = player.getLevel()
        newHp = player.getHp()
        newDamage = player.getAttack()
        newExperience = player.getExperience()
        
        self.assertTrue(newLevel > originalLevel, "Player did not level up.")
        self.assertTrue(newHp > originalHp, "Player HP did not increase.")
        self.assertTrue(newDamage > originalDamage, "Player damage did not increase.")
        self.assertTrue(newExperience > originalExperience, "Player experience did not increase.")
>>>>>>> dmitriy-branch

    def testHeal(self):
        #Heal where healing amount is greater than total amount possible
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)

        maxHp = player._maxHp
        attackAmount = 2
        healAmount = 3
        
        player.takeAttack(attackAmount)
        player.heal(healAmount)

        self.assertEqual(player._hp, maxHp, "Healing testcase #1 failed.")

        #Heal where healing amount is less than total amount possible
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.")
        player = Player("Frodo", space)

        maxHp = player._maxHp
        attackAmount = 3
        healAmount = 2
        
        player.takeAttack(attackAmount)
        player.heal(healAmount)

        self.assertEqual(player._hp, maxHp - 1, "Healing testcase #2 failed.")
        
    def testEquipUnequip(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
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
        self.assertFalse(newItem in player.getEquipped(), "Equipped %s and should not have." %newItem)
        player.equip(newWeapon)
        self.assertTrue(newWeapon in player.getEquipped(), "Failed to equip %s" %newWeapon)
        player.equip(newArmor)
        self.assertTrue(newArmor in player.getEquipped(), "Failed to equip %s" %newArmor)
        
        #Attempt to unequip items
        player.unequip(newWeapon)
        self.assertFalse(newWeapon in player.getEquipped(), "Failed to unequip %s" %newWeapon)
        player.unequip(newArmor)
        self.assertFalse(newArmor in player.getEquipped(), "Failed to unequip %s" %newArmor)
    
if __name__ == '__main__':
    #Supress output from game with "buffer=true"
    unittest.main()
