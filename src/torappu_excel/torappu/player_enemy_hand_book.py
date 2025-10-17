from ..common import BaseStruct


class PlayerEnemyHandBook(BaseStruct):
    enemies: dict[str, int]
    stage: dict[str, list[str]]
