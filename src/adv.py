from room import Room
from player import Player

# Declare all the rooms

room = {
    'spaceship':   Room("Space Ship", "You step onto the spaceship and find a space gun."),
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].secret = room['spaceship']
room['spaceship'].n_to = room['outside']
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(room['outside'].n_to.name)
# print(room['outside'].n_to.description)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input("Please enter your name: "), room['outside'])

if player.name == "Hexley":
    print(f"It's great to see you again, Doctor.")
else:
    print(f"Hello, {player.name}")


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

# LOOP

while True:
    print(player.current_room.name)
    print("")
    print(player.current_room.description)

    

    # READ
    cmd = input("~~> ")
# EVAL
    if cmd == "q":
        print("Goodbye!")
        exit(0)
    elif cmd == "n":
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        else:
            print("You cannot move in that direction.")
    elif cmd == "e":
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        else:
            print("You cannot move in that direction.")
    elif cmd == "s":
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        else:
            print("You cannot move in that direction.")
    elif cmd == "w":
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
        else:
            print("You cannot move in that direction.")
    elif cmd == "secret":
        if player.current_room.secret is not None:
            player.current_room = player.current_room.secret
        else: 
            print("Nice try")
    else:
        print("I did not understand that command")
# PRINT
