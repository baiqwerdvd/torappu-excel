from .fifth_anniv_explore_broadcast_data import FifthAnnivExploreBroadcastData
from .fifth_anniv_explore_const import FifthAnnivExploreConst
from .fifth_anniv_explore_event_choice_data import FifthAnnivExploreEventChoiceData
from .fifth_anniv_explore_event_data import FifthAnnivExploreEventData
from .fifth_anniv_explore_group_data import FifthAnnivExploreGroupData
from .fifth_anniv_explore_mission_data import FifthAnnivExploreMissionData
from .fifth_anniv_explore_stage_data import FifthAnnivExploreStageData
from .fifth_anniv_explore_target_data import FifthAnnivExploreTargetData
from ..common import BaseStruct


class FifthAnnivExploreData(BaseStruct):
    exploreGroupData: dict[str, FifthAnnivExploreGroupData]
    exploreStageData: dict[str, FifthAnnivExploreStageData]
    exploreTargetData: dict[str, FifthAnnivExploreTargetData]
    exploreEventData: dict[str, FifthAnnivExploreEventData]
    exploreChoiceData: dict[str, FifthAnnivExploreEventChoiceData]
    broadcastData: dict[str, FifthAnnivExploreBroadcastData]
    exploreConst: FifthAnnivExploreConst
    missionData: dict[str, FifthAnnivExploreMissionData]
