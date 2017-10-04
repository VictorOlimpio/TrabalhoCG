import numpy
from graphics import *

class Solid:
    def __init__(self):
        self.vertices = numpy.zeros((0, 4))
        self.edges = []

    def add_vertices(self, vertice_list):
        ones_column = numpy.ones((len(vertice_list), 1))
        list_with_ones = numpy.hstack((vertice_list, ones_column))
        self.vertices = numpy.vstack((self.vertices, list_with_ones))

    def add_edges(self, edge_list):
        self.edges = edge_list

    def print_vertices(self):
        print "\n #### Vertices #### "
        for i, (x, y, z, _) in enumerate(self.vertices):
            print " %d: (%.2f, %.2f, %.2f)" % (i, x, y, z)

    def print_edges(self):
        print "\n #### Edges #### "
        for i, (vertice1, vertice2) in enumerate(self.edges):
            print "%d: %d -> %d" % (i, vertice1, vertice2)

    def rot_x(self, angle):
        c = numpy.cos(angle)
        s = numpy.sin(angle)
        rX = numpy.array([[1, 0, 0, 0],
                          [0, c, -s, 0],
                          [0, s, c, 0],
                          [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = numpy.dot(rX, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def rot_y(self, angle):
        c = numpy.cos(angle)
        s = numpy.sin(angle)
        rY = numpy.array([[c, 0, s, 0],
                          [0, 1, 0, 0],
                          [-s, 0, c, 0],
                          [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = numpy.dot(rY, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def rot_z(self, angle):
        c = numpy.cos(angle)
        s = numpy.sin(angle)
        rZ = numpy.array([[c, -s, 0, 0],
                          [s, c, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = numpy.dot(rZ, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def isometric_projection(self, angle_x, angle_y):
        angle_x *= -1
        c_x = numpy.cos(angle_x)
        s_x = numpy.sin(angle_x)

        c_y = numpy.cos(angle_y)
        s_y = numpy.sin(angle_y)

        iso = numpy.array([[c_y, s_y * s_x, 0, 0],
                           [0, c_x, 0, 0],
                           [s_y, (-s_x) * c_y, 0, 0],
                           [0, 0, 0, 1]]).transpose()

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = numpy.dot(iso, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def perspective(self, zcp):
        pers = numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 0, -1/zcp],
                            [0, 0, 0, 1]]).transpose()

        self.vertices = self.vertices.transpose()
        self.vertices = numpy.dot(pers, self.vertices)
        self.vertices = self.vertices.transpose()

        for vertex in self.vertices:
            vertex[0] = abs(vertex[0] / vertex[3])
            vertex[1] = abs(vertex[1] / vertex[3])
            vertex[2] = abs(vertex[2] / vertex[3])
            vertex[3] = abs(vertex[3] / vertex[3])

        self.scale(70, 70, 70)
        self.translation(750, 250, 0)

    def oblique(self, l, angle):
        c = numpy.cos(angle)
        s = numpy.sin(angle)

        obl = numpy.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [l*c, l*s, 0, 0],
                           [0, 0, 0, 1]]).transpose()


        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = self.vertices.transpose()
        self.vertices = numpy.dot(obl, self.vertices)
        self.vertices = self.vertices.transpose()
        self.translation(center[0], center[1], center[2])

    def translation(self, dx=0, dy=0, dz=0):
        t = numpy.array([[1, 0, 0, dx],
                         [0, 1, 0, dy],
                         [0, 0, 1, dz],
                         [0, 0, 0, 1]])

        self.vertices = self.vertices.transpose()
        self.vertices = numpy.dot(t, self.vertices)
        self.vertices = self.vertices.transpose()

    def scale(self, sx=0, sy=0, sz=0):

        e = numpy.array([[sx, 0, 0, 0],
                         [0, sy, 0, 0],
                         [0, 0, sz, 0],
                         [0, 0, 0, 1]])

        center = self.get_center()
        self.translation(-center[0], -center[1], -center[2])
        self.vertices = numpy.dot(self.vertices, e)
        self.translation(center[0], center[1], center[2])

    def get_center(self):
        n_vertices = len(self.vertices)
        vertice = [sum(self.vertices[:, i]) / n_vertices for i in range(4)]
        return (vertice[0], vertice[1], vertice[2])

    def draw(self, window, delay):
        for index1, index2 in self.edges:
            start_point = Point(int(self.vertices[index1][0]), int(self.vertices[index1][1]))
            end_point = Point(int(self.vertices[index2][0]), int(self.vertices[index2][1]))
            start_circle = Circle(start_point, 3)
            end_circle = Circle(end_point, 3)
            line = Line(start_point, end_point)

            start_circle.setFill("yellow")
            end_circle.setFill("red")

            start_circle.draw(window)
            time.sleep(delay)
            update(60)

            line.draw(window)
            time.sleep(delay)
            update(60)

            end_circle.draw(window)
            time.sleep(delay)
            update(60)

            end_circle.setFill("yellow")
            time.sleep(delay)
            update(60)

    def paint(self, faces, window):
        colors = ["skyblue", "violet", "green", "purple", "pink", "blue", "brown", "indigo", "grey", "orange"]
        j = 0
        for face in faces:
            points = []
            for i in range(len(face)):
                point = Point(self.vertices[face[i]][0], self.vertices[face[i]][1])
                points.append(point)

            f = Polygon(points)
            f.setFill(colors[j])
            f.setOutline("black")
            f.draw(window)
            time.sleep(0.2)

            update(60)

            if (j > 8):
                j = 0
            j += 1

    def paint_points(self, window):
        i = 15
        j = 0
        squares = []
        for vertice in self.vertices:
            s = ', '.join(str(e) for e in (vertice[0], vertice[1], vertice[2]))

            squares.append([" "] * 2)

            point1 = Point(10, i)
            point2 = Point(30, i + 20)

            squares[j][0] = point1
            squares[j][1] = point2

            square = Rectangle(point1, point2)
            square.setFill("green")
            square.draw(window)
            txt = Text(Point(200, i + 10), s)
            txt.setFace("arial")
            txt.setStyle("bold")
            txt.draw(window)
            i += 18
            j+= 1

        return squares