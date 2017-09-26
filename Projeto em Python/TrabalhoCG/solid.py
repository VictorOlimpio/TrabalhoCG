import sys, math, time
import numpy as num
from graphics import *

class Solid:
    def __init__(self):
        self.vertices = []
        self.vertices = num.zeros((0, 4))
        self.edges = []

    def add_vertices(self, vertice_list):
        coluna_uns = num.ones((len(vertice_list), 1))
        uns_added = num.hstack((vertice_list, coluna_uns))
        self.vertices = num.vstack((self.vertices, uns_added))

    def add_edges(self, edge_list):
        self.edges = edge_list

    def print_vertices(self):
        print "\n --- Vertices --- "
        for i, (x, y, z, _) in enumerate(self.vertices):
            print " %d: (%.2f, %.2f, %.2f)" % (i, x, y, z)

    def print_edges(self):
        print "\n --- Edges --- "
        for i, (vertice1, vertice2) in enumerate(self.edges):
            print "%d: %d -> %d" % (i, vertice1, vertice2)

    def rot_x(self, radians):
        c = num.cos(radians)
        s = num.sin(radians)
        rX = num.array([[1, 0, 0, 0],
                        [0, c, -s, 0],
                        [0, s, c, 0],
                        [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = num.dot(rX, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def rot_y(self, radians):
        c = num.cos(radians)
        s = num.sin(radians)
        rY = num.array([[c, 0, s, 0],
                        [0, 1, 0, 0],
                        [-s, 0, c, 0],
                        [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = num.dot(rY, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def rot_z(self, angle):
        c = num.cos(angle)
        s = num.sin(angle)
        rZ = num.array([[c, -s, 0, 0],
                        [s, c, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = num.dot(rZ, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def isometric_projection(self, angle_x, angle_y):
        angle_x *= -1
        c_x = num.cos(angle_x)
        s_x = num.sin(angle_x)

        c_y = num.cos(angle_y)
        s_y = num.sin(angle_y)

        iso = num.array([[c_y, s_y * s_x, 0, 0],
                         [0, c_x, 0, 0],
                         [s_y, (-s_x) * c_y, 0, 0],
                         [0, 0, 0, 1]]).transpose()

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = num.dot(iso, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def perspective(self, zcp):
        pers = num.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, -1/zcp],
                          [0, 0, 0, 1]]).transpose()

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = num.dot(pers, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def oblique(self, l, angle):
        c = num.cos(angle)
        s = num.sin(angle)

        obl = num.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [l*c, l*s, 0, 0],
                        [0, 0, 0, 1]]).transpose()


        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = num.dot(obl, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def translation(self, dx=0, dy=0, dz=0):
        t = num.array([[1, 0, 0, dx],
                       [0, 1, 0, dy],
                       [0, 0, 1, dz],
                       [0, 0, 0, 1]])

        self.vertices = self.vertices.transpose()
        self.vertices = num.dot(t, self.vertices)
        self.vertices = self.vertices.transpose()

    def scale(self, sx=0, sy=0, sz=0):

        e = num.array([[sx, 0, 0, 0],
                       [0, sy, 0, 0],
                       [0, 0, sz, 0],
                       [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = num.dot(self.vertices, e)
        self.translation(center[0], center[1], center[2])

    def get_center(self):
        n_vertices = len(self.vertices)
        vertice = [sum(self.vertices[:, i]) / n_vertices for i in range(4)]
        return (vertice[0], vertice[1], vertice[2])

    def draw(self, graph, delay):
        for n1, n2 in self.edges:
            ptI = Point(int(self.vertices[n1][0]), int(self.vertices[n1][1]))
            ptF = Point(int(self.vertices[n2][0]), int(self.vertices[n2][1]))
            cI = Circle(ptI, 3)
            cF = Circle(ptF, 3)
            cI.setFill("yellow")
            cI.draw(graph)
            time.sleep(delay)
            update(60)
            ln = Line(ptI, ptF)
            ln.draw(graph)
            time.sleep(delay)
            update(60)
            cF.setFill("red")
            cF.draw(graph)
            time.sleep(delay)
            update(60)
            cF.setFill("yellow")
            time.sleep(delay)
            update(60)

    def paint(self, faces, window):
        colors = ["skyblue", "violet", "green", "purple", "pink", "blue", "brown", "indigo", "grey", "orange"]
        j = 0
        for face in faces:
            pts = []
            for i in range(len(face)):
                pt = Point(self.vertices[face[i]][0], self.vertices[face[i]][1])
                pts.append(pt)
            p = Polygon(pts)
            p.setFill(colors[j])
            p.setOutline("black")
            p.draw(window)
            time.sleep(0.2)
            update(60)
            if (j > 8):
                j = 0
            j += 1

    def paint_points(self, window):
        i = 15
        points = []
        for vertice in self.vertices:
            s = ', '.join(str(e) for e in (vertice[0], vertice[1], vertice[2]))
            dot = Point(10, i)
            points.append((10, i))
            marker = Circle(dot, 6)
            marker.setFill("green")
            marker.draw(window)
            txt = Text(Point(200, i), s)
            txt.setFace("arial")
            txt.setStyle("bold")
            txt.draw(window)
            i += 18
        return points