from pydantic import BaseModel, ConfigDict


class AprilFoolConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    battleFinishLoseDes: str
    killEnemyDes: str
    killBossDes: str
    totalTime: str
