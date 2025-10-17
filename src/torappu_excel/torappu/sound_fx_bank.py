from enum import StrEnum

from ..common import BaseStruct


class SoundFXBank(BaseStruct):
    name: str
    sounds: list["SoundFXBank.SoundFX"] | None
    maxSoundAllowed: int
    popOldest: bool
    customMixerGroup: str | None
    loop: bool
    mixerDesc: "MixerDesc | None"

    class SoundFX(BaseStruct):
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

    class MixerDesc(BaseStruct):
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
