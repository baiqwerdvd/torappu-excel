from pydantic import BaseModel, ConfigDict

from .rune_data import RuneData


class RuneTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    runeStages: list["RuneTable.RuneStageExtraData"]

    class PackedRuneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        points: float
        mutexGroupKey: str | None
        description: str | None
        runes: list[RuneData]

    class RuneStageExtraData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        runes: list["RuneTable.PackedRuneData"]
