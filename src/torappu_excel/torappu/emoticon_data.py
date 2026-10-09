from .emoji_scene_type import EmojiSceneType
from ..common import BaseStruct


class EmoticonData(BaseStruct):
    emojiDataDict: dict[str, "EmoticonData.EmojiData"]
    emoticonThemeDataDict: dict[str, list[str]]
    emoticonThemeTypeDict: dict[str, "EmoticonData.EmoticonThemeTypeData"]
    emoticonThemeReverseDict: dict[str, list[str]]

    class EmojiData(BaseStruct):
        id: str
        type: EmojiSceneType
        sortId: int
        picId: str
        desc: str | None

    class EmoticonThemeTypeData(BaseStruct):
        itemId: str
        sortId: int
        isBasic: bool
        isDyn: bool
        picSceneList: list[EmojiSceneType]
