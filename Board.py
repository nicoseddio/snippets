class Board:
    def __init__(self,width,height,origin=(0,0),tile_default=None):
        self._tile_default = d = tile_default
        self._width  = w = width
        self._height = h = height
        self._origin = origin
        self._layout = [[d for x in range(w)] for y in range(h)]
    def __str__(self):
        s = ""
        # Build string backwards so (0,0) is in the lower-left corner.
        for y in range(len(self._layout)-1,-1,-1):
            for x in self._layout[y]:
                if x == None or len(x) < 1: x = " "
                s += "[{}]".format(x[0:1])
            if y != 0: s += "\n"
        return s
    
    def get(self,x,y):
        return self._layout[y + self._origin[1]][x + self._origin[0]]
    def set(self,object,x,y):
        deposed = self.get(x,y)
        self._layout[y + self._origin[1]][x + self._origin[0]] = object
        return deposed
    def remove(self,x,y):
        return self.set(self._tile_default,x,y)
    def move(self,xy1,xy2):
        return self.set(self.remove(xy1[0],xy1[1]),xy2[0],xy2[1])
    def reset(self):
        # Reset board to initial layout. Different than clear(), which
        # honors changes in board size.
        self.__init__(self._width,self._height)
    def clear(self):
        for y in range(len(self._layout)):
            for x in range(len(self._layout[y])):
                self._layout[y][x] = self._tile_default
    
if __name__ == "__main__":
    b = Board(7,5,(-1,-1))
    print("New board!\n{}".format(b))
    b.set("Hello World!",2,3)
    print("Let's add a piece:\n{}".format(b))
    b.move((2,3),(1,1))
    print("It moves!\n{}".format(b))
    print("What is it?!\n...\"{}\"!".format(b.get(1,1)))
    b.set("Goodbye World!",1,2)
    print("Let's add another:\n{}\n\"{}\"".format(b,b.get(1,2)))
    deposed = b.move((1,2),(1,1))
    print("Attack!\n{}".format(b))
    print("\"{}\" deposed \"{}\"!".format(b.get(1,1),deposed))
    b.reset()
    print("Goodbye!\n{}".format(b))
    
    print()
    c = Board(35,35,(17,17))
    print(c)
    c.set("N",1,1)
    c.set("N",-1,-1)
    print(c.get(1,1))
    print(c)