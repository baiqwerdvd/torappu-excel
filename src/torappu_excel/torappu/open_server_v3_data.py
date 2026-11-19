from .open_server_v3_check_in_group_data import OpenServerV3CheckInGroupData
from .open_server_v3_gift_package_data import OpenServerV3GiftPackageData
from .open_server_v3_milestone_group_data import OpenServerV3MilestoneGroupData
from .open_server_v3_mission_data import OpenServerV3MissionData
from .open_server_v3_mission_group_data import OpenServerV3MissionGroupData
from .open_server_v3_mission_type_desc_data import OpenServerV3MissionTypeDescData
from .open_server_v3_stage_campaign_data import OpenServerV3StageCampaignData
from .open_server_v3_story_recommend_data import OpenServerV3StoryRecommendData
from ..common import BaseStruct


class OpenServerV3Data(BaseStruct):
    checkInData: dict[str, OpenServerV3CheckInGroupData]
    missionData: dict[str, OpenServerV3MissionData]
    missionGroupData: dict[str, OpenServerV3MissionGroupData]
    missionTypeDescData: dict[str, OpenServerV3MissionTypeDescData]
    milestoneGroupData: dict[str, OpenServerV3MilestoneGroupData]
    giftPackageList: list[OpenServerV3GiftPackageData]
    stageCampaignData: list[OpenServerV3StageCampaignData]
    storyRecommendData: list[OpenServerV3StoryRecommendData]
