from PyQt5.QtWidgets import QApplication, QLabel
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

vertices = np.array(
    [
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5]
    ]
)

print(type(vertices))


def RotateX(M, angle):
    rotation = np.array(
        [
            [1, 0, 0],
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle), math.cos(angle)]
        ]
    )
    return M.dot(rotation)


def RotateY(M, angle):
    rotation = np.array(
        [
            [math.cos(angle), 0, -math.sin(angle)],
            [0, 1, 0],
            [math.sin(angle), 0, math.cos(angle)]
        ]
    )
    return M.dot(rotation)


def RotateZ(M, angle):
    rotation = np.array(
        [
            [math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]
        ]
    )
    return M.dot(rotation)


def ProjectOrtho(M):

    M = np.atleast_2d(M)

    projection = np.array(
        [
            [1, 0, 0],
            [0, 1, 0]
        ]
    )

    return M.dot(projection.T)




def DrawPoints(angle):
    glBegin(GL_POINTS)
    for vertex in vertices:
        v = RotateX(vertex.transpose(), angle)
        v = RotateY(v, angle)
        v = RotateZ(v, angle)
        v = ProjectOrtho(v)
        glVertex2f(v[0][0], v[0][1])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw functions here

        DrawPoints(angle)

        pygame.display.flip()
        pygame.time.wait(10)

        angle = angle + 0.01


main()
