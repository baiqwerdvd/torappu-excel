from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .stage_data import StageData
from .weight_item_bundle import WeightItemBundle


class CampaignData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class CampaignStageType(StrEnum):
        NONE = "NONE"
        PERMANENT = "PERMANENT"
        ROTATE = "ROTATE"
        TRAINING = "TRAINING"

    stageId: str
    isSmallScale: int
    breakLadders: list["CampaignData.BreakRewardLadder"]
    isCustomized: bool
    dropGains: dict[CampaignStageType, "CampaignData.DropGainInfo"]

    class BreakRewardLadder(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        killCnt: int
        breakFeeAdd: int
        rewards: list[ItemBundle]

    class CampaignDropInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        firstPassRewards: list[ItemBundle] | None
        passRewards: list[list[WeightItemBundle]] | None
        displayDetailRewards: list["StageData.DisplayDetailRewards"] | None

    class DropLadder(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        killCnt: int
        dropInfo: "CampaignData.CampaignDropInfo"

    class GainLadder(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        killCnt: int
        apFailReturn: int
        favor: int
        expGain: int
        goldGain: int
        displayDiamondShdNum: int

    class DropGainInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        dropLadders: list["CampaignData.DropLadder"]
        gainLadders: list["CampaignData.GainLadder"]
        displayRewards: list["StageData.DisplayRewards"]
        displayDetailRewards: list["StageData.DisplayDetailRewards"]
