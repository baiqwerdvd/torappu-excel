from .roguelike_difficulty_upgrade_relic_data import RoguelikeDifficultyUpgradeRelicData
from ..common import BaseStruct


class RoguelikeDifficultyUpgradeRelicGroupData(BaseStruct):
    relicData: list[RoguelikeDifficultyUpgradeRelicData]
