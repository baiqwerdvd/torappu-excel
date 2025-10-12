from pydantic import BaseModel, ConfigDict


class ActMultiV3MapData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stageId: str
    modeId: str
    sortId: int
    missionIdList: list[str]
    displayEnemyIdList: list[str]
    previewIconId: str
