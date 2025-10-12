from pydantic import BaseModel, ConfigDict


class ReturnConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    startTime: int
    systemTab_time: int
    afkDays: int
    unlockLv: int
    unlockLevel: str
    juniorClear: bool
    ifvisitor: bool
    permMission_time: int
    needPoints: int
    defaultIntro: str
    pointId: str
