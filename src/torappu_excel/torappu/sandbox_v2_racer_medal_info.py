from pydantic import BaseModel, ConfigDict


class SandboxV2RacerMedalInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    medalId: str
    sortId: int
    name: str
    desc: str
    iconId: str
    smallIconId: str
