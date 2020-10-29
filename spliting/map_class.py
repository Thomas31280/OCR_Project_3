import constant_storage

class Map:
    """
    The Map class manages all the logical part of the Map and contains
    all the methods needed for its generation.
    """

    def __init__(self, path_builder):

        self.height = constant_storage.HEIGHT_UNITY
        self.width = constant_storage.WIDTH_UNITY
        self.path_builder = path_builder

    def practicable_zones(self, path_builder):
        """
        From the path_builder.txt, we generate the list of all tuples
        of two elements, which correspond to the cartesian coordinates of the
        sectors of the matrix which will be considered as practicables.
        """

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

    def map_generation(self, height, width):
        """
        This method generates all the sectors of the matrix
        representing the map. Each sector is represented by a tuple
        of cartesian coordinates and stored in the list global_map.
        """

        global_map = []

        for x_axe in range(0, width):
            for y_axe in range(0, height):
                grid = (x_axe, y_axe)
                global_map.append(grid)
        return global_map

    def not_practicable_zones(self, global_map, practicable_zones):
        """
        Having generated the global matrix and identified the practicable
        sectors, we can deduce the impracticable sectors.
        """

        not_practicable_zones = []

        for element in global_map:
            if element not in practicable_zones:
                not_practicable_zones.append(element)
        return not_practicable_zones
