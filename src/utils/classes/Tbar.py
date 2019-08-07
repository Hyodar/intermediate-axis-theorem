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
from utils.classes.Axes import Axes

# Class
# ----------------------------------------------------------------------------

plot_t = 0

class Tbar:

    def __init__(self, size, pos, rotation, angvel):

        self.size = size
        self.rotation = np.array(rotation, dtype=np.float)

        self.angvel = np.array(angvel, dtype=np.float)
        self.angacc = np.array((0., 0., 0.), dtype=np.float)

        self.pos = np.array(pos, dtype=np.float)

        # positions and rotations relative to the tbar

        self.handle = Cylinder(rotation=(90., 0., 0.),
                               pos=(0, 0, 0),
                               radius=(1/3) * self.size,
                               height=2 * self.size,
                               mass=(4/3) * self.size,
                               color=BLUE3F)

        self.axis = Cylinder(rotation=(0., 90., 0.),
                             pos=(0, 0, 0),
                             radius=(1/4) * self.size,
                             height=1 * self.size,
                             mass=(1/3) * self.size,
                             color=GREEN3F)

        self.handle.pos[1] = self.axis.height
        self.axis.pos[0] = -(self.axis.height + self.handle.radius)

        # TODO - adaptar ao size
        self.cm = np.array((-1.5, 0, 0), dtype=np.float)

        self.handle_relpos = self.handle.pos - self.cm
        self.axis_relpos = self.axis.pos - self.cm

        self.axes = Axes(pos=self.cm)

        self._compute_moment_inertia()

        self.a = 0

    def render(self):

        self._compute_angacc()
        self._compute_angvel()
        self._compute_rotation()

        self.handle.render(self.cm, self.handle_relpos)
        self.axis.render(self.cm, self.axis_relpos)

    def _compute_angacc(self):

        self.angacc[0] = (self.moment_inertia[1] - self.moment_inertia[2]) * self.angvel[1] * self.angvel[2] / self.moment_inertia[0]
        self.angacc[1] = (self.moment_inertia[2] - self.moment_inertia[0]) * self.angvel[2] * self.angvel[0] / self.moment_inertia[1]
        self.angacc[2] = (self.moment_inertia[0] - self.moment_inertia[1]) * self.angvel[0] * self.angvel[1] / self.moment_inertia[2]

    def _compute_angvel(self):

        with open('test.dat', 'a') as f:
            f.write('{}\t{}\t{}\t{}\n'.format(self.a, *self.angvel))
        
        self.a += 1/DEFAULT_DELAY

        for axis in range(3):
            self.angvel[axis] += self.angacc[axis] * (1/DEFAULT_DELAY)

    def _compute_rotation(self):

        angx, angy, angz = self.angvel * (1/DEFAULT_DELAY) * (180/np.pi)

        glRotate(angx, 1, 0, 0)
        glRotate(angy, 0, 1, 0)
        glRotate(angz, 0, 0, 1)

    def _compute_moment_inertia(self):

        # distance between center of mass of the handle and the total object
        self.cm_distance = - (self.axis.height / 6 + self.handle.radius / 3)

        iyy = ((1 / 2) * (self.handle.mass) * (self.handle.radius ** 2)
               + (self.handle.mass) * self.cm_distance ** 2 + (self.axis.mass / 4) * (self.axis.radius ** 2)
               + (self.axis.mass / 12) * (self.axis.height ** 2)
               + self.axis.mass * (self.axis.height / 2 + self.handle.radius - self.cm_distance))

        izz = ((1 / 4) * (self.handle.mass) * (self.handle.radius ** 2)
               + (1 / 12) * (self.handle.mass) * (self.handle.height ** 2)
               + self.handle.mass * (self.cm_distance ** 2)
               + (1 / 4) * self.axis.mass * (self.axis.radius ** 2)
               + (1 / 12) * (self.axis.mass) * (self.axis.height ** 2)
               + self.axis.mass * (self.axis.height / 2 + self.handle.radius - self.cm_distance))

        ixx = ((1 / 2) * (self.axis.mass) * (self.axis.radius ** 2)
               + (1 / 4) * (self.handle.mass) * (self.handle.radius ** 2)
               + (1 / 12) * (self.handle.mass) * (self.handle.height ** 2))

        self.moment_inertia = np.array((ixx, iyy, izz), dtype=np.float)

