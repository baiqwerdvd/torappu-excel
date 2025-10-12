from pydantic import BaseModel, ConfigDict

from .act1_vhalf_idle_item_data import Act1VHalfIdleItemData


class HalfIdleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemData: dict[str, Act1VHalfIdleItemData]
