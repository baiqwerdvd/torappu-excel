from pydantic import BaseModel, ConfigDict

from .emoticon_data import EmoticonData
from .guidebook_group_data import GuidebookGroupData
from .home_background_data import HomeBackgroundData
from .mail_archive_data import MailArchiveData
from .mail_sender_data import MailSenderData
from .name_card_v2_data import NameCardV2Data
from .player_avatar_data import PlayerAvatarData
from .story_variant_data import StoryVariantData


class DisplayMetaData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    playerAvatarData: PlayerAvatarData
    homeBackgroundData: HomeBackgroundData
    nameCardV2Data: NameCardV2Data
    mailArchiveData: MailArchiveData
    mailSenderData: MailSenderData
    emoticonData: EmoticonData
    storyVariantData: dict[str, StoryVariantData]
    guidebookGroupDatas: dict[str, GuidebookGroupData]
