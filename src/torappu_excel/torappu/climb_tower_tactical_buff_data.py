from .climb_tower_tatical_buff_type import ClimbTowerTaticalBuffType
from ..common import BaseStruct

from msgspec import field


class ClimbTowerTacticalBuffData(BaseStruct):
    id_: str = field(name="id")
    desc: str
    profession: str
    isDefaultActive: bool
    sortId: int
    buffType: ClimbTowerTaticalBuffType
