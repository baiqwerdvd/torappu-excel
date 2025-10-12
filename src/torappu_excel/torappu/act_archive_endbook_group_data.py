from pydantic import BaseModel, ConfigDict

from .act_archive_endbook_item_data import ActArchiveEndbookItemData


class ActArchiveEndbookGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    endId: str
    endingId: str
    sortId: int
    title: str
    cgId: str
    backBlurId: str
    cardId: str
    hasAvg: bool
    avgId: str
    clientEndbookItemDatas: list[ActArchiveEndbookItemData]
