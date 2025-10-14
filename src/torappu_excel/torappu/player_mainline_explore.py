from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class PlayerMainlineExplore(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    game: "PlayerMainlineExplore.PlayerExploreGameContext | None"
    outer: "PlayerMainlineExplore.PlayerExploreOuterContext"

    class DecisionNodeType(StrEnum):
        NONE = "NONE"
        CHECK = "CHECK"
        EVENT = "EVENT"

    class PlayerExploreGameContext(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        state: "PlayerMainlineExplore.PlayerExploreGameContextState"
        node: "PlayerMainlineExplore.PlayerExploreGameContextNode"
        map: "PlayerMainlineExplore.PlayerExploreGameContextMap"
        log: "PlayerMainlineExplore.PlayerExploreGameContextLog"

    class GameState(StrEnum):
        NONE = "NONE"
        WIN = "WIN"
        FINISH_NODE = "FINISH_NODE"
        BLOCKING = "BLOCKING"
        WAIT_CONFIRM = "WAIT_CONFIRM"
        FAIL = "FAIL"

    class PlayerExploreGameContextState(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        abilities: dict[str, int]
        groupId: str
        groupCode: str
        state: "PlayerMainlineExplore.GameState"
        targets: list[str]
        stageId: str
        nextStageId: str
        stageNodeIndex: int
        blockStageId: str
        broadCast: list[str]
        startTs: int

    class PlayerExploreGameContextNode(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: "PlayerMainlineExplore.DecisionNodeType"
        event: "PlayerMainlineExplore.PlayerExploreGameContextNodeEvent"

    class PlayerExploreGameContextNodeEvent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        events: list[str]
        choices: "list[PlayerMainlineExplore.PlayerExploreGameContextNodeEventChoice]"

    class PlayerExploreGameContextNodeEventChoice(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        eventId: str
        choiceId: str
        abilitiesDelta: dict[str, int]
        abilitiesCondition: dict[str, int]
        successRate: float

    class PlayerExploreGameContextMap(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        display: "PlayerMainlineExplore.PlayerExploreGameContextMapDisplay"

    class PlayerExploreGameContextMapDisplay(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        nodeSeed: int
        pathSeed: int
        controlPoints: "list[PlayerMainlineExplore.PlayerExploreGameContextMapControlPoint]"

    class PlayerExploreGameContextMapControlPoint(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        stageId: str
        pos: "PlayerMainlineExplore.PlayerPosition"

    class PlayerPosition(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        x: int | float
        y: int | float

    class PlayerExploreGameContextLog(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        passEvents: list[str]
        passTargets: list[str]

    class PlayerExploreOuterContext(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isOpen: bool
        mission: dict[str, "PlayerMainlineExplore.PlayerExploreOuterContextMissionState"]
        lastGameResult: "PlayerMainlineExplore.PlayerExploreGameResult"
        historyPaths: "list[PlayerMainlineExplore.PlayerExploreOuterContextHistoryPath]"

    class PlayerExploreGameResult(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        groupId: str
        groupCode: str
        heritageAbilities: dict[str, int]

    class PlayerExploreOuterContextMissionState(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        state: int
        progress: list[int]

    class PlayerExploreOuterContextHistoryPath(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        success: bool
        path: "PlayerMainlineExplore.PlayerExploreGameContextMapDisplay"
