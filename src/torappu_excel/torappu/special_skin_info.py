from pydantic import BaseModel, ConfigDict


class SpecialSkinInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skinId: str
    startTime: int
    endTime: int
