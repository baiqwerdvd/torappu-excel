from pydantic import BaseModel, ConfigDict

from .act_archive_trap_item_data import ActArchiveTrapItemData


class ActArchiveTrapData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    trap: dict[str, ActArchiveTrapItemData]
