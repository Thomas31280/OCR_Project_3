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
        
        for list_element in path_builder:                                           # Pour chaque tuple de la liste path_builder...
            free_zone = ((list_element[0], list_element[1]))                        # On va lire les deux premiers éléments (0 et 1) et on va créer un nouveau tuple (not_free) avec ces éléments...
            practicable_zones.append(free_zone)                                     # On va stocker ce tuple not_free dans practicable_zones (pour ne pas qu'il se perde)
            x_translation = list_element[2]                                         # ...et on va venir lire les trois derniers éléments (2,3 et 4) du tuple, et on va les stocker indépendament dans 3 variables.
            y_translation = list_element[3]
            operator = list_element[4]
            
            if x_translation != 0:                                               # Puis si l'élément 2 est différent de 0 :
                for k in range(1, x_translation):                                # ... on initialise une boucle qui va itérer sur cette valeur.
                    if operator == "+":                                          # On va maintenant venir lire l'élément 4 ( stocké dans une variable ) et s'il vaut "+":
                        new_zone = (list_element[0]+k, list_element[1])          # ... alors on prend le tuple "not_free" et à chaque itération, on va ajouter 1 à l'élément 0 du tuple...
                        practicable_zones.append(new_zone)                       # ... puis on envoie le tuple dans practicable_zones !
                    elif operator == "-":                                          # Et si l'élément 4 vaut "-":
                        new_zone = (list_element[0]-k, list_element[1])          # ... alors on prend le tuple "not_free" et à chaque itération, on va soustraire 1 à l'élément 0 du tuple...
                        practicable_zones.append(new_zone)                       # ... puis on envoie le tuple dans practicable_zones !

            if y_translation != 0:                                               # Enfin, si c'est l'élément 3 est différent de 0 :
                for k in range(1, y_translation):                                # ... on initialise une boucle qui va itérer sur cette valeur.
                    if operator == "+":                                          # On va maintenant venir lire l'élément 4 ( stocké dans une variable ) et s'il vaut "+":
                        new_zone = (list_element[0], list_element[1]+k)          # ... alors on prend le tuple "not_free" et à chaque itération, on va ajouter 1 à l'élément 1 du tuple...
                        practicable_zones.append(new_zone)                       # ... puis on envoie le tuple dans practicable_zones !
                    elif operator == "-":                                          # Et si l'élément 4 vaut "-":
                        new_zone = (list_element[0], list_element[1]-k)          # ... alors on prend le tuple "not_free" et à chaque itération, on va soustraire 1 à l'élément 1 du tuple...
                        practicable_zones.append(new_zone)                       # ... puis on envoie le tuple dans practicable_zones !
            
            else:                                                                # Si ni l'élément 2 ni l'élément 3 ne sont différent de 0:
                pass                                                             # On ne fait rien

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
        self.looted = False
        self.name = name

################################################
###Répartition du loot dans practicable_zones###
################################################

    def item_location(self, possible_positions):
        
        random_loc = random.randint(1, len(possible_positions) - 1)                # On va générer un nombre aléatoire compris dans l'intervalle [1;len(practicable_zones) - 1]
        self.location = possible_positions[random_loc]                             # On assigne ensuite un attribut position à l'instance qui vaut practicable_zones[x]

        return self.location


####################################
###Gestion du ramassage des items###
####################################

    def item_looted(self, macgyver):
        
        if self.location == macgyver.position:
            self.looted = True
            macgyver.stuff.append(self.name)
            self.location = None                                                    # Pour que l'item ramassé ne soit plus récupérable !!!
        return macgyver.stuff                                                       # En option, car nous n'avons pas vraiment besoin de retourner quoi que ce soit...


class Guard:

    def __init__(self, position, name):

        self.position = position
        self.name = name
        

class MacGyver:

    def __init__(self, starting_position, name):

        self.stuff = []
        self.live = True
        self.position = starting_position
        self.name = name

    def move(self, input, practicable_zones):
        
        buffer_position = None

        if input == "front":
            buffer_position = (self.position[0], self.position[1]+1)
        
        elif input == "back":
            buffer_position = (self.position[0], self.position[1]-1)
        
        elif input == "right":
            buffer_position = (self.position[0]+1, self.position[1])
        
        elif input == "left":
            buffer_position = (self.position[0]-1, self.position[1])
        
        if buffer_position in practicable_zones:
            self.position = buffer_position
            return self.position
        else:
            return print("Déplacement impossible. Vous devez rester dans les limites du labyrinthe")


    def craft(self):
        
        if "aiguille" and "tube_plastique" and "ether" in self.stuff:
            self.stuff = ["seringue"]


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
    with open("starting_characters_position.txt") as scp:
        for line in scp.readlines():
            (name, x_loc, y_loc) = line.split()
            if name == "Guard":
                guard = Guard((int(x_loc), int(y_loc)), name)
            elif name == "MacGyver":
                macgyver = MacGyver((int(x_loc), int(y_loc)), name)
    
    
if __name__ == "__main__":
    main()