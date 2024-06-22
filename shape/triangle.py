from .base_shape import *
from math import *

class Triangle(BaseShape):
    def __init__(self,s0,s1,s2,color=None,label=False):
        BaseShape.__init__(self,color)

        self.s0=s0
        self.s1=s1
        self.s2=s2
        self.label=label

    def generate(self):
        # Format de vertex
        format = GeomVertexFormat.get_v3c4()
        
        # Données de vertex
        vdata = GeomVertexData('triangle', format, Geom.UH_static)
        
        vertex = GeomVertexWriter(vdata, 'vertex')
        color = GeomVertexWriter(vdata, 'color')

        # Définissez les sommets du triangle
        vertices = [
            Point3(self.s0),  # Sommet 0
            Point3(self.s1),  # Sommet 1
            Point3(self.s2)   # Sommet 2
        ]

        # Ajout des données de vertex et couleurs
        for pos in vertices:
            vertex.add_data3(pos)
            color.add_data4(self.color)
        for pos in vertices:
            vertex.add_data3(pos)
            color.add_data4(self.color)

        # Création des triangles
        tris = GeomTriangles(Geom.UH_static)
        tris.add_vertices(0, 1, 2)
        tris.add_vertices(5, 4, 3)

        # Création du Geom et GeomNode
        geom = Geom(vdata)
        geom.add_primitive(tris)
        geom_node = GeomNode('triangle')
        geom_node.add_geom(geom)

        # Attach the triangle to the scene graph
        triangle_np = NodePath(geom_node)
        
        # Ajouter des labels pour chaque sommet
        if self.label:
            self.add_labels(triangle_np,vertices)
        self.np=triangle_np
        return triangle_np

    def add_labels(self, parent, vertices):
        # Liste des labels pour les sommets
        labels = ['0', '1', '2']

        for i, pos in enumerate(vertices):
            # Créez un TextNode pour chaque label
            text_node = TextNode('vertex_label')
            text_node.set_text(labels[i])
            text_node.set_text_color(1, 1, 1, 1)  # Blanc

            # Créez un NodePath pour positionner le TextNode
            text_np = parent.attach_new_node(text_node)
            text_np.set_pos(pos)

            # Ajustez l'échelle pour que le texte soit lisible
            text_np.set_scale(1)
            # Légère élévation pour éviter le chevauchement avec le triangle
            text_np.set_y(text_np, 0.1)


class EquilateralTriangle(Triangle):
    def __init__(self,s0=(0,0,0),side_length=1,color=None):
        x,y,z=s0
        l=side_length/2
        h = side_length*sqrt(3)/2
        s1=(x+l,y,z+h)
        s2=(x+side_length,y,z)
        Triangle.__init__(self,s0,s1,s2,color,label=False)

    

