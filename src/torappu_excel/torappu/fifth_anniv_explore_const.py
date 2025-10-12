from pydantic import BaseModel, ConfigDict


class FifthAnnivExploreConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    prevRecordNum: int
    maxBoard: int
    valueMin: int
    valueMax: int
    targetStuckDesc: str
    stageStuckDesc: str
    missionName: str
    missionDesc: str
    choiceValueOrder: list[str]
    teamPassTargeDesc: str
    teamPassEndDesc: str
