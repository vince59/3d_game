from panda3d.core import *
from shape import *

class Test(BaseApp):

    def __init__(self):
        BaseApp.__init__(self)
        triangle=Triangle()
        triangle.generate()
        triangle.reparent_to(render)

app = Test()
app.run()