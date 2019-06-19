import math

class Point:

    """Get the distance between two points in a 2 dimensional space."""

    def __init__(self, coords=(0, 0)):
        self.coords = coords

    def __eq__(self, other_point):
        if self.coords == other_point.coords:
            return True
        else: 
            return False
    
    def add(self, other_point):
        x = other_point.coords[0] + self.coords[0]
        y = other_point.coords[1] + self.coords[1]
        self.coords = (x, y)

    def __add__(self, other_point):
        coords = ((self.coords[0] + other_point.coords[0], self.coords[1] + other_point.coords[1]))
        print(coords)
        return Point(coords)

    def __str__(self):
        return "P({}, {})".format(self.coords[0], self.coords[1])
    
    def distance_to(self, other_point):
        second_x = other_point.coords[0]
        second_y = other_point.coords[1]
        distance =  ((self.coords[0] - second_x)**2 + (self.coords[1] - second_y)**2 ) ** 0.5
        print(distance)
        return distance

class DimensionalPoint:

    """This class handles points in any dimesional space."""

    def __init__(self, coords=(0,0,0)):
        self.coords = coords
        self.length = len(coords)
    
    def __eq__(self, other_point):
        if self.coords == other_point.coords:
            return True
        else: 
            return False
    
    def add(self, other_point):

        if self.length != other_point.length:
            print("Points do not have the same lengths.")
            return False
        
        else:
            new_coords = []
            for i in range(0, self.length):
                new_coords.append(self.coords[i] + other_point.coords[i])

        self.coords = tuple(new_coords)

    def __add__(self, other_point):

        if self.length != other_point.length:
            print("Points do not have the same lengths.")
            return False
        
        else:
            new_coords = []
            for i in range(0, self.length):
                new_coords.append(self.coords[i] + other_point.coords[i])
      
        return DimensionalPoint(new_coords)

    def __str__(self):
        return "P{}".format(self.coords)
    
    def distance_to(self, other_point):
        
        distance = 0
        
        for i in range(0, self.length):
            distance += (self.coords[i] - other_point.coords[i])**2
        
        distance = distance ** 0.5
        return distance