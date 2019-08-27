import janusgraphy
from .edges import Administers


class User(janusgraphy.Vertex):
    Structure = ['name', 'password', 'salt']
    pass


class Place(janusgraphy.Vertex):
    Structure = ['name', 'display_name']

    def __init__(self, name: str, display_name: str, adm: User, **kwargs):
        super().__init__(name=name, display_name=display_name, **kwargs)
        adm.add_edge(Administers, self)
