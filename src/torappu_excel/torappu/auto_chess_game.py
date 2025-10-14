from pydantic import BaseModel, ConfigDict

from .auto_chess_game_state import AutoChessGameState
from .shared_consts import SharedConsts


class AutoChessGame(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Effect(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        instId: int
        effectId: str
        ts: int
        startRound: int

    class Health(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        hp: int
        shield: int

    class Store(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        lv: int
        coin: int
        isForzen: bool
        upgradePrice: int
        refreshPrice: int
        charGoods: dict[int, "AutoChessGame.AutoChessCharGoods"]
        trapGoods: dict[int, "AutoChessGame.AutoChessTrapGoods"]

    class Table(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        chars: "list[AutoChessGame.AutoChessChar]"
        trap: "list[AutoChessGame.AutoChessTrap]"
        recruitCard: "AutoChessGame.Table.RecruitCard"
        spellUsing: dict[int, "AutoChessGame.Table.Spell"]
        gameInfo: "AutoChessGame.AutoChessGameInfo"

        class RecruitCard(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            instId: int
            effect: "list[AutoChessGame.AutoChessCharGoods]"

        class Spell(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            instId: int
            chessId: str
            startRound: int
            activated: bool

    class AutoChessGameInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        chessInstMap: dict[int, "AutoChessGame.AutoChessGameInfo.BattleChessInst"]

        class BattleChessInst(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            instId: int
            isToken: bool
            dir: "SharedConsts.Direction"
            buildSeq: int

    class AutoChessCharGoods(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        price: int

    class AutoChessTrapGoods(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        price: int

    class AutoChessInst(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        instId: int
        chessId: str
        overrideChessId: str

    class AutoChessTrap(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        instId: int
        chessId: str
        overrideChessId: str

    class AutoChessChar(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        equip: dict[int, "AutoChessGame.AutoChessTrap"]
        damage: int
        instId: int
        chessId: str
        overrideChessId: str

    class AutoChessForce(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        forceId: str
        hp: int
        extraForce: list[str]
        effect: "list[AutoChessGame.Effect]"

    class Buff(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        gainCoinCounter: dict[str, "AutoChessGame.Buff.GainCoinCounter"]
        killEnemyCounter: dict[str, "AutoChessGame.Buff.EnemyCounter"]
        chessPurchase: dict[str, int]
        speRefresh: "AutoChessGame.Buff.SpecialRefresh"
        battleLayers: dict[str, "list[AutoChessGame.Buff.BattleLayerEffect]"]
        equipCoinJar: dict[int, int]
        slotAdd: int
        effectShow: dict[int, "AutoChessGame.Buff.EffectShowItem"]

        class SpecialRefresh(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            cnt: int

        class EnemyCounter(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            base: int
            process: int

        class GainCoinCounter(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            base: int
            reduce: int
            process: int

        class EffectShowItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            leftCnt: int

        class BattleLayerEffect(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            effectInst: int
            count: int
