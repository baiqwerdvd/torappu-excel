from ..common import BaseStruct

from msgspec import field


class ClimbTowerCurseCardData(BaseStruct):
    id_: str = field(name="id")
    towerIdList: list[str]
    name: str
    desc: str
    trapId: str
