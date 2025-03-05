from .evolve_phase import EvolvePhase  # noqa: F401 # pyright: ignore[reportUnusedImport]
from .roguelike_event_type import RoguelikeEventType
from ..common import BaseStruct


class RoguelikeConstTable(BaseStruct):
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

    class PlayerLevelData(BaseStruct):
        exp: int
        populationUp: int
        squadCapacityUp: int
        battleCharLimitUp: int

    class RecruitData(BaseStruct):
        recruitPopulation: int
        upgradePopulation: int

    class CharUpgradeData(BaseStruct):
        evolvePhase: int  # FIXME: EvolvePhase
        skillLevel: int
        skillSpecializeLevel: int

    class EventTypeData(BaseStruct):
        name: str
        description: str
