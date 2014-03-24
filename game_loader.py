#!/usr/bin/python

from space import Space
from player import Player
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from commands.command_words import CommandWords
from commands.help_command import HelpCommand 
from commands.quit_command import QuitCommand
from commands.describe_command import DescribeCommand
from commands.drop_command import DropCommand
from commands.pick_up_command import PickUpCommand
from commands.equip_command import EquipCommand
from commands.unequip_command import UnequipCommand
from commands.check_inventory_command import CheckInventoryCommand
from commands.check_equipment_command import CheckEquipmentCommand
from commands.check_stats_command import CheckStatsCommand
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand

def getWorld():
    shire = Space("Shire", "Home of the Hobbitses.")
    mordor = Space("Mordor", "Oppressive locale. Bad for health!")
    shire.createExit("north", mordor, outgoingOnly=False)
    
    return shire
    
def getStartingInventory():
    weapon = Weapon("Rock", "Really heavy", 2, 1000)
    armor = Armor("Leather tunic", "Travel cloak", 3, 1)
    potion = Potion("Vodka", "Good for health", 1, 1)

    startingInventory = [weapon, armor, potion]
    
    return startingInventory

def getPlayer(world, startingInventory):
    player = Player("Russian", world)

    for item in startingInventory:
        player.addInventory(item)
    for item in startingInventory:
        player.equip(item)
        
    return player
    
def getCommandList(player):

    #Create commandWords object
    commandWords = CommandWords()
    
    #Commands
    helpCmd = HelpCommand("help", 
        "Provides help information for game.", commandWords)
    commandWords.addCommand("help", helpCmd)

    quitCmd = QuitCommand("quit", "Exits the game.")
    commandWords.addCommand("quit", quitCmd)
   
    dropCmd = DropCommand("drop", "Drops an item from inventory into local environment.", player)
    commandWords.addCommand("drop", dropCmd)

    pickupCmd = PickUpCommand("pick up", "Picks up an item from a location and adds to inventory.", player)
    commandWords.addCommand("pick up", pickupCmd)

    equipCmd = EquipCommand("equip", "Equips item in inventory.", player)
    commandWords.addCommand("equip", equipCmd)

    unequipCmd = UnequipCommand("unequip", "Unequips item that is currently equipped.", player)
    commandWords.addCommand("unequip", unequipCmd)

    checkInventoryCmd = CheckInventoryCommand("inventory", "Displays contents of inventory.", player)
    commandWords.addCommand("inventory", checkInventoryCmd)

    checkEquipmentCmd = CheckEquipmentCommand("equipment", "Displays current equipment and equipment stats.", player)
    commandWords.addCommand("equipment", checkEquipmentCmd)

    checkStatsCmd = CheckStatsCommand("stats", "Displays current character stats.", player)
    commandWords.addCommand("stats", checkStatsCmd)

    northCmd = NorthCommand("north", 
                "Moves the player to the space north of current space")
    commandWords.addCommand("north", northCmd)
    
    southCmd = SouthCommand("south", 
                "Moves the player to the space south of current space")
    commandWords.addCommand("south", southCmd)
    
    eastCmd = EastCommand("east", 
                "Moves the player to the space east of current space")
    commandWords.addCommand("east", eastCmd)
    
    westCmd = WestCommand("west", 
                "Moves the player to the space west of current space")
    commandWords.addCommand("west", westCmd)
    
    descCmd = DescribeCommand("describe", "Gives description of current space", player)
    commandWords.addCommand("describe", descCmd)

    return commandWords
