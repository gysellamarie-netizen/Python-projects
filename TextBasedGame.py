# Gysella Martin

# Instructions
def show_instructions():
    # Print game title and instructions
    print("Welcome to The Restaurant Ingredient Hunt Game")
    print("Collect all 6 ingredients before entering the Kitchen to win the game, or the grand opening will fail")
    print("Move commands: go North, go South, go East, go West")
    print("Add to inventory: get 'item name'")

# Show players current room, inventory, and available item
def show_current_status(current_room, inventory, rooms):
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])

# Dictionary of rooms, directions, and items
def main():
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
            "item": "Chicken"
        },
        "Produce Market": {
            "West": "Poultry Farm",
            "item": "Lettuce"
        },
        "Butcher Shop": {
            "East": "Restaurant Lobby",
            "item": "Beef"
        },
        "Potato Warehouse": {
            "North": "Restaurant Lobby",
            "East": "Storage Room",
            "item": "Potatoes"
        },
        "Storage Room": {
            "West": "Potato Warehouse",
            "item": "Cooking oil"
        },
        "Dairy Shop": {
            "West": "Restaurant Lobby",
            "North": "Kitchen",
            "item": "Cheese"
        },
        "Kitchen": {}
    }

    # Items needed to win
    required_items = ["Beef", "Chicken", "Potatoes", "Lettuce", "Cheese", "Cooking oil"]

    # Starting values
    current_room = "Restaurant Lobby"
    inventory = []

    # Show instructions at the start of game
    show_instructions()

    # Game loop
    while True:
        show_current_status(current_room, inventory, rooms)

        # Get player input
        move = input("Enter your move: ").strip()
        if move.lower().startswith("go "):
            direction = move.split()[1].capitalize()

            # Validate move
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Get item from rooms
        elif move.lower().startswith("get "):
            item_name = move[4:].strip()

            # Validate item
            if "item" in rooms[current_room] and rooms[current_room]["item"].lower() == item_name.lower():
                inventory.append(rooms[current_room]["item"])
                print(rooms[current_room]["item"], "retrieved!")
                # Remove the item once collected
                del rooms[current_room]["item"]
            else:
                print("Can't get", item_name + "!")

        # Invalid Input
        else:
            print("Invalid Input!")

        # Lose condition: player enters the kitchen without all items
        if current_room == "Kitchen" and len(inventory) < len(required_items):
            print("You are in the Kitchen")
            print("Inventory:", inventory)
            print("You are missing ingredients!")
            print("Grand opening failed...Game Over!")
            break

        # Win condition: player enters the kitchen with all items collected
        if current_room == "Kitchen" and len(inventory) == len(required_items):
            print("You are in the Kitchen")
            print("Inventory:", inventory)
            print("Congratulations! You have collected all the ingredients!")
            print("Grand opening successful! You Win!")
            break

    # End game
    print("Thanks for playing!")

# Run program
main()

