#!/usr/bin/python

from space import Space
from cities.city import City
from cities.inn import Inn
from cities.square import Square
from cities.shop import Shop
from player import Player
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from commands.command_words import CommandWords
from commands.help_command import HelpCommand 
from commands.quit_command import QuitCommand
from commands.describe_command import DescribeCommand
from commands.drop_command import DropCommand
from commands.enter_command import EnterCommand
from commands.pick_up_command import PickUpCommand
from commands.equip_command import EquipCommand
from commands.unequip_command import UnequipCommand
from commands.check_inventory_command import CheckInventoryCommand
from commands.check_equipment_command import CheckEquipmentCommand
from commands.check_money_command import CheckMoneyCommand
from commands.check_stats_command import CheckStatsCommand
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand
import constants

def getWorld():
    sallyInn = Inn("Sally's Inn", "A place for strangers", "Hi welcome to Sally's Inn", 2)
    sallyShop = Shop("Sally's Shop", "Buy things", "We have strange wares", 4, 3)
    chocoSquare = Square("Choco Square", "Lots of Hobbits", "Welcome to Choco Square", {"Samwise Gamgee": "Hi I'm Sam", "Jim Ladd Jr.": "Hi I'm Jim, the dear Ladd, friend of Master Wang"})
    nenuial = Space("Nenuial", "")
    northDowns = Space("North Downs", "")
    ettenmoors = Space("Ettenmoors", "")
    mistyMountainsOne = Space("Misty Mountains - One", "")
    mirkwood = Space("Mirkwood", "")
    erebor = Space("Erebor", "")
    
    hobbiton = City("Hobbiton", "Village in the Shire", "Welcome to Hobbinton", [sallyInn, sallyShop, chocoSquare])
    shire = Space("Shire", "Home of the Hobbitses", city = hobbiton)
    oldForest = Space("Old Forest", "")
    weatherHills = Space("Weather Hills", "")
    trollshows = Space("Trollshows", "")
    minstyMountainsTwo = Space("Misty Mountains - Two", "")
    highPass = Space("High Pass", "")
    
    sarnFord = Space("Sarn Ford", "")
    barrowDowns = Space("Barrow Downs", "")
    southDowns = Space("South Downs", "")
    bruinen = Space("Bruinen", "")
    mistyMountainsThree = Space("Misty Mountains - Three", "")
    
    cardolan = Space("Cardolan", "")
    mitheithel = Space("Mitheithel", "")
    mistyMountainsFour = Space("Misty Mountains - Four", "")
    
    tharbad = Space("Tharbad", "")
    swanfleet = Space("Swanfleet", "")
    moria = Space("Moria", "")
    mistyMountainsFive = Space("Misty Mountains - Five", "")
    
    enedwaith = Space("Enedwaith", "")
    mistyMountainsSix = Space("Misty Mountains - Six", "")
    lorein = Space("Lorein", "")
    dolGuldor = Space("Dol Guldor", "")

    druwaithIaur = Space("Druwaith Iaur", "")
    dunland = Space("Dunland", "")
    fangorn = Space("Fangorn", "")
    fieldOfCelebrant = Space("Field of Celebrant", "")
    theBrownLands = Space("The Brown lands", "")

    isenguard = Space("Isenguard", "")
    theWold = Space("The Wold", "")

    fordsOfIsen = Space("Fords of Isen", "")
    westFold = Space("West Fold", "")
    westEmmet = Space("West Emmet", "")
    eastEmmet = Space("East Emmet", "")
    emynMuil = Space("Emyn Muil", "")

    eredNimrais = Space("Ered Nimrais", "")
    eastFold = Space("East Fold", "")
    nimdalf = Space("Nimdalf", "")
    deadMarshes = Space("Dead Marshes", "")
    udun = Space("Udun", "")
    eredLithui = Space("Ered Lithui", "")

    cairAndros = Space("Cair Andros", "")
    morgai = Space("Morgai", "")
    isenmouthe = Space("Isenmouthe", "")
    baradDur = Space("Barad Dur", "")
    orodruin = Space("Orodruin", "")
    easternMordor = Space("Eastern Mordor", "")

    pinnathGelin = Space("Pinnath Gelin", "")
    lamedon = Space("Lamedon", "")
    minasTirith = Space("Minas Tirith", "")
    osgiliath = Space("Osgiliath", "")
    minasMorgul = Space("Minas Morgul", "")
    plateauOfGorgoth = Space("Plateau of Gorgoth", "")
    andrast = Space("Andrast", "")
    anfalas = Space("Anfalas", "")
    lebennin = Space("Lebennin", "")
    dorEnernil = Space("Dor Enernil", "")
    belfas = Space("Belfas", "")
    lossamarch = Space("Lossamarch", "")
    sIthilien = Space("S. Ithilien", "")
    southGondor = Space("South Gondor", "")
    mountainsOfShadow = Space("Mountains of Shadow", "")
    nurn = Space("Nurn", "")
    seaOfNurn = Space("Sea of Nurn", "")
    
    
    

    """
    oldForest = Space("Old Forest", "Home of Tom Bombadil")
    bree = Space("Bree")
    rivendell = City("Rivendell", "The last homely house east of the sea")
    weatherHills = Space("Weather Hills")
    rhudaur = Space("Rhudaur")
    eregion = Space("Eregion")
    dunland = Space("Dunland")
    isengard = City("Isengard", "Fortress of Saruman")
    fangorm = Space("Fangorm", "Mystic forest containing the Entmoot")
    moria = Space("Moria", "Called \'Khazad-Dum\' by the dwarves"
    helmsDeep = Space("Helm's Deep", "Fortress of Rohan")
    lorein = Space("Lorein", "Refuge of the Elves")
    enedwaith = Space("Enedwaith")
    anfalas = Space("Anfalas")
    osgiliath = Space("Osgiliath", "Past capital of Gondor, now in ruins")
    minasTirith = Space("Minas Tirith", "City of the kings")
    ithilien = Space("Ithilien")
    orodruin = Space("Orodruin", "Mount Doom")
    plateauOfGorgoroth = Space("Plateau of Gorgoroth", "Heart of Mordor")
    baradDur = Space("Barad Dur", "Fortress of Sauron")
    nurn = Space("Nurn")
    
    mordor = Space("Mordor", "Oppressive locale. Bad for health!")
    shire.createExit(constants.Direction.SOUTH, mordor)
    """
    return shire
    
