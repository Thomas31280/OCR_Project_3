import logging as lg

from spliting import map_class
from spliting import macgyver_class
from spliting import items_class
from spliting import guard_class
from spliting import display_class
import constant_storage
import txt_interpretor

lg.basicConfig(level=lg.INFO)

def main():
    """
    We define our main function, encapsulated in a conditional structure.
    We will successively call each method of each class, and finish
    by displaying the graphical interface.
    """

    path_builder = txt_interpretor.path_builder()
    my_map = map_class.Map(path_builder)
    practicable_zones = map_class.Map.practicable_zones\
                        (my_map, my_map.path_builder)
    global_map = map_class.Map.map_generation\
                 (my_map, my_map.height, my_map.width)
    guard = guard_class.Guard()
    macgyver = macgyver_class.MacGyver()
    items = txt_interpretor.items_creator(practicable_zones, guard)
    lg.info("Le jeu a été initialisé avec succès !")
    display_class.Display.display_routine(global_map, practicable_zones,
                            guard, macgyver, items)


if __name__ == "__main__":
    main()
