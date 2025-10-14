from pydantic import BaseModel, ConfigDict

from .building_music import BuildingMusic
from .player_building_char import PlayerBuildingChar
from .player_building_diypreset import PlayerBuildingDIYPreset
from .player_building_furniture_info import PlayerBuildingFurnitureInfo
from .player_building_room import PlayerBuildingRoom
from .player_building_room_slot import PlayerBuildingRoomSlot
from .player_building_status import PlayerBuildingStatus


class PlayerBuilding(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    status: PlayerBuildingStatus
    chars: dict[str, PlayerBuildingChar]
    assist: list[int]
    roomSlots: dict[str, PlayerBuildingRoomSlot]
    rooms: PlayerBuildingRoom
    furniture: dict[str, PlayerBuildingFurnitureInfo]
    diyPresetSolutions: dict[str, PlayerBuildingDIYPreset]
    solution: "PlayerBuilding.PlayerBuildingSolution"
    music: BuildingMusic

    class PlayerBuildingSolution(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        furnitureTs: dict[str, int]
