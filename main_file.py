import random

class Map:

    def __init__(self):
        
        map_stats = {}
        path_builder = []
        
        with open("map_stats.txt") as ms:
            for line in ms:
                (key, val) = line.split()
                map_stats[key] = int(val)
        
        with open ("path_builder.txt") as pb:
            for line in pb.readlines():
                value = line.split(",")
                path_builder.append((int(value[0]),int(value[1]),int(value[2]),int(value[3]),str(value[4])))

        self.height = map_stats["Height_Unity"]
        self.width = map_stats["Width_Unity"]
        self.path_builder = path_builder


##############################################
###Génération de la liste practicable_zones###
##############################################

    
    def practicable_zones(self, path_builder):
        
        practicable_zones = []
        
        for list_element in path_builder:                                          # Pour chaque tuple de la liste path_builder...
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
                    elif tuple_element_4 == "-":                                     # Et si l'élément 4 vaut "-":
                        new_zone = (list_element[0]-k, list_element[1])            # ... alors on prend le tuple "not_free" et à chaque itération, on va soustraire 1 à l'élément 0 du tuple...
                        practicable_zones.append(new_zone)                         # ... puis on envoie le tuple dans practicable_zones !

            if tuple_element_3 != 0:                                               # Enfin, si c'est l'élément 3 est différent de 0 :
                for k in range(1, tuple_element_3):                                # ... on initialise une boucle qui va itérer sur cette valeur.
                    if tuple_element_4 == "+":                                     # On va maintenant venir lire l'élément 4 ( stocké dans une variable ) et s'il vaut "+":
                        new_zone = (list_element[0], list_element[1]+k)            # ... alors on prend le tuple "not_free" et à chaque itération, on va ajouter 1 à l'élément 1 du tuple...
                        practicable_zones.append(new_zone)                         # ... puis on envoie le tuple dans practicable_zones !
                    elif tuple_element_4 == "-":                                     # Et si l'élément 4 vaut "-":
                        new_zone = (list_element[0], list_element[1]-k)            # ... alors on prend le tuple "not_free" et à chaque itération, on va soustraire 1 à l'élément 1 du tuple...
                        practicable_zones.append(new_zone)                         # ... puis on envoie le tuple dans practicable_zones !
            
            else:                                                                  # Si ni l'élément 2 ni l'élément 3 ne sont différent de 0:
                pass                                                               # On ne fait rien

        return practicable_zones


#######################################
###Génération de la liste global_map###
#######################################

    def map_generation(self, height, width):
        
        global_map = []
        
        for x_axe in range(0, width):                                              # On commence par initialiser une boucle qui va itérer sur la largeur de la map
            for y_axe in range(0, height):                                         # ... puis une seconde boucle qui va itérer sur la hauteur...
                grid = (x_axe, y_axe)                                              # Et à chaque itération, on génère un tuple avec la variable de la première boucle pour premier élément, et celle de la seconde pour second élément.
                global_map.append(grid)                                            # Puis on envoie ce tuple dans la liste global_map. On va ainsi obtenir toutes les cases de notre map sous forme de tuples.
        return global_map


##################################################
###Génération de la liste not_practicable_zones###
##################################################

    def not_practicable_zones(self, global_map, practicable_zones):
        
        not_practicable_zones = []

        for element in global_map:                                                 # On créé une boucle qui va itérer sur global_map
            if element not in practicable_zones:                                   # Si l'élément en cours de lecture n'est pas dans practicable_zones
                not_practicable_zones.append(element)                              # On ajoute l'élément dans not_practicable_zones
        return not_practicable_zones


class Items:

    def __init__(self, possible_positions, name):
        
        self.possible_positions = possible_positions
        self.weight = 1
        self.looted = False
        self.name = name

################################################
###Répartition du loot dans practicable_zones###
################################################

    def item_location(self, possible_positions):
        
        random_loc = random.randint(1, len(possible_positions) - 1)                # On va générer un nombre aléatoire compris dans l'intervalle [1;len(practicable_zones) - 1]
        self.location = possible_positions[random_loc]                             # On assigne ensuite un attribut position à l'instance qui vaut practicable_zones[x]

        return self.location


    def item_looted(self):
        pass


class Guard:

    def __init__(self, position, name):

        self.position = position
        self.name = name
        self.asleep = False
        

class MacGyver:

    def __init__(self, starting_position, name):

        self.stuff = []
        self.live = True
        self.position = starting_position
        self.name = name

    def move(self, input, practicable_zones):
        pass

    def craft(self, stuff):
        pass


def main():

    my_map = Map()
    practicable_zones = Map.practicable_zones(my_map, my_map.path_builder)
    global_map = Map.map_generation(my_map, my_map.height, my_map.width)
    not_practicable_zones = Map.not_practicable_zones(my_map, global_map, practicable_zones)
    items = []
    guard = None
    macgyver = None
    with open("items.txt") as itms:                                                # On va travailler sur le fichier items.txt
        for line in itms:                                                          # On va créer une boucle qui va itérer sur les lignes de items.txt
            line = Items(practicable_zones, line)                                  # Pour chaque ligne, on va créer une instance de la classe items nommée d'après la ligne...
            Items.item_location(line, line.possible_positions)                     # Et on va la faire passer dans la méthode item_location
            items.append(line)                                                     # Et pour finir on stocke l'instance dans la liste items ( pour pouvoir les appeler plus tard )
    with open("starting_characters_position.txt") as shp:
        for line in shp.readlines():
            (name, x_loc, y_loc) = line.split()
            if name == "Guard":
                guard = Guard((int(x_loc), int(y_loc)), name)
            elif name == "MacGyver":
                macgyver = MacGyver((int(x_loc), int(y_loc)), name)
            else:
                pass
    print(practicable_zones)
    
if __name__ == "__main__":
    main()