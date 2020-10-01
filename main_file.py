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


#######################################
###Génération de la liste global_map###
#######################################

    def map_generation(self, height, width):
        
        global_map = []
        
        for x_axe in range(0, width):
            for y_axe in range(0, height):
                grid = (x_axe, y_axe)
                global_map.append(grid)
        return global_map


##################################################
###Génération de la liste not_practicable_zones###
##################################################

    def not_practicable_zones(self, global_map, practicable_zones):
        
        not_practicable_zones = []

        for element in global_map:
            if element not in practicable_zones:
                not_practicable_zones.append(element)
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
        
        random_loc = random.randint(1, len(possible_positions) - 1)
        self.location = possible_positions[random_loc]

        return self.location


####################################
###Gestion du ramassage des items###
####################################

    def item_looted(self, macgyver):
        
        if self.location == macgyver.position:
            self.looted = True
            macgyver.stuff.append(str(self.name))
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

    def move(self, player_input, practicable_zones):
        
        buffer_position = None

        if player_input == "front":
            buffer_position = (self.position[0], self.position[1]+1)
        
        elif player_input == "back":
            buffer_position = (self.position[0], self.position[1]-1)
        
        elif player_input == "right":
            buffer_position = (self.position[0]+1, self.position[1])
        
        elif player_input == "left":
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
    with open("items.txt") as itms:
        for line in itms:
            line = Items(practicable_zones, line)
            Items.item_location(line, line.possible_positions)
            items.append(line)
    with open("starting_characters_position.txt") as scp:
        for line in scp.readlines():
            (name, x_loc, y_loc) = line.split()
            if name == "Guard":
                guard = Guard((int(x_loc), int(y_loc)), name)
            elif name == "MacGyver":
                macgyver = MacGyver((int(x_loc), int(y_loc)), name)
    while macgyver.position != guard.position:
        player_input = input("Entrez votre déplacement : front, back, right ou left")
        MacGyver.move(macgyver, player_input, practicable_zones)
        for i in range(0, len(items)):
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
        
    
if __name__ == "__main__":
    main()