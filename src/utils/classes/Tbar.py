#!/usr/bin/python

# Intermediate Axis Theorem Simulator -> Tbar
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import numpy as np
import math
import pygame as pyg

import vpython as vp

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


def normalize(vector):
    norm = np.linalg.norm(vector)

    if not norm:
        return vector
    return vector / norm

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

xaxis = vp.arrow(pos=vp.vec(0, 0, 0),
              axis=vp.vec(4, 0, 0),
              shaftwidth=.1,
              color=vp.color.red,
              opacity=.5)

yaxis = vp.arrow(pos=vp.vec(0, 0, 0),
              axis=vp.vec(0, 4, 0),
              shaftwidth=.1,
              color=vp.color.green,
              opacity=.5)

zaxis = vp.arrow(pos=vp.vec(0, 0, 0),
              axis=vp.vec(0, 0, 4),
              shaftwidth=.1,
              color=vp.color.blue,
              opacity=.5)


# ----------------------------------------------------------------------------

"""
rotate_tbar(obj: object, obj_omega: vector, axes: list, dt: float):
    rotates object based on its omega (angular velocity)
"""
    
def rotate_obj(obj, obj_omega, axes, dt):

    # rotation on x, y and z

    #print('')
    #print(obj_omega[0]*dt)

    print()
    print(obj_omega*dt)

    obj.rotate(angle=obj_omega[0] * dt, axis=vp.norm(axes[0].axis), origin=obj.pos)
    obj.rotate(angle=obj_omega[1] * dt, axis=vp.norm(axes[1].axis), origin=obj.pos)
    obj.rotate(angle=obj_omega[2] * dt, axis=vp.norm(axes[2].axis), origin=obj.pos)

    angx, angy, angz = obj_omega*dt*(180/np.pi)

    """
    glRotate(-angz, axes[2].axis.x, axes[2].axis.y, axes[2].axis.z)
    glRotate(angx, axes[0].axis.x, axes[0].axis.y, axes[0].axis.z)
    glRotate(-angy, axes[1].axis.x, axes[1].axis.y, axes[1].axis.z)"""


    print((angx, angy, angz))
    print()

    """
    glRotate(angz, axes[2].axis.x, axes[2].axis.y, axes[2].axis.z)
    glRotate(angy, axes[1].axis.x, axes[1].axis.y, axes[1].axis.z)
    glRotate(angx, axes[0].axis.x, axes[0].axis.y, axes[0].axis.z)"""

    glRotate(angx, 1, 0, 0)
    glRotate(angy, 0, 1, 0)
    glRotate(angz, 0, 0, 1)
   

# ----------------------------------------------------------------------------

"""
update_axis(axes: list, omega: vector, dt: float):
    rotating the vectors and adjusting length to be proportional to omega
"""

def update_axis(axes, obj_omega, dt):
    
    old_axes = axes

    # rotates the three axes using rotate_obj
    for i in range(len(axes)):
        rotate_obj(axes[i], obj_omega, old_axes, dt)
        #print(vp.norm(axes[0].axis))


# ----------------------------------------------------------------------------

