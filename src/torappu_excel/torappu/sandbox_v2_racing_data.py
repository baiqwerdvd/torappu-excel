from .sandbox_v2_racer_basic_info import SandboxV2RacerBasicInfo
from .sandbox_v2_racer_medal_info import SandboxV2RacerMedalInfo
from .sandbox_v2_racer_name_info import SandboxV2RacerNameInfo
from .sandbox_v2_racer_talent_info import SandboxV2RacerTalentInfo
from .sandbox_v2_racing_const_data import SandboxV2RacingConstData
from .sandbox_v2_racing_item_info import SandboxV2RacingItemInfo
from ..common import BaseStruct


class SandboxV2RacingData(BaseStruct):
    racerBasicInfo: dict[str, SandboxV2RacerBasicInfo]
    racerTalentInfo: dict[str, SandboxV2RacerTalentInfo]
    racerNameInfo: dict[str, SandboxV2RacerNameInfo]
    racerMedalInfo: dict[str, SandboxV2RacerMedalInfo]
    enemyItemMap: dict[str, str]
    racingItemInfo: dict[str, SandboxV2RacingItemInfo]
    constData: SandboxV2RacingConstData
