import math
class Circle:
    def __init__(self,x,y,radius):
        self.x_position=x
        self.y_position=y
        self.radius=radius
    def get_area(self):
        return self.radius**2 * math.pi
    def translate(self,x_delta,y_delta):
        self.x_position += x_delta
        self.y_position += y_delta