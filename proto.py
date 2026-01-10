#!/usr/bin/env python3

import pygame
from pygame.locals import *
from pygame import mouse

"""
    Used to update user inputs.
"""
class Input:
    def __init__(self):
        self.name = "__name__"
    def change_name(self, in_name):
        self.name = in_name
    def update(self, event):
        pass

"""
    A scene in the game.
"""
class Slide:
    def __init__(self):
        self.name = "slide_name"
        self.size = (100, 100)
    def change_name(self, sld_name):
        self.name = sld_name
    def change_size(self, sld_size):
        if type(sld_size) == tuple:
            self.size = sld_size
    def present_slide_name(self):
        print(self.name)

"""
    An left click input
"""
class LeftClickInput(Input):
    def __init__(self):
        Input.__init__(self)
        
        self.input = (0, 0)
        self.prev_input = (0, 0)
        
        self.change_name("__click__")
        
    # Return true if the input has changed since the last time you asked.
    def has_input_changed(self):
    	input_changed = self.input != self.prev_input
    	self.prev_input = self.input 
    	return input_changed
    	
    # If the left button was clicked
    # make last input variable hold the new input
    # and replace the input variable with the current click
    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.last_input = self.input
            self.input = mouse.get_pos()

class ProtoSlide(Slide):
    def __init__(self):
        Slide.__init__(self)
        self.change_name("Prototype Scene")
        self.change_size((200, 200))
        
