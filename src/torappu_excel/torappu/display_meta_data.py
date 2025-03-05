from .home_background_data import HomeBackgroundData
from .mail_archive_data import MailArchiveData
from .mail_sender_data import MailSenderData
from .name_card_v2_data import NameCardV2Data
from .player_avatar_data import PlayerAvatarData
from ..common import BaseStruct


class DisplayMetaData(BaseStruct):
    playerAvatarData: PlayerAvatarData
    homeBackgroundData: HomeBackgroundData
    nameCardV2Data: NameCardV2Data
    mailArchiveData: MailArchiveData
    mailSenderData: MailSenderData
