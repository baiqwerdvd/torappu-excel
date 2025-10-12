from pydantic import BaseModel, ConfigDict


class Act42SideConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    coffeeName: str
    dailyCoffee: int
    coffeeLimit: int
    coffeeContent: str
    minGunTaskDisplay: str
    unlockStageId: str
    toastGunTaskCompleted: str
    toastGunTaskLocked: str
    toastStageBlock: str
    toastEntryLocked: str
    toastFileLocked: str
    toastGunLocked: str
    toastNoCoffee: str
    toastOuterUnlock: str
