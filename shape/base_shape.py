from panda3d.core import *

class BaseShape:
    def __init__(self,color=None):
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
