from pydantic import BaseModel, ConfigDict


class CharMasterLevelData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    level: int
    name: str
    description: str
    conditionDesc: str