def getStartingInventory():
    """
    Generate's player's starting inventory.

    @return:   A list of the items.
    """
    weapon = Weapon("Rock", "Really heavy", 2, 1000, 1)
    armor = Armor("Leather Tunic", "Travel cloak", 3, 1, 1)
    potion = Potion("Vodka", "Good for health", 1, 1, 1)

    startingInventory = [weapon, armor, potion]
    
    return startingInventory

def getPlayer(world, startingInventory):
    """
    Create player and give player starting inventory and equipment.

    @return:     A fully-loaded player
    """
    player = Player("Russian", world)

    for item in startingInventory:
        player.addInventory(item)
    for item in startingInventory:
        player.equip(item)
        
    return player
    
def getCommandList(player):
    """
    Generates the list of commands used in the game.

    @return:   The commandWords object, which stores the game's commands.
    """
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

    enterCmd = EnterCommand("enter", "Allows player to enter a building.", player)
    commandWords.addCommand("enter", enterCmd)

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

    checkMoneyCmd = CheckMoneyCommand("money", "Displays player money", player)
    commandWords.addCommand("money", checkMoneyCmd)

    checkStatsCmd = CheckStatsCommand("stats", "Displays current character stats.", player)
    commandWords.addCommand("stats", checkStatsCmd)

    northCmd = NorthCommand("north", 
                "Moves the player to the space north of current space", player)
    commandWords.addCommand("north", northCmd)
    
    southCmd = SouthCommand("south", 
                "Moves the player to the space south of current space", player)
    commandWords.addCommand("south", southCmd)
    
    eastCmd = EastCommand("east", 
                "Moves the player to the space east of current space", player)
    commandWords.addCommand("east", eastCmd)
    
    westCmd = WestCommand("west", 
                "Moves the player to the space west of current space", player)
    commandWords.addCommand("west", westCmd)
    
    descCmd = DescribeCommand("describe", "Gives description of current space", player)
    commandWords.addCommand("describe", descCmd)

    return commandWords
