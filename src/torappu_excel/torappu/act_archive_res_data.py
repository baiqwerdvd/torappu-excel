from .act_archive_pic_type import ActArchivePicType
from ..common import BaseStruct, CustomIntEnum

from msgspec import field


class ActArchiveResData(BaseStruct):
    class ArchiveNewsLineType(CustomIntEnum):
        TextContent = "TextContent", 0
        ImageContent = "ImageContent", 1

    pics: dict[str, "ActArchiveResData.PicArchiveResItemData"]
    audios: dict[str, "ActArchiveResData.AudioArchiveResItemData"]
    avgs: dict[str, "ActArchiveResData.AvgArchiveResItemData"]
    stories: dict[str, "ActArchiveResData.StoryArchiveResItemData"]
    news: dict[str, "ActArchiveResData.NewsArchiveResItemData"]
    landmarks: dict[str, "ActArchiveResData.LandmarkArchiveResItemData"]
    logs: dict[str, "ActArchiveResData.LogArchiveResItemData"]
    challengeBooks: dict[str, "ActArchiveResData.ChallengeBookArchiveResItemData"]

    class PicArchiveResItemData(BaseStruct):
        id_: str = field(name="id")
        desc: str
        assetPath: str
        type_: ActArchivePicType = field(name="type")
        subType: str | None
        picDescription: str
        kvId: str | None

    class AudioArchiveResItemData(BaseStruct):
        id_: str = field(name="id")
        desc: str
        name: str

    class AvgArchiveResItemData(BaseStruct):
        id_: str = field(name="id")
        desc: str
        breifPath: str | None
        contentPath: str
        imagePath: str
        rawBrief: str | None
        titleIconPath: str | None

    class StoryArchiveResItemData(BaseStruct):
        id_: str = field(name="id")
        desc: str
        date: str | None
        pic: str
        text: str
        titlePic: str | None

    class NewsArchiveResItemData(BaseStruct):
        id_: str = field(name="id")
        desc: str
        newsType: str
        newsFormat: "ActArchiveResData.NewsFormatData"
        newsText: str
        newsAuthor: str
        paramP0: int
        paramK: int
        paramR: float
        newsLines: list["ActArchiveResData.ActivityNewsLine"]

    class NewsFormatData(BaseStruct):
        typeId: str
        typeName: str
        typeLogo: str
        typeMainLogo: str
        typeMainSealing: str

    class ActivityNewsLine(BaseStruct):
        lineType: "ActArchiveResData.ArchiveNewsLineType"
        content: str

    class LandmarkArchiveResItemData(BaseStruct):
        landmarkId: str
        landmarkName: str
        landmarkPic: str
        landmarkDesc: str
        landmarkEngName: str

    class LogArchiveResItemData(BaseStruct):
        logId: str
        logDesc: str

    class ChallengeBookArchiveResItemData(BaseStruct):
        storyId: str
        titleName: str
        storyName: str
        textId: str
