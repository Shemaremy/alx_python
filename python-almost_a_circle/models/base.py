"""
Creating a base class and 
everything will be included inside here
"""

class Base:
    """
    A class representing a Base object.

    Attributes:
    - __nb_objects (int): A private class attribute to keep track of the number of objects created.
    - id (int): A public instance attribute representing the object's identifier.

    Methods:
    - __init__: The constructor method to initialize the Base object.
    """

    __nb_objects = 0 # private class attribute

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Parameters:
        - id (int): An optional parameter representing the identifier for the object.

        If id is not provided:
        - Increments __nb_objects.
        - Assigns the new value of __nb_objects to the public instance attribute id.
        If id is provided:
        - Assigns the provided id to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# Example usage:
#obj1 = Base()
#print(obj1.id) # Output: 1

#obj2 = Base(100)
#print(obj2.id) # Output: 100
