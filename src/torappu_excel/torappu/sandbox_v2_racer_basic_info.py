from pydantic import BaseModel, ConfigDict


class SandboxV2RacerBasicInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    racerId: str
    sortId: int
    racerName: str
    itemId: str
    attributeMaxValue: list[int]
