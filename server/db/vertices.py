import janusgraphy
from .edges import Administers, HasMenu, HasItem


class User(janusgraphy.Vertex):
    Structure = ['name', 'password', 'salt']
    pass


class Place(janusgraphy.Vertex):
    Structure = ['name', 'display_name']

    def __init__(self, name: str, display_name: str, adm: User, **kwargs):
        super().__init__(name=name, display_name=display_name, **kwargs)
        adm.add_edge(Administers, self)


class Menu(janusgraphy.Vertex):
    Structure = ['name']

    def __init__(self, name: str, place: Place, **kwargs):
        super().__init__(name=name, **kwargs)
        place.add_edge(HasMenu, self)


class MenuItem(janusgraphy.Vertex):
    Structure = ['name', 'value']

    def __init__(self, name: str, value: float, menu: Menu, **kwargs):
        super().__init__(name=name, value=value, **kwargs)
        menu.add_edge(HasItem, self)
