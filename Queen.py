import numpy as np
class Queen:
    
    Queen_objects = []
    Queen_child_temp=[]
    only_pop = []

    def __init__(self,conflict=0,fitness =0):
        self.board = np.zeros((8, 8))
        self.chromosome = []
        self.x_and_y_location= []
        self.conflict = conflict
        self.fitness = fitness
           
    def setBoard(self,cross):
        
        for y,x in enumerate(cross):

            self.board[x][y]=1
            self.x_and_y_location.append([])
            self.x_and_y_location[y].append(y)
            self.x_and_y_location[y].append(x)
            self.chromosome.append(x)
            

