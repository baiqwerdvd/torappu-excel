from pydantic import BaseModel, ConfigDict, Field

from .act_archive_avg_data import ActArchiveAvgData
from .act_archive_challenge_book_data import ActArchiveChallengeBookData
from .act_archive_chapter_log_data import ActArchiveChapterLogData
from .act_archive_landmark_item_data import ActArchiveLandmarkItemData
from .act_archive_music_data import ActArchiveMusicData
from .act_archive_news_data import ActArchiveNewsData
from .act_archive_pic_data import ActArchivePicData
from .act_archive_story_data import ActArchiveStoryData
from .act_archive_timeline_data import ActArchiveTimelineData


class ActArchiveComponentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    timeline: ActArchiveTimelineData | None = Field(default=None)
    music: ActArchiveMusicData | None = Field(default=None)
    pic: ActArchivePicData | None = Field(default=None)
    story: ActArchiveStoryData | None = Field(default=None)
    avg: ActArchiveAvgData | None = Field(default=None)
    news: ActArchiveNewsData | None = Field(default=None)
    landmark: dict[str, ActArchiveLandmarkItemData] | None = Field(default=None)
    log: dict[str, ActArchiveChapterLogData] | None = Field(default=None)
    challengeBook: ActArchiveChallengeBookData | None = Field(default=None)
