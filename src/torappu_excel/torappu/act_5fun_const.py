from ..common import BaseStruct


class Act5funConst(BaseStruct):
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
