from pydantic import BaseModel, ConfigDict


class ConditionalDropInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    template: str
    param: list[str]
    countLimit: int
