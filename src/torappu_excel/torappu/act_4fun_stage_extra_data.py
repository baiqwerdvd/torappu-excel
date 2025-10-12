from pydantic import BaseModel, ConfigDict


class Act4funStageExtraData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    description: str
    valueIconId: str | None
