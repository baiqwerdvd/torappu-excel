from pydantic import BaseModel, ConfigDict


class Act4funLiveMatEffectInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    liveMatEffectId: str
    valueId: str
    performGroup: str
