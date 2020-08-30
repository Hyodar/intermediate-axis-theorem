#!/usr/bin/env python

# Intermediate Axis Theorem Simulator -> Cylinder
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import math
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

from utils.constants import DEFAULT_DELAY
from utils.classes.Axes import Axes


# Draw Cylinder
# from: https://stackoverflow.com/questions/41912261/pyopengl-creating-a-cylinder-without-using-glucylinder-function
# ----------------------------------------------------------------------------

def draw_cylinder(radius, height, num_slices):
    r = radius
    h = height
    n = float(num_slices)

    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)

    glBegin(GL_TRIANGLE_FAN)#drawing the back circle
    glColor(1, 0, 0)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)#drawing the front circle
    glColor(0, 0, 1)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)#draw the tube
    glColor(0, 1, 0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
        glVertex(x, y, -z)
    glEnd()


# Class
# ----------------------------------------------------------------------------


class Cylinder:

    def __init__(self, pos, rotation, height, radius, mass):

        self.rotation = np.array(rotation, dtype=np.float64)
        self.pos = np.array(pos, dtype=np.float64)
        self.height = height
        self.radius = radius
        self.mass = mass

        self.slices = 10

    """
    Cylinder.render()
        renders the cylinder
    """

    def render(self):
        glPushMatrix()
        glTranslate(*self.pos)

        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)

        draw_cylinder(self.radius, self.height, self.slices)

        glPopMatrix()

