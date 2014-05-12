#!/usr/bin/python

def generateMenu(prompt, options, appendQuit = False):
    """
    Generates menus and solicit and returns user choice.

    @param prompt:       User prompt. For example: "You are in the store."
    @param options:      List of options, stored as strings.
    @param appendQuit:   Whether there should be the option to quit.
     """
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
    
    
