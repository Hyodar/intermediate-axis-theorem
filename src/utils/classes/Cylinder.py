#!/usr/bin/python

# Intermediate Axis Theorem Simulator -> Cylinder
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import numpy as np
import pygame as pyg

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import DEFAULT_DELAY
from utils.classes.Axes import Axes


# Class
# ----------------------------------------------------------------------------


class Cylinder:

    def __init__(self, pos, rotation, color, height, radius, mass):

        self.rotation = np.array(rotation, dtype=np.float)
        self.pos = np.array(pos, dtype=np.float)
        self.height = height
        self.radius = radius
        self.color = color
        self.mass = mass

        self.slices = 50
        self.stacks = 50

    def render(self, tbar_angle, tbar_cm, tbar_pos, rel_pos, rot_axis_list):

        glPushMatrix()
        glTranslate(*tbar_cm)
        
        """
        glRotatef(tbar_angle[0], 1, 0, 0)
        glRotatef(tbar_angle[1], 0, 1, 0)
        glRotatef(tbar_angle[2], 0, 0, 1)
        """
        
        #print('------')
        #print(len(rot_axis_list))
        #print(len(tbar_angle))
        #print('------')

        #rot_axis = (normalize(rot_axis_list[0]), normalize(rot_axis_list[1]), normalize(rot_axis_list[2]))
        #rot_axis = ((1,0,0),(0,1,0),(0,0,1))

        #for i in range(len(rot_axis_list)):
        #    glRotate(180 * (1/DEFAULT_DELAY) * tbar_angle[i][0] / np.pi, *rot_axis_list[i-1][0])
        #    glRotate(180 * (1/DEFAULT_DELAY) * tbar_angle[i][1] / np.pi, *rot_axis_list[i-1][1])
        #    glRotate(180 * (1/DEFAULT_DELAY) * tbar_angle[i][2] / np.pi, *rot_axis_list[i-1][2])

        glTranslate(*rel_pos)

        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)

        glColor3f(*self.color)
        glutWireCylinder(self.radius, self.height, self.slices, self.stacks)

        glTranslate(*(-rel_pos))
        glTranslate(*(-tbar_cm))

        glPopMatrix()

