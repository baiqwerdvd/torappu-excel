from pydantic import BaseModel, ConfigDict

from .act_archive_avg_item_data import ActArchiveAvgItemData


class ActArchiveAvgData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    avgs: dict[str, ActArchiveAvgItemData]
