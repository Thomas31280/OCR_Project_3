wall = [(1,0,0,4,"+"),(1,4,3,0,"+"),(4,4,0,5,"+"),(4,9,3,0,"+"),(7,9,0,4,"+"),(7,13,4,0,"+"),(11,13,0,7,"-"),(11,6,4,0,"-"),(7,6,0,3,"-"),(7,3,6,0,"+"),(13,3,0,4,"-"),(6,12,4,0,"-"),(2,12,0,3,"-"),(9,12,0,3,"-"),(12,8,1,0,"+"),(13,8,0,3,"-"),(6,3,0,2,"-"),(6,1,5,0,"+")]
global_map = []
practicable_zones = []
not_practicable_zones = []


##############################################
###Génération de la liste practicable_zones###
##############################################

for list_element in wall:                                                  # Pour chaque tuple de la liste wall...
    not_free = ((list_element[0], list_element[1]))                        # On va lire les deux premiers éléments (0 et 1) et on va créer un nouveau tuple (not_free) avec ces éléments...
    practicable_zones.append(not_free)                                     # On va stocker ce tuple not_free dans practicable_zones (pour ne pas qu'il se perde)
    tuple_element_2 = list_element[2]                                      # ...et on va venir lire les trois derniers éléments (2,3 et 4) du tuple, et on va les stocker indépendament dans 3 variables.
    tuple_element_3 = list_element[3]
    tuple_element_4 = list_element[4]
    
    if tuple_element_2 != 0:                                               # Puis si l'élément 2 est différent de 0 :
        for k in range(1, tuple_element_2):                                # ... on initialise une boucle qui va itérer sur cette valeur.
            if tuple_element_4 == "+":                                     # On va maintenant venir lire l'élément 4 ( stocké dans une variable ) et s'il vaut "+":
                new_zone = (list_element[0]+k, list_element[1])            # ... alors on prend le tuple "not_free" et à chaque itération, on va ajouter 1 à l'élément 0 du tuple...
                practicable_zones.append(new_zone)                         # ... puis on envoie le tuple dans practicable_zones !
            if tuple_element_4 == "-":                                     # Et si l'élément 4 vaut "-":
                new_zone = (list_element[0]-k, list_element[1])            # ... alors on prend le tuple "not_free" et à chaque itération, on va soustraire 1 à l'élément 0 du tuple...
                practicable_zones.append(new_zone)                         # ... puis on envoie le tuple dans practicable_zones !

    if tuple_element_3 != 0:                                               # Enfin, si c'est l'élément 3 est différent de 0 :
        for k in range(1, tuple_element_3):                                # ... on initialise une boucle qui va itérer sur cette valeur.
            if tuple_element_4 == "+":                                     # On va maintenant venir lire l'élément 4 ( stocké dans une variable ) et s'il vaut "+":
                new_zone = (list_element[0], list_element[1]+k)            # ... alors on prend le tuple "not_free" et à chaque itération, on va ajouter 1 à l'élément 1 du tuple...
                practicable_zones.append(new_zone)                         # ... puis on envoie le tuple dans practicable_zones !
            if tuple_element_4 == "-":                                     # Et si l'élément 4 vaut "-":
                new_zone = (list_element[0], list_element[1]-k)            # ... alors on prend le tuple "not_free" et à chaque itération, on va soustraire 1 à l'élément 1 du tuple...
                practicable_zones.append(new_zone)                         # ... puis on envoie le tuple dans practicable_zones !
    
    else:                                                                  # Si ni l'élément 2 ni l'élément 3 ne sont différent de 0:
        pass                                                               # On ne fait rien

print("Practicable Zones List :")
print()
print(practicable_zones)
print("----------------------------------------------")
print()


#######################################
###Génération de la liste global_map###
#######################################

height = 15                                                                # On commence par déterminer Height comme la hauteur de notre global_map
width = 15                                                                 # On fait de même avec Width la largeur

for x_axe in range(0, width):                                              # On commence par initialiser une boucle qui va itérer sur la largeur de la map
    for y_axe in range(0, height):                                         # ... puis une seconde boucle qui va itérer sur la hauteur...
        grid = (x_axe, y_axe)                                              # Et à chaque itération, on génère un tuple avec la variable de la première boucle pour premier élément, et celle de la seconde pour second élément.
        global_map.append(grid)                                            # Puis on envoie ce tuple dans la liste global_map. On va ainsi obtenir toutes les cases de notre map sous forme de tuples.

print("Global Map List :")
print()
print(global_map)
print("----------------------------------------------")
print()



##################################################
###Génération de la liste not_practicable_zones###
##################################################

for element in global_map:                                                 # On créé une boucle qui va itérer sur global_map
    if element not in practicable_zones:                                   # Si l'élément en cours de lecture n'est pas dans practicable_zones
        not_practicable_zones.append(element)                              # On ajoute l'élément dans not_practicable_zones
    else:                                                                  # Sinon :
        pass                                                               # On ne fait rien

print("Not Practicable Zones :")
<<<<<<< HEAD
print(not_practicable_zones)

while macgyver.position != guard.position:
        player_input = input("Entrez votre déplacement : front, back, right ou left")
        MacGyver.move(macgyver, player_input, practicable_zones)
        for i in range(0, len(items) - 1):
            Items.item_looted(items[i], macgyver)
        MacGyver.craft(macgyver)
        print(items[0].location, items[1].location, items[2].location)
        print("Position :", macgyver.position)
        print("Stuff :", macgyver.stuff)
        if macgyver.position == guard.position:
            if "seringue" in macgyver.stuff:
                print("You win the game")
            else:
                print("Game Over")
=======
print(not_practicable_zones)
>>>>>>> cbb2c8feef4f21f44674860fae74e7e6ab4f678d
