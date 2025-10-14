from pydantic import BaseModel, ConfigDict


class PlayerPerMedal(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    val: list[list[int]]
    fts: int
    rts: int
    reward: str | None = None
