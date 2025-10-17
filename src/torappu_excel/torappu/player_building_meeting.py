from .player_building_diysolution import PlayerBuildingDIYSolution
from .player_building_meeting_buff import PlayerBuildingMeetingBuff
from .player_building_meeting_clue import PlayerBuildingMeetingClue
from .player_building_meeting_info_share_state import PlayerBuildingMeetingInfoShareState
from .player_building_meeting_social_reward import PlayerBuildingMeetingSocialReward
from .player_building_message_leave import PlayerBuildingMessageLeave
from .player_room_state import PlayerRoomState
from ..common import BaseStruct


class PlayerBuildingMeeting(BaseStruct):
    buff: PlayerBuildingMeetingBuff
    state: PlayerRoomState
    processPoint: int
    speed: float
    ownStock: list[PlayerBuildingMeetingClue]
    receiveStock: list[PlayerBuildingMeetingClue]
    board: dict[str, str]
    socialReward: PlayerBuildingMeetingSocialReward
    received: int
    infoShare: PlayerBuildingMeetingInfoShareState
    lastUpdateTime: int
    dailyReward: PlayerBuildingMeetingClue
    mustgetClue: list[str]
    startApCounter: dict[str, int]
    mfc: dict[str, int]
    completeWorkTime: int
    presetQueue: list[list[int]]
    messageLeave: PlayerBuildingMessageLeave
    diySolution: PlayerBuildingDIYSolution
    expiredReward: int | None
    visitedUser: list[str] | None = None
