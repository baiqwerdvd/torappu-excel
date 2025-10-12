from pydantic import BaseModel, ConfigDict

from .item_type import ItemType
from .stage_drop_type import StageDropType


class WeightItemBundle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: ItemType
    dropType: StageDropType
    count: int
    weight: int
