from pydantic import BaseModel, ConfigDict

from .data_unlock_type import DataUnlockTypeInt


class HandBookInfoTextViewData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    infoList: list["HandBookInfoTextViewData.InfoTextAudio"]
    unLockorNot: bool
    unLockType: DataUnlockTypeInt
    unLockParam: str
    unLockLevel: int
    unLockLevelAdditive: int
    unLockString: str

    class InfoTextAudio(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        infoText: str
        audioName: str
