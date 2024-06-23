from panda3d.core import *
from panda3d.core import LMatrix4f, LQuaternion
import math

class BaseShape:
    def __init__(self,color=None,rotation=None):
        self.np=None
        self.color=Vec4(1.0, 0.0, 0.0, 1.0) if color is None else Vec4(color['r']/255,color['g']/255,color['b']/255,1)
        
    def reparent_to(self,render):
        self.np.reparent_to(render)

    def toggle(self):
        # Bascule l'affichage
        if self.np.is_hidden():
            self.np.show()
        else:
            self.np.hide()

    def createRotationMatrix(self, rotation):
        p,r,h = rotation
        
        # Créer un quaternion pour la rotation
        quat = LQuaternion()
        quat.setHpr((h, p, r))
        
        # Convertir le quaternion en une matrice de transformation
        rotation_matrix = LMatrix4f()
        quat.extractToMatrix(rotation_matrix)
        
        return rotation_matrix