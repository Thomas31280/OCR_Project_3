import random
import pygame                                                                                                # Importation librairie pygame
from pygame.locals import *

import constant_storage as cs
import txt_interpretor as ti

"""
The Map class manages all the logical part of the Map and contains
all the methods needed for its generation.
"""

class Map:

    def __init__(self, path_builder):
        
        self.height = cs.HEIGHT_UNITY
        self.width = cs.WIDTH_UNITY
        self.path_builder = path_builder

    """
    From the path_builder.txt, we generate the list of all tuples
    of two elements, which correspond to the cartesian coordinates of the
    sectors of the matrix which will be considered as practicables.
    """

    def practicable_zones(self, path_builder):

        practicable_zones = []
        
        for list_element in path_builder:
            free_zone = ((list_element[0], list_element[1]))
            practicable_zones.append(free_zone)
            x_translation = list_element[2]
            y_translation = list_element[3]
            operator = list_element[4]
            
            if x_translation != 0:
                for k in range(1, x_translation):
                    if operator == "+":
                        new_zone = (list_element[0]+k, list_element[1])
                        practicable_zones.append(new_zone)
                    elif operator == "-":
                        new_zone = (list_element[0]-k, list_element[1])
                        practicable_zones.append(new_zone)

            if y_translation != 0:
                for k in range(1, y_translation):
                    if operator == "+":
                        new_zone = (list_element[0], list_element[1]+k)
                        practicable_zones.append(new_zone)
                    elif operator == "-":
                        new_zone = (list_element[0], list_element[1]-k)
                        practicable_zones.append(new_zone)
            
            else:
                pass

        return practicable_zones

    """
    This method generates all the sectors of the matrix
    representing the map. Each sector is represented by a tuple
    of cartesian coordinates and stored in the list global_map.
    """

    def map_generation(self, height, width):
        
        global_map = []
        
        for x_axe in range(0, width):
            for y_axe in range(0, height):
                grid = (x_axe, y_axe)
                global_map.append(grid)
        return global_map

    """
    Having generated the global matrix and identified the practicable sectors,
    we can deduce the impracticable sectors.
    """

    def not_practicable_zones(self, global_map, practicable_zones):
        
        not_practicable_zones = []

        for element in global_map:
            if element not in practicable_zones:
                not_practicable_zones.append(element)
        return not_practicable_zones


"""
Management of all the logical part of Items.
"""

class Items:

    def __init__(self, name):
        
        self.looted = False
        self.name = name.strip()

    """
    Knowing the practicable areas of the matrix, we will assign
    to the items a random position among these areas. We will exclude
    the positions of MacGyver and the guard, and ensure that once
    a sector assigned to an item, it is no longer available!
    """

    def item_location(self, possible_positions, not_possible_position):
        
        random_loc = random.randint(1, len(possible_positions) - 1)
        self.location = possible_positions[random_loc]
        self.item_index = random_loc                                  # Réduction du nombre d'opérations
        return self.location

    """
    Here we manage the logical part of collecting items. When
    MacGyver passes on an item, he picks it up and the status "picked up"
    of the item changes to True. It also removes its position attribute.
    """

    def item_looted(self, macgyver):
        
        if self.location == macgyver.position:
            self.looted = True
            macgyver.stuff.append(str(self.name))
            self.location = None
        return macgyver.stuff


"""
Guard generation. We notice that the instance of this
class has only attributes and no method.
"""

class Guard:

    def __init__(self, position, name):

        self.position = position
        self.name = name
        

"""
Management of all MacGyver's methods and attributes.
"""

class MacGyver:

    def __init__(self, starting_position, name):

        self.stuff = []
        self.position = starting_position
        self.name = name

    """
    Logic of MacGyver's displacement in the matrix. We
    here will vary its position attribute by checking
    that the user's command is consistent.
    """

    def move(self, player_input, practicable_zones):
        
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
            return print("Déplacement impossible. Vous devez rester dans les limites du labyrinthe")

    """
    Definition of the method allowing to recover the syringe.
    We check here that all the conditions are met for its
    manufacturing.
    """
    def craft(self, items):
        
        if items[0].looted and items[1].looted and items[2].looted:
            print("Seringue fabriquée ! Vous pouvez endormir le garde.")
            self.stuff = ["seringue"]


