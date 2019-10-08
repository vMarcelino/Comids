import janusgraphy

from .edges import Administers, HasMenu, HasItem, From, Orders, Has
from .vertices import User, Place, Menu, MenuItem, Order

connect = janusgraphy.connect_master