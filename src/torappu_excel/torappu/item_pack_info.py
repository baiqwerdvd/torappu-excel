from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ItemPackInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    packId: str
    content: list[ItemBundle]
