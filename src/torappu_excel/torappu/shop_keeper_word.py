from ..common import BaseStruct

from msgspec import field


class ShopKeeperWord(BaseStruct):
    id_: str = field(name="id")
    text: str
