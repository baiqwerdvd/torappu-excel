from .art_gallery_collect_data import ArtGalleryCollectData
from .emoticon_data import EmoticonData
from .guidebook_group_data import GuidebookGroupData
from .home_background_data import HomeBackgroundData
from .magazine_leaf_data import MagazineLeafData
from .mail_archive_data import MailArchiveData
from .mail_sender_data import MailSenderData
from .name_card_v2_data import NameCardV2Data
from .pckey_data import PCKeyData
from .player_avatar_data import PlayerAvatarData
from .resolution_setting_item_data import ResolutionSettingItemData
from .sticker_data import StickerData
from .story_variant_data import StoryVariantData
from ..common import BaseStruct


class DisplayMetaData(BaseStruct):
    playerAvatarData: PlayerAvatarData
    homeBackgroundData: HomeBackgroundData
    nameCardV2Data: NameCardV2Data
    mailArchiveData: MailArchiveData
    mailSenderData: MailSenderData
    emoticonData: EmoticonData
    storyVariantData: dict[str, StoryVariantData]
    guidebookGroupDatas: dict[str, GuidebookGroupData]
    pcKeyData: PCKeyData
    resolutionSettingList: list[ResolutionSettingItemData]
    artGalleryCollectData: ArtGalleryCollectData
    magazineLeafData: MagazineLeafData
    stickerData: StickerData
