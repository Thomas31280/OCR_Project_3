import main_file as mf

"""
Initialization of the position of the characters.
"""

def position_initializer(character):
    
    guard = None
    macgyver = None
    with open("starting_characters_position.txt") as scp:
        for line in scp.readlines():
            (name, x_loc, y_loc) = line.split()
            if name == "Guard" and character == "Guard":
                guard = mf.Guard((int(x_loc), int(y_loc)), name)
                return guard
            elif name == "MacGyver" and character == "MacGyver":
                macgyver = mf.MacGyver((int(x_loc), int(y_loc)), name)
                return macgyver
    

"""
Generation of items from the data of items.txt.
We will make sure that the list of possible positions
passed to the main_file function which assigns a
item position is consistent. For that, we will proceed
removing unwanted values.
"""

def items_creator(practicable_zones, guard):
    
    items = []
    with open("items.txt") as itms:
        possible_positions = []
        possible_positions = possible_positions + practicable_zones
        possible_positions.remove(guard.position)
        for line in itms:
            line = mf.Items(line)
            mf.Items.item_location(line, possible_positions)
            items.append(line)
            del possible_positions[line.item_index]
            del line.item_index
    return items


"""
From path_builder.txt, we will generate a
list of tuples. This list will be used to generate
the practicable sectors of the matrix.
"""

def path_builder():
    
    path_builder = []
     
    with open ("path_builder.txt") as pb:
        for line in pb.readlines():
            value = line.split(",")
            path_builder.append((int(value[0]),int(value[1]),int(value[2]),int(value[3]),str(value[4])))
    return path_builder