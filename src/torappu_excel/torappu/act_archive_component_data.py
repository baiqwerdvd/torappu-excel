from .act_archive_avg_data import ActArchiveAvgData
from .act_archive_challenge_book_data import ActArchiveChallengeBookData
from .act_archive_chapter_log_data import ActArchiveChapterLogData
from .act_archive_landmark_item_data import ActArchiveLandmarkItemData
from .act_archive_music_data import ActArchiveMusicData
from .act_archive_news_data import ActArchiveNewsData
from .act_archive_pic_data import ActArchivePicData
from .act_archive_story_data import ActArchiveStoryData
from .act_archive_timeline_data import ActArchiveTimelineData
from ..common import BaseStruct

from msgspec import field


class ActArchiveComponentData(BaseStruct):
    timeline: ActArchiveTimelineData | None = field(default=None)
    music: ActArchiveMusicData | None = field(default=None)
    pic: ActArchivePicData | None = field(default=None)
    story: ActArchiveStoryData | None = field(default=None)
    avg: ActArchiveAvgData | None = field(default=None)
    news: ActArchiveNewsData | None = field(default=None)
    landmark: dict[str, ActArchiveLandmarkItemData] | None = field(default=None)
    log: dict[str, ActArchiveChapterLogData] | None = field(default=None)
    challengeBook: ActArchiveChallengeBookData | None = field(default=None)
