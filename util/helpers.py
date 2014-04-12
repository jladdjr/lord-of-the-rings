#!/usr/bin/python

def generateMenu(prompt, options, appendQuit = False):
    print prompt
    print ""

    if appendQuit:
        options.append("Quit")

    index = 1
    for option in options:
        print "%s)\t%s" % (str(index), option) 
        index += 1

    choice = raw_input("Choice: ")

    return choice
