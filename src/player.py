# Write a class to hold player information, e.g. what room they are in
# currently.
#* Put the Player class in `player.py`.
  #* Players should have a `name` and `current_room` attributes
from item import Potion

class Player: 
    def __init__(self, name, current_room):
      self.name = name
      self.current_room = current_room
      self.items = []
      self.hp = 100
    def travel(self, direction):
      if getattr(self.current_room, f"{direction}_to"):
        self.current_room = getattr(self.current_room, f"{direction}_to")
        print(self.current_room)
        print(f"\nHealth: {self.hp}\n")
      else:
        print("You cannot move in that direction.")
    def print_inventory(self):
      print("Inventory: ")
      for item in self.items:
        print(f"{item.name}: {item.description}")
    def drink(self, drink_item):
      if type(drink_item) != Potion:
        print(f"You cannot drink {drink_item.name}")
      else:
        self.hp += drink_item.health
        print(f"You drank the {drink_item.name}, your health is now {self.hp}")
        self.items.remove(drink_item)