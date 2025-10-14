from pydantic import BaseModel, ConfigDict


class PlayerSettingPerf(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    lowPower: bool
