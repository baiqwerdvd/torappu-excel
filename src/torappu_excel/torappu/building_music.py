from .building_music_state import BuildingMusicState
from ..common import BaseStruct


class BuildingMusic(BaseStruct):
    inUse: bool
    selected: str
    state: dict[str, BuildingMusicState]
