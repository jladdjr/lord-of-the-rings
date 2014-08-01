#!/usr/bin/python

import math
import random

import factories.monster_factory
from commands.use_potion_command import UsePotionCommand
from util.helpers import triangular
from items.unique_items import lowLevelFindableUniques
from items.unique_items import highLevelFindableUniques
from items.unique_items import eliteLevelFindableUniques
import constants

def battle(player, context, monsters = None):
    """
    The battle engine of Lord of the Rings.

    @param player:     The player object.
    @param context:    Context constant for battle engine. Battle engine 
                       behaves differently
                       in different contexts. Battles are either random battles 
                       or story-based battles (e.g., boss battles).
    @param monsters:   An optional parameter used for story-based battles. 
                       Consists of the list of monsters to fight.
                       
    @return:           True if battle was won; False otherwise.

    Differences between random battles and story-based battles:
    -Random battles: monster factory called by battle engine and monsters are 
    supplied by monster factory. Player can run successfully in random battles.
    -Story-based battles: monsters must be supplied through the "monsters" 
    parameter. Player cannot run from battle.
    """
    #Battle setup
    output = _battleSetup(player, context)
    if context == constants.BattleEngineContext.RANDOM:
        bonusDifficulty = output[0]
        monsters = output[1]
    else:
        bonusDifficulty = output
    
    #Main battle sequence
    while len(monsters) != 0:
        #Display enemy monsters
        print "Monsters:"
        for monster in monsters:
            print "\t%s: %s" % (monster.getName(), monster.getDescription())
        print ""
        
        #Solicit user input
        choice = None
        acceptable = ["attack", "use potion", "run", "explode"]
        while choice not in acceptable:
            choice = raw_input("You may: 'attack', 'use potion', 'run.' ")
        
        #Player attack option
        if choice == 'attack':
            earnings = _playerAttackPhase(player, monsters, bonusDifficulty)
            
        #Use potion option
        elif choice == "use potion":
            _usePotion(player)
            
        #Run option
        elif choice == "run":
            if context == constants.BattleEngineContext.RANDOM:
                if random.random() < constants.RUN_PROBABILITY_SUCCESS:
                    print "You ran away succesfully!"
                    print ""
                    return True
                else:
                    print "Your path is blocked!"
            else:
                print "Your path is blocked!"
                
        #Code - eliminates all enemies
        elif choice == "explode":
            monsters = []
            earnings = [0, 0]

        #Break between player and monster phases
        raw_input("Press 'enter' to continue. ")
        print ""

        #Monsters attack phase
        continueBattle = _monsterAttackPhase(player, monsters)
        
        #Escape sequence given battle loss
        if not continueBattle:
            print ""
            print "Gandalf bails you out."
            player.heal(1)
            
            return False
        
    #Battle end sequence - loot received
    _endSequence(player, earnings)
    
    return True

def _battleSetup(player, context):
    """
    Generates variables for battle engine and prints battle
    splash screen.
    """
    #For random battles
    if context == constants.BattleEngineContext.RANDOM:
        #Create variables
        location = player.getLocation()
        region = location.getRegion()
        bonusDifficulty = location.getBattleBonusDifficulty()

        #Spawn monsters
        monsterCount = _monsterNumGen(player)
        monsters = factories.monster_factory.getMonsters(monsterCount, region, 
        bonusDifficulty)

        #Declare battle
        print "Zonkle-tronks! Wild monsters appeared!"
        print ""

        return bonusDifficulty, monsters
    
    #For story-based battles
    elif context == constants.BattleEngineContext.STORY:
        #Create variables
        location = player.getLocation()
        region = location.getRegion()
        bonusDifficulty = location.getBattleBonusDifficulty()
    
        #Display splash screen
        print """
()==[:::::::::::::> ()==[:::::::::::::> ()==[:::::::::::::>
"""
        return bonusDifficulty
    
    else:
        errorMsg = "_battleSetup given invalid context parameter."
        raise AssertionError(errorMsg)

def _monsterNumGen(player):
    """
    Helper function used to determine the number of monsters to spawn.
    
    Default spawn comes from a parameter supplied by space. A normal 
    distribution is applied to introduce variation.
    
    @param player:     Player object.

    @return:           Number of monsters to spawn.
    """
    location = player.getLocation()
    region = location.getRegion()

    #Calculate region spawn
    if region == constants.RegionType.ERIADOR:
        monsterCount = constants.RegionBaseSpawn.ERIADOR
    elif region == constants.RegionType.BARROW_DOWNS:
        monsterCount = constants.RegionBaseSpawn.BARROW_DOWNS
    elif region == constants.RegionType.HIGH_PASS:
        monsterCount = constants.RegionBaseSpawn.HIGH_PASS
    elif region == constants.RegionType.ENEDWAITH:
        monsterCount = constants.RegionBaseSpawn.ENEDWAITH
    elif region == constants.RegionType.MORIA:
        monsterCount = constants.RegionBaseSpawn.MORIA
    elif region == constants.RegionType.RHOVANION:
        monsterCount = constants.RegionBaseSpawn.RHOVANION
    elif region == constants.RegionType.ROHAN:
        monsterCount = constants.RegionBaseSpawn.ROHAN
    elif region == constants.RegionType.GONDOR:
        monsterCount = constants.RegionBaseSpawn.GONDOR
    elif region == constants.RegionType.MORDOR:
        monsterCount = constants.RegionBaseSpawn.MORDOR
    else:
        errorMsg = "Invalid region - region base monster determination."
        raise AssertionError(errorMsg)
        
    #Apply normal distribution to introduce variation
    standardDeviation = monsterCount/constants.STANDARD_DEVIATION
    
    monsterCount = random.normalvariate(monsterCount, standardDeviation)
    monsterCount = math.floor(monsterCount)
    monsterCount = int(monsterCount)
    
    return monsterCount

