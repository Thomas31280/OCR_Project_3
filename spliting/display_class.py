import pygame
from pygame.locals import *

import constant_storage
from spliting import macgyver_class

class Display:
    """
    Management of all the graphic part of the program.
    This class has only one class method,
    because it is not intended to create instances.
    """

    @classmethod
    def display_routine(cls, global_map, practicable_zones, guard,
                        macgyver, items):
        """
        Here, we will use all the elements of the logical structure
        code to generate the correct display. We will therefore inject
        a lot of parameters in this class method. We
        will find a while function that will iterate 30 times per second as
        long as that the user does not close the pygame graphic interface.
        """

        pygame.init()
        window = pygame.display.set_mode((constant_storage.WINDOW_WIDTH,
                                          constant_storage.WINDOW_HEIGHT))
        display = True
        moving_functions = True

        while display:
            pygame.time.Clock().tick(30)
            for map_zone in global_map:
                if map_zone in practicable_zones:
                    window.blit(constant_storage.PATH_SPRITE, (map_zone[0] *
                                constant_storage.WIDTH_PPS, map_zone[1] *
                                constant_storage.HEIGHT_PPS))
                else:
                    window.blit(constant_storage.WALL_SPRITE, (map_zone[0] *
                                constant_storage.WIDTH_PPS,
                                map_zone[1]*constant_storage.HEIGHT_PPS))

            window.blit(constant_storage.GUARD_SPRITE, (guard.position[0] *
                        constant_storage.WIDTH_PPS,
                        guard.position[1]*constant_storage.HEIGHT_PPS))
            window.blit(constant_storage.MACGYVER_SPRITE,
                        (macgyver.position[0]*constant_storage.WIDTH_PPS,
                         macgyver.position[1]*constant_storage.HEIGHT_PPS))

            for event in pygame.event.get():
                if moving_functions:
                    if event.type == KEYDOWN and event.key == K_UP:
                        player_input = "front"
                        macgyver_class.MacGyver.move(macgyver, player_input,
                                      practicable_zones)
                    elif event.type == KEYDOWN and event.key == K_DOWN:
                        player_input = "back"
                        macgyver_class.MacGyver.move(macgyver, player_input,
                                      practicable_zones)
                    elif event.type == KEYDOWN and event.key == K_RIGHT:
                        player_input = "right"
                        macgyver_class.MacGyver.move(macgyver, player_input,
                                      practicable_zones)
                    elif event.type == KEYDOWN and event.key == K_LEFT:
                        player_input = "left"
                        macgyver_class.MacGyver.move(macgyver, player_input,
                                      practicable_zones)

                    elif event.type == QUIT:
                        display = False
                else:
                    if event.type == QUIT:
                        display = False

            constant_storage.items_auto_finder(items, macgyver)

            if "seringue" not in macgyver.stuff:
                macgyver_class.MacGyver.craft(macgyver, items)

            pygame.display.flip()

            if macgyver.position == guard.position and moving_functions:
                if "seringue" in macgyver.stuff:
                    print("You win the game")
                else:
                    print("Game Over")
                moving_functions = False
