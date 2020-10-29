import constant_storage
import logging as lg

lg.basicConfig(level=lg.INFO)

class MacGyver:
    """
    Management of all MacGyver's methods and attributes.
    """

    def __init__(self):

        self.stuff = []
        self.position = constant_storage.MACGYVER_POSITION_INIT
        self.name = "MacGyver"

    def move(self, player_input, practicable_zones):
        """
        Logic of MacGyver's displacement in the matrix. We
        here will vary its position attribute by checking
        that the user's command is consistent.
        """

        buffer_position = None

        if player_input == "front":
            buffer_position = (self.position[0], self.position[1]-1)

        elif player_input == "back":
            buffer_position = (self.position[0], self.position[1]+1)

        elif player_input == "right":
            buffer_position = (self.position[0]+1, self.position[1])

        elif player_input == "left":
            buffer_position = (self.position[0]-1, self.position[1])

        if buffer_position in practicable_zones:
            self.position = buffer_position
            return self.position
        else:
            return lg.info("Déplacement impossible. Vous devez rester \
dans les limites du labyrinthe")

    def craft(self, items):
        """
        Definition of the method allowing to recover the syringe.
        We check here that all the conditions are met for its
        manufacturing.
        """

        if items[0].looted and items[1].looted and items[2].looted:
            print("Seringue fabriquée ! Vous pouvez endormir le garde.")
            self.stuff = ["seringue"]
