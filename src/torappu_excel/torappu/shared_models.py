from .evolve_phase import EvolvePhase
from .player_battle_rank import PlayerBattleRank
from ..common import BaseStruct


class ActivityTable(BaseStruct):
    class ActHiddenAreaPreposeStageData(BaseStruct):
        stageId: str
        unlockRank: PlayerBattleRank

    class ActivityHiddenAreaData(BaseStruct):
        name: str
        desc: str
        preposedStage: list["ActivityTable.ActHiddenAreaPreposeStageData"]
        preposedTime: int

    class CustomUnlockCond(BaseStruct):
        actId: str | None
        stageId: str


class CharacterData(BaseStruct):
    class UnlockCondition(BaseStruct):
        phase: EvolvePhase
        level: int
