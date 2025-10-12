from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class SoundFXBank(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    name: str
    sounds: list["SoundFXBank.SoundFX"] | None
    maxSoundAllowed: int
    popOldest: bool
    customMixerGroup: str | None
    loop: bool
    mixerDesc: "MixerDesc | None"

    class SoundFX(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        asset: str
        weight: float
        important: bool
        is2D: bool
        delay: float
        minPitch: float
        maxPitch: float
        minVolume: float
        maxVolume: float
        ignoreTimeScale: bool

    class MixerDesc(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        category: "Category"
        customGroup: str
        important: bool

        class Category(StrEnum):
            NONE = "NONE"
            BATTLE = "BATTLE"
            UI = "UI"
            BUILDING = "BUILDING"
            GACHA = "GACHA"
            MISC = "MISC"
            ALL = "ALL"
