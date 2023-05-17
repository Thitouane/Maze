#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`maze` module 

:author: ` HELLE Thitouane, TALEB-AHMED Hacène
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2018, november.


"""
#nous avons laissé les différentes étapes par lesquels nous sommes passé en commantaire
from cell import Cell
from random import randint
from stack import Stack

def neighborhood(x, y, width, height):
    """
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :param height: height of the grid
    :type height: int
    :param width: width of the grid
    :type width: int
    :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 3), (3, 2), (3, 4), (4, 3)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4),  (1, 3)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 9), (3, 8), (4, 9)]
    """
    liste = [(x-1,y), (x,y-1), (x,y+1), (x+1,y)]
    result = []
    for tuple in liste :
        if not (tuple[0] >= width or tuple[1] >= height or tuple[0] < 0 or tuple[1] < 0 ):
            result.append(tuple)
    return result

class Maze():
    """
    Mazes are defined by width and height.
    >>> maze = Maze(6, 4)
    >>> maze.get_height()
    4
    >>> maze.get_width()
    6
    """
    
    def __init__(self, width = 6, height = 4):
        """
        build a labyrinth of size width*height cells 

        :param width:[optional] horizontal size of maze (default = 6)
        :type width: int
        :param height: [optional] vertical size of maze (default = 4)
        :type height: int
        :return: a labyrinth of width*height
        :rtype: Maze
        :UC: 
        :Example:

        >>> maze=Maze()
        >>> maze.get_height()
        4
        >>> maze.get_width()
        6
        """
        self.__width = width
        self.__height = height
        self.__grid =[]
        self.__grid_txt=[]

#_______ maze basic constructor __________________________________________________________________
##        test_maze=[("+-"*width+"+"),]
##        for line in range(height) :
##            test_maze+=[("| "*width+"|"),]    
##            test_maze+= [("+-"*width+"+"),]
##        print(test_maze)
#_________________________________________________________________________________________________


#_______ Maintenant on essaie de faire une grille aléatoire ______________________________________
##        for line in range(height*2) :
##            self.__grid+=['']
##            if line%2 == 0 :
##                for col in range(width) :
##                    alea = randint(0,1)
##                    if alea == 0 :
##                        self.__grid[line] += ("|"+str(Cell()))
##                    else :                            
##                        self.__grid[line] += (" "+str(Cell()))
##            else :
##                for col in range(width) :
##                    alea = randint(0,1)
##                    if alea == 0 :
##                        self.__grid[line] += "+ "
##                    else :
##                        self.__grid[line] += "+-"       
##        
##        self.__grid = [("+-"*width)] + self.__grid
##        self.__grid[-1] = self.__grid[0]
##        
##        x=0
##        for finishedLine in self.__grid :
##            if "+" in finishedLine :
##                self.__grid[x] += "+"
##            else :
##                self.__grid[x] = "|" + finishedLine[1:]
##                self.__grid[x] += "|"
##            x+=1
#_________________________________________________________________________________________________
            
#_____________ Maintenant on essaie de faire un labyrinthe qu'avec des cell ______________________
        #____construit la structure du maze ______________________________________________________
##        cpt=0
##        for column in range(height):
##            column_cell = []
##            for line in range(width):
##                column_cell.append( Cell() )
##            self.__grid.append(column_cell)
#________ On change de méthode on va faire une grille et on creusera le labyrinthe avec une fonction
    
    def get_height(self):
        """
        :return: height of the maze
        :rtype: int
        :UC: none
        """
        return self.__height

    def get_width(self):
        """
        :return: width of the maze
        :rtype: int
        :UC: none
        """
        return self.__width
    
    def grid(self, width ,height):
        """
        :param width: the width of the grid
        :param height: the height of the grid
        :type width: int
        :type height: int
        :side effect: build the grid of cells
        :UC: None
        
        """
        cpt=0
        for column in range(height):
            column_cell = []
            for line in range(width):
                column_cell.append( Cell() )
            self.__grid.append(column_cell)
        
    def miner(self,width,height):
        """
        :param width: the width of the grid
        :param height: the height of the grid
        :type width: int
        :type height: int
        :side effect: dig the maze's grid
        :UC: None
        
        """
        pile=Stack()
        x=randint(0,width-1)
        y=randint(0,height-1)
        pile.push((x,y))
        
        while not pile.is_empty() :
            x,y = pile.top()
            l = []
            
            #on trie les voisins
            neigh = neighborhood(x, y, width, height)
            for i in neigh :
                nx,ny = i
                if not self.__grid[ny][nx].check() :
                    l += [(nx,ny)]
                    
            if l == [] :
                pile.pop()
            else :
                rx,ry = l[randint(0,len(l)-1)]
                self.__grid[ry][rx].checked()
                               
                if rx == x-1 :
                    self.__grid[ry][rx].unset_left()
                elif rx == x+1 :
                    self.__grid[ry][rx].unset_right()
                elif ry == y-1 :
                    self.__grid[ry][rx].unset_top()
                elif ry == y+1 :
                    self.__grid[ry][rx].unset_bottom()  
                pile.push((rx,ry))  
        
    def writer(self,stream):
        """
        :param stream: a file
        :type stream: str
        :side effect: write the maze structure in a .txt file
        :UC: none
        """
        fichier = open(stream, "w")
        fichier.write(self.__width)
        fichier.write(self.__height)
        for line in self.__grid_txt :        
            fichier.write(line+"\n")
        fichier.close()
    
    def reader(self,stream):
        """
        :param stream: a file
        :type stream: str
        :side effect: read a file and create the grid corresponding to it
        :UC: none
        
        """
        with open(stream,"r") as entree :
            lines = entree.readlines()
        entree.close()
        width = lines[0]
        height = lines[1]
        grid = grid(width,height)
        y=0
        for i in lines[2:] :
            x=0
            if '+' in i :
                for elmnt in i :
                    if elmnt ==  ' ' :
                        grid[y][x].unset_bottom()
                        x+=1
                    elif elmnt == '-' :
                        x+=1
            else :
                prec=''
                for elmnt in i :
                    if elmnt ==  ' ' and prec == ' ' :
                        grid[y][x].unset_right()
                    
                    prec = elmnt
                y+=1

    def miner_ajustement(self,width,height): #cette fonction ajuste les cellules avec leurs voisines
        """
        :param width: the width of the grid
        :param height: the height of the grid
        :type width: int
        :type height: int
        :side effect: tunes cells together
        :UC: None
        """
        y=0
        for i in self.__grid:
            x=0
            for elmnt in i :
                if x==0 and y==0 :
                    elmnt_right = self.__grid[y][x+1]
                    elmnt_bottom = self.__grid[y+1][x]
                    
                    if not elmnt.is_right():
                        elmnt_right.unset_left()
                    elif not elmnt.is_bottom():
                        elmnt_bottom.unset_top()
                        
                elif x==0 and y== height-1 :
                    elmnt_top = self.__grid[y-1][x]
                    elmnt_right = self.__grid[y][x+1]
                    
                    if not elmnt.is_top():
                        elmnt_top.unset_bottom()
                    elif not elmnt.is_right():
                        elmnt_right.unset_left()
                        
                elif x==width-1 and y==height-1 :
                    elmnt_top = self.__grid[y-1][x]
                    elmnt_left = self.__grid[y][x-1]
                    
                    if not elmnt.is_top():
                        elmnt_top.unset_bottom()
                    elif not elmnt.is_left():
                        elmnt_left.unset_right()
                        
                elif x==width-1 and y == 0 :
                    elmnt_bottom = self.__grid[y+1][x]
                    elmnt_left = self.__grid[y][x-1]
                    
                    if not elmnt.is_bottom():
                        elmnt_bottom.unset_top()
                    elif not elmnt.is_left():
                        elmnt_left.unset_right()
                        
                elif x==0 and y!=0 and y!=height-1:
                    elmnt_top = self.__grid[y-1][x]
                    elmnt_right = self.__grid[y][x+1]
                    elmnt_bottom = self.__grid[y+1][x]
                    
                    if not elmnt.is_top():
                        elmnt_top.unset_bottom()
                    elif not elmnt.is_right():
                        elmnt_right.unset_left()
                    elif not elmnt.is_bottom():
                        elmnt_bottom.unset_top()
                        
                elif x == width-1 and y !=0 and y!=height-1 :
                    elmnt_top = self.__grid[y-1][x]
                    elmnt_left = self.__grid[y][x-1]
                    elmnt_bottom = self.__grid[y+1][x]
                    
                    if not elmnt.is_top():
                        elmnt_top.unset_bottom()
                    elif not elmnt.is_bottom():
                        elmnt_bottom.unset_top()
                    elif not elmnt.is_left():
                        elmnt_left.unset_right()
                        
                elif x!=0 and x!=width-1 and y==0 :
                    elmnt_right = self.__grid[y][x+1]
                    elmnt_left = self.__grid[y][x-1]
                    elmnt_bottom = self.__grid[y+1][x]
                    
                    if not elmnt.is_right():
                        elmnt_right.unset_left()
                    elif not elmnt.is_left():
                        elmnt_left.unset_right()
                    elif not elmnt.is_bottom():
                        elmnt_bottom.unset_top()
                        
                elif x!=0 and y==height-1 :
                    elmnt_top = self.__grid[y-1][x]
                    elmnt_right = self.__grid[y][x+1]
                    elmnt_left = self.__grid[y][x-1]
                    
                    if not elmnt.is_top():
                        elmnt_top.unset_bottom()
                    elif not elmnt.is_right():
                        elmnt_right.unset_left()
                    elif not elmnt.is_left():
                        elmnt_left.unset_right()   
                else :
                    elmnt_top = self.__grid[y-1][x]
                    elmnt_bottom = self.__grid[y+1][x]
                    elmnt_left = self.__grid[y][x-1]
                    elmnt_right = self.__grid[y][x+1]
                    
                    if not elmnt.is_top():
                        elmnt_top.unset_bottom()
                    elif not elmnt.is_right():
                        elmnt_right.unset_left()
                    elif not elmnt.is_bottom():
                        elmnt_bottom.unset_top()
                    elif not elmnt.is_left():
                        elmnt_left.unset_right()
                x+=1
            y+=1
            
    def draw(self):
        """
        :return: draws the grid in a txt file
        :rtype: list
        :UC: none
        
        """
        self.__grid_txt= []
        cpt_line=0
        for line in self.__grid:
            self.__grid_txt+=[""]*2
            cpt_line=len(self.__grid_txt)-1
            for elmnt in line :
                if elmnt.is_top() :
                    self.__grid_txt[cpt_line-1] += '+-'
                else :
                    self.__grid_txt[cpt_line-1] += '+ '
                
                if elmnt.is_left() :
                    self.__grid_txt[cpt_line] += '| '
                else :
                    self.__grid_txt[cpt_line] += '  '
        
        self.__grid_txt[0]=("+-"*self.__width)
        self.__grid_txt+=[("+-"*self.__width)]
        x=0
        for finishedLine in self.__grid_txt :
            if "+" in finishedLine :
                self.__grid_txt[x] = "+" + self.__grid_txt[x][1:] + "+"
            else :
                self.__grid_txt[x] = "|" + self.__grid_txt[x][1:] + "|"
            x+=1
        return self.__grid_txt
        
##        cpt = 0
##        x = 0
##        y = 0
##        #on set la liste
##        l=[("+-"*width+"+"), (['']*(height*2 - 1)), ("+-"*width+"+")]
##        
##        for lines in self.__grid :
##            cpt += 2*y-1
##            x=0
##            #on dessine que les cellules impaires 
##            if y%2==0 :
##                for elmnt in lines :
##                    #elmnt = une cellule
##                    if x%2==0 : 
##                        # attention si c'est un bord !
##                        if x=0 and y=0 :
##                            elmnt_bottom = self.__grid[y+1][x]
##                            elmnt_right = self.__grid[y][x+1]
##                            l[cpt-1] += '+-'
##                            l[cpt]+= '| '
##                            if
##                            l[cpt+1]+=
##                        elif x=0 and y= height :
##                            
##                        elif x=width and y=height :
##                            elmnt_top = self.__grid[y-1][x]
##                            elmnt_left = self.__grid[y][x-1]
##                            
##                        elif x=width and y = 0 :
##                            
##                        elif x=0 and y!=0 :
##                            
##                        elif x = widht and y !=0 :
##                            
##                        elif x!=0 and y=0 :
##                            
##                        elif x!=0 and y=height :
##                           
##                        #maintenant on gère le centre
##                        else :
##                            elmnt_top = self.__grid[y-1][x]
##                            elmnt_bottom = self.__grid[y+1][x]
##                            elmnt_left = self.__grid[y][x-1]
##                            elmnt_right = self.__grid[y][x+1]
##                            
##                            if elmnt.is_top() and elmnt_top.is_bottom() :
##                                l[cpt-1] += '+-'
##                            else :
##                                l[cpt-1] += '+ '
##                                     
##                            if elmnt.is_bottom and elmnt_bottom.is_top() :
##                                l[cpt+1] += '+-'
##                            else :
##                                l[cpt+1] += '+ '
##                                
##                            if elmnt.is_left() and elmnt_left.is_right() :
##                                l[cpt] += '|'
##                            else :
##                                l[cpt] += ' '
##                                
##                            l[cpt] += ' '    
##                                
##                            if elmnt.is_right() and elmnt_right.is_left() :
##                                l[cpt] += '|'
##                            else :
##                                l[cpt] += ' '
##                    else :
##                        #on fait le bord du haut impair
##                    x+=1
##            else :
##                #faire la ligne y impair
##            y+=1        
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
