from enum import StrEnum

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
from ..common import BaseStruct


class PlayerRoguelikePendingEvent(BaseStruct):
    type: PlayerRoguelikePlayerEventType
    content: "PlayerRoguelikePendingEvent.Content"

    class BattleRewardContent(BaseStruct):
        rewards: list[RoguelikeReward]
        earn: RoguelikeStageEarn
        show: str
        state: int
        isPerfect: int

    class BattleContent(BaseStruct):
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

    class InitRecruitContent(BaseStruct):
        step: list[int]
        tickets: list[str]
        showChar: "list[PlayerRoguelikePendingEvent.InitRecruitContent.ShowChar]"
        team: str

        class ShowChar(BaseStruct):
            charId: str
            tmplId: str
            uniEquipIdOfChar: str
            type: RoguelikeCharState

    class InitRecruitSetContent(BaseStruct):
        step: list[int]
        option: list[str]

    class InitRelicContent(BaseStruct):
        step: list[int]
        items: dict[str, RoguelikeItemBundle]

    class InitModeRelic(BaseStruct):
        step: list[int]
        items: list[str]

    class InitTeam(BaseStruct):
        step: list[int]
        chars: "list[PlayerRoguelikePendingEvent.InitTeam.Char]"
        team: str

        class Char(BaseStruct):
            charId: str
            tmplId: str
            uniEquipIdOfChar: str
            type: RoguelikeCharState

    class InitSupport(BaseStruct):
        step: list[int]
        scene: "PlayerRoguelikePendingEvent.SceneContent"

    class InitExploreTool(BaseStruct):
        step: list[int]
        items: dict[str, RoguelikeItemBundle]

    class PlayerRoguelikeChoiceRewardType(StrEnum):
        NONE = "NONE"
        ITEM = "ITEM"
        MISSION = "MISSION"

    class ChoiceAddition(BaseStruct):
        rewards: "list[PlayerRoguelikePendingEvent.ChoiceAddition.Reward]"

        class Reward(BaseStruct):
            id: str
            type: "PlayerRoguelikePendingEvent.PlayerRoguelikeChoiceRewardType"

    class SceneContent(BaseStruct):
        id: str
        choices: dict[str, bool]
        choiceAdditional: dict[str, "PlayerRoguelikePendingEvent.ChoiceAddition"]

    class Recruit(BaseStruct):
        ticket: str

    class Dice(BaseStruct):
        result: "PlayerRoguelikePendingEvent.Dice.Result"
        rerollCount: int

        class Result(BaseStruct):
            diceEventId: str
            diceRoll: int
            mutation: "PlayerRoguelikePendingEvent.Dice.MutationResult"
            virtue: list[str]

        class MutationResult(BaseStruct):
            id: str
            chars: list[str]

    class ShopContent(BaseStruct):
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

        class Bank(BaseStruct):
            cost: int
            open: bool
            canPut: bool
            canWithdraw: bool
            withdraw: int
            withdrawLimit: int

        class Goods(BaseStruct):
            index: str
            itemId: str
            count: int
            priceId: str
            priceCount: int
            origCost: int
            displayPriceChg: bool

    class SacrificeContent(BaseStruct):
        type: RoguelikeSacrificeType
        priceId: str
        cost: int
        _choiceId: str

    class ExpeditionContent(BaseStruct):
        type: RoguelikeExpeditionType
        priceId: str
        cost: int
        _choiceId: str

    class EndingResult(BaseStruct):
        brief: "PlayerRoguelikePendingEvent.EndingBrief"
        record: "PlayerRoguelikePendingEvent.EndingRecord"

    class EndingBrief(BaseStruct):
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

    class EndingRecord(BaseStruct):
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

    class AlchemyContent(BaseStruct):
        canAlchemy: bool

    class UseStashedTicketContent(BaseStruct):
        count: int
        recruitCostAdd: int

    class AlchemyRewardContent(BaseStruct):
        items: list[RoguelikeItemBundle]
        isSSR: bool
        isFail: bool

    class SwapCopper(BaseStruct):
        newCopper: str

    class DrawCopper(BaseStruct):
        copper: list[str]
        divineEventId: str

    class Content(BaseStruct):
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