class Tbar:

    def __init__(self, size, pos, rotation, angvel):

        self.size = size
        self.rotation = np.array(rotation, dtype=np.float)

        self.angvel = [np.array(angvel, dtype=np.float)]
        self.angacc = np.array((0., 0., 0.), dtype=np.float)

        self.pos = np.array(pos, dtype=np.float)

        self.axis_list = [[np.array((1,0,0), dtype=np.float),
                                   np.array((0,1,0), dtype=np.float),
                                   np.array((0,0,1), dtype=np.float)]]

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

        # mockup - TODO
        self.cm = np.array((-1.5, 0, 0), dtype=np.float)
        #self.cm = np.array((-(self.axis.height / 6 + self.handle.radius / 3), 0, 0), dtype=np.float)
        #self.cm = np.array((0., 0., 0.), dtype=np.float)

        self.handle_relpos = self.handle.pos - self.cm
        self.axis_relpos = self.axis.pos - self.cm

        self.axes = Axes(pos=self.cm)

        self._compute_moment_inertia()

    def render(self):

        #print('')
        self._compute_angacc()
        self._compute_angvel()
        self._compute_rotation()

        # drawing a sphere on the center of mass
        #glTranslate(*(self.cm + np.array((0, 0, 0))))
        #glColor(0., 0., 0.)
        #glutSolidSphere(.3 * self.size, 20, 20)
        #glTranslate(*(-self.cm - np.array((0, 0, 0))))

        angvels = len(self.angvel)

        update_axis([xaxis, yaxis, zaxis], self.angvel[angvels-1], 1/DEFAULT_DELAY)
        
        #axis = [0, 0, 0]
        #axis[0] = np.array((vp.norm(xaxis.axis).x, vp.norm(xaxis.axis).y, vp.norm(xaxis.axis).z), dtype=np.float)
        #axis[1] = np.array((vp.norm(yaxis.axis).x, vp.norm(yaxis.axis).y, vp.norm(yaxis.axis).z), dtype=np.float)
        #axis[2] = np.array((vp.norm(zaxis.axis).x, vp.norm(zaxis.axis).y, vp.norm(zaxis.axis).z), dtype=np.float)
        #self.axis_list.append(axis)

        self.handle.render(self.angvel, self.cm, self.pos, self.handle_relpos, self.axis_list)
        self.axis.render(self.angvel, self.cm, self.pos, self.axis_relpos, self.axis_list)

        """
        rotx = rotation_matrix(-old_axes[0], self.rotation[0])
        roty = rotation_matrix(-old_axes[1], self.rotation[1])
        rotz = rotation_matrix(-old_axes[2], self.rotation[2])

        for i in range(3):        
            self.axis_list[i] = np.dot(rotx, self.axis_list[i])
            self.axis_list[i] = np.dot(roty, self.axis_list[i])                        
            self.axis_list[i] = np.dot(rotz, self.axis_list[i])                    
        print(self.axis_list)
        """

        """rx = m3d.Orientation.new_axis_angle(old_axes[0], self.rotation[0])
        ry = m3d.Orientation.new_axis_angle(old_axes[1], self.rotation[1])
        rz = m3d.Orientation.new_axis_angle(old_axes[2], self.rotation[2])
        v = m3d.Vector(*self.axis_list[i])
        v = v * rx * ry * rz

        self.axis_list[i] = np.array((i for i in v))"""

        #self.axes.render(180*self.rotation/np.pi, self.cm)

    def _compute_angacc(self):
        # v -> o

        # 2 -> 0
        # 0 -> 1
        # 1 -> 2
        """
        self.angacc[1] = (self.moment_inertia[2] - self.moment_inertia[0]) * self.angvel[2] * self.angvel[0] / self.moment_inertia[1]
        self.angacc[2] = (self.moment_inertia[0] - self.moment_inertia[1]) * self.angvel[0] * self.angvel[1] / self.moment_inertia[2]
        self.angacc[0] = (self.moment_inertia[1] - self.moment_inertia[2]) * self.angvel[1] * self.angvel[2] / self.moment_inertia[0]
        """

        angvels = len(self.angvel)
        
        self.angacc[0] = (self.moment_inertia[1] - self.moment_inertia[2]) * self.angvel[angvels-1][1] * self.angvel[angvels-1][2] / self.moment_inertia[0]
        self.angacc[1] = (self.moment_inertia[2] - self.moment_inertia[0]) * self.angvel[angvels-1][2] * self.angvel[angvels-1][0] / self.moment_inertia[1]
        self.angacc[2] = (self.moment_inertia[0] - self.moment_inertia[1]) * self.angvel[angvels-1][0] * self.angvel[angvels-1][1] / self.moment_inertia[2]

        #print('Angacc: {} | {} | {}'.format(*self.angacc))

    def _compute_angvel(self):

        pos = len(self.angvel)
        angvel = np.array((0, 0, 0), dtype=np.float)
        for axis in range(3):
            angvel[axis] = self.angvel[pos-1][axis] + self.angacc[axis] * (1 / DEFAULT_DELAY)
        self.angvel.append(angvel)

        #print('Angvel: {} | {} | {}'.format(*self.angvel))

    def _compute_rotation(self):

        a = 1
        #for axis in range(3):
        #    self.rotation[axis] += self.angvel[axis] * (1 / DEFAULT_DELAY)

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
        #print(self.moment_inertia)

