#!/usr/bin/env python

# Intermediate Axis Theorem Simulator -> Tbar
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import GREEN3F
from utils.constants import BLUE3F

from utils.constants import DEFAULT_DELAY

from utils.constants import GRAPH_INTERVAL
from utils.constants import GRAPH_POINTS

from utils.classes.Cylinder import Cylinder
from utils.classes.Axes import Axes

# Class
# ----------------------------------------------------------------------------

class Tbar:

    def __init__(self, size=3, pos=(0, 0, 0), angvel=(4, .1, .1)):

        self.size = size

        self.initial_angvel = np.array(angvel, dtype=np.float)
        self.angvel = self.initial_angvel.copy()
        self.angvels = [self.initial_angvel.copy()]
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

        self.cm = np.array((-(self.axis.height / 5 + 2 * self.handle.radius / 5), 0, 0), dtype=np.float)

        self.handle_relpos = self.handle.pos - self.cm
        self.axis_relpos = self.axis.pos - self.cm

        self.axes = Axes(pos=self.cm)

        self.graph_count = 0
        self.angvels_count = 1

        self._compute_moment_inertia()

    """
    Tbar.render()
        computes the new velocities and renders all the components (handle, axis, and axes)
    """

    def render(self):

        self._compute_angacc()
        self._compute_angvel()
        self._compute_rotation()

        self.handle.render(self.cm, self.handle_relpos)
        self.axis.render(self.cm, self.axis_relpos)
        self.axes.render()

    """
    Tbar._compute_angacc()
        computes the new angular acceleration based on Euler's equations
    """

    def _compute_angacc(self):

        self.angacc[0] = ((self.moment_inertia[1] - self.moment_inertia[2])
                          * self.angvel[1] * self.angvel[2] / self.moment_inertia[0])

        self.angacc[1] = ((self.moment_inertia[2] - self.moment_inertia[0])
                          * self.angvel[2] * self.angvel[0] / self.moment_inertia[1])

        self.angacc[2] = ((self.moment_inertia[0] - self.moment_inertia[1])
                          * self.angvel[0] * self.angvel[1] / self.moment_inertia[2])

    """
    Tbar._compute_angvel()
        computes the new angular velocity based on the angular acceleration
        and appends it to the plot
    """

    def _compute_angvel(self):

        for axis in range(3):
            self.angvel[axis] += self.angacc[axis] * (1/DEFAULT_DELAY)

        if self.graph_count == GRAPH_INTERVAL:
            self.graph_count = 0
            self.angvels_count += 1

            self.angvels.append(self.angvel.copy())

            if self.angvels_count >= GRAPH_POINTS:
                del self.angvels[0]

        self.graph_count += 1

    """
    Tbar._compute_rotation()
        rotates the tbar based on the angular velocity
    """

    def _compute_rotation(self):

        angx, angy, angz = self.angvel * (1/DEFAULT_DELAY) * (180/np.pi)

        glRotate(angx, 1, 0, 0)
        glRotate(angy, 0, 1, 0)
        glRotate(angz, 0, 0, 1)

    """
    Tbar._compute_moment_inertia()
        computes the moment of inertia of the tbar
    """

    def _compute_moment_inertia(self):

        # h -> v
        # 0 -> 2
        # 1 -> 0
        # 2 -> 1

        # distance between center of mass of the handle and the total object
        self.cm_distance = self.cm[0]

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

