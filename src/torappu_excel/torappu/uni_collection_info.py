from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class UniCollectionInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    uniCollectionItemId: str
    uniqueItem: list[ItemBundle]
