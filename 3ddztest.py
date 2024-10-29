import time
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return points

def opengl_line(x0, y0, x1, y1):
    glBegin(GL_LINES)
    glVertex2i(x0, y0)
    glVertex2i(x1, y1)
    glEnd()

def measure_bresenham():
    start = time.time()
    points = bresenham_line(0, 0, 999999, 999999)  # Отрезок длиной 1 миллион пикселей
    end = time.time()
    print(f"Брезенхем: {end - start} секунд, {len(points)} пикселей отрисовано.")

def measure_opengl():
    start = time.time()
    glutInit(sys.argv)
    glutCreateWindow('OpenGL Line')
    glClear(GL_COLOR_BUFFER_BIT)
    opengl_line(0, 0, 999999, 999999)  # Отрезок длиной 1 миллион пикселей
    glFlush()
    end = time.time()
    print(f"OpenGL: {end - start} секунд.")

if __name__ == "__main__":
    print("Запуск теста Брезенхема:")
    measure_bresenham()

    print("Запуск теста OpenGL:")
    measure_opengl()

