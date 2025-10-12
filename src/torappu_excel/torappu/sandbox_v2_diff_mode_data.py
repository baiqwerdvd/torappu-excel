from pydantic import BaseModel, ConfigDict


class SandboxV2DiffModeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    title: str
    desc: str
    buffList: list[str]
    detailList: str
    sortId: int
