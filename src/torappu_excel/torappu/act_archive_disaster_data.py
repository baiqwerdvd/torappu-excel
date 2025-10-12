from pydantic import BaseModel, ConfigDict

from .act_archive_disaster_item_data import ActArchiveDisasterItemData


class ActArchiveDisasterData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    disasters: dict[str, ActArchiveDisasterItemData]
