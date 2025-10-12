from pydantic import BaseModel, ConfigDict


class Act5funConst(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    storyStageId: str
    betStageId: str
    storyRoundnumber: int
    betRoundnumber: int
    initialFundStory: int
    initialFundBet: int
    minFundDrop: int
    maxFund: int
    selectTime: float | int
    npcCountInRound: int
    selectDescription: str
    selectLeftDescription: str
    selectRightDescription: str
    fundDescription: str
    confirmDescription: str
    loadingDescription: str
