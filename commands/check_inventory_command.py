from command import Command
from items.weapon import Weapon
from items.armor import Armor

class CheckInventoryCommand(Command):
    """
    Prints player inventory and details item stats.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check inventory command.

        @param name: Command name.
        @param explanation: Explanation of command.
        @param player: The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Finish initializing help-specific settings
        self._player = player

    def execute(self):
        """
        Displays character inventory.
        """
        playerName = self._player.getName()
        inventory = self._player.getInventory()
        inventoryList = inventory.getItems()

        totalWeight = 0
        
        for item in inventoryList:
            itemName = item.getName()
            itemDescription = item.getDescription()
            itemWeight = item.getWeight()

            if isinstance(item, Armor):
                itemDefense = item.getDefense()
            elif isinstance(item, Weapon):
                itemAttack = item.getAttack()

            print "%s's inventory:\n" %playerName
            print "%s:%s\t%s weights %s." (itemName, itemDescription, itemName, itemWeight)

            if isinstance(item, Armor):
                print "%s has a defense of %s." %(itemName, itemDefense)
            elif isinstance(item, Weapon):
                print "%s has an attack value of %s."(itemName, itemAttack)
            print ""

            totalWeight += itemWeight

        print "Total weight of inventory: %s" %totalWeight
