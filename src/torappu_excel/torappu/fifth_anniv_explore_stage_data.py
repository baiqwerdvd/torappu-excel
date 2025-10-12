from pydantic import BaseModel, ConfigDict


class FifthAnnivExploreStageData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    eventCount: int
    prevNodeCount: int
    stageNum: int
    stageEventNum: int
    stageDisplayNum: str
    name: str | None
    desc: str | None
    nextStageId: str | None
    stageFailureDescription: str | None
