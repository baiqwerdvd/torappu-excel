from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase
from .player_battle_rank import PlayerBattleRank


class ActivityTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class ActHiddenAreaPreposeStageData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        unlockRank: PlayerBattleRank

    class ActivityHiddenAreaData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        name: str
        desc: str
        preposedStage: list["ActivityTable.ActHiddenAreaPreposeStageData"]
        preposedTime: int

    class CustomUnlockCond(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        actId: str | None
        stageId: str


class CharacterData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class UnlockCondition(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        phase: EvolvePhase
        level: int
