import main_file as mf

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
    

def items_creator(practicable_zones, guard):
    
    items = []
    with open("items.txt") as itms:
        for line in itms:
            line = mf.Items(practicable_zones, line)
            mf.Items.item_location(line, line.possible_positions, guard.position)
            items.append(line)
    return items


def path_builder():
    
    path_builder = []
     
    with open ("path_builder.txt") as pb:
        for line in pb.readlines():
            value = line.split(",")
            path_builder.append((int(value[0]),int(value[1]),int(value[2]),int(value[3]),str(value[4])))
    return path_builder