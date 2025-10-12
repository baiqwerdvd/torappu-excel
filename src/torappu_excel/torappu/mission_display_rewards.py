from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class MissionDisplayRewards(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: ItemType
    id: str
    count: int
