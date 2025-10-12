from pydantic import BaseModel, ConfigDict

from .evolve_phase import EvolvePhase  # noqa: F401 # pyright: ignore[reportUnusedImport]
from .roguelike_event_type import RoguelikeEventType


class RoguelikeConstTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    playerLevelTable: dict[str, "RoguelikeConstTable.PlayerLevelData"]
    recruitPopulationTable: dict[str, "RoguelikeConstTable.RecruitData"]
    charUpgradeTable: dict[str, "RoguelikeConstTable.CharUpgradeData"]
    eventTypeTable: dict[RoguelikeEventType, "RoguelikeConstTable.EventTypeData"]
    shopDialogs: list[str]
    shopRelicDialogs: list[str]
    shopTicketDialogs: list[str]
    mimicEnemyIds: list[str]
    clearZoneScores: list[int]
    moveToNodeScore: int
    clearNormalBattleScore: int
    clearEliteBattleScore: int
    clearBossBattleScore: int
    gainRelicScore: int
    gainCharacterScore: int
    unlockRelicSpecialScore: int
    squadCapacityMax: int
    bossIds: list[str]

    class PlayerLevelData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        exp: int
        populationUp: int
        squadCapacityUp: int
        battleCharLimitUp: int

    class RecruitData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        recruitPopulation: int
        upgradePopulation: int

    class CharUpgradeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        evolvePhase: int  # FIXME: EvolvePhase
        skillLevel: int
        skillSpecializeLevel: int

    class EventTypeData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        name: str
        description: str
