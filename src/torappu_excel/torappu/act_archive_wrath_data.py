from pydantic import BaseModel, ConfigDict

from .act_archive_wrath_item_data import ActArchiveWrathItemData


class ActArchiveWrathData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    wraths: dict[str, ActArchiveWrathItemData]
