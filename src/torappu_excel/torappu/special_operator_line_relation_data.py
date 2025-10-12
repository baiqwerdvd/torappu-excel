from pydantic import BaseModel, ConfigDict


class SpecialOperatorLineRelationData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startPointList: list[str]
    endPointList: list[str]
