from point2D import Point2D
class Point3D(Point2D):
    _z:int

    def __init__(self,x,y,z):
        super().__init__(x,y)
        self._z = z
    
    def __getZ__(self) -> int:
        return(self._z)

    def __setZ__(self,z):
        self._z=z
