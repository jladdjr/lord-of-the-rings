#!/usr/bin/python

import random

import constants
import factories.monster_factory

def battle(player):
    """
    Battle engine for Lord of the Rings

    @param player:     The player object.
    """
    #Create variables for monster_factory
    location = player.getLocation()
    monsterDifficulty = location.getBattleDifficulty()

    #TODO: Magic number
    number = 3 * monsterDifficulty
    #TODO: Add support for regions
    region = "Doesn't matter right now"
    difficulty = monsterDifficulty

    #Create variables for victory sequence
    #TODO: Magic number
    experience = 55 * number * monsterDifficulty
    money = 3 * number * monsterDifficulty

    #Spawn monsters
    monsters = factories.monster_factory.getMonsters(number, region, difficulty)

    #User prompt
    print "Zonkle-tronks! Wild monsters appeared!"
    print ""

    #Battle sequence
    while len(monsters) != 0:
        print "Monsters:"
        for monster in monsters:
            print "\t%s: %s" % (monster.getName(), monster.getDescription())
        print ""
        choice = raw_input("You may: 'attack', 'potion', 'run.' ")
        #Attack
        if choice == 'attack':
            playerAttackPhase(player, monsters)
        #Use potion - TODO
        elif choice == "potion":
            usePotionCmd.execute()
        #Attempt run
        elif choice == 'run':
            #TODO: Magic number
            if random.random() < .3:
                print "You ran away succesfully!"
                return
            else:
                print "Your path is blocked!"
        #Invalid selection
        else:
            print "Huh?"
        print ""
        
        #Monsters attack now.
        monsterAttackPhase(player, monsters)

    #Battle end sequence - loot received
    endSequence(player, experience, money)

def playerAttackPhase(player, monsters):
    """
    When the user gets to attack a single monster object.
    If monster health is reduced to zero, monster is removed
    from battle.

    @param player:      The player object.
    @param monsters:    The list of monster objects.
    """
    #Solicit attack target
    target = raw_input("Whom? ")
    print ""
    #Find monster object
    for monster in monsters:
        if monster.getName() == target:
            #Carry out attack
            player.attack(monster)
            print "%s did %s damage to %s!" % (player.getName(), player.getTotalAttack(), monster.getName())
            #If monster is still alive
            if monster.getHp() > 0:
                print "%s has %s hp remaining." % (monster.getName(), monster.getHp())
            #If monster has died
            else:
                print "%s was cleaved in two!" % monster.getName()
                #Remove monster from monsters list
                for monster in monsters:
                    if monster.getName() == target:
                        monsters.remove(monster)
                        #No need to keep iterating through monsters
                        break
            #No need to keep iterating through monsters
            break
    else:
        print "%s looks at you in confusion." % player.getname()

def monsterAttackPhase(player, monsters):
    """
    Monster attack phase - when monsters attack player.

    @param player:      The player object.
    @param monsters:    The offending list of monsters.
    """
    #Monsters attack
    for monster in monsters:
        monster.attack(player)
        print "%s attacked %s for %s damage!" % (monster.getName(), player.getName(), monster.getAttack())
        print "%s has %s hp remaining." % (player.getName(), player.getHp())
        #TODO: Check to see if player is still alive
    print ""

def endSequence(player, experience, money):
    """
    Battle cleanup - player experience and money increases, etc.

    @param player:      The player object.
    @param experience:  The experience player should increase by.
    @param money:       The money that player should receive.
    """
    player.increaseMoney(money)
    player.increaseExperience(experience)
    print "Enemies are vanguished!"
    print "%s gains %s money and %s experience!" % (player.getName(), money, experience)
    
