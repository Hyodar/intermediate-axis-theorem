#!/usr/bin/python

# Intermediate Axis Theorem Simulator -> Tbar
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import numpy as np
import pygame as pyg

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import GREEN3F
from utils.constants import BLUE3F

from utils.classes.Cylinder import Cylinder

# Class
# ----------------------------------------------------------------------------


class Tbar:

    def __init__(self, size):

        self.size = size

        self.handle = Cylinder(rotation=(0., 90., 0.),
                               pos=(-2/6 * self.size, 1., 0.),
                               radius=.25 * self.size,
                               height=(2/3) * self.size,
                               mass=4 * self.size,
                               color=BLUE3F)

        self.axis = Cylinder(rotation=(-90., 0., 0.),
                             pos=(0., -.25 * self.size, .0),
                             radius=1/6 * self.size,
                             height=1 * self.size,
                             mass=1 * self.size,
                             color=GREEN3F)

        self._compute_moment_inertia()

    def _compute_moment_inertia(self):

        # distance between center of mass of handle and of the total object
        self.cm_distance = - (self.axis.height / 6 + self.handle.radius / 3)

        ixx = ((1 / 2) * (self.handle.mass) * (self.handle.radius ** 2)
               + (self.handle.mass) * self.cm_distance ** 2 + (self.axis.mass / 4) * (self.axis.radius ** 2)
               + (self.axis.mass / 12) * (self.axis.height ** 2)
               + self.axis.mass * (self.axis.height / 2 + self.handle.radius - self.cm_distance))

        iyy = ((1 / 4) * (self.handle.mass) * (self.handle.radius ** 2)
               + (1 / 12) * (self.handle.mass) * (self.handle.height ** 2)
               + self.handle.mass * (self.cm_distance ** 2)
               + (1 / 4) * self.axis.mass * (self.axis.radius ** 2)
               + (1 / 12) * (self.axis.mass) * (self.axis.height ** 2)
               + self.axis.mass * (self.axis.height / 2 + self.handle.radius - self.cm_distance))

        izz = ((1 / 2) * (self.axis.mass) * (self.axis.radius ** 2)
               + (1 / 4) * (self.handle.mass) * (self.handle.radius ** 2)
               + (1 / 12) * (self.handle.mass) * (self.handle.height ** 2))

        self.moment_inertia = np.array((ixx, iyy, izz))

    def render(self):

        self.handle.render()
        self.axis.render()
