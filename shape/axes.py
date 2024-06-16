from .base_shape import *

class Axes(BaseShape):
    def __init__(self):
        BaseShape.__init__(self)

    def generate(self):
        # Créez une instance de LineSegs
        lines = LineSegs()

        # Axe X en rouge
        lines.set_color(Vec4(1, 0, 0, 1))
        lines.move_to(Point3(0, 0, 0))
        lines.draw_to(Point3(10, 0, 0))

        # Axe Y en vert
        lines.set_color(Vec4(0, 1, 0, 1))
        lines.move_to(Point3(0, 0, 0))
        lines.draw_to(Point3(0, 10, 0))

        # Axe Z en bleu
        lines.set_color(Vec4(0, 0, 1, 1))
        lines.move_to(Point3(0, 0, 0))
        lines.draw_to(Point3(0, 0, 10))

        # Créez un noeud à partir des lignes
        axis_node = lines.create()
        axis_np = NodePath(axis_node)

        # Créez des labels pour chaque axe
        self.add_labels(axis_np)

        # Attachez l'ensemble des axes avec labels à la scène
        self.np=axis_np
        return axis_np

    def add_labels(self, parent):
        # Labels pour les axes
        labels = {'X': (10, 0, 0), 'Y': (0, 10, 0), 'Z': (0, 0, 10)}
        colors = {'X': Vec4(1, 0, 0, 1), 'Y': Vec4(0, 1, 0, 1), 'Z': Vec4(0, 0, 1, 1)}

        for axis, pos in labels.items():
            # Créez un TextNode pour chaque label
            text_node = TextNode('axis_label')
            text_node.set_text(axis)
            text_node.set_text_color(colors[axis])

            # Créez un NodePath pour positionner le TextNode
            text_np = parent.attach_new_node(text_node)
            text_np.set_pos(Point3(pos))

            # Ajustez l'échelle pour que le texte soit lisible
            text_np.set_scale(0.5)