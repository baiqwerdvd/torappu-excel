from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActivityLoginData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    description: str
    itemList: list[ItemBundle]
    apSupplyOutOfDateDict: dict[str, int]
