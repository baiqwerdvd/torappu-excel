from ..common import BaseStruct


class PlayerBuildingWorkshopStatus(BaseStruct):
    bonus: dict[str, list[int]]
    bonusActive: int | None
