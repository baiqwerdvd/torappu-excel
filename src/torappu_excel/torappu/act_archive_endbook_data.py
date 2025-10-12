from pydantic import BaseModel, ConfigDict

from .act_archive_endbook_group_data import ActArchiveEndbookGroupData


class ActArchiveEndbookData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    endbook: dict[str, ActArchiveEndbookGroupData]
