from panda3d.core import Point3, GeomVertexFormat, GeomVertexData, GeomVertexWriter
from panda3d.core import Geom, GeomTriangles, GeomNode, NodePath, LMatrix4f, LQuaternion
from direct.showbase.ShowBase import ShowBase
import math

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Créer quelques cubes avec des paramètres différents
        self.createCube((0, 10, 0), (45, 0, 0), 1)

    def createCube(self, position, rotation, size):
        # Crée le format et les données des sommets
        format = GeomVertexFormat.getV3cp()
        vdata = GeomVertexData('cube', format, Geom.UHStatic)
        
        vertex = GeomVertexWriter(vdata, 'vertex')
        color = GeomVertexWriter(vdata, 'color')
        
        # Calculer les sommets en fonction de la taille du cube
        half_size = size / 2
        vertices = [
            Point3(-half_size, -half_size, -half_size), Point3(half_size, -half_size, -half_size), 
            Point3(half_size, half_size, -half_size), Point3(-half_size, half_size, -half_size),  # face arrière
            Point3(-half_size, -half_size, half_size), Point3(half_size, -half_size, half_size), 
            Point3(half_size, half_size, half_size), Point3(-half_size, half_size, half_size)   # face avant
        ]
        
        colors = [
            (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1),  # rouge
            (0, 1, 0, 1), (0, 1, 0, 1), (0, 1, 0, 1), (0, 1, 0, 1),  # vert
            (0, 0, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1),  # bleu
            (1, 1, 0, 1), (1, 1, 0, 1), (1, 1, 0, 1), (1, 1, 0, 1),  # jaune
            (1, 0, 1, 1), (1, 0, 1, 1), (1, 0, 1, 1), (1, 0, 1, 1),  # magenta
            (0, 1, 1, 1), (0, 1, 1, 1), (0, 1, 1, 1), (0, 1, 1, 1)   # cyan
        ]
        
        # Créer une matrice de transformation pour la rotation
        rotation_matrix = self.createRotationMatrix(rotation)

        for i in range(8):
            rotated_vertex = rotation_matrix.xformPoint(vertices[i])
            vertex.addData3(rotated_vertex)
            color.addData4f(colors[i % 6])
        
        # Définir les triangles qui composent le cube
        tris = GeomTriangles(Geom.UHStatic)
        indices = [
            (0, 1, 2), (2, 3, 0),  # face arrière
            (4, 5, 6), (6, 7, 4),  # face avant
            (0, 3, 7), (7, 4, 0),  # face gauche
            (1, 5, 6), (6, 2, 1),  # face droite
            (3, 2, 6), (6, 7, 3),  # face supérieure
            (0, 1, 5), (5, 4, 0)   # face inférieure
        ]
        
        for tri in indices:
            tris.addVertices(*tri)
            tris.closePrimitive()
        
        geom = Geom(vdata)
        geom.addPrimitive(tris)
        
        node = GeomNode('cube')
        node.addGeom(geom)
        
        cube = NodePath(node)
        cube.setPos(position)
        cube.reparentTo(self.render)

    def createRotationMatrix(self, rotation):
        # Convertir les angles de rotation en radians
        h, p, r = rotation
        #h = math.radians(h)
        #p = math.radians(p)
        #r = math.radians(r)
        
        # Créer un quaternion pour la rotation
        quat = LQuaternion()
        quat.setHpr((h, p, r))
        
        # Convertir le quaternion en une matrice de transformation
        rotation_matrix = LMatrix4f()
        quat.extractToMatrix(rotation_matrix)
        
        return rotation_matrix

app = MyApp()
app.run()
