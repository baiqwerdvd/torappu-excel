from .emoji_scene_type import EmojiSceneType
from ..common import BaseStruct


class EmoticonData(BaseStruct):
    emojiDataDict: dict[str, "EmoticonData.EmojiData"]
    emoticonThemeDataDict: dict[str, str]

    class EmojiData(BaseStruct):
        id: str
        type: EmojiSceneType
        sortId: int
        picId: str
        desc: str
