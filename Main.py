from PyQt5.QtWidgets import QApplication, QLabel
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math


a_file = open("CubeTriangulated.obj")
lines = a_file.readlines()


def OpenObj():
    ListOfVertices = []

    for line in lines:
        if 'v' in line:
            if 'vt' not in line:
                if 'vn' not in line:
                    if 'Blender' not in line:
                        vertex = line.replace('v', '')
                        val = vertex.split()
                        ListOfVertices.append(np.array([float(val[0]), float(val[1]), float(val[2])]))
    print(val[0])
    return np.asarray(ListOfVertices)


def FacesOfObj():

    ListOfFaces = []

    for line in lines:
        if 'f' in line:
            if 's' not in line:
                edge = line.replace('f', '')
                edges = edge.split()
                # print(edges[1][0])
                ListOfFaces.append(np.array([int(edges[0][0]), int(edges[1][0]), int(edges[2][0])]))
    print(edges[0][0])
    return np.asarray(ListOfFaces)


vertices = OpenObj()
faces = FacesOfObj()
#print(len(faces))


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
            [1 / 5, 0, 0],
            [0, 1 / 5, 0]
        ]
    )

    return M.dot(projection.T)


def DrawPoints(angle):
    glBegin(GL_POINTS)
    for vertex in vertices:
        v = RotateX(vertex, angle)
        v = RotateY(v, angle)
        v = RotateZ(v, angle)
        v = ProjectOrtho(v)
        glVertex2f(v[0][0], v[0][1])
    glEnd()

    #for face in faces:
    #    glBegin(GL_LINES)
    #    glVertex2f(0.1, 0)
    #    glVertex2f(0, 0)
    #    glEnd()


    #glBegin(GL_LINES)
    #glVertex3f(0, 0, 0)
    #glVertex3f(0.5, 0.5, -0.5)
    #glEnd()


def main():
    pygame.init()
    pygame.display.set_caption('Maya But Actually Good V.001Alpha')
    display = (600, 600)
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
