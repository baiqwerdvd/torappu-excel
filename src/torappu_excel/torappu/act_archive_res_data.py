from pydantic import BaseModel, ConfigDict

from torappu_excel.common import CustomIntEnum

from .act_archive_pic_type import ActArchivePicType


class ActArchiveResData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class PicArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        desc: str
        assetPath: str
        type: ActArchivePicType
        subType: str | None
        picDescription: str
        kvId: str | None

    class AudioArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        desc: str
        name: str

    class AvgArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        desc: str
        breifPath: str | None
        contentPath: str
        imagePath: str
        rawBrief: str | None
        titleIconPath: str | None

    class StoryArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        desc: str
        date: str | None
        pic: str
        text: str
        titlePic: str | None

    class NewsArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        desc: str
        newsType: str
        newsFormat: "ActArchiveResData.NewsFormatData"
        newsText: str
        newsAuthor: str
        paramP0: int
        paramK: int
        paramR: float
        newsLines: list["ActArchiveResData.ActivityNewsLine"]

    class NewsFormatData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        typeId: str
        typeName: str
        typeLogo: str
        typeMainLogo: str
        typeMainSealing: str

    class ActivityNewsLine(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        lineType: "ActArchiveResData.ArchiveNewsLineType"
        content: str

    class LandmarkArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        landmarkId: str
        landmarkName: str
        landmarkPic: str
        landmarkDesc: str
        landmarkEngName: str

    class LogArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        logId: str
        logDesc: str

    class ChallengeBookArchiveResItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        storyId: str
        titleName: str
        storyName: str
        textId: str
