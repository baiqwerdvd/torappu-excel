from pydantic import BaseModel, ConfigDict


class Act42SideGunData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    gunId: str
    gunName: str
    trustorName: str
    gunContent: str
    gunSmallIcon: str
    gunWhiteIcon: str
    gunColorIcon: str
