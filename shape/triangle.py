from .base_shape import *
from math import *

class Triangle(BaseShape):
    def __init__(self,s0,s1,s2,color=None,label=False,rotation=None):
        BaseShape.__init__(self,color,rotation)

        self.s0=s0
        self.s1=s1
        self.s2=s2
        self.label=label
        # Format de vertex
        format = GeomVertexFormat.get_v3c4()
        
        # Données de vertex
        self.vdata = GeomVertexData('triangle', format, Geom.UH_static)
        
        self.vertex = GeomVertexWriter(self.vdata, 'vertex')
        self.vcolor = GeomVertexWriter(self.vdata, 'color')

        # Définissez les sommets du triangle
        self.vertices = [
            Point3(self.s0),  # Sommet 0
            Point3(self.s1),  # Sommet 1
            Point3(self.s2)   # Sommet 2
        ]

        if rotation is not None:
            self.rotate(rotation)

    def rotate(self,rotation):
        angle=rotation["angle"]
        rot=(angle["x"],angle["y"],angle["z"])
        center=rotation["center"]
        rotation_matrix = self.createRotationMatrix(rot)
        for i in range(3):
            if center is not None:
                self.vertices[i]=self.vertices[i]-Point3(center)    
            self.vertices[i]= rotation_matrix.xformPoint(self.vertices[i])
            if center is not None:
                self.vertices[i]=self.vertices[i]+Point3(center)

    def build_node(self):
        # Ajout des données de vertex et couleurs
        for v in self.vertices:
            self.vertex.add_data3(v)
            self.vcolor.add_data4(self.color)
        for v in self.vertices:
            self.vertex.add_data3(v)
            self.vcolor.add_data4(self.color)

        # Création des triangles
        tris = GeomTriangles(Geom.UH_static)
        tris.add_vertices(0, 1, 2)
        tris.add_vertices(5, 4, 3)

        # Création du Geom et GeomNode
        geom = Geom(self.vdata)
        geom.add_primitive(tris)
        geom_node = GeomNode('triangle')
        geom_node.add_geom(geom)
        self.geom_node=geom_node
        return geom_node
    
    def generate(self):
        self.build_node()
        # Attach the triangle to the scene graph
        self.np = NodePath(self.geom_node)
        
        # Ajouter des labels pour chaque sommet
        if self.label:
            self.add_labels()
        return self.np

    def add_labels(self):
        # Liste des labels pour les sommets
        labels = ['0', '1', '2']

        for i, pos in enumerate(self.vertices):
            # Créez un TextNode pour chaque label
            text_node = TextNode('vertex_label')
            text_node.set_text(labels[i])
            text_node.set_text_color(1, 1, 1, 1)  # Blanc

            # Créez un NodePath pour positionner le TextNode
            text_np = self.np.attach_new_node(text_node)
            text_np.set_pos(pos)

            # Ajustez l'échelle pour que le texte soit lisible
            text_np.set_scale(1)
            # Légère élévation pour éviter le chevauchement avec le triangle
            text_np.set_y(text_np, 0.1)

class EquilateralTriangle(Triangle):
    def __init__(self,s0=(0,0,0),side_length=1,color=None,rotation=None):
        x,y,z=s0
        l=side_length/2
        h = side_length*sqrt(3)/2
        s1=(x+l,y,z+h)
        s2=(x+side_length,y,z)
        Triangle.__init__(self,s0,s1,s2,color,False,rotation)