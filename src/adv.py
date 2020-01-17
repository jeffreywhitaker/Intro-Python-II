from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("outside the entrace of a spooky cave!",
                     "North of you, the cave mouth beckons ominously."),

    'foyer':    Room("standing in a dimly lit foyer.", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.
There seems to be a rock loose on the north wall..."""),

    'hidden': Room("Hidden Room", """You found a hidden room behind the wall! It's
    small, dark, and only has a single exit, from whence you came.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['hidden']
room['hidden'].s_to = room['treasure']

# make items

room['foyer'].items = [Item("Flashlight", "This is a flashlight"), Item(
    "Laptop", "This could be pretty handy")]
room['hidden'].items = [
    Item("Shield_Key", "This key has an emblem of a skeleton on it.")]

# helper functions


def movement_helper(keypress):
    if keypress == 'w':
        if hasattr(p.location, 'n_to'):
            p.location = p.location.n_to
        else:
            print("A room does not exist in that direction")
    if keypress == 'a':
        if hasattr(p.location, 'w_to'):
            p.location = p.location.w_to
        else:
            print("A room does not exist in that direction")
    if keypress == 's':
        if hasattr(p.location, 's_to'):
            p.location = p.location.s_to
        else:
            print("A room does not exist in that direction")
    if keypress == 'd':
        if hasattr(p.location, 'e_to'):
            p.location = p.location.e_to
        else:
            print("A room does not exist in that direction")


def get_item_helper(objct):
    for item in p.location.items:
        if objct == item.name.lower():
            p.location.items.remove(item)
            p.items.append(item)


def drop_item_helper(objct):
    for item in p.items:
        p.location.items.append(item)
        p.items.remove(item)


# needs something in list to not break
userInput = ['placeholder']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("""

So you seek to play a game, do you?

What is your name, adventurer?

""")
userName = input(">>> ")
p = Player(userName, room['outside'])
print("")
print("Welcome to Jeff's Adventure Game, " + p.name + "!")

# always loops until exit()
while True:

    # Print player location/status
    print("")
    print("Alright, " + userName +
          ", you are currently " + p.location.name)
    print(p.location.description)
    print("")
    if len(p.location.items) > 0:
        print(
            f"You can see items in this room! You see:")
        for item in p.location.items:
            print("- " + item.name)
        print("")
    print("What do you do? ")

    # collect input
    userInput = input(
        ">>> ").lower().split(" ")

    # act on input
    if userInput[0] == 'q':
        exit(1)

    if len(userInput) == 1:
        movement_helper(userInput[0])

    if len(userInput) == 2:
        verb = userInput[0]
        objct = userInput[1]

        # call a helper get/drop function and pass in objct
        if verb == "take":
            get_item_helper(objct)

        if verb == "drop":
            drop_item_helper(objct)

        # if player has more than 0 items, print list to screen
        if len(p.items) > 0:
            print("""
            You now have the following items:""")
            for item in p.items:
                print("- " + item.name)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
