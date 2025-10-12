from pydantic import BaseModel, ConfigDict


class ActMultiV3ReportData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    sortId: int
    txt: str
    desc: str
