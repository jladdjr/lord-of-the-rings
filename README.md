# Lord of the Rings
By Chris Wang, Dmitriy Chukhin, and Jim Ladd
October 3, 2014

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Introduction
Lord of the Rings is an object-oriented adventure game built on Python. It was 
made purely for educational and entertainment purposes.

# How to Play
To start a game, simply type: 
$ ./main.py

"help" displays the game's total command list and should be referenced.

# How to Test
To test the game, type:
$ ./test.py

You should see output similar to the following:

Ran 96 tests in 0.005s
 
OK

(The number of tests may vary)
 
 To run the tests (test.py), you must have the mock library installed:
 $ sudo pip install mock
 
# Status
Game is fun but suffers seriously from poor user interface. Player reaches max
level mid-way through the game.

# Future Work
Future editions of this game should:
* Implement a better user interface that is more forgiving. Currently, users
get frustated at the UI.
* Develop the ability to access certain "in world" commands in cities. For 
instance, user should be able to equip item in cities.
