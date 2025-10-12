from pydantic import BaseModel, ConfigDict

from .act_archive_totem_type import ActArchiveTotemType


class ActArchiveTotemItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: ActArchiveTotemType
    enrollConditionId: str | None
    sortId: int
