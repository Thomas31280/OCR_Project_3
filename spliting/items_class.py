import random

class Items:
    """
    Management of all the logical part of Items.
    """

    def __init__(self, name):

        self.looted = False
        self.name = name.strip()

    def item_location(self, possible_positions):
        """
        Knowing the practicable areas of the matrix, we will assign
        to the items a random position among these areas. We will exclude
        the positions of MacGyver and the guard, and ensure that once
        a sector assigned to an item, it is no longer available!
        """

        random_loc = random.randint(1, len(possible_positions) - 1)
        self.location = possible_positions[random_loc]
        self.item_index = random_loc
        return self.location

    def item_looted(self, macgyver):
        """
        Here we manage the logical part of collecting items. When
        MacGyver passes on an item, he picks it up and the status "picked up"
        of the item changes to True. It also removes its position attribute.
        """

        if self.location == macgyver.position:
            self.looted = True
            macgyver.stuff.append(str(self.name))
            self.location = None
        return macgyver.stuff
