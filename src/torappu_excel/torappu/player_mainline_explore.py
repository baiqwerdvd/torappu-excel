from enum import StrEnum

from ..common import BaseStruct


class PlayerMainlineExplore(BaseStruct):
    game: "PlayerMainlineExplore.PlayerExploreGameContext | None"
    outer: "PlayerMainlineExplore.PlayerExploreOuterContext"

    class DecisionNodeType(StrEnum):
        NONE = "NONE"
        CHECK = "CHECK"
        EVENT = "EVENT"

    class PlayerExploreGameContext(BaseStruct):
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

    class PlayerExploreGameContextState(BaseStruct):
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

    class PlayerExploreGameContextNode(BaseStruct):
        type: "PlayerMainlineExplore.DecisionNodeType"
        event: "PlayerMainlineExplore.PlayerExploreGameContextNodeEvent"

    class PlayerExploreGameContextNodeEvent(BaseStruct):
        events: list[str]
        choices: "list[PlayerMainlineExplore.PlayerExploreGameContextNodeEventChoice]"

    class PlayerExploreGameContextNodeEventChoice(BaseStruct):
        eventId: str
        choiceId: str
        abilitiesDelta: dict[str, int]
        abilitiesCondition: dict[str, int]
        successRate: float

    class PlayerExploreGameContextMap(BaseStruct):
        display: "PlayerMainlineExplore.PlayerExploreGameContextMapDisplay"

    class PlayerExploreGameContextMapDisplay(BaseStruct):
        nodeSeed: int
        pathSeed: int
        controlPoints: "list[PlayerMainlineExplore.PlayerExploreGameContextMapControlPoint]"

    class PlayerExploreGameContextMapControlPoint(BaseStruct):
        stageId: str
        pos: "PlayerMainlineExplore.PlayerPosition"

    class PlayerPosition(BaseStruct):
        x: int | float
        y: int | float

    class PlayerExploreGameContextLog(BaseStruct):
        passEvents: list[str]
        passTargets: list[str]

    class PlayerExploreOuterContext(BaseStruct):
        isOpen: bool
        mission: dict[str, "PlayerMainlineExplore.PlayerExploreOuterContextMissionState"]
        lastGameResult: "PlayerMainlineExplore.PlayerExploreGameResult"
        historyPaths: "list[PlayerMainlineExplore.PlayerExploreOuterContextHistoryPath]"

    class PlayerExploreGameResult(BaseStruct):
        groupId: str
        groupCode: str
        heritageAbilities: dict[str, int]

    class PlayerExploreOuterContextMissionState(BaseStruct):
        state: int
        progress: list[int]

    class PlayerExploreOuterContextHistoryPath(BaseStruct):
        success: bool
        path: "PlayerMainlineExplore.PlayerExploreGameContextMapDisplay"
