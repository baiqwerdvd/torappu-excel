from pydantic import BaseModel, ConfigDict


class ActArchiveCopperGildData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    gildTypeId: str
    gildName: str
    gildDesc: str
