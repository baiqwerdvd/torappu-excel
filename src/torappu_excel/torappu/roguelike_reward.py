from pydantic import BaseModel, ConfigDict

from .roguelike_item_bundle import RoguelikeItemBundle


class RoguelikeReward(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    index: str
    items: list[RoguelikeItemBundle]
    done: bool
    exDrop: bool
    exDropSrc: str
