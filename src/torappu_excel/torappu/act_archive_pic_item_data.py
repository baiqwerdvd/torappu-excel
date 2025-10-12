from pydantic import BaseModel, ConfigDict


class ActArchivePicItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    picId: str
    picSortId: int
