from ..common import BaseStruct, CustomIntEnum


class Act38SideData(BaseStruct):
    class NpcDialogType(CustomIntEnum):
        NONE = "NONE", 0
        ENTER_PUZZLE = "ENTER_PUZZLE", 1
        PLATE_ERROR = "PLATE_ERROR", 2
        HINT_SUCC = "HINT_SUCC", 3
        HINT_FAIL = "HINT_FAIL", 4
        PUZZLE_SOLVED = "PUZZLE_SOLVED", 5

    class NpcEmoType(CustomIntEnum):
        NONE = "NONE", 0
        EMO_1 = "EMO_1", 1
        EMO_2 = "EMO_2", 2
        EMO_3 = "EMO_3", 3

    zoneAdditionDataMap: dict[str, "Act38SideData.Act38SideZoneAdditionData"]
    puzzleInfoMap: dict[str, "Act38SideData.Act38SidePuzzleInfo"]
    npcDialogList: list["Act38SideData.Act38SideNpcDialogData"]
    constData: "Act38SideData.ConstData"
    puzzleGroupFocusDataMap: dict[str, "Act38SideData.Act38SidePuzzleGroupFocusData"]

    class Act38SideZoneAdditionData(BaseStruct):
        zoneId: str
        unlockText: str

    class Act38SidePuzzleInfo(BaseStruct):
        puzzleId: str
        startTime: int
        puzzleGroupId: str

    class Act38SideNpcDialogData(BaseStruct):
        desc: str
        dialogType: "Act38SideData.NpcDialogType"
        emoSpineName: str

    class Act38SidePuzzleGroupFocusData(BaseStruct):
        puzzleGroupId: str
        xAxisFocusPos: float

    class ConstData(BaseStruct):
        npcIdleSpineName: str
        puzzleMapAnimGroupId: str
        puzzleCrossDayTrackId: str
        puzzleListText: str
        puzzleRewardNum: int
