from .player_stage_state import PlayerStageStateStrEnum
from ..common import BaseStruct


class KVSwitchInfo(BaseStruct):
    isDefault: bool
    displayTime: int
    stageId: str | None
    passState: PlayerStageStateStrEnum
