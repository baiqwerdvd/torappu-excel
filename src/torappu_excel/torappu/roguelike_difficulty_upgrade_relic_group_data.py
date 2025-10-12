from pydantic import BaseModel, ConfigDict

from .roguelike_difficulty_upgrade_relic_data import RoguelikeDifficultyUpgradeRelicData


class RoguelikeDifficultyUpgradeRelicGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    relicData: list[RoguelikeDifficultyUpgradeRelicData]
