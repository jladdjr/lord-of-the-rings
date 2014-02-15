#!/usr/bin/python

import unittest
from mock import (MagicMock, patch)

class GameTest(unittest.TestCase):
    """
    Tests Game class.
    """

    def test_next_turn(self):
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

if __name__ == "__main__":
    #Supress output from game with "buffer=true"
    unittest.main(buffer=True)
