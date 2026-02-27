# Gysella Martin

# Dictionary that links rooms together
rooms = {
    "Restaurant Lobby": {
        "North": "Poultry Farm",
        "South": "Potato Warehouse",
        "East": "Dairy Shop",
        "West": "Butcher Shop"
    },
    "Poultry Farm": {
        "South": "Restaurant Lobby",
        "East": "Produce Market",
    },
    "Produce Market": {
        "West": "Poultry Farm"
    },
    "Butcher Shop": {
        "East": "Restaurant Lobby"
    },
    "Potato Warehouse": {
        "North": "Restaurant Lobby",
        "East": "Storage Room"
    },
    "Storage Room": {
        "West": "Potato Warehouse"
    },
    "Dairy Shop": {
        "West": "Restaurant Lobby",
        "North": "Kitchen"
    },
    "Kitchen": {},
    "Exit": {}
}

# Starting room
current_room = "Restaurant Lobby"

# Main game loop
while current_room != "Exit":

    # Show current room
    print("You are in the", current_room)

    # Get input from player
    command = input("Enter your move: ").strip()

    # Check if player wants to exit
    if command.lower() == "exit":
        current_room = "Exit"

    # Check if player entered a move command
    elif command.lower().startswith("go "):
        direction = command.split()[1].capitalize()

        #check if the direction is valid for current room
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")

    # Any other input is invalid
    else:
        print("Invalid command!")

# End of game
