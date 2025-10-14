from pydantic import BaseModel, ConfigDict

from .roguelike_goods import RoguelikeGoods


class RoguelikeShop(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    goods: list[RoguelikeGoods]
