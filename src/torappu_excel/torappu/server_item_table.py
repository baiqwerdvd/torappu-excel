from .activity_potential_character_info import ActivityPotentialCharacterInfo
from .ap_supply_feature import ApSupplyFeature
from .char_voucher_item_feature import CharVoucherItemFeature
from .exp_item_feature import ExpItemFeature
from .favor_character_info import FavorCharacterInfo
from .full_potential_character_info import FullPotentialCharacterInfo
from .item_data import ItemData
from .item_pack_info import ItemPackInfo
from .server_item_reminder_info import ServerItemReminderInfo
from .uni_collection_info import UniCollectionInfo
from ..common import BaseStruct

from msgspec import field


class ServerItemTable(BaseStruct):
    items: dict[str, ItemData]
    expItems: dict[str, ExpItemFeature]
    potentialItems: dict[str, dict[str, str]]
    apSupplies: dict[str, ApSupplyFeature]
    uniqueInfo: dict[str, int]
    itemTimeLimit: dict[str, int]
    uniCollectionInfo: dict[str, UniCollectionInfo]
    itemPackInfos: dict[str, ItemPackInfo]
    fullPotentialCharacters: dict[str, FullPotentialCharacterInfo]
    activityPotentialCharacters: dict[str, ActivityPotentialCharacterInfo]
    favorCharacters: dict[str, FavorCharacterInfo]
    reminderInfo: ServerItemReminderInfo | None = field(default=None)
    charVoucherItems: dict[str, CharVoucherItemFeature] | None = field(default=None)
