import numpy
import math

from graphics import *

class Solid:

    def __init__(self):
        self.p = [1000, 1000, -50]
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

        self.scale(30, 30, 30)
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

    def normals(self, faces):
        normals = []
        for i in range(len(faces)):
            v1 = self.vertices[faces[i][0]]
            v2 = self.vertices[faces[i][1]]
            v3 = self.vertices[faces[i][2]]
            if i == len(faces) - 1:
                v1 = self.vertices[faces[i][2]]
                v2 = self.vertices[faces[i][1]]
                v3 = self.vertices[faces[i][0]]
            normals.append(self.normal(v1, v2, v3))

        return normals

    def visibles(self, faces):
        visibles = []
        normals = self.normals(faces)

        for i in range(len(faces)):
            visibles.append(self.back_face_culling(normals[i], self.vertices[faces[i][0]]))

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
        return numpy.subtract(normal, self.p)

    def lights(self, faces):
        lights = []
        for normal in self.normals(faces):
            lights.append(self.vector_light(normal))
        return lights


    def hsv(self, angle, coef, cos):
        h = angle
        s = 1
        v = coef * 255 * cos

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

        result = []
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255
        result.append(r)
        result.append(g)
        result.append(b)
        return result


    def quaternios_rotation(self, n):
        angle = numpy.pi/3
        s = numpy.cos(angle/2)
        v = numpy.dot(numpy.sin(angle/2), n)
        resp = []
        for i in range(len(self.vertices)):
            r = self.vertices[i][:3]
            vv = numpy.dot(v, v)
            vr = numpy.dot(v, r)
            result = numpy.dot(s**2, r) - numpy.dot(vv, r) + numpy.dot(2*(vr), v) + numpy.dot(2*s, numpy.cross(v, r))
            resp.append(result)

        for i in range(len(self.vertices)):
            self.vertices[i][:3] = resp[i]


    def convex_hull(self, vertices):
        t = 0
        n = 16
        answer = []
        while (t < 1):

            parcial = [0, 0, 0]

            for i in range(n+1):
                binomial = math.factorial(n) / (float(math.factorial(i) * math.factorial(n - i)))
                print n-i
                pol_bern = binomial * ((1 - t) ** (n - i)) * (t ** i)
                parcial = [parcial[0] + (pol_bern * vertices[i][0]), parcial[1] + (pol_bern * vertices[i][1]), 10]


            answer.append(parcial)
            # t += 0.0625
            t += 0.001
        for i in range(len(answer)):
            answer.append([answer[i][0], answer[i][1], 50])
        print len(answer)
        return answer

    def create_faces(self):
        faces = []
        front = []
        back = []
        side = []
        j = len(self.vertices) / 2
        for i in range(len(self.vertices[0:j])):
            front.append(i)

        faces.append(front)

        for i in range(len(self.vertices[j:])):
            back.append(i + j)

        for i in range(len(front) - 1):
            faces.append([front[i], back[i], back[i + 1], front[i + 1]])

        faces.append([front[len(front)-1], back[len(back)-1], back[0], front[0]])

        faces.append(back)
        print faces

        return faces

    def paint(self, faces, window, type):
        coef = 0.5
        l = 0
        visibles = self.visibles(faces)
        normals = self.normals(faces)
        lights = self.lights(faces)
        for face in faces:
            points = []

            if visibles[l]:
                for i in range(len(face)):
                    point = Point(self.vertices[face[i]][0], self.vertices[face[i]][1])
                    points.append(point)

                f = Polygon(points)
                v1 = numpy.array(lights[l])
                v2 = numpy.array(normals[l])
                cos = self.angle(v1, v2)

                if type == 1:
                    hsv = self.hsv(0, coef, cos)
                    converted = self.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
                    r = converted[0]
                    g = converted[1]
                    b = converted[2]

                if type == 2:
                    hsv = self.hsv(60, coef, cos)
                    converted = self.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
                    r = converted[0]
                    g = converted[1]
                    b = converted[2]

                if type == 3:
                    hsv = self.hsv(120, coef, cos)
                    converted = self.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
                    r = converted[0]
                    g = converted[1]
                    b = converted[2]

                if type == 4:
                    hsv = self.hsv(180, coef, cos)
                    converted = self.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
                    r = converted[0]
                    g = converted[1]
                    b = converted[2]

                if type == 5:
                    hsv = self.hsv(240, coef, cos)
                    converted = self.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
                    r = converted[0]
                    g = converted[1]
                    b = converted[2]

                if type == 6:
                    hsv = self.hsv(300, coef, cos)
                    converted = self.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
                    r = converted[0]
                    g = converted[1]
                    b = converted[2]


                f.setFill(color_rgb(r, g, b))
                f.setOutline(color_rgb(r, g, b))
                f.draw(window)
               # time.sleep(0.2)

                update(60)

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


