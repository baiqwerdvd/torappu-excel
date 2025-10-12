from pydantic import BaseModel, ConfigDict


class Act4funPerformWordData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    text: str
    picId: str
    backgroundId: str
