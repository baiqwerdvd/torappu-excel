from pydantic import BaseModel, ConfigDict

from .act_archive_chaos_item_data import ActArchiveChaosItemData


class ActArchiveChaosData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chaos: dict[str, ActArchiveChaosItemData]
