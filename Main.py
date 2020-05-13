from PyQt5.QtWidgets import QApplication, QLabel
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices = np.array(
    [
        [0.5, 0, 0],
        [0.1, 0, 0]
    ]
)

print(vertices)


def DrawPoints():
    glBegin(GL_POINTS)
    for vertex in vertices:
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw functions here

        DrawPoints()



        pygame.display.flip()
        pygame.time.wait(10)


main()
