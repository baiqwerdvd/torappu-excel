from pydantic import BaseModel, ConfigDict


class FifthAnnivExploreTargetData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    linkStageId: str
    targetValues: dict[str, int]
    lockedLevelId: str
    isEnd: bool
    name: str
    desc: str
    successDesc: str
    successIconId: str
    requireEventId: str | None
    endName: str | None
