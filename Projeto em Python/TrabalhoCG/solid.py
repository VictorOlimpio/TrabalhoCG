import numpy
import math
from numpy.distutils.system_info import numarray_info

from graphics import *

class Solid:

    def __init__(self):
        self.p = [765, 301, -1000]
        self.rgb_scale = 255
        self.cmyk_scale = 100
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

            #start_circle.setFill("yellow")
            #end_circle.setFill("red")

            #start_circle.draw(window)
            time.sleep(delay)
            update(60)

            line.draw(window)
            time.sleep(delay)
            update(60)

            #end_circle.draw(window)
            time.sleep(delay)
            update(60)

            #end_circle.setFill("yellow")
            time.sleep(delay)
            update(60)

    def normal(self, vertice1, vertice2, vertice3):
        v1 = numpy.subtract(vertice2, vertice1)
        v2 = numpy.subtract(vertice3, vertice1)
        normal = numpy.cross(v1[:3], v2[:3])
        return normal

    def normals(self):
        normals = []
        normals.append(self.normal(self.vertices[0], self.vertices[1], self.vertices[2]))
        normals.append(self.normal(self.vertices[0], self.vertices[16], self.vertices[17]))
        normals.append(self.normal(self.vertices[1], self.vertices[17], self.vertices[18]))
        normals.append(self.normal(self.vertices[2], self.vertices[18], self.vertices[19]))
        normals.append(self.normal(self.vertices[3], self.vertices[19], self.vertices[20]))
        normals.append(self.normal(self.vertices[4], self.vertices[20], self.vertices[21]))
        normals.append(self.normal(self.vertices[5], self.vertices[21], self.vertices[22]))
        normals.append(self.normal(self.vertices[6], self.vertices[22], self.vertices[23]))
        normals.append(self.normal(self.vertices[7], self.vertices[23], self.vertices[24]))
        normals.append(self.normal(self.vertices[8], self.vertices[24], self.vertices[25]))
        normals.append(self.normal(self.vertices[9], self.vertices[25], self.vertices[26]))
        normals.append(self.normal(self.vertices[10], self.vertices[26], self.vertices[27]))
        normals.append(self.normal(self.vertices[11], self.vertices[27], self.vertices[28]))
        normals.append(self.normal(self.vertices[12], self.vertices[28], self.vertices[29]))
        normals.append(self.normal(self.vertices[13], self.vertices[29], self.vertices[30]))
        normals.append(self.normal(self.vertices[14], self.vertices[30], self.vertices[31]))
        normals.append(self.normal(self.vertices[15], self.vertices[31], self.vertices[16]))
        normals.append(self.normal(self.vertices[22], self.vertices[21], self.vertices[20]))

        return normals

    def visibles(self):
        visibles = []
        normals = self.normals()
        visibles.append(self.back_face_culling(normals[0], self.vertices[0]))
        visibles.append(self.back_face_culling(normals[1], self.vertices[0]))
        visibles.append(self.back_face_culling(normals[2], self.vertices[1]))
        visibles.append(self.back_face_culling(normals[3], self.vertices[2]))
        visibles.append(self.back_face_culling(normals[4], self.vertices[3]))
        visibles.append(self.back_face_culling(normals[5], self.vertices[4]))
        visibles.append(self.back_face_culling(normals[6], self.vertices[5]))
        visibles.append(self.back_face_culling(normals[7], self.vertices[6]))
        visibles.append(self.back_face_culling(normals[8], self.vertices[7]))
        visibles.append(self.back_face_culling(normals[9], self.vertices[8]))
        visibles.append(self.back_face_culling(normals[10], self.vertices[9]))
        visibles.append(self.back_face_culling(normals[11], self.vertices[10]))
        visibles.append(self.back_face_culling(normals[12], self.vertices[11]))
        visibles.append(self.back_face_culling(normals[13], self.vertices[12]))
        visibles.append(self.back_face_culling(normals[14], self.vertices[13]))
        visibles.append(self.back_face_culling(normals[15], self.vertices[14]))
        visibles.append(self.back_face_culling(normals[16], self.vertices[15]))
        visibles.append(self.back_face_culling(normals[17], self.vertices[18]))

        return visibles


    def back_face_culling(self, normal, vertice):
        if numpy.inner(numpy.subtract(vertice[:3], self.p), normal) > 0:
            return True
        return False

    def unit_vector(self, vector):
        return vector / numpy.linalg.norm(vector)

    def angle(self, v1, v2):
        v1_u = self.unit_vector(v1)
        v2_u = self.unit_vector(v2)
        return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

    def vector_light(self, normal):
        return numpy.subtract(self.p, normal)

    def lights(self):
        lights = []
        for normal in self.normals():
            lights.append(self.vector_light(normal))
        return lights


    def rgb_to_cmyk(self, r, g, b):
        result = []
        if (r == 0) and (g == 0) and (b == 0):
            # black
            c = 0
            m = 0
            y = 0
            k = self.cmyk_scale
            result.append(c)
            result.append(m)
            result.append(y)
            result.append(k)
            return result

        c = 1 - r / float(self.rgb_scale)
        m = 1 - g / float(self.rgb_scale)
        y = 1 - b / float(self.rgb_scale)

        min_cmy = min(c, m, y)
        c = abs((c - min_cmy))
        m = abs((m - min_cmy))
        y = abs((y - min_cmy))
        k = min_cmy

        c = c * self.cmyk_scale
        m = m * self.cmyk_scale
        y = y * self.cmyk_scale
        k = k * self.cmyk_scale

        result.append(c)
        result.append(m)
        result.append(y)
        result.append(k)

        return result

    def cmyk_to_rgb(self, c, m, y, k):
        result = []

        r = abs(self.rgb_scale * (1.0 - c / float(self.cmyk_scale)) * (1.0 - k / float(self.cmyk_scale)))
        g = abs(self.rgb_scale * (1.0 - m / float(self.cmyk_scale)) * (1.0 - k / float(self.cmyk_scale)))
        b = abs(self.rgb_scale * (1.0 - y / float(self.cmyk_scale)) * (1.0 - k / float(self.cmyk_scale)))

        result.append(r)
        result.append(g)
        result.append(b)
        return result

    def rgb_to_hsv(self, r, g, b):

        mx = max(r, g, b)
        mn = min(r, g, b)

        delta = mx - mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * (abs(g - b) / delta) + 360)
        elif mx == g:
            h = (60 * (abs(b - r) / delta) + 120)
        elif mx == b:
            h = (60 * (abs(r - g) / delta) + 240)
        if mx == 0:
            s = 0
        else:
            s = delta / mx
        v = mx

        result = []
        result.append(h)
        result.append(s)
        result.append(v)
        return result

    def hsv_to_rgb(self, h, s, v):
        h = float(h)
        s = float(s)
        v = float(v)

        h60 = h / 60.0
        h60f = math.floor(h60)
        hi = int(h60f) % 6

        f = h60 - h60f
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        r, g, b = 0, 0, 0

        if hi == 0:
            r, g, b = v, t, p
        elif hi == 1:
            r, g, b = q, v, p
        elif hi == 2:
            r, g, b = p, v, t
        elif hi == 3:
            r, g, b = p, q, v
        elif hi == 4:
            r, g, b = t, p, v
        elif hi == 5:
            r, g, b = v, p, q
        r, g, b = int(r * 255), int(g * 255), int(b * 255)

        result = []
        result.append(r)
        result.append(g)
        result.append(b)
        return result

    def paint(self, faces, window, colors, type):
        #colors = ["skyblue", "violet", "green", "purple", "pink", "blue", "brown", "indigo", "grey", "orange"]
        coef = 0.7
        j = 0
        l = 0
        visibles = self.visibles()
        normals = self.normals()
        lights = self.lights()
        for face in faces:
            points = []

            if visibles[l]:
                for i in range(len(face)):
                    point = Point(self.vertices[face[i]][0], self.vertices[face[i]][1])
                    points.append(point)

                f = Polygon(points)
                v1 = numpy.array(normals[l])
                v2 = numpy.array(lights[l])

                cos = self.angle(v1, v2)

                if type == 1:
                    r = abs(coef * colors[0] * cos)
                    g = abs(coef * colors[1] * cos)
                    b = abs(coef * colors[2] * cos)

                if type == 2:

                    converted = self.rgb_to_cmyk(colors[0], colors[1], colors[2])

                    r = abs(coef * converted[0] * cos)
                    g = abs(coef * converted[1] * cos)
                    b = abs(coef * converted[2] * cos)
                    k = abs(coef * converted[3] * cos)

                    converted = self.cmyk_to_rgb(r, g, b, k)

                    r = converted[0]
                    g = converted[1]
                    b = converted[2]

                if type == 3:
                    converted = self.rgb_to_hsv(colors[0], colors[1], colors[2])

                    r = abs(coef * converted[0] * cos)
                    g = abs(coef * converted[1] * cos)
                    b = abs(coef * converted[2] * cos)

                    converted = self.hsv_to_rgb(r, g, b)

                    r = converted[0]
                    g = converted[1]
                    b = converted[2]

                f.setFill(color_rgb(r, g, b))
                f.setOutline(color_rgb(r, g, b))
                f.draw(window)
                time.sleep(0.2)

                update(60)

                if (j > 8):
                    j = 0
                j += 1

            l += 1

    def paint_points(self, window):
        i = 15
        j = 0
        squares = []
        for vertice in self.vertices:
            string_number = str(j)
            s = string_number + ': ' + ', '.join(str(e) for e in (vertice[0], vertice[1], vertice[2]))

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


