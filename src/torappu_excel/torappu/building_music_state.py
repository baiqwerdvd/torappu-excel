from ..common import BaseStruct


class BuildingMusicState(BaseStruct):
    progress: list[int] | None
    unlock: bool
