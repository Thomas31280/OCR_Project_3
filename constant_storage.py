import pygame

HEIGHT_UNITY = 15
WIDTH_UNITY = 15
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 720

pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WIDTH_PPS = WINDOW_WIDTH/WIDTH_UNITY
HEIGHT_PPS = WINDOW_HEIGHT/HEIGHT_UNITY
WALL_SPRITE = pygame.image.load("display/wall.png").convert()
PATH_SPRITE = pygame.image.load("display/path.png").convert()
MACGYVER_SPRITE = pygame.image.load("display/MacGyver.png").convert_alpha()
GUARD_SPRITE = pygame.image.load("display/Gardien.png").convert_alpha()