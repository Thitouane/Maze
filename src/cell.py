#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cell` module

:author: HELLE Thitouane, TALEB-AHMED Hacene

:date: november 2018


"""
from random import randint  

class Cell():
    
    def __init__(self):
        """
        :return: a new hidden cell of a maze's grid.
        :rtype: Cell
        :UC: none
        :Examples:

        >>> cel = Cell()
        >>> cel.check()
        False
        >>> cel.checked()
        >>> cel.check()
        True
        >>> cel.is_top()
        True
        >>>cel.is_right()
        True
        >>>cel.is_left()
        True
        >>>cel.is_bottom()
        True
        """
        self.__check = False
        self.__check_txt = False
        
        self.__top = True
        self.__right = True
        self.__bottom = True
        self.__left = True
    
##    def alea_cell(self):
##        """
##        """
##        alea = randint(0,1)
##        if alea == 0 :
##            self.__top = False
##        else :
##            self.__top = True
##        
##        alea = randint(0,1)
##        if alea == 0 :
##            self.__right = False
##        else :
##            self.__right = True
##        
##        alea = randint(0,1)
##        if alea == 0 :
##            self.__bottom = False
##        else :
##            self.__bottom = True
##        
##        alea = randint(0,1)
##        if alea == 0 :
##            self.__left = False
##        else :
##            self.__left = True
        
    def is_top(self) :
        """
        :return: True if case got a wall at the top, false otherwise
        :rtype: bool
        :UC: none

        """
        return self.__top
    
    def is_right(self) :
        """
        :return: True if case got a wall at the right, false otherwise
        :rtype: bool
        :UC: none
        
        """
        return self.__right
    
    def is_bottom(self) :
        """
        :return: True if case got a wall at the bottom, false otherwise
        :rtype: bool
        :UC: none
        
        """
        return self.__bottom
    
    def is_left(self) :
        """
        :return: True if case got a wall at the left, false otherwise
        :rtype: bool
        :UC: none
        
        """
        return self.__left
    
    def unset_top(self):
        """
        :return: None
        :side effect: delete the top wall
        :UC: None
        >>> cel.is_top()
        True
        >>>cel.unset_top()
        >>>cel.is_top()
        False
        """
        self.__top = False
        
    def unset_right(self):
        """
        :return: None
        :side effect: delete the right wall
        :UC: None
        >>>cel.is_right()
        True
        >>>cel.unset_right()
        >>>cel.is_right()
        False
        """

        self.__right = False
    
    def unset_bottom(self):
        """
        :return: None
        :side effect: delete the bottom wall
        :UC: None
        >>>cel.is_bottom()
        True
        >>>cel.unset_bottom()
        >>>cel.is_bottom()
        False
        """
        self.__bottom = False
    
    def unset_left(self):
        """
        :return: None
        :side effect: delete the left wall
        :UC: None
        >>>cel.is_left()
        True
        >>>cel.unset_left()
        >>>cel.is_left()
        False
        """
        self.__left = False
    
    def checked(self):
        """
        :return: none
        :side effect: put a check on the cell
        :UC: none
        >>> cel = Cell()
        >>> cel.check()
        False
        >>> cel.checked()
        >>> cel.check()
        True
        """
        self.__check = True
    
    def check(self):
        """
        :return: True if someone has passed overe there, False otherwise
        :rtype: Cell
        :UC: none
        >>> cel = Cell()
        >>> cel.check()
        False
        >>> cel.checked()
        >>> cel.check()
        True
        """
        return self.__check
           
    def checked_txt(self):
        """
        :return: none
        :side effect: put a check on the cell
        :UC: none
        >>> cel = Cell()
        >>> cel.check()
        False
        >>> cel.checked()
        >>> cel.check()
        True
        """
        self.__check_txt = True
    
    def check_txt(self):
        """
        :return: True if someone has passed overe there, False otherwise
        :rtype: Cell
        :UC: none
        >>> cel = Cell()
        >>> cel.check()
        False
        >>> cel.checked()
        >>> cel.check()
        True
        """
        return self.__check_txt
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
