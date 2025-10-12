from pydantic import BaseModel, ConfigDict


class SandboxV2RiftTeamBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    teamId: str
    teamName: str
    buffLevel: int
    buffDesc: str
    teamSmallIconId: str
    teamBigIconId: str
    teamDesc: str
    teamBgId: str
