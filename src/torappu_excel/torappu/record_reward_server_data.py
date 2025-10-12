from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class RecordRewardServerData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    rewards: list[ItemBundle]
