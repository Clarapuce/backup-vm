from point2D import Point2D
from point3D import Point3D

A = Point2D(1,2)
print(A.__getY__())
A.__setY__(-2)
print(A.__getY__())

B=Point3D(8,2,3)
print(B.__getX__())