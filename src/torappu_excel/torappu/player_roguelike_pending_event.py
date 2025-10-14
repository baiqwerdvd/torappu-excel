from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .PlayerRoguelikeV2_CurrentData_Char import Char
from .player_roguelike_player_event_type import PlayerRoguelikePlayerEventType
from .roguelike_battle_fail_display import RoguelikeBattleFailDisplay
from .roguelike_buff import RoguelikeBuff
from .roguelike_char_state import RoguelikeCharState
from .roguelike_expedition_type import RoguelikeExpeditionType
from .roguelike_item_bundle import RoguelikeItemBundle
from .roguelike_reward import RoguelikeReward
from .roguelike_sacrifice_type import RoguelikeSacrificeType
from .roguelike_stage_earn import RoguelikeStageEarn
from .roguelike_topic_mode import RoguelikeTopicMode


class PlayerRoguelikePendingEvent(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: PlayerRoguelikePlayerEventType
    content: "PlayerRoguelikePendingEvent.Content"

    class BattleRewardContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rewards: list[RoguelikeReward]
        earn: RoguelikeStageEarn
        show: str
        state: int
        isPerfect: int

    class BattleContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        state: int
        chestCnt: int
        goldTrapCnt: int
        tmpChar: "list[Char]"
        unKeepBuff: list[RoguelikeBuff]
        diceRoll: list[int]
        sanity: int
        boxInfo: dict[str, int]
        isFailProtect: bool
        seed: int
        enemyHpInfo: dict[str, float]
        battleSnapshot: str
        battleFailDisplay: RoguelikeBattleFailDisplay

    class InitRecruitContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        step: list[int]
        tickets: list[str]
        showChar: "list[PlayerRoguelikePendingEvent.InitRecruitContent.ShowChar]"
        team: str

        class ShowChar(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            charId: str
            tmplId: str
            uniEquipIdOfChar: str
            type: RoguelikeCharState

    class InitRecruitSetContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        step: list[int]
        option: list[str]

    class InitRelicContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        step: list[int]
        items: dict[str, RoguelikeItemBundle]

    class InitModeRelic(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        step: list[int]
        items: list[str]

    class InitTeam(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        step: list[int]
        chars: "list[PlayerRoguelikePendingEvent.InitTeam.Char]"
        team: str

        class Char(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            charId: str
            tmplId: str
            uniEquipIdOfChar: str
            type: RoguelikeCharState

    class InitSupport(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        step: list[int]
        scene: "PlayerRoguelikePendingEvent.SceneContent"

    class InitExploreTool(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        step: list[int]
        items: dict[str, RoguelikeItemBundle]

    class PlayerRoguelikeChoiceRewardType(StrEnum):
        NONE = "NONE"
        ITEM = "ITEM"
        MISSION = "MISSION"

    class ChoiceAddition(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rewards: "list[PlayerRoguelikePendingEvent.ChoiceAddition.Reward]"

        class Reward(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            type: "PlayerRoguelikePendingEvent.PlayerRoguelikeChoiceRewardType"

    class SceneContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        choices: dict[str, bool]
        choiceAdditional: dict[str, "PlayerRoguelikePendingEvent.ChoiceAddition"]

    class Recruit(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        ticket: str

    class Dice(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        result: "PlayerRoguelikePendingEvent.Dice.Result"
        rerollCount: int

        class Result(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            diceEventId: str
            diceRoll: int
            mutation: "PlayerRoguelikePendingEvent.Dice.MutationResult"
            virtue: list[str]

        class MutationResult(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            chars: list[str]

    class ShopContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        bank: "PlayerRoguelikePendingEvent.ShopContent.Bank"
        id: str
        goods: "list[PlayerRoguelikePendingEvent.ShopContent.Goods]"
        canBattle: bool
        hasBoss: bool
        showRefresh: bool
        refreshCnt: int
        refreshCost: int
        recycleGoods: "list[PlayerRoguelikePendingEvent.ShopContent.Goods]"
        recycleCount: int

        class Bank(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            cost: int
            open: bool
            canPut: bool
            canWithdraw: bool
            withdraw: int
            withdrawLimit: int

        class Goods(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            index: str
            itemId: str
            count: int
            priceId: str
            priceCount: int
            origCost: int
            displayPriceChg: bool

    class SacrificeContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: RoguelikeSacrificeType
        priceId: str
        cost: int
        _choiceId: str

    class ExpeditionContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: RoguelikeExpeditionType
        priceId: str
        cost: int
        _choiceId: str

    class EndingResult(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        brief: "PlayerRoguelikePendingEvent.EndingBrief"
        record: "PlayerRoguelikePendingEvent.EndingRecord"

    class EndingBrief(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        level: int
        success: int
        ending: str
        failEnding: str
        theme: str
        mode: RoguelikeTopicMode
        predefined: str
        band: str
        startTs: int
        endTs: int
        endZoneId: str
        modeGrade: int
        seed: str
        activity: str

    class EndingRecord(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        cntZone: int
        relicList: list[str]
        capsuleList: list[str]
        activeToolList: list[str]
        charBuff: list[str]
        squadBuff: list[str]
        totemList: list[str]
        exploreToolList: list[str]
        fragmentList: list[str]
        copperCounter: dict[str, int]

    class AlchemyContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        canAlchemy: bool

    class UseStashedTicketContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        count: int
        recruitCostAdd: int

    class AlchemyRewardContent(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        items: list[RoguelikeItemBundle]
        isSSR: bool
        isFail: bool

    class SwapCopper(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        newCopper: str

    class DrawCopper(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        copper: list[str]
        divineEventId: str

    class Content(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        scene: "PlayerRoguelikePendingEvent.SceneContent"
        initRecruit: "PlayerRoguelikePendingEvent.InitRecruitContent"
        battle: "PlayerRoguelikePendingEvent.BattleContent"
        initRelic: "PlayerRoguelikePendingEvent.InitRelicContent"
        initRecruitSet: "PlayerRoguelikePendingEvent.InitRecruitSetContent"
        initModeRelic: "PlayerRoguelikePendingEvent.InitModeRelic"
        initTeam: "PlayerRoguelikePendingEvent.InitTeam"
        initSupport: "PlayerRoguelikePendingEvent.InitSupport"
        initExploreTool: "PlayerRoguelikePendingEvent.InitExploreTool"
        battleReward: "PlayerRoguelikePendingEvent.BattleRewardContent"
        recruit: "PlayerRoguelikePendingEvent.Recruit"
        dice: "PlayerRoguelikePendingEvent.Dice"
        shop: "PlayerRoguelikePendingEvent.ShopContent"
        result: "PlayerRoguelikePendingEvent.EndingResult"
        battleShop: "PlayerRoguelikePendingEvent.ShopContent"
        sacrifice: "PlayerRoguelikePendingEvent.SacrificeContent"
        expedition: "PlayerRoguelikePendingEvent.ExpeditionContent"
        detailStr: str
        popReport: bool
        alchemy: "PlayerRoguelikePendingEvent.AlchemyContent"
        alchemyReward: "PlayerRoguelikePendingEvent.AlchemyRewardContent"
        changeCopper: "PlayerRoguelikePendingEvent.SwapCopper"
        drawCopper: "PlayerRoguelikePendingEvent.DrawCopper"
        useStashedTicket: "PlayerRoguelikePendingEvent.UseStashedTicketContent"
        done: bool
