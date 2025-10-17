from ..common import BaseStruct


class ClimbTowerCurseCardData(BaseStruct):
    id: str
    towerIdList: list[str]
    name: str
    desc: str
    trapId: str
