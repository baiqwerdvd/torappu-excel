from .open_server_item_data import OpenServerItemData
from ..common import BaseStruct


class ChainLoginData(BaseStruct):
    order: int
    item: OpenServerItemData
    colorId: int
