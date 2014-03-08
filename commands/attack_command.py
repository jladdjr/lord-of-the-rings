from command import Command

class AttackCommand(Command):
    """
    Allows a player to pick up an item from a location.
    """

    def __init__(self, name, explanation, player, target):
        """
        Initializes new pick up command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object (e.g. "Frodo").
        @param target:       The target object (e.g. "Monster").
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Finish initializing attack-specific settings
        self._player = player
        self._attack = player.getAttack()
        self._target = target

    def execute(self):
        """
        Allows player to attack target.
        """
        self._player.attack(self._target)
