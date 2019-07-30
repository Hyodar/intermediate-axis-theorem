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

from utils.constants import DEFAULT_DELAY

from utils.classes.Cylinder import Cylinder

# Class
# ----------------------------------------------------------------------------


class Tbar:

    def __init__(self, size, pos, rotation, angvel):

        self.size = size
        self.rotation = np.array(rotation, dtype=np.float)

        self.angvel = np.array(angvel, dtype=np.float)
        self.angacc = np.array((0., 0., 0.), dtype=np.float)

        self.pos = np.array(pos, dtype=np.float)

        # positions and rotations relative to the tbar
        self.handle = Cylinder(rotation=(90., 0., 0.),
                               pos=(0, 3/8, 0),
                               radius=1/8 * self.size,
                               height=(3/4) * self.size,
                               mass=4 * self.size,
                               color=BLUE3F)

        self.axis = Cylinder(rotation=(0., 90., 0.),
                             pos=(-(3/8 + self.handle.radius), 0, 0),
                             radius=1/12 * self.size,
                             height=3/8 * self.size,
                             mass=1 * self.size,
                             color=GREEN3F)

        # mockup - TODO
        #self.cm = np.array((-self.handle.radius, 0, self.handle.radius), dtype=np.float)
        self.cm = np.array((0, 0, 0), dtype=np.float)

        self.handle_relpos = self.handle.pos - self.cm
        self.axis_relpos = self.axis.pos - self.cm

        #self.rotate(rotation)
        #self.translate(pos)

        self._compute_moment_inertia()

    def render(self):

        #self.rotate(self.rotation)
        #self.translate(self.pos)

        
        self._compute_angacc()
        self._compute_angvel()
        self._compute_rotation()

        self.handle.render(self.rotation, self.cm, self.pos, self.handle_relpos)
        self.axis.render(self.rotation, self.cm, self.pos, self.axis_relpos)

    def _compute_angacc(self):
        # 2 -> 0
        # 0 -> 1
        # 1 -> 2        
        
        self.angacc[1] = (self.moment_inertia[2] - self.moment_inertia[0]) * self.angvel[2] * self.angvel[0] / self.moment_inertia[1]
        self.angacc[2] = (self.moment_inertia[0] - self.moment_inertia[1]) * self.angvel[0] * self.angvel[1] / self.moment_inertia[2]
        self.angacc[0] = (self.moment_inertia[1] - self.moment_inertia[2]) * self.angvel[1] * self.angvel[2] / self.moment_inertia[0]
        """
        self.angacc[0] = (self.moment_inertia[1] - self.moment_inertia[2]) * self.angvel[1] * self.angvel[2] / self.moment_inertia[0]
        self.angacc[1] = (self.moment_inertia[2] - self.moment_inertia[0]) * self.angvel[2] * self.angvel[0] / self.moment_inertia[1]
        self.angacc[2] = (self.moment_inertia[0] - self.moment_inertia[1]) * self.angvel[0] * self.angvel[1] / self.moment_inertia[2]
        """


    def _compute_angvel(self):
        
        for axis in range(2):
            self.angvel[axis] += self.angacc[axis] * (1 / DEFAULT_DELAY)

    def _compute_rotation(self):

        for axis in range(2):
            self.rotation[axis] += self.angvel[axis] * (1 / DEFAULT_DELAY)

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

        self.moment_inertia = np.array((ixx, iyy, izz), dtype=np.float)
