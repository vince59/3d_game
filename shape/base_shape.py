from panda3d.core import *

class BaseShape:
    def __init__(self):
        self.np=None

    def reparent_to(self,render):
        self.np.reparent_to(render)

    def toggle(self):
        # Bascule l'affichage
        if self.np.is_hidden():
            self.np.show()
        else:
            self.np.hide()
