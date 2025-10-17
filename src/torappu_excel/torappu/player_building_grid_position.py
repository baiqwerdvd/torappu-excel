from ..common import BaseStruct


class PlayerBuildingGridPosition(BaseStruct):
    x: int
    y: int
    dir: int | None = None
