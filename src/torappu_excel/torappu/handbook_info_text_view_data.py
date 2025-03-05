from .data_unlock_type import DataUnlockTypeInt
from ..common import BaseStruct


class HandBookInfoTextViewData(BaseStruct):
    infoList: list["HandBookInfoTextViewData.InfoTextAudio"]
    unLockorNot: bool
    unLockType: DataUnlockTypeInt
    unLockParam: str
    unLockLevel: int
    unLockLevelAdditive: int
    unLockString: str

    class InfoTextAudio(BaseStruct):
        infoText: str
        audioName: str
