from spliting import items_class


def items_creator(practicable_zones, guard):
    """
    Generation of items from the data of items.txt.
    We will make sure that the list of possible positions
    passed to the main_file function which assigns a
    item position is consistent. For that, we will proceed
    removing unwanted values.
    """

    items = []
    with open("items.txt") as itms:
        possible_positions = []
        possible_positions = possible_positions + practicable_zones
        possible_positions.remove(guard.position)
        for line in itms:
            line = items_class.Items(line)
            items_class.Items.item_location(line, possible_positions)
            items.append(line)
            del possible_positions[line.item_index]
            del line.item_index
    return items


def path_builder():
    """
    From path_builder.txt, we will generate a
    list of tuples. This list will be used to generate
    the practicable sectors of the matrix.
    """

    path_builder = []

    with open("path_builder.txt") as pb:
        for line in pb.readlines():
            value = line.split(",")
            path_builder.append((int(value[0]), int(value[1]), int(value[2]),
                                 int(value[3]), str(value[4])))
    return path_builder
