#!/usr/bin/env python3

import pygame
from pygame.locals import *
from pygame import mouse
import numpy as np


"""
    Used to update user inputs.
"""

map = """* * * * * * * *
*             *
*             *
*             *
***************"""


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
    def __init__(self, sld_name):
        self.name = sld_name
        self.render()

    def change_name(self, sld_name):
        self.name = sld_name

    def change_size(self, sld_size):
        if type(sld_size) == tuple:
            self.size = sld_size

    def present_slide_name(self):
        print(self.name)

    def render(self):
        # rows = map.split("\n")
        # split_rows = [row.split() for row in rows]

        # max_len = max(len(r) for r in split_rows)
        # padded_rows = [r + [" "] * (max_len - len(r)) for r in split_rows]

        # array = np.array(padded_rows, dtype=str)
        # print(array)
        rows = map.split("\n")
        array = np.array([list(row) for row in rows], dtype=str)
        print(array)


"""
    An left click input
"""


class LeftClickInput(Input):
    def __init__(self):
        Input.__init__(self)

        self.click_code = 1
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
        if event.type == MOUSEBUTTONDOWN and event.button == self.click_code:
            self.last_input = self.input
            self.input = mouse.get_pos()
            print(self.input)


class ProtoSlide(Slide):
    def __init__(self):
        Slide.__init__(self, "Prototype Scene")
