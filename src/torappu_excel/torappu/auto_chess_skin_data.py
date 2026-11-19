from .auto_chess_skin_time_limit_info import AutoChessSkinTimeLimitInfo
from .auto_chess_skin_type import AutoChessSkinType
from .auto_chess_skin_voice_pack_type import AutoChessSkinVoicePackType
from .item_rarity import ItemRarity
from ..common import BaseStruct


class AutoChessSkinData(BaseStruct):
    id: str
    name: str
    type: AutoChessSkinType
    skinTrapId: str | None
    rarity: ItemRarity
    sortId: int
    isTimeLimit: bool
    thumbnailPicId: str
    previewPicId: str
    backgroundPreviewPicId: str
    voicePackType: AutoChessSkinVoicePackType
    voiceCv: str | None
    skinStartTime: int
    skinDesc: str
    usageDesc: str
    skinApproach: str
    timeLimitInfoList: dict[str, AutoChessSkinTimeLimitInfo]
