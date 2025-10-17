from ..common import BaseStruct


class SoundFXCtrlBank(BaseStruct):
    name: str
    targetBank: str
    ctrlStop: bool
    ctrlStopFadetime: float
