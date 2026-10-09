from .roguelike_buoy_item_data import RoguelikeBuoyItemData
from .roguelike_grid_zone_focus_view_hint_data import RoguelikeGridZoneFocusViewHintData
from .roguelike_grid_zone_mission_banner_data import RoguelikeGridZoneMissionBannerData
from .roguelike_grid_zone_module_consts import RoguelikeGridZoneModuleConsts
from ..common import BaseStruct


class RoguelikeGridZoneModuleData(BaseStruct):
    zoneMissionBannerData: dict[str, RoguelikeGridZoneMissionBannerData]
    scrapSideBarStepZeroHintBannerData: dict[str, RoguelikeGridZoneFocusViewHintData]
    buoyItemDatas: dict[str, RoguelikeBuoyItemData]
    moduleConsts: RoguelikeGridZoneModuleConsts
