from pydantic import BaseModel, ConfigDict


class ActivityYear5GeneralConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rewPoint: int
    rewMainDesc: str
    rewApDesc: str
    rewEndDesc: str
    actPrimaryDesc: str
    actEntryDesc: str
    actSecondaryDesc: str
    actRewardDesc: str
    missionArchiveTopicId: str
    missionArchiveUnlockDesc: str
