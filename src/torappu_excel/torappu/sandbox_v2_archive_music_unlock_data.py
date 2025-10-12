from pydantic import BaseModel, ConfigDict


class SandboxV2ArchiveMusicUnlockData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    musicId: str
    unlockCondDesc: str | None
