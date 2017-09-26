# -*- coding: utf-8 -*-
from solid import *
import numpy as num
import time

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def main():
    w, h = 1300, 700
    window = GraphWin("window", w, h, autoflush=False)
    window.setBackground(color_rgb(255, 255, 255))

    solid_vertices = [[100, 200, 10],
                      [150, 150, 10],
                      [150, 80, 10],
                      [220, 80, 10],
                      [270, 30, 10],
                      [320, 80, 10],
                      [390, 80, 10],
                      [390, 150, 10],
                      [440, 200, 10],
                      [390, 250, 10],
                      [390, 320, 10],
                      [320, 320, 10],
                      [270, 370, 10],
                      [220, 320, 10],
                      [150, 320, 10],
                      [150, 250, 10],
                      [100, 200, 50],
                      [150, 150, 50],
                      [150, 80, 50],
                      [220, 80, 50],
                      [270, 30, 50],
                      [320, 80, 50],
                      [390, 80, 50],
                      [390, 150, 50],
                      [440, 200, 50],
                      [390, 250, 50],
                      [390, 320, 50],
                      [320, 320, 50],
                      [270, 370, 50],
                      [220, 320, 50],
                      [150, 320, 50],
                      [150, 250, 50]]

    star = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11],
            [11, 12], [12, 13], [13, 14], [14, 15], [15, 0], [0, 16], [1, 17], [2, 18], [3, 19],
            [4, 20], [5, 21], [6, 22], [7, 23], [8, 24], [9, 25], [10, 26], [11, 27], [12, 28], [13, 29],
            [14, 30], [15, 31], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22],
            [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 16]]

    faces = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
              [0, 16, 17, 1],
              [1, 17, 18, 2],
              [2, 18, 19, 3],
              [3, 19, 20, 4],
              [4, 20, 21, 5],
              [5, 21, 22, 6],
              [6, 22, 23, 7],
              [7, 23, 24, 8],
              [8, 24, 25, 9],
              [9, 25, 26, 10],
              [10, 26, 27, 11],
              [11, 27, 28, 12],
              [12, 28, 29, 13],
              [13, 29, 30, 14],
              [14, 30, 31, 15],
              [15, 31, 16, 0],
              [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]

    solid = Solid()
    solid.add_vertices(num.array(solid_vertices))
    solid.add_edges(star)

    solid.scale(1, 1, 6)
    solid.translation(650, 120, 0)

    solid.rot_x(0.7)
    #solid.rot_y(0.4)
    #solid.rot_z(0.5)

    #solid.isometric_projection(0.5, 0.5)

    #solid.oblique(0.5, 13 * 5)

    #solid.perspective(100 + 10 * 13)

    solid.paint_points(window)
    solid.draw(window, 0.05)
    solid.paint(faces, window)
    update(60)

    active = True
    while active:
        anwser = input("Digite um numero de 0 a 31 para destacar um vértice, ou digite S/N para sair: ")
        if anwser != "s" or "n":
            point = anwser
        elif anwser == "s":
            active = False

        pt = Circle(Point(solid.vertices[point][0], solid.vertices[point][1]), 4)
        pt.setFill("red")
        pt.draw(window)
        update(60)
        time.sleep(0.2)
        pt.undraw()
        update(60)

    window.getMouse()
    window.close()
main()
