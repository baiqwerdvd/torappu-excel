from ..common import BaseStruct


class Act4funSpLiveMatInfoData(BaseStruct):
    spLiveMatId: str
    spLiveEveId: str
    stageId: str
    name: str
    picId: str
    tagTxt: str
    emojiIcon: str
    accordingPerformId: str | None
    selectedPerformId: str | None
    valueEffectId: str
    accordingSuperChatId: str | None