"""
Management of all the graphic part of the program.
This class has only one class method,
because it is not intended to create instances.
"""

class Display:

    """
    Here, we will use all the elements of the logical structure
    code to generate the correct display. We will therefore inject
    a lot of parameters in this class method. We
    will find a while function that will iterate 30 times per second as long as
    that the user does not close the pygame graphic interface.
    """

    @classmethod
    def display_routine(cls, global_map, practicable_zones, guard, macgyver, items):

        pygame.init()
        window = pygame.display.set_mode((cs.WINDOW_WIDTH, cs.WINDOW_HEIGHT))
        AIGUILLE_SPRITE = pygame.image.load("display/aiguille.png").convert()
        ETHER_SPRITE = pygame.image.load("display/ether.png").convert()
        TUBE_PLASTIQUE_SPRITE = pygame.image.load("display/tube_plastique.png").convert()

        display = True
        moving_functions = True
        while display:
            pygame.time.Clock().tick(30)
            for map_zone in global_map:
                if map_zone in practicable_zones:
                    window.blit(cs.PATH_SPRITE, (map_zone[0]*cs.WIDTH_PPS, map_zone[1]*cs.HEIGHT_PPS))
                else:
                    window.blit(cs.WALL_SPRITE, (map_zone[0]*cs.WIDTH_PPS, map_zone[1]*cs.HEIGHT_PPS))
        
            window.blit(cs.GUARD_SPRITE, (guard.position[0]*cs.WIDTH_PPS, guard.position[1]*cs.HEIGHT_PPS))
            window.blit(cs.MACGYVER_SPRITE, (macgyver.position[0]*cs.WIDTH_PPS, macgyver.position[1]*cs.HEIGHT_PPS))
            
            for event in pygame.event.get():
                if moving_functions:
                    if event.type == KEYDOWN and event.key == K_UP:
                        player_input = "front"
                        MacGyver.move(macgyver, player_input, practicable_zones)
                    elif event.type == KEYDOWN and event.key == K_DOWN:
                        player_input = "back"
                        MacGyver.move(macgyver, player_input, practicable_zones)
                    elif event.type == KEYDOWN and event.key == K_RIGHT:
                        player_input = "right"
                        MacGyver.move(macgyver, player_input, practicable_zones)
                    elif event.type == KEYDOWN and event.key == K_LEFT:
                        player_input = "left"
                        MacGyver.move(macgyver, player_input, practicable_zones)
                        
                    elif event.type == QUIT:
                        display = False
                else:
                    if event.type == QUIT:
                        display = False

            
            for i in range(0, len(items)):
                Items.item_looted(items[i], macgyver)
                if items[i].location != None:
                    name = vars()[items[i].name.strip()+"_SPRITE"]
                    window.blit(name, (items[i].location[0]*(cs.WIDTH_PPS), items[i].location[1]*(cs.HEIGHT_PPS)))
            
            if "seringue" not in macgyver.stuff:
                MacGyver.craft(macgyver, items)

            pygame.display.flip()
        
            if macgyver.position == guard.position and moving_functions:
                if "seringue" in macgyver.stuff:
                    print("You win the game")   
                else:
                    print("Game Over")
                moving_functions = False


"""
We define our main function, encapsulated in a conditional structure.
We will successively call each method of each class, and finish
by displaying the graphical interface.
"""

def main():

    path_builder = ti.path_builder()
    my_map = Map(path_builder)
    practicable_zones = Map.practicable_zones(my_map, my_map.path_builder)
    global_map = Map.map_generation(my_map, my_map.height, my_map.width)
    not_practicable_zones = Map.not_practicable_zones(my_map, global_map, practicable_zones)
    guard = ti.position_initializer("Guard")
    macgyver = ti.position_initializer("MacGyver")
    items = ti.items_creator(practicable_zones, guard)
    print("Le jeu a été initialisé avec succès !")
    Display.display_routine(global_map, practicable_zones, guard, macgyver, items)

if __name__ == "__main__":
    main()