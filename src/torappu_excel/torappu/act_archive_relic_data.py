from pydantic import BaseModel, ConfigDict

from .act_archive_relic_item_data import ActArchiveRelicItemData


class ActArchiveRelicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    relic: dict[str, ActArchiveRelicItemData]
