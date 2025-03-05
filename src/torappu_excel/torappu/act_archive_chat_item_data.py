from ..common import BaseStruct


class ActArchiveChatItemData(BaseStruct):
    floor: int
    chatZoneId: str
    chatDesc: str | None
    chatStoryId: str
