from pydantic import BaseModel, ConfigDict


class Act4funValueEffectInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    valueEffectId: str
    effectParams: dict[str, int]
