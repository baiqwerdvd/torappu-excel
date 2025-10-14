from enum import IntEnum

from pydantic import BaseModel, ConfigDict

from .player_character import PlayerCharacter
from .player_hand_book_addon import PlayerHandBookAddon
from .player_special_operator_node import PlayerSpecialOperatorNode
from .player_squad import PlayerSquad


class PlayerTroop(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    troopCapacity: int | None = None
    curSquadCount: int
    curCharInstId: int
    curCharInstCount: int | None = None
    squads: dict[str, PlayerSquad]
    chars: dict[str, PlayerCharacter]
    charGroup: dict[str, "PlayerTroop.PlayerCharGroup"]
    addon: dict[str, PlayerHandBookAddon]
    charMission: dict[str, dict[str, "PlayerTroop.CharMissionState"]]
    spOperator: dict[str, dict[str, dict[str, PlayerSpecialOperatorNode]]]

    class CharMissionState(IntEnum):
        UNCOMPLETE = 0
        FULLFILLED = 1
        COMPLETE = 2

    class PlayerCharGroup(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        favorPoint: int
