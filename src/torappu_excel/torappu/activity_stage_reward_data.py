from .stage_data import StageData
from ..common import BaseStruct


class ActivityStageRewardData(BaseStruct):
    stageRewardsDict: dict[str, list["StageData.DisplayDetailRewards"]]
