# -*- coding: utf-8 -*-
from solid import *
from graphics import *
import numpy
import time


def clear_window(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def mouse_click(window, points, vertices):
    click = window.getMouse().clone()
    result = Rectangle(Point(-1, -1), Point(0, 0))
    for i in range(len(points)):
        if ((click.getX() >= points[i][0].x) and (points[i][1].x >= click.getX()) and
                (click.getY() >= points[i][0].y) and (points[i][1].y >= click.getY())):
            pontoAtual = Point(vertices[i][0], vertices[i][1])
            point = Circle(pontoAtual, 6)
            point.setOutline("black")

            point.setFill("red")
            point.draw(window)
            update(60)
            time.sleep(0.1)
            point.undraw()

            update(60)
            point.setFill("yellow")
            point.draw(window)
            update(60)

            return point

    result.draw(window)
    return result


def main():
    w, h = 1300, 700
    window = GraphWin("window", w, h, autoflush=False)
    window.setBackground(color_rgb(255, 255, 255))

    solid_vertices = [[100, 200, 10],
                      [110, 130, 10],
                      [150, 80, 10],
                      [205, 45, 10],
                      [270, 30, 10],
                      [335, 45, 10],
                      [390, 80, 10],
                      [430, 130, 10],
                      [440, 200, 10],
                      [430, 265, 10],
                      [390, 320, 10],
                      [335, 355, 10],
                      [270, 370, 10],
                      [205, 355, 10],
                      [150, 320, 10],
                      [110, 265, 10],
                      [100, 200, 50],
                      [110, 130, 50],
                      [150, 80, 50],
                      [205, 45, 50],
                      [270, 30, 50],
                      [335, 45, 50],
                      [390, 80, 50],
                      [430, 130, 50],
                      [440, 200, 50],
                      [430, 265, 50],
                      [390, 320, 50],
                      [335, 355, 50],
                      [270, 370, 50],
                      [205, 355, 50],
                      [150, 320, 50],
                      [110, 265, 50]]

    star = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11],
            [11, 12], [12, 13], [13, 14], [14, 15], [15, 0], [0, 16], [1, 17], [2, 18], [3, 19],
            [4, 20], [5, 21], [6, 22], [7, 23], [8, 24], [9, 25], [10, 26], [11, 27], [12, 28], [13, 29],
            [14, 30], [15, 31], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22],
            [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 16]]


    active = True
    type = 0
    a = -1

    solid = Solid()
    solid.add_vertices(numpy.array(solid_vertices))
    solid.add_edges(star)

    faces = solid.create_faces()

    subtitle_message = ""
    sub_title = Text(Point(683, 30), subtitle_message)
    solid.print_vertices()
    sub_title.setFace("arial")
    sub_title.setStyle("bold")

    solid.scale(0.5, 0.5, 4)
    solid.translation(450, 120, 0)

    solid.oblique(0.5, 13 * 5)
    solid.scale(1, 1, 6)
    while active:

        type += 1
        a += 1

        axis = [[-1, 0, 1], [0, 1, 0], [1, -1, -1], [0, 1, -1], [-1, 0, 0], [1, -1, 0], [0, 0, -1]]
        if a > len(axis) - 1:
            a = 0
        if type > 6:
            type = 1

        center = solid.get_center()
        aux_vet = solid.vertices.copy()

        solid.translation(-center[0], -center[1], -center[2])

        solid.quaternios_rotation(axis[a])

        solid.translation(center[0], center[1], center[2])

        time.sleep(.8)
        clear_window(window)
        update(60)

        solid.paint(faces, window, type)
        solid.vertices = aux_vet

main()
