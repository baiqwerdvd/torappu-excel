from pydantic import BaseModel, ConfigDict


class ActArchiveAvgItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    avgId: str
    avgSortId: int
