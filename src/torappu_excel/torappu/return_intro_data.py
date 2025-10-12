from pydantic import BaseModel, ConfigDict


class ReturnIntroData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    sort: int
    pubTime: int
    image: str
