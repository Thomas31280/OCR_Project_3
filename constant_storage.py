import pygame

from spliting import items_class

HEIGHT_UNITY = 15
WIDTH_UNITY = 15
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 720
MACGYVER_POSITION_INIT = (1, 0)
GUARD_POSITION_INIT = (13, 0)

pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WIDTH_PPS = WINDOW_WIDTH/WIDTH_UNITY
HEIGHT_PPS = WINDOW_HEIGHT/HEIGHT_UNITY
WALL_SPRITE = pygame.image.load("display/wall.png").convert()
PATH_SPRITE = pygame.image.load("display/path.png").convert()
MACGYVER_SPRITE = pygame.image.load("display/MacGyver.png").convert_alpha()
GUARD_SPRITE = pygame.image.load("display/Gardien.png").convert_alpha()


def items_auto_finder(items, macgyver):
    """
    This function automates two things: The search and
     display of items on the map. We place at the start of the function
     the variables that refer to the item sprites. The function goes
     then check for each item of items.txt if it should be displayed,
     and if this is the case, it will automatically fetch the sprite
     corresponding to the item it is reading in items.txt.
    """

    AIGUILLE_SPRITE = pygame.image.load("display/aiguille.png").convert()
    ETHER_SPRITE = pygame.image.load("display/ether.png").convert()
    TUBE_PLASTIQUE_SPRITE = pygame.image.load("display/\
tube_plastique.png").convert()
    for i in range(0, len(items)):
        items_class.Items.item_looted(items[i], macgyver)
        if items[i].location is not None:
            name = vars()[items[i].name.strip()+"_SPRITE"]
            window.blit(name, (items[i].location[0]*(WIDTH_PPS),
                        items[i].location[1]*(HEIGHT_PPS)))
    return items
