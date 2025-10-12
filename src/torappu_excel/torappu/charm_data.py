from pydantic import BaseModel, ConfigDict

from .charm_item_data import CharmItemData


class CharmData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charmList: list[CharmItemData]
