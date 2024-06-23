from .base_shape import *
from .triangle import *

class Tetrahedron(BaseShape):
    def __init__(self,s0=(0,0,0),side_length=1,colors=None):
        if colors is None:
            for i in range(4):
                colors[i]=None
        BaseShape.__init__(self,colors[0])
        self.t1=EquilateralTriangle(s0,side_length,colors[0])
        self.t2=EquilateralTriangle(self.t1.s2,side_length,colors[1])

    def generate(self):
        self.t1.build_node()
        rotation={"angle":{"x":0,"y":-60,"z":0},"center":(1,0,0)}
        self.t2.rotate(rotation)
        self.t2.build_node()

        self.np = NodePath(self.t1.geom_node)
        self.np.attach_new_node(self.t2.geom_node)
        return self.np