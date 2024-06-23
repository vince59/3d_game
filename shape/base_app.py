from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from .axes import Axes

class BaseApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        #self.messenger.toggleVerbose()
        axes=Axes()
        axes.generate()
        axes.reparent_to(render)
        axes.toggle()
        self.accept('a', axes.toggle)
        return 
        self.reset_camera()
        self.accept('a', axes.toggle)
        self.accept('z', self.reset_camera)
        
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

    def updateKeyMap(self, key, state):
        self.keyMap[key] = state
        if key=='up' and state==False:
            self.keyMap['shift_up'] = False
        if key=='down' and state==False:
            self.keyMap['shift_down'] = False

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
    
    def reset_camera(self):
        self.cameraX = 0
        self.cameraY = -10
        self.cameraZ = 0
        self.targetX = 0
        self.targetY = 0
        self.targetZ = 0