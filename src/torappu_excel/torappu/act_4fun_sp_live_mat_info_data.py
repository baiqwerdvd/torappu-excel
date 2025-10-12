from pydantic import BaseModel, ConfigDict


class Act4funSpLiveMatInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
