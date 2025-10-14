from pydantic import BaseModel, ConfigDict


class PlayerZoneRecordMissionProcessData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    target: int
    value: int
