import janusgraphy
from .edges import Administers, HasMenu, HasItem, From, Orders, Has
from typing import Union


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
    Structure = ['name', 'value', 'description']

    def __init__(self, name: str, value: float, description: str, menu: Menu, **kwargs):
        super().__init__(name=name, value=value, description=description, **kwargs)
        menu.add_edge(HasItem, self)

    def is_from_place(self, place_id: Union[int, Place]) -> bool:
        q = self.get_place_query().filter_by_property(id=place_id)
        count = q.count().fetch_first()
        return count == 1

    def get_place_query(self):
        q = self.query()
        q.through_incoming_edge(HasItem)
        q.through_incoming_edge(HasMenu)
        q.filter_by_property(Label=Place)
        return q


class Order(janusgraphy.Vertex):
    Structure = ['done']

    def __init__(self, done: bool, place: Place, user: User, **kwargs):
        super().__init__(done=done, **kwargs)
        self.add_edge(From, place)
        user.add_edge(Orders, self)

    def accept(self):
        self.set_properties(done=True)

    def add_item(self, item: MenuItem):
        place = self.get_place_query().fetch_first()
        if item.is_from_place(place):
            self.add_edge(Has, item)
        else:
            raise Exception('Item is not from the same place as the order')

    def get_place_query(self) -> janusgraphy.Query:
        q = self.query()
        q.through_outgoing_edge(From)
        q.filter_by_property(Label=Place)
        return q

    def is_from_place(self, place_id: Union[int, Place]) -> bool:
        q = self.get_place_query()
        q.filter_by_property(id=place_id)

        count = q.count().fetch_first()
        return count == 1

    def is_from_user(self, user_id: Union[int, User]):
        q = self.query()
        q.through_incoming_edge(Orders)
        q.filter_by_property(Label=User, id=user_id)

        count = q.count().fetch_first()
        return count == 1