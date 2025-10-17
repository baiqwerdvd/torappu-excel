from .auto_chess_game_state import AutoChessGameState
from .shared_consts import SharedConsts
from ..common import BaseStruct


class AutoChessGame(BaseStruct):
    startTs: str
    seed: int
    mode: str
    state: AutoChessGameState
    bandId: str
    talent: "list[AutoChessGame.Effect]"
    talentChoices: list[str]
    currForce: str
    allForces: dict[str, "AutoChessGame.AutoChessForce"]
    rewardEnemyRound: int
    health: "AutoChessGame.Health"
    turn: int
    roundId: str
    stageId: str
    store: "AutoChessGame.Store"
    table: "AutoChessGame.Table"
    buff: "AutoChessGame.Buff"

    class Effect(BaseStruct):
        instId: int
        effectId: str
        ts: int
        startRound: int

    class Health(BaseStruct):
        hp: int
        shield: int

    class Store(BaseStruct):
        lv: int
        coin: int
        isForzen: bool
        upgradePrice: int
        refreshPrice: int
        charGoods: dict[int, "AutoChessGame.AutoChessCharGoods"]
        trapGoods: dict[int, "AutoChessGame.AutoChessTrapGoods"]

    class Table(BaseStruct):
        chars: "list[AutoChessGame.AutoChessChar]"
        trap: "list[AutoChessGame.AutoChessTrap]"
        recruitCard: "AutoChessGame.Table.RecruitCard"
        spellUsing: dict[int, "AutoChessGame.Table.Spell"]
        gameInfo: "AutoChessGame.AutoChessGameInfo"

        class RecruitCard(BaseStruct):
            instId: int
            effect: "list[AutoChessGame.AutoChessCharGoods]"

        class Spell(BaseStruct):
            instId: int
            chessId: str
            startRound: int
            activated: bool

    class AutoChessGameInfo(BaseStruct):
        chessInstMap: dict[int, "AutoChessGame.AutoChessGameInfo.BattleChessInst"]

        class BattleChessInst(BaseStruct):
            instId: int
            isToken: bool
            dir: "SharedConsts.Direction"
            buildSeq: int

    class AutoChessCharGoods(BaseStruct):
        id: str
        price: int

    class AutoChessTrapGoods(BaseStruct):
        id: str
        price: int

    class AutoChessInst(BaseStruct):
        instId: int
        chessId: str
        overrideChessId: str

    class AutoChessTrap(BaseStruct):
        instId: int
        chessId: str
        overrideChessId: str

    class AutoChessChar(BaseStruct):
        equip: dict[int, "AutoChessGame.AutoChessTrap"]
        damage: int
        instId: int
        chessId: str
        overrideChessId: str

    class AutoChessForce(BaseStruct):
        forceId: str
        hp: int
        extraForce: list[str]
        effect: "list[AutoChessGame.Effect]"

    class Buff(BaseStruct):
        gainCoinCounter: dict[str, "AutoChessGame.Buff.GainCoinCounter"]
        killEnemyCounter: dict[str, "AutoChessGame.Buff.EnemyCounter"]
        chessPurchase: dict[str, int]
        speRefresh: "AutoChessGame.Buff.SpecialRefresh"
        battleLayers: dict[str, "list[AutoChessGame.Buff.BattleLayerEffect]"]
        equipCoinJar: dict[int, int]
        slotAdd: int
        effectShow: dict[int, "AutoChessGame.Buff.EffectShowItem"]

        class SpecialRefresh(BaseStruct):
            cnt: int

        class EnemyCounter(BaseStruct):
            base: int
            process: int

        class GainCoinCounter(BaseStruct):
            base: int
            reduce: int
            process: int

        class EffectShowItem(BaseStruct):
            leftCnt: int

        class BattleLayerEffect(BaseStruct):
            effectInst: int
            count: int
