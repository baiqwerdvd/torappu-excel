from pydantic import BaseModel, ConfigDict, Field

from .act_archive_buff_data import ActArchiveBuffData
from .act_archive_capsule_data import ActArchiveCapsuleData
from .act_archive_challenge_book_data import ActArchiveChallengeBookData
from .act_archive_chaos_data import ActArchiveChaosData
from .act_archive_chat_data import ActArchiveChatData
from .act_archive_copper_data import ActArchiveCopperData
from .act_archive_disaster_data import ActArchiveDisasterData
from .act_archive_endbook_data import ActArchiveEndbookData
from .act_archive_fragment_data import ActArchiveFragmentData
from .act_archive_relic_data import ActArchiveRelicData
from .act_archive_totem_data import ActArchiveTotemData
from .act_archive_trap_data import ActArchiveTrapData
from .act_archive_wrath_data import ActArchiveWrathData


class RoguelikeArchiveComponentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    relic: ActArchiveRelicData
    capsule: ActArchiveCapsuleData | None
    trap: ActArchiveTrapData
    chat: ActArchiveChatData
    endbook: ActArchiveEndbookData
    buff: ActArchiveBuffData
    totem: ActArchiveTotemData | None
    chaos: ActArchiveChaosData | None
    wrath: ActArchiveWrathData | None
    copper: ActArchiveCopperData | None
    fragment: ActArchiveFragmentData | None = Field(default=None)
    disaster: ActArchiveDisasterData | None = Field(default=None)
    challengeBook: ActArchiveChallengeBookData | None = Field(default=None)
