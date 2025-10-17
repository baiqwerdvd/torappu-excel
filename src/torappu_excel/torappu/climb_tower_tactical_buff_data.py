from .climb_tower_tatical_buff_type import ClimbTowerTaticalBuffType
from ..common import BaseStruct


class ClimbTowerTacticalBuffData(BaseStruct):
    id: str
    desc: str
    profession: str
    isDefaultActive: bool
    sortId: int
    buffType: ClimbTowerTaticalBuffType
