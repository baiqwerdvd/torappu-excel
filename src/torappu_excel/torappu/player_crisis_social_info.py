from ..common import BaseStruct


class PlayerCrisisSocialInfo(BaseStruct):
    assistCnt: int
    maxPnt: str
    chars: "list[PlayerCrisisSocialInfo.AssistChar]"

    class AssistChar(BaseStruct):
        charId: str
        cnt: int
