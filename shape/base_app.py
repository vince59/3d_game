from direct.showbase.ShowBase import ShowBase
from .axes import Axes

class BaseApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.cam.set_pos(10, -40, 10)
        self.cam.look_at(0, 0, 0)
        axes=Axes()
        axes.generate()
        axes.reparent_to(render)
        axes.toggle()
        self.accept('a', axes.toggle)