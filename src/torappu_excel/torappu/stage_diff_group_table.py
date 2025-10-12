from pydantic import BaseModel, ConfigDict


class StageDiffGroupTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    normalId: str
    toughId: str | None
    easyId: str
