import constant_storage

class Guard:
    """
    Guard generation. We notice that the instance of this
    class has only attributes and no method.
    """

    def __init__(self):

        self.position = constant_storage.GUARD_POSITION_INIT
        self.name = "Guard"
