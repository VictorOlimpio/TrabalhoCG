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

    active = True
    type = 0
    while active:
        colors = [50, 100, 20]

        solid = Solid()
        solid.add_vertices(numpy.array(solid_vertices))
        solid.add_edges(star)

        solid.scale(1, 1, 6)
        solid.translation(650, 120, 0)

        # message = "Bem Vindo, selecione uma das opções no console do terminal"
        # subtitle_message = ""
        #
        # title = Text(Point(683, 10), message)
        # sub_title = Text(Point(683, 30), subtitle_message)
        #
        # title.setFace("arial")
        # title.setStyle("bold")
        #
        # sub_title.setFace("arial")
        # sub_title.setStyle("bold")

        # title.draw(window)
        # solid.print_vertices()

        # anwser = input("Escolha uma das opções abaixo, ou digite N para sair:\n"
        #                "1- Para uma rotação no eixo x:\n"
        #                "2- Para uma rotação no eixo y:\n"
        #                "3- Para uma rotação no eixo z:\n"
        #                "4- Para uma projeção isométrica:\n"
        #                "5- Para uma projeção obliqua:\n"
        #                "6- Para uma projeção em perspectiva usando um ponto de fuga:\n")
        # if anwser == "n":
        #     active = False
        #
        # if anwser == 1:
        #     clear_window(window)
        #     subtitle_message = "Rotação no eixo X"
        #     sub_title = Text(Point(683, 30), subtitle_message)
        #     sub_title.draw(window)
        #     angle = input("Insira o valor de um angulo")
        #     solid.rot_x(angle)
        #
        # if anwser == 2:
        #     clear_window(window)
        #     subtitle_message = "Rotação no eixo Y"
        #     sub_title = Text(Point(683, 30), subtitle_message)
        #     sub_title.draw(window)
        #     angle = input("Insira o valor de um angulo")
        #     solid.rot_y(angle)
        #
        # if anwser == 3:
        #     clear_window(window)
        #     subtitle_message = "Rotação no eixo Z"
        #     sub_title = Text(Point(683, 30), subtitle_message)
        #     sub_title.draw(window)
        #     angle = input("Insira o valor de um angulo")
        #     solid.rot_z(angle)
        #
        # if anwser == 4:
        #     clear_window(window)
        #     subtitle_message = "Projeção Isométrica com angulo em x 35.26 e em y 45"
        #     sub_title = Text(Point(683, 30), subtitle_message)
        #     sub_title.draw(window)
        #     solid.isometric_projection(35.26, 45)
        #
        #     option = input("Escolha uma das opções abaixo, ou digite N para sair:\n"
        #                    "1- Para exibir em RGB:\n"
        #                    "2- Para exibir em CMY:\n"
        #                    "3- Para exibir em HSV:\n")
        #
        #     if option == 1:
        #         solid.paint(faces, window, colors, 1)
        #     if option == 2:
        #         solid.paint(faces, window, colors, 2)
        #     if option == 3:
        #         solid.paint(faces, window, colors, 3)
        # if anwser == 5:
        #     clear_window(window)
        #     subtitle_message = "Projeção Obliqua Cabinet"
        #     sub_title = Text(Point(683, 30), subtitle_message)
        #     sub_title.draw(window)
        #     solid.oblique(0.5, 13 * 5)
        #
        #     option = input("Escolha uma das opções abaixo, ou digite N para sair:\n"
        #                    "1- Para exibir em RGB:\n"
        #                    "2- Para exibir em CMY:\n"
        #                    "3- Para exibir em HSV:\n")
        #     if option == 1:
        #         solid.paint(faces, window, colors, 1)
        #     if option == 2:
        #         solid.paint(faces, window, colors, 2)
        #     if option == 3:
        #         solid.paint(faces, window, colors, 3)
        #
        # if anwser == 6:
        #     clear_window(window)
        #     subtitle_message = "Projeção em Perspectiva com 1 ponto de fuga"
        #     sub_title = Text(Point(683, 30), subtitle_message)
        #     sub_title.draw(window)
        #     solid.perspective(100 + 10 * 13)
        #
        #     option = input("Escolha uma das opções abaixo, ou digite N para sair:\n"
        #                    "1- Para exibir em RGB:\n"
        #                    "2- Para exibir em CMY:\n"
        #                    "3- Para exibir em HSV:\n")
        #     if option == 1:
        #         solid.paint(faces, window, colors, 1)
        #     if option == 2:
        #         solid.paint(faces, window, colors, 2)
        #     if option == 3:
        #         solid.paint(faces, window, colors, 3)
        solid.isometric_projection(35.26, 45)
        type += 1

        if type > 6:
            type = 1

        solid.paint(faces, window, type)
        time.sleep(1)
        update(60)
        clear_window(window)

        # title = Text(Point(683, 10), message)
        # title.draw(window)

        # points = solid.paint_points(window)

        #solid.draw(window, 0.05)



        # title.undraw()
        # sub_title.undraw()

        # stil = True
        # while (stil):
        #     subtitle_message = "Clique em um dos quadrados na esquerda da tela para destacar \n " \
        #                        "o respectivo ponto no sólido, ou clique em qualquer lugar da tela para prosseguir."
        #     sub_title = Text(Point(683, 30), subtitle_message)
        #     sub_title.draw(window)
        #     update(60)
        #     result = mouse_click(window, points, solid.vertices)
        #     if (result.getP1().x == -1):
        #         sub_title.undraw()
        #         stil = False
        #     time.sleep(0.2)
        #     result.undraw()
        #
        #     sub_title.undraw()
        # update(60)

    # window.getMouse()
    # window.close()


main()
