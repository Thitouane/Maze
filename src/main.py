#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`main` module 

:author: ` HELLE Thitouane, TALEB-AHMED Hacène
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2018, november.


"""

from maze import Maze
from random import randint

def main():
    """
    main function for console minesweeper game
    """
    maze = Maze()
    w = maze.get_width()
    h = maze.get_height()
    maze.grid(w,h)
    maze.miner(w,h)
    maze.miner_ajustement(w,h)
    return maze.draw()
    
    
if __name__ == '__main__':
    for i in main() :
        print(i)
    