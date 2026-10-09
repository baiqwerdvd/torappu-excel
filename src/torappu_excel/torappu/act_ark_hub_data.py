from .act_ark_hub_const_data import ActArkHubConstData
from .act_ark_hub_interactive_unit_data import ActArkHubInteractiveUnitData
from .act_ark_hub_menu_data import ActArkHubMenuData
from .act_ark_hub_module_data import ActArkHubModuleData
from .act_ark_hub_move_fix_data import ActArkHubMoveFixData
from .act_ark_hub_player_state_info_data import ActArkHubPlayerStateInfoData
from .act_ark_hub_reward_data import ActArkHubRewardData
from .act_arkhub_loading_tip_data import ActArkhubLoadingTipData
from .arkvent_move_preset_data import ArkventMovePresetData
from .common_report_player_data import CommonReportPlayerData
from ..common import BaseStruct


class ActArkHubData(BaseStruct):
    moduleData: ActArkHubModuleData
    interactiveUnitData: dict[str, ActArkHubInteractiveUnitData]
    enabledEmoticonThemeIdList: list[str]
    reportPlayerDataList: list[CommonReportPlayerData]
    menuData: dict[str, ActArkHubMenuData]
    constData: ActArkHubConstData
    moveFixData: dict[str, ActArkHubMoveFixData]
    movePresetData: dict[str, ArkventMovePresetData]
    skinPresetDict: dict[str, str]
    playerStateInfoData: dict[str, ActArkHubPlayerStateInfoData]
    rewardDataDict: dict[str, ActArkHubRewardData]
    spawnFxDurationDict: dict[str, float]
    loadingTipList: list[ActArkhubLoadingTipData]
