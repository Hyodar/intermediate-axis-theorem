#!/usr/bin/python

# Intermediate Axis Theorem Simulator -> Screen
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import sys

import numpy as np
import pygame as pyg

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import GRAPH_POINTS

from utils.constants import WINDOW_SIZE

from utils.constants import YELLOW3F
from utils.constants import BLACK3F
from utils.constants import GREEN3F
from utils.constants import BLUE3F

# Class
# ----------------------------------------------------------------------------

class Screen:

    def __init__(self, display, tbar, window_size=WINDOW_SIZE):

        # display
        self.display = display
        self.window_size = window_size

        # menu
        self.menu_h = 1
        self.menu_padding = .2

        # graph
        self.colors = (YELLOW3F, GREEN3F, BLUE3F)
        self.graph_ratio = ((self.menu_h/2 - self.menu_padding) 
                            / (tbar.initial_angvel[0] * tbar.moment_inertia[0] + 3))
        self.time_interval = 2 * (1 - self.menu_padding) / GRAPH_POINTS
        self.tbar = tbar

    """
    Screen.render()
        renders both the graph and the black overlay
    """

    def render(self):
        
        glPushMatrix()
        glLoadIdentity()

        self._render_graph()
        self._render_menu()

        glPopMatrix()

    """
    Screen._render_menu()
        renders the black overlay using the properties menu_h and menu_padding
    """

    def _render_menu(self):

        glColor4f(*BLACK3F, .25)
        glBegin(GL_POLYGON)
        glVertex3f(-1, -1, 0)
        glVertex3f(1, -1, 0)
        glVertex3f(1, -1 + self.menu_h, 0)
        glVertex3f(-1, -1 + self.menu_h, 0)
        glEnd()

    """
    Screen._render_graph()
        plots the tbar's angular momentum
    """

    def _render_graph(self):

        glColor3f(*BLACK3F)

        glBegin(GL_LINES)
        # vertical line
        glVertex3f(-1 + self.menu_padding, -1.1 + self.menu_padding, 0)
        glVertex3f(-1 + self.menu_padding, -self.menu_padding +.1, 0)

        # horizontal line
        glVertex3f(-1 + self.menu_padding, -.5, 0)
        glVertex3f(1 - self.menu_padding, -.5, 0)
        glEnd()

        self._render_graph_info()
        
        for axis in range(3):
            time = 0

            glBegin(GL_LINE_STRIP)

            glColor3f(*self.colors[axis])
            for angvel in self.tbar.angvels:
                glVertex3f(-1 + self.menu_padding + time,
                          -.5 + angvel[axis] * self.graph_ratio * self.tbar.moment_inertia[axis],
                           0)
                time += self.time_interval

            glEnd()

    """
    Screen._render_graph_info()
        renders the title and legend of the plot
    """

    def _render_graph_info(self):

        self._render_text((-1 + self.menu_padding + .05, -.1), "Momentos angulares")

        glBegin(GL_LINES)

        glColor3f(*YELLOW3F)
        glVertex3f(.85, -.1, 0)
        glVertex3f(.9, -.1, 0)

        glColor3f(*GREEN3F)
        glVertex3f(.85, -.17, 0)
        glVertex3f(.9, -.17, 0)

        glColor3f(*BLUE3F)
        glVertex3f(.85, -.23, 0)
        glVertex3f(.9, -.23, 0)

        glEnd()

        self._render_text((.92, -.11), "X")
        self._render_text((.92, -.18), "Y")
        self._render_text((.92, -.25), "Z")

    """
    Screen._render_text(pos:tuple, text:str[, color:tuple])
        renders bitmap text
    """
        
    def _render_text(self, pos, text, color=BLACK3F):
        
        glColor(*color)
        glRasterPos2f(pos[0], pos[1])
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))
        


