from pydantic import BaseModel, ConfigDict

from .stage_data import StageData


class ActivityStageRewardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageRewardsDict: dict[str, list["StageData.DisplayDetailRewards"]]
