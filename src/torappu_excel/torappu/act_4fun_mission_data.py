from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class Act4funMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missionId: str
    sortId: str
    missionDes: str
    rewardIconIds: list[str]
    rewards: list[ItemBundle]
