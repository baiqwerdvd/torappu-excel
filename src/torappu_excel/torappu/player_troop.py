from enum import IntEnum

from .player_character import PlayerCharacter
from .player_hand_book_addon import PlayerHandBookAddon
from .player_special_operator_node import PlayerSpecialOperatorNode
from .player_squad import PlayerSquad
from ..common import BaseStruct


class PlayerTroop(BaseStruct):
    curSquadCount: int
    curCharInstId: int
    squads: dict[str, PlayerSquad]
    chars: dict[str, PlayerCharacter]
    charGroup: dict[str, "PlayerTroop.PlayerCharGroup"]
    addon: dict[str, PlayerHandBookAddon]
    charMission: dict[str, dict[str, "PlayerTroop.CharMissionState"]]
    spOperator: dict[str, dict[str, dict[str, PlayerSpecialOperatorNode]]]
    troopCapacity: int | None = None
    curCharInstCount: int | None = None

    class CharMissionState(IntEnum):
        UNCOMPLETE = 0
        FULLFILLED = 1
        COMPLETE = 2

    class PlayerCharGroup(BaseStruct):
        favorPoint: int
