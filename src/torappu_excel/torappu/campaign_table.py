from .campaign_const_table import CampaignConstTable
from .campaign_data import CampaignData
from .campaign_group_data import CampaignGroupData
from .campaign_mission_data import CampaignMissionData
from .campaign_region_data import CampaignRegionData
from .campaign_rotate_open_time_data import CampaignRotateOpenTimeData
from .campaign_training_all_open_time_data import CampaignTrainingAllOpenTimeData
from .campaign_training_open_time_data import CampaignTrainingOpenTimeData
from .campaign_zone_data import CampaignZoneData
from ..common import BaseStruct


class CampaignTable(BaseStruct):
    campaigns: dict[str, CampaignData]
    campaignGroups: dict[str, CampaignGroupData]
    campaignRegions: dict[str, CampaignRegionData]
    campaignZones: dict[str, CampaignZoneData]
    campaignMissions: dict[str, CampaignMissionData]
    stageIndexInZoneMap: dict[str, int]
    campaignConstTable: CampaignConstTable
    campaignRotateStageOpenTimes: list[CampaignRotateOpenTimeData]
    campaignTrainingStageOpenTimes: list[CampaignTrainingOpenTimeData]
    campaignTrainingAllOpenTimes: list[CampaignTrainingAllOpenTimeData]
