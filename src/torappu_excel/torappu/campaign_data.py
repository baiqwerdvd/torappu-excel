from enum import StrEnum

from .item_bundle import ItemBundle
from .stage_data import StageData
from .weight_item_bundle import WeightItemBundle
from ..common import BaseStruct


class CampaignData(BaseStruct):
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

    class BreakRewardLadder(BaseStruct):
        killCnt: int
        breakFeeAdd: int
        rewards: list[ItemBundle]

    class CampaignDropInfo(BaseStruct):
        firstPassRewards: list[ItemBundle] | None
        passRewards: list[list[WeightItemBundle]] | None
        displayDetailRewards: list["StageData.DisplayDetailRewards"] | None

    class DropLadder(BaseStruct):
        killCnt: int
        dropInfo: "CampaignData.CampaignDropInfo"

    class GainLadder(BaseStruct):
        killCnt: int
        apFailReturn: int
        favor: int
        expGain: int
        goldGain: int
        displayDiamondShdNum: int

    class DropGainInfo(BaseStruct):
        dropLadders: list["CampaignData.DropLadder"]
        gainLadders: list["CampaignData.GainLadder"]
        displayRewards: list["StageData.DisplayRewards"]
        displayDetailRewards: list["StageData.DisplayDetailRewards"]
