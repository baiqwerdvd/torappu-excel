from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .recal_rune_stage_data import RecalRuneStageData


class RecalRuneSeasonData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    seasonId: str
    sortId: int
    startTs: int
    seasonCode: str
    juniorReward: ItemBundle
    seniorReward: ItemBundle
    seniorRewardHint: str
    mainMedalId: str
    picId: str
    stages: dict[str, RecalRuneStageData]
