from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .return_v2_jump_type import ReturnV2JumpType


class ReturnV2MissionItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missionId: str
    groupId: str
    sortId: int
    jumpType: ReturnV2JumpType
    jumpParam: str | None
    desc: str
    rewardList: list[ItemBundle]
