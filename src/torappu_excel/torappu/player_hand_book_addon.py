from pydantic import BaseModel, ConfigDict, Field


class PlayerHandBookAddon(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stage: dict[str, "PlayerHandBookAddon.StageInfo"] = Field(default_factory=dict)
    story: dict[str, "PlayerHandBookAddon.GetInfo"]

    class GetInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        fts: int
        rts: int

    class StageInfo(GetInfo):
        startTimes: int
        completeTimes: int
        state: int
        startTime: int | None = None
