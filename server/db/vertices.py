import janusgraphy
from .edges import Administers


class User(janusgraphy.Vertex):
    Structure = ['name', 'password', 'salt']
    pass


class Place(janusgraphy.Vertex):
    def __init__(self, name: str, adm: User, **kwargs):
        super().__init__(name=name, **kwargs)
        adm.add_edge(Administers, self)
