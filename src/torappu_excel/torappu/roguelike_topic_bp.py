from pydantic import BaseModel, ConfigDict

from .item_type import ItemType


class RoguelikeTopicBP(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    level: int
    tokenNum: int
    nextTokenNum: int
    itemID: str
    itemType: ItemType
    itemCount: int
    isGoodPrize: bool
    isGrandPrize: bool
