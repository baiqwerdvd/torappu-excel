from pydantic import BaseModel, ConfigDict


class PlayerSpecialStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: str
    val: list[bool | list[int]]
    fts: int
    rts: int
