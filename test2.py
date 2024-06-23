from panda3d.core import Point3, GeomVertexFormat, GeomVertexData, GeomVertexWriter
from panda3d.core import Geom, GeomTriangles, GeomNode
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.messenger.toggleVerbose()

        # Initialisation de la position de la caméra et du point visé
        self.cameraX = 0
        self.cameraY = -10
        self.cameraZ = 0
        self.targetX = 0
        self.targetY = 0
        self.targetZ = 0
        
        # Dictionnaire pour stocker l'état des touches
        self.keyMap = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "shift_up": False,
            "shift_down": False
        }
        
        # Attacher les événements de clavier
        self.accept("arrow_left", self.updateKeyMap, ["left", True])
        self.accept("arrow_left-up", self.updateKeyMap, ["left", False])
        self.accept("arrow_right", self.updateKeyMap, ["right", True])
        self.accept("arrow_right-up", self.updateKeyMap, ["right", False])
        self.accept("arrow_up", self.updateKeyMap, ["up", True])
        self.accept("arrow_up-up", self.updateKeyMap, ["up", False])
        self.accept("arrow_down", self.updateKeyMap, ["down", True])
        self.accept("arrow_down-up", self.updateKeyMap, ["down", False])
        self.accept("shift-arrow_up", self.updateKeyMap, ["shift_up", True])
        self.accept("shift-arrow_down", self.updateKeyMap, ["shift_down", True])
        
        # Ajouter une tâche pour mettre à jour la position de la caméra
        self.taskMgr.add(self.updateCamera, "updateCameraTask")
        
        # Créer et afficher un cube avec des couleurs différentes sur chaque face
        self.createColoredCube()
        
    def updateKeyMap(self, key, state):
        print(key,state)
        self.keyMap[key] = state
        if key=='up' and state==False:
            self.keyMap['shift_up'] = False
        if key=='down' and state==False:
            self.keyMap['shift_down'] = False

    def createColoredCube(self):
        format = GeomVertexFormat.getV3cp()
        vdata = GeomVertexData('cube', format, Geom.UHStatic)
        
        vertex = GeomVertexWriter(vdata, 'vertex')
        color = GeomVertexWriter(vdata, 'color')
        
        # Définir les sommets et les couleurs
        vertices = [
            Point3(-1, -1, -1), Point3(1, -1, -1), Point3(1, 1, -1), Point3(-1, 1, -1),  # face arrière
            Point3(-1, -1, 1), Point3(1, -1, 1), Point3(1, 1, 1), Point3(-1, 1, 1)   # face avant
        ]
        
        colors = [
            (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1),  # rouge
            (0, 1, 0, 1), (0, 1, 0, 1), (0, 1, 0, 1), (0, 1, 0, 1),  # vert
            (0, 0, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1),  # bleu
            (1, 1, 0, 1), (1, 1, 0, 1), (1, 1, 0, 1), (1, 1, 0, 1),  # jaune
            (1, 0, 1, 1), (1, 0, 1, 1), (1, 0, 1, 1), (1, 0, 1, 1),  # magenta
            (0, 1, 1, 1), (0, 1, 1, 1), (0, 1, 1, 1), (0, 1, 1, 1)   # cyan
        ]
        
        for i in range(8):
            vertex.addData3(vertices[i])
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
        self.render.attachNewNode(node)
        
    def updateCamera(self, task):
        # Mettre à jour la position de la caméra et du point visé en fonction de l'état des touches
        if self.keyMap["left"]:
            self.targetX -= 0.1
        if self.keyMap["right"]:
            self.targetX += 0.1
        if self.keyMap["up"]:
            self.cameraY += 0.1
        if self.keyMap["down"]:
            self.cameraY -= 0.1
        if self.keyMap["shift_up"]:
            self.targetZ += 0.1
        if self.keyMap["shift_down"]:
            self.targetZ -= 0.1
        
        self.camera.setPos(self.cameraX, self.cameraY, self.cameraZ)
        self.camera.lookAt(self.targetX, self.targetY, self.targetZ)
        return Task.cont

app = MyApp()
app.run()
