from ..common import BaseStruct

from msgspec import field


class MusicData(BaseStruct):
    id_: str = field(name="id")
    name: str
    bank: str
