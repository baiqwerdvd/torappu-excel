from pydantic import BaseModel, ConfigDict

from .emoji_scene_type import EmojiSceneType


class EmoticonData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    emojiDataDict: dict[str, "EmoticonData.EmojiData"]
    emoticonThemeDataDict: dict[str, list[str]]

    class EmojiData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        type: EmojiSceneType
        sortId: int
        picId: str
        desc: str | None
