<<<<<<< HEAD
import pygame
from pygame.locals import *

pygame.init()

global_map = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14)]
practicable_zones = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 9), (6, 9), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (8, 13), (9, 13), (10, 13), (11, 13), (11, 12), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (11, 6), (10, 6), (9, 6), (8, 6), (7, 6), (7, 5), (7, 4), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (13, 2), (13, 1), (13, 0), (6, 12), (5, 12), (4, 12), (3, 12), (2, 12), (2, 11), (2, 10), (9, 12), (9, 11), (9, 10), (12, 8), (13, 8), (13, 7), (13, 6), (6, 3), (6, 2), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]
window = pygame.display.set_mode((720, 720))
wall_sprite = pygame.image.load("wall.png").convert()
path_sprite = pygame.image.load("path.png").convert()
mg = pygame.image.load("MacGyver.png").convert_alpha()
ether_sprite = pygame.image.load("ether.png").convert()
continuer = 1
items = []

with open("items.txt") as itms:
    for line in itms:
        items.append(line)
print(items)
a = items[0]+"_sprite"
print(a)

for map_zone in global_map:
    if map_zone in practicable_zones:
        window.blit(path_sprite, (map_zone[0]*48, map_zone[1]*48))
    else:
        window.blit(wall_sprite, (map_zone[0]*48, map_zone[1]*48))

cond = None
while continuer:
    window.blit(mg, (48,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_SPACE:
            print("Espace")
        if event.type == KEYDOWN and event.key == K_DOWN and cond != None:
            window.blit(mg,(96,0))
        if event.type == KEYDOWN and event.key == K_RIGHT:
            window.blit(ether_sprite,(96,96))    
        if event.type == QUIT:
            continuer = 0
    
    window.blit(ether_sprite,(212,96))
    pygame.display.flip()
=======
<<<<<<< HEAD
k = (1,2,3)

print(len(k)-1)
=======
k = []

with open("test_text_file.txt") as f:
    for line in f:
        print(line)
        print(type(line))
>>>>>>> cbb2c8feef4f21f44674860fae74e7e6ab4f678d
>>>>>>> 5d35739b316d81f6a006853957b48211ac4078f7