def _playerAttackPhase(player, monsters, bonusDifficulty):
    """
    When the user gets to attack a single monster object.
    If monster health is reduced to zero, monster is removed
    from battle.

    Additionally, experience and money is calculated for winnings.

    @param player:        The player object.
    @param monsters:      The list of monster objects.

    @return:              2-element tuple carrying battle earnings.
                          First element is money earned, second
                          element is experience received.
    """
    #Starting battle earnings
    money      = 0
    experience = 0

    #Solicit attack target
    target = raw_input("Whom? ")
    print ""
    #Find monster object
    for monster in monsters:
        if monster.getName() == target:
            #Carry out attack
            player.attack(monster)
            print ("%s did %s damage to %s!" % (player.getName(), 
            player.getTotalAttack(), monster.getName()))
            #If monster is still alive
            if monster.getHp() > 0:
                print ("%s has %s hp remaining." % (monster.getName(), 
                monster.getHp()))
            #If monster has died
            else:
                print "%s" % monster.getDeathString()
                #Generate earnings from winning battle
                money += monster.getExperience() * (1 + bonusDifficulty)
                experience += monster.getExperience() * (1 + bonusDifficulty)
                #Remove monster from monsters list
                for monster in monsters:
                    if monster.getName() == target:
                        monsters.remove(monster)
                        #No need to keep iterating through monsters
                        break
            #No need to keep iterating through monsters
            break
    else:
        print "%s looks at you in confusion." % player.getName()
        
    return money, experience

def _usePotion(player):
    """
    Creates an additional UsePotionCommand object
    for battle purposes only and then executes the 
    action sequence of this usePotion.

    @param player:   The player object.
    """
    usePotionCmd = UsePotionCommand(" ", " ", player)
    usePotionCmd.execute()

def _monsterAttackPhase(player, monsters):
    """
    Monster attack phase - when monsters attack player.

    @param player:      The player object.
    @param monsters:    The offending list of monsters.

    @return:            True if battle is to continue. False
                        otherwise.
    """
    #Monsters attack
    for monster in monsters:
        monster.attack(player)
        print ("%s %s for %s damage!" % (monster.getName(), 
        monster.getAttackString(), monster.getAttack()))
        print "%s has %s HP remaining." % (player.getName(), player.getHp())
        
        #Battle ends
        if player.getHp() == 0:
            print ""
            return False
    print ""
    
    #Battle continuation
    return True

def _itemFind(player, experience):
    """
    Calculates whether player finds an item and which item he finds.
    
    @param player:         The player object.
    @param experience:     The experience gained from the battle.
    """
    location = player.getLocation()

    #Item find for low-level uniques
    lowLevel = triangular(constants.ItemFind.lowLevel)
    if experience > lowLevel:
        item = random.choice(lowLevelFindableUniques)
        print "You found %s!" % item.getName()
        if player.addToInventory(item):
            lowLevelFindableUniques.remove(item)
        else:
            location.addItem(item)
    
    #Item find for high-level uniques
    highLevel = triangular(constants.ItemFind.highLevel)
    if experience > highLevel:
        item = random.choice(highLevelFindableUniques)
        print "You found %s!" % item.getName()
        if player.addToInventory(item):
            highLevelFindableUniques.remove(item)
        else:
            location.addItem(item)
            
    #Item find for elite-level uniques
    eliteLevel = triangular(constants.ItemFind.eliteLevel)
    if experience > eliteLevel:
        item = random.choice(eliteLevelFindableUniques)
        print "You found %s!" % item.getName()
        if player.addToInventory(item):
            eliteLevelFindableUniques.remove(item)
        else: 
            location.addItem(item)
    print ""
    
def _endSequence(player, earnings):
    """
    Battle cleanup:
    -Victory sequence displayed.
    -Player experience and money increase.

    @param player:      The player object.
    @param earnings:    2-element tuple: first element is 
                        money and second is experience.
    """
    money = earnings[0]
    experience = earnings[1]
    
    #Calculate splash screen variables
    victoryDeclaration = "Enemies are vanguished!"
    gainsDeclaration = ("%s gains %s %s and %s experience!" 
    % (player.getName(), money, constants.CURRENCY, experience))
    
    lengthBar = len(gainsDeclaration)
    victoryDeclaration = victoryDeclaration.center(lengthBar)
    bar = "$" * lengthBar
    
    #Victory sequence
    print bar
    print victoryDeclaration
    print gainsDeclaration
    print ""
    _itemFind(player, experience)
    player.increaseMoney(money)
    player.increaseExperience(experience)
    print bar
    print ""