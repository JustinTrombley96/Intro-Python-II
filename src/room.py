# Implement a class to hold room information. This should have name and
# description attributes.

# * Put the Room class in `room.py` based on what you see in `adv.py`.

#   * The room should have `name` and `description` attributes.

#   * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#     which point to the room in that respective direction.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.secret_to = None
    def __str__(self):
        return_string = ("--------------")
        return_string += "\n"
        return_string += (self.name)
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n"
        return_string += f"{self.get_exits_string()}"
        return return_string
    def get_exits_string(self):
            exits = []
            if self.n_to:
                exits.append("n")
            if self.s_to:
                exits.append("s")
            if self.e_to:
                exits.append("e")
            if self.w_to:
                exits.append("w")
            return exits
