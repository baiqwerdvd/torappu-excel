from pydantic import BaseModel, ConfigDict


class GuidebookConfigData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    configId: str
    sortId: int
    pageIdList: list[str]
