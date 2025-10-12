from pydantic import BaseModel, ConfigDict

from .act_archive_buff_item_data import ActArchiveBuffItemData


class ActArchiveBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: dict[str, ActArchiveBuffItemData]
