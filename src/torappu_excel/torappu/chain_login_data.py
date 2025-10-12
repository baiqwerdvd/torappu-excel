from pydantic import BaseModel, ConfigDict

from .open_server_item_data import OpenServerItemData


class ChainLoginData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    order: int
    item: OpenServerItemData
    colorId: int
