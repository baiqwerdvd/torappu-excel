from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class TrainingCampConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlockStageId: str
    updateDesc: str
    rewardItem: ItemBundle
