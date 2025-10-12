from pydantic import BaseModel, ConfigDict


class ActMultiV3TitleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    order: int
    titleDesc: str
    isBack: bool
