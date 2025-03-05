from ..common import BaseStruct


class SoundFXBank(BaseStruct):
    name: str
    sounds: list["SoundFXBank.SoundFX"] | None
    maxSoundAllowed: int
    popOldest: bool
    customMixerGroup: str | None
    loop: bool

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
