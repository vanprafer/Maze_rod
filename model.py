class MazeState:
    """This class represents a state in the proposed maze problem. A state contains the following: x coordinate, y coordinate and an orientation. 
    This orientation is represented as a boolean value that is True when the rod is horizontal
    """
    def __init__(self, x, y, o):
        self.x = x
        self.y = y
        self.o = o
    
    
    def __str__(self): 
        return "x:% s y:% s o:% s" % (self.x, self.y, self.o) 
    
    
    def __eq__(self, b):
        return self.x == b.x and self.y == b.y and self.o == b.o
    
    
    def __hash__(self):
        return hash((self.x, self.y, self.o))
    
    
    def is_final(self, w, h):
        # Returns true when it is at the bottom right corner 
        return (self.x == w - 2 and self.y == h - 1 and self.o) or (self.x == w - 1 and self.y == h - 2 and not self.o)
    
    
    def visualize_maze(self, maze):
        # Debug function to visualize mazes in console. The full rod is not drawn, just the direction
        maze_str = ''
        
        for i_y, row in enumerate(maze):
            for i_x, p in enumerate(row):
                if i_y == self.y and i_x == self.x:
                    if self.o:
                        maze_str = maze_str + '-'
                        
                    else:
                        maze_str = maze_str + '|'

                else:
                    maze_str = maze_str + p
                
            maze_str = maze_str + '\n'
                
        print(maze_str)