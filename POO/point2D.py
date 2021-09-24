class Point2D:
    _x: int
    _y : int 

    def __init__ (self,x,y):
        self._x=x
        self._y=y
    
    #get
    def __getX__(self) -> int:
        return self._x
    def __getY__(self) -> int:
        return self._y
    #set
    def __setX__(self,x):
        self._x=x
    def __setY__(self,y):
        self._y=y
