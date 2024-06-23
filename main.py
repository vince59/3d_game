from panda3d.core import *
from shape import *

class Test(BaseApp):

    def __init__(self):
        BaseApp.__init__(self)
        """
        triangle=Triangle(
            s0=(0, 1, 0),
            s1=(0, -1, 0),
            s2=(0, 0, 1),
            label=True,
            color={"r":22,"g":147,"b":148},
            rotation={"x":45,"y":0,"z":0}
            )
        triangle.generate()
        triangle.reparent_to(render)

        equilateral_triangle=EquilateralTriangle(
            s0=(0,0,0),
            side_length=1,
            color={"r":148,"g":42,"b":133}
            )
        equilateral_triangle.generate()
        equilateral_triangle.reparent_to(render)

        equilateral_triangle=EquilateralTriangle(
            s0=(1,0,0),
            side_length=1,
            color={"r":0,"g":42,"b":133},
            rotation={"angle":{"x":60,"y":0,"z":0},"center":(1,0,0)}
            )
        equilateral_triangle.generate()
        equilateral_triangle.reparent_to(render)

        """

        tetrahedron=Tetrahedron(
            s0=(0,0,0),
            side_length=1,
            colors=[{"r":148,"g":42,"b":133},
                    {"r":77,"g":150,"b":73},
                    {"r":150,"g":122,"b":132},
                    {"r":187,"g":194,"b":66}
                    ]
            )
        tetrahedron.generate()
        tetrahedron.reparent_to(render)
        

app = Test()
app.run()