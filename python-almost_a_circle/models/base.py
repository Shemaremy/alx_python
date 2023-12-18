"""
Creating a base class and 
everything will be included inside here
"""

class Base:
    """
    A class representing a Base object.
    """

    __nb_objects = 0 # private class attribute

    def __init__(self, id=None):
        """
        Initializes a Base object
        and assigns the provided id to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


