from pydantic import BaseModel, ConfigDict

from .act_archive_totem_item_data import ActArchiveTotemItemData


class ActArchiveTotemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    totem: dict[str, ActArchiveTotemItemData]
