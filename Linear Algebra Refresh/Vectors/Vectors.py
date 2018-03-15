##################################### Vector Module ###############################################
from math import sqrt, pi, acos
from decimal import Decimal, getcontext



class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be noempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        '''Función que nos permite imprimir el vector haciendo uso de la
        función print'''
        return 'Vector : {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.new_coordinates == v.new_coordinates
    

    def plus(self, v):
        new_coordinates = [x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    

    def minus(self, v):
        new_coordinates = [x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


    def scalar(self, c):
        new_coordinates = [c*coordinate for coordinate in self.coordinates]
        return Vector(new_coordinates)


    def magnitude(self):
        magnitude = sqrt(sum([cor*cor for cor in self.coordinates]))
        return magnitude


    def normalized(self):
        try:
            direction_cor = self.scalar(1.0/self.magnitude())
            return direction_cor
        
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def product(self,v):
            product = sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
            return product

    def angle(self,v,in_degrees = False):
        u1 = self.normalized()
        u2 = v.normalized()
        angle_in_radians = acos(u1.product(u2))
        if in_degrees:
            degrees_per_radian = 180./pi
            return angle_in_radians * degrees_per_radian
        else:
            return angle_in_radians


    def component_parallel(self,b):
        u = b.normalized()
        proj = self.product(u)
        return u.scalar(proj)


    def orthogonal(self, b):
        proj = self.component_parallel(b)
        return self.minus(proj)


    def cross_product(self, v):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates
        cross_vector = [y1*z2 - y2*z1, x2*z1 - x1*z2, x1*y2 - x2*y1]
        return Vector(cross_vector)

    def area_parallelogram(self,v):
        cross_vector = self.cross_product(v)
        return cross_vector.magnitude()
    

    def area_triangle(self,v):
        cross_vector = self.cross_product(v)
        return 1/2*cross_vector.magnitude()
        
            
    

    



