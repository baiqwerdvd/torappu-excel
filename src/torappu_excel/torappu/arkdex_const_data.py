from .arkvent_range_data import ArkventRangeData
from .ping_cond import PingCond
from ..common import BaseStruct


class ArkdexConstData(BaseStruct):
    arkdexCreatureBagMaxNum: int
    arkdexCreatureBagAlertNum: int
    operatorTeamSize: int
    totalSquadCnt: int
    teamSlots: int
    teamSize: int
    maxTeamRarityCount: int
    soloCharacterLimit: int
    brawlCharacterLimit: int
    buildEntryMaxTime: float
    battleEntryMaxTime: float
    settleMaxTime: float
    pingConds: list[PingCond]
    maxLoadingTime: int
    deployPhaseTime: int
    deployPhaseHintTime: int
    battlePhaseTimeMax: int
    modeOperationRankTime: int
    petFollowPanelScale: float
    tradeRequestTime: int
    creaturedDisappearAlert: float
    creatureInteractRange: ArkventRangeData
    creatureInteractStyleId: str
    creatureDisplayNameId: str
    creatureHeadUpStyleId: str
