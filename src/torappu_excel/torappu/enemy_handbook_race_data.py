from ..common import BaseStruct

from msgspec import field


class EnemyHandbookRaceData(BaseStruct):
    id_: str = field(name="id")
    raceName: str
    sortId: int
