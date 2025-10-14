from enum import IntEnum, StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict

from .act_multi_v3_match_pos_type import ActMultiV3MatchPosType
from .auto_chess_game import AutoChessGame
from .avatar_info import AvatarInfo
from .cart_competition_rank import CartCompetitionRank
from .firework_data import FireworkData
from .item_bundle import ItemBundle
from .item_type import ItemType
from .jobject import JObject
from .mile_stone_player_info import MileStonePlayerInfo
from .player_squad import PlayerSquad
from .player_squad_item import PlayerSquadItem
from .player_squad_tmpl import PlayerSquadTmpl
from .player_stage_state import PlayerStageState
from .shared_char_data import SharedCharData


class PlayerActivity(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    DEFAULT: dict[str, "PlayerActivity.PlayerDefaultActivity"]
    MISSION_ONLY: dict[str, "PlayerActivity.PlayerMissionOnlyTypeActivity"]
    CHECKIN_ONLY: dict[str, "PlayerActivity.PlayerCheckinOnlyTypeActivity"]
    CHECKIN_ALL_PLAYER: dict[str, "PlayerActivity.PlayerCheckinAllTypeActivity"]
    CHECKIN_VS: dict[str, "PlayerActivity.PlayerCheckinVsTypeActivity"]
    COLLECTION: dict[str, "PlayerActivity.PlayerCollectionTypeActivity"]
    AVG_ONLY: dict[str, "PlayerActivity.PlayerAVGOnlyTypeActivity"]
    LOGIN_ONLY: dict[str, "PlayerActivity.PlayerLoginOnlyTypeActivity"]
    MINISTORY: dict[str, "PlayerActivity.PlayerMiniStoryActivity"]
    ROGUELIKE: dict[str, "PlayerActivity.PlayerRoguelikeActivity"]
    SANDBOX: dict[str, "PlayerActivity.PlayerActSandbox"]
    PRAY_ONLY: dict[str, "PlayerActivity.PlayerPrayOnlyActivity"]
    FLIP_ONLY: dict[str, "PlayerActivity.PlayerFlipOnlyActivity"]
    MULTIPLAY: dict[str, "PlayerActivity.PlayerMultiplayActivity"]
    MULTIPLAY_VERIFY2: dict[str, "PlayerActivity.PlayerMultiplayV2Activity"]
    MULTIPLAY_V3: dict[str, "PlayerActivity.PlayerMultiV3Activity"]
    INTERLOCK: dict[str, "PlayerActivity.PlayerInterlockActivity"]
    TYPE_ACT3D0: dict[str, "PlayerActivity.PlayerAct3D0Activity"]
    TYPE_ACT4D0: dict[str, "PlayerActivity.PlayerAct4D0Activity"]
    TYPE_ACT5D0: dict[str, "PlayerActivity.PlayerAct5D0Activity"]
    TYPE_ACT5D1: dict[str, "PlayerActivity.PlayerAct5D1Activity"]
    TYPE_ACT9D0: dict[str, "PlayerActivity.PlayerAct9D0Activity"]
    TYPE_ACT17D7: dict[str, "PlayerActivity.PlayerAct17D7Activity"]
    TYPE_ACT38D1: dict[str, "PlayerActivity.PlayerAct38D1Activity"]
    TYPE_ACT12SIDE: dict[str, "PlayerActivity.PlayerAct12sideActivity"]
    TYPE_ACT13SIDE: dict[str, "PlayerActivity.PlayerAct13sideActivity"]
    GRID_GACHA: dict[str, "PlayerActivity.PlayerGridGachaActivity"]
    GRID_GACHA_V2: dict[str, JObject]
    APRIL_FOOL: dict[str, "PlayerActivity.PlayerAprilFoolActivity"]
    TYPE_ACT17SIDE: dict[str, "PlayerActivity.PlayerAct17SideActivity"]
    BOSS_RUSH: dict[str, "PlayerActivity.PlayerBossRushActivity"]
    ENEMY_DUEL: dict[str, "PlayerActivity.PlayerEnemyDuelActivity"]
    VEC_BREAK_V2: dict[str, "PlayerActivity.PlayerVecBreakV2"]
    ARCADE: dict[str, "PlayerActivity.PlayerArcadeActivity"]
    TYPE_ACT20SIDE: dict[str, "PlayerActivity.PlayerAct20SideActivity"]
    FLOAT_PARADE: dict[str, "PlayerActivity.PlayerActFloatParadeActivity"]
    TYPE_ACT21SIDE: dict[str, "PlayerActivity.PlayerAct21SideActivity"]
    MAIN_BUFF: dict[str, "PlayerActivity.PlayerActMainlineBuff"]
    TYPE_ACT24SIDE: dict[str, "PlayerActivity.PlayerAct24SideActivity"]
    TYPE_ACT25SIDE: dict[str, "PlayerActivity.PlayerAct25SideActivity"]
    SWITCH_ONLY: dict[str, "PlayerActivity.PlayerSwitchOnlyActivity"]
    TYPE_ACT27SIDE: dict[str, "PlayerActivity.PlayerAct27SideActivity"]
    UNIQUE_ONLY: dict[str, "PlayerActivity.PlayerUniqueOnlyActivity"]
    MAINLINE_BP: dict[str, JObject]
    TYPE_ACT42D0: dict[str, "PlayerActivity.PlayerAct42D0Activity"]
    TYPE_ACT29SIDE: dict[str, "PlayerActivity.PlayerAct29SideActivity"]
    BLESS_ONLY: dict[str, "PlayerActivity.PlayerBlessOnlyActivity"]
    CHECKIN_ACCESS: dict[str, JObject]
    YEAR_5_GENERAL: dict[str, "PlayerActivity.PlayerYear5GeneralActivity"]
    TYPE_ACT35SIDE: dict[str, "PlayerActivity.PlayerAct35SideActivity"]
    TYPE_ACT36SIDE: dict[str, "PlayerActivity.PlayerAct36SideActivity"]
    TYPE_ACT38SIDE: dict[str, "PlayerActivity.PlayerAct38SideActivity"]
    AUTOCHESS_VERIFY1: dict[str, "PlayerActivity.PlayerAutoChessV1Activity"]
    CHECKIN_VIDEO: dict[str, JObject]
    TYPE_MAINSS: dict[str, "PlayerActivity.PlayerActMainSSActivity"]
    TYPE_ACT42SIDE: dict[str, "PlayerActivity.PlayerAct42SideActivity"]
    TYPE_ACT44SIDE: dict[str, "PlayerActivity.PlayerAct44SideActivity"]
    HALFIDLE_VERIFY1: dict[str, "PlayerActivity.PlayerAct1VHalfIdleActivity"]
    TYPE_ACT45SIDE: dict[str, "PlayerActivity.PlayerAct45SideActivity"]
    TEAM_QUEST: dict[str, JObject] | None = None
    RECRUIT_ONLY: dict[str, "PlayerActivity.PlayerRecruitOnlyAct"] | None = None
    VEC_BREAK: Any  # TODO: 临时占位

    class PlayerDefaultActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        shop: dict[str, int]

    class PlayerMissionOnlyTypeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        pass

    class PlayerCheckinOnlyTypeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        history: list[int]
        dynOpt: list[str]
        extraHistory: list[int]

    class PlayerCheckinVsTypeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        sweetVote: int
        saltyVote: int
        canVote: bool
        todayVoteState: int
        voteRewardState: int
        signedCnt: int
        availSignCnt: int
        socialState: int
        actDay: int

    class PlayerCheckinAllTypeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        history: list[int]
        allRecord: dict[str, int]
        allRewardStatus: dict[str, int]
        personalRecord: dict[str, int]

    class MilestoneInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        point: int
        got: list[str]

    class PlayerCollectionTypeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        point: dict[str, int]
        history: dict[str, "PlayerActivity.PlayerCollectionTypeActivity.PlayerCollectionInfo"]

        class PlayerCollectionInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            ts: str

    class PlayerAVGOnlyTypeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isOpen: bool

    class PlayerLoginOnlyTypeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        reward: int

    class PlayerMiniStoryActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        favorList: list[str]

    class PlayerRoguelikeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        buffToken: int
        milestone: "PlayerActivity.PlayerRoguelikeActivity.MileStone"
        game: "PlayerActivity.PlayerRoguelikeActivity.GameStatus"

        class MileStone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            token: int
            got: dict[str, int]

        class GameStatus(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            lastTs: int

    class PlayerActSandbox(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        map: "PlayerActivity.PlayerActSandbox.Map"
        status: "PlayerActivity.PlayerActSandbox.GameStatus"
        game: "PlayerActivity.PlayerActSandbox.Game"
        bag: dict[str, dict[str, int]]
        cook: "PlayerActivity.PlayerActSandbox.Cook"
        build: "PlayerActivity.PlayerActSandbox.Build"
        stage: dict[str, "PlayerActivity.PlayerActSandbox.NodeStage"]
        event: dict[str, "PlayerActivity.PlayerActSandbox.NodeEvent"]
        npc: dict[str, list["PlayerActivity.PlayerActSandbox.Npc"]]
        enemy: "PlayerActivity.PlayerActSandbox.MapEnemyData"
        mission: dict[str, "PlayerActivity.PlayerActSandbox.Mission"]
        troop: "PlayerActivity.PlayerActSandbox.TroopData"
        tech: "PlayerActivity.PlayerActSandbox.Tech"
        box: "PlayerActivity.PlayerActSandbox.Box"
        bank: "PlayerActivity.PlayerActSandbox.Bank"
        trigger: "PlayerActivity.PlayerActSandbox.Trigger"
        task: "PlayerActivity.PlayerActSandbox.Task"
        milestone: "PlayerActivity.PlayerActSandbox.Milestone"

        class Map(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            zone: dict[str, "PlayerActivity.PlayerActSandbox.Map.Zone"]
            node: dict[str, "PlayerActivity.PlayerActSandbox.Map.Node"]

            class Zone(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                weather: int

            class Node(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                zone: str
                tag: int
                type: int
                state: int
                relate: "PlayerActivity.PlayerActSandbox.Map.Node.NodeRelate"
                weather: "PlayerActivity.PlayerActSandbox.Map.Node.NodeWeather"
                stageId: str

                class NodeRelate(BaseModel):
                    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                    adj: list[str]
                    layer: int
                    angle: float | int
                    depth: int

                class NodeWeather(BaseModel):
                    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                    level: int

        class GameStatus(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: int
            flag: "PlayerActivity.PlayerActSandbox.GameStatus.GameFlag"

            class GameFlag(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                guide: int

        class Game(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            day: int
            totalDay: int
            ap: int
            maxAp: int
            initCharCount: int
            crossDay: "PlayerActivity.PlayerActSandbox.Game.CrossDay | None"
            settleType: int
            ts: int

            class CrossDay(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                enemyRushNew: list[str]
                enemyRushMove: dict[str, str]
                trapRewards: list["PlayerActivity.PlayerActSandbox.Game.CrossDay.SandboxRewardItem"]
                missionRewards: list["PlayerActivity.PlayerActSandbox.Game.CrossDay.SandboxRewardItem"]
                missionIds: list[str]
                vagabond: dict[str, int]

                class SandboxRewardItem(BaseModel):
                    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                    id: str
                    type: str
                    count: int

        class Cook(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            water: int
            foodSum: int
            cookbook: dict[str, int]
            food: dict[str, "PlayerActivity.PlayerActSandbox.Cook.Food"]

            class Food(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                itemId: str
                minorBuff: list[str]
                count: int

        class Build(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            blueprint: dict[str, int]
            building: dict[str, int]
            tactical: dict[str, int]

        class NodeStage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: int
            view: str
            id: str | None
            nest: list["PlayerActivity.PlayerActSandbox.NodeStage.Nest"] | None
            cave: list["PlayerActivity.PlayerActSandbox.NodeStage.Cave"] | None
            base: list["PlayerActivity.PlayerActSandbox.NodeStage.BaseInfo"] | None
            enemy: list["PlayerActivity.PlayerActSandbox.NodeStage.Enemy"] | None
            building: list["PlayerActivity.PlayerActSandbox.NodeStage.Building"] | None
            trap: list["PlayerActivity.PlayerActSandbox.NodeStage.Trap"] | None
            action: list[list[int]] | None

            class BaseInfo(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                key: str
                pos: list[int]
                isDead: int
                hpRatio: int

            class EntityStatus(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                key: str
                pos: list[int]
                isDead: int
                hpRatio: int

            class Nest(EntityStatus):
                pass

            class Cave(EntityStatus):
                pass

            class Enemy(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                key: str
                count: list[int]

            class Building(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                key: str
                pos: list[int]
                hpRatio: int
                direction: int

            class Trap(EntityStatus):
                count: list[int] | None
                extraParam: int | None

        class NodeEvent(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            eventList: list["PlayerActivity.PlayerActSandbox.NodeEvent.Event"]
            originId: str

            class Event(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                id: str
                enter: str
                state: bool | int
                scene: str | None

        class Npc(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            life: int
            skillId: int
            startDialog: str | None
            npcDialog: str | None

        class MapEnemyData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            enemyRush: dict[str, "PlayerActivity.PlayerActSandbox.MapEnemyData.EnemyRush"]
            rareAnimal: dict[str, "PlayerActivity.PlayerActSandbox.MapEnemyData.RareAnimal"]

            class EnemyRush(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                path: list[str]
                groupKey: str
                days: int
                enemyRushType: int
                enemy: dict[str, list[int]]
                boss: dict[str, "PlayerActivity.PlayerActSandbox.MapEnemyData.EnemyRush.RushBossStatus"] | None

                class RushBossStatus(BaseModel):
                    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                    hpRatio: int
                    modeIndex: int

            class RareAnimal(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                nodeId: str
                enemyId: str
                enemyGroupKey: str
                life: int

        class Mission(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            missionId: str
            days: int
            charList: list[int]

        class TroopData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            charAp: dict[str, int]
            todayAddAp: list[str | int]
            charFood: dict[str | int, "PlayerActivity.PlayerActSandbox.TroopData.CharFood"]

            class CharFood(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                itemId: str
                minorBuff: list[str]
                ts: int

        class Tech(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            techs: list[str]
            researchTechs: list[str]
            researchTasks: dict[str, list[int]]
            token: int
            cent: int

        class Box(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            enabled: bool
            foods: dict[str, "PlayerActivity.PlayerActSandbox.Box.Food"]
            items: dict[str, dict[str, int]]
            cap: int
            day: int

            class Food(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                itemId: str
                minorBuff: list[str]
                count: int

        class Bank(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            enabled: bool
            count: int
            ratio: int

        class Trigger(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            flag: dict[str, int]

        class Task(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            token: dict[str, int]

        class Milestone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

    class PlayerPrayOnlyActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        lastTs: int
        extraCount: int
        prayDaily: int
        prayMaxIndex: int
        praying: bool
        prayArray: "list[PlayerActivity.PlayerPrayOnlyActivity.RewardInfo]"

        class RewardInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            index: int
            count: int

    class PlayerSwitchOnlyActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rewards: dict[str, int]

    class PlayerFlipOnlyActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        raffleCount: int
        todayRaffleCount: int
        remainingRaffleCount: int
        luckyToday: bool
        normalRewards: dict[int, "PlayerActivity.PlayerFlipOnlyActivity.ActFlipItemBundle"]
        grandStatus: int

        class ActFlipItemBundle(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            type: str
            count: int
            ts: int
            prizeId: str

    class PlayerGridGachaActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        lastDay: bool
        firstDay: bool
        openedPosition: list[int]
        openedType: int
        rewardCount: int
        grandPositions: list[int]

    class PlayerMultiplayActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        troop: dict[str, "PlayerActivity.PlayerMultiplayActivity.Troop"]
        stages: dict[str, "PlayerActivity.PlayerMultiplayActivity.Stage"]

        class Troop(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            init: int
            squads: list[PlayerSquad]

        class Stage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            state: PlayerStageState
            completeTimes: int

    class PlayerMultiplayV2Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        squads: "PlayerActivity.PlayerMultiplayV2Activity.Squads"
        dailyMission: "PlayerActivity.PlayerMultiplayV2Activity.DailyMission"
        milestone: "PlayerActivity.PlayerMultiplayV2Activity.MilestoneInfo"
        stage: dict[str, "PlayerActivity.PlayerMultiplayV2Activity.StageInfo"]
        match: "PlayerActivity.PlayerMultiplayV2Activity.Match"
        globalBan: bool

        class PlayerMultiplayV2SquadItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            instId: int
            charInstId: int
            currentTmpl: str
            tmpl: dict[str, PlayerSquadTmpl]

        class Squads(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            prefer: "list[PlayerActivity.PlayerMultiplayV2Activity.PlayerMultiplayV2SquadItem]"
            backup: "list[PlayerActivity.PlayerMultiplayV2Activity.PlayerMultiplayV2SquadItem]"

        class DailyMissionState(StrEnum):
            NOT_CLAIM = "NOT_CLAIM"
            CLAIMED = "CLAIMED"

        class DailyMission(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            process: int
            state: "PlayerActivity.PlayerMultiplayV2Activity.DailyMissionState"

        class StageState(StrEnum):
            LOCK = "LOCK"
            UNLOCKED = "UNLOCKED"

        class StageInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            score: int
            state: "PlayerActivity.PlayerMultiplayV2Activity.StageState"
            startTimes: int
            completeTimes: int

        class Match(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            beMentorCnt: int
            lockMentor: bool
            bannedUntilTs: int

        class MilestoneInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

    class PlayerMultiV3Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        collection: "PlayerActivity.PlayerMultiV3Activity.Collection"
        troop: "PlayerActivity.PlayerMultiV3Activity.Troop"
        match: "PlayerActivity.PlayerMultiV3Activity.MatchInfo"
        milestone: "PlayerActivity.PlayerMultiV3Activity.Milestone"
        daily: "PlayerActivity.PlayerMultiV3Activity.Daily"
        stage: dict[str, "PlayerActivity.PlayerMultiV3Activity.StageInfo"]
        scene: "PlayerActivity.PlayerMultiV3Activity.Scene"
        globalBan: bool

        class Collection(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            info: "PlayerActivity.PlayerMultiV3Activity.CollectionInfo"
            title: "PlayerActivity.PlayerMultiV3Activity.Title"
            photo: "PlayerActivity.PlayerMultiV3Activity.Photo"

        class CollectionInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            finishCnt: int
            mentorCnt: int
            likeCnt: int

        class Title(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            unlock: list[str]
            select: list[str]

        class Photo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            template: dict[str, dict[str, "PlayerActivity.PlayerMultiV3Activity.PhotoInstance"]]
            album: dict[str, "PlayerActivity.PlayerMultiV3Activity.Album"]

        class PhotoInstance(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            players: "PlayerActivity.PlayerMultiV3Activity.PhotoPlayerInfo"
            chars: "list[PlayerActivity.PlayerMultiV3Activity.PhotoCharInfo]"
            stageId: str
            ts: int

        class PhotoPlayerInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            mine: "PlayerActivity.PlayerMultiV3Activity.PhotoSelfInfo"
            mate: "PlayerActivity.PlayerMultiV3Activity.PhotoAssistInfo"

        class PhotoSelfInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            title: list[str]

        class PhotoAssistInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            uid: str
            sameChannel: bool
            title: list[str]
            nickName: str
            avatar: AvatarInfo
            level: int
            nameCardSkinId: str
            nameCardSkinTmpl: int

        class PhotoCharInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            charId: str
            currentTmpl: str
            skinId: str
            slotIdx: int
            frame: int
            flip: bool

        class Album(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            commit: bool
            slot: dict[str, str]

        class Troop(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            buff: "PlayerActivity.PlayerMultiV3Activity.TroopBuff"
            squads: dict[str, "PlayerActivity.PlayerMultiV3Activity.Squad"]

        class TroopBuff(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            unlock: list[str]
            coin: int
            star: int

        class Squad(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            prefer: "list[PlayerActivity.PlayerMultiV3Activity.SquadItem]"
            backup: "list[PlayerActivity.PlayerMultiV3Activity.SquadItem]"
            buffId: str

        class SquadItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            innerInstId: int
            charInstId: int
            currentTmpl: str
            tmpl: dict[str, PlayerSquadTmpl]

        class StageInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            star: int
            exScore: int
            matchTimes: int
            startTimes: int
            finishTimes: int

        class MatchInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            bannedUntilTs: int
            lastModeList: list[str]
            lastMentorType: ActMultiV3MatchPosType
            lastReverse: int

        class Milestone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class Daily(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            process: int
            state: int

        class Scene(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            lastMate: list[str]

    class PlayerInterlockActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestoneCoin: int
        milestoneGot: list[str]
        specialDefendStageId: str
        defend: dict[str, "list[PlayerActivity.PlayerInterlockActivity.DefendCharData]"]
        squad: dict[str, list[PlayerSquadItem]]

        class DefendCharData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            charInstId: int
            currentTmpl: str

    class PlayerAct3D0Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        faction: str
        gachaCoin: int
        ticket: int
        clue: dict[str, int]
        box: dict[str, "PlayerActivity.PlayerAct3D0Activity.BoxState"]
        milestone: "PlayerActivity.PlayerAct3D0Activity.MileStone"
        favorList: list[str]

        class BoxState(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            content: dict[str, int]

        class MileStone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            rewards: dict[str, int]

    class PlayerAct4D0Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        story: dict[str, int]
        milestone: "PlayerActivity.PlayerAct4D0Activity.MileStone"

        class MileStone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            rewards: dict[str, int]

    class PlayerAct5D0Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        point_reward: MileStonePlayerInfo

    class PlayerAct5D1Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        pt: int
        shop: "PlayerActivity.PlayerAct5D1Activity.PlayerAct5D1Shop"
        runeStage: dict[str, "PlayerActivity.PlayerAct5D1Activity.PlayerActRuneStage"]
        stageEnemy: dict[str, list[str]]

        class PlayerAct5D1Shop(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            info: dict[str, int]
            progressInfo: dict[str, "PlayerActivity.PlayerAct5D1Activity.PlayerAct5D1Shop.ProgressInfo"]

            class ProgressInfo(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                count: int
                order: int

        class PlayerActRuneStage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            schedule: str
            available: int
            scores: int
            rune: dict[str, int]

    class PlayerAct9D0Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        favorList: list[str]
        news: dict[str, int]
        campaignCnt: int

    class PlayerAct12sideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        campaignCnt: int
        favorList: list[str]
        milestone: "PlayerActivity.PlayerAct12sideActivity.MilestoneInfo"
        charm: "PlayerActivity.PlayerAct12sideActivity.CharmInfo"

        class MilestoneInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class CharmInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            recycleStack: int
            firstGotReward: list[str]

    class PlayerAct13sideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        token: int
        favorList: list[str]
        milestone: "PlayerActivity.PlayerAct13sideActivity.MilestoneInfo"
        agenda: int
        flag: "PlayerActivity.PlayerAct13sideActivity.Flag"
        mission: "PlayerActivity.PlayerAct13sideActivity.DailyMissionPoolData"

        class MilestoneInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class Flag(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            agenda: bool
            mission: bool

        class SearchReward(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            type: ItemType

        class SearchCondition(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            orgId: str
            reward: "PlayerActivity.PlayerAct13sideActivity.SearchReward"

        class DailyMissionData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            missionId: str
            orgId: str
            principalId: str
            principalDescIdx: int
            rewardGroupId: str

        class DailyMissionProgress(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            target: int
            value: int

        class DailyMissionWithProgressData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            mission: "PlayerActivity.PlayerAct13sideActivity.DailyMissionData"
            progress: "PlayerActivity.PlayerAct13sideActivity.DailyMissionProgress"

        class DailyMissionPoolData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            random: int
            condition: "PlayerActivity.PlayerAct13sideActivity.SearchCondition"
            pool: "list[PlayerActivity.PlayerAct13sideActivity.DailyMissionData]"
            board: "list[PlayerActivity.PlayerAct13sideActivity.DailyMissionWithProgressData]"

    class PlayerAct17D7Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isOpen: bool

    class PlayerAct38D1Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        permanent: "PlayerActivity.PlayerAct38D1Activity.PermanentMapInfo"
        temporary: dict[str, "PlayerActivity.PlayerAct38D1Activity.BasicMapInfo"]

        class BasicMapInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: int
            scoreTotal: list[int]
            rune: dict[str, int]
            challenge: dict[str, int]
            box: dict[str, int]

        class PermanentMapInfo(BasicMapInfo):
            scoreSingle: list[int]
            comment: list[str]
            reward: dict[str, "PlayerActivity.PlayerAct38D1Activity.PermanentMapInfo.RewardInfo"]
            daily: dict[str, int]

            class RewardInfo(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                state: int
                progress: int

    class PlayerAprilFoolActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isOpen: bool

    class PlayerAct17SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isOpen: bool
        coin: int
        favorList: list[str]

    class PlayerBossRushActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestone: "PlayerActivity.PlayerBossRushActivity.MilestoneInfo"
        relic: "PlayerActivity.PlayerBossRushActivity.RelicInfo"
        best: dict[str, int]

        class MilestoneInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class TokenInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            current: int
            total: int

        class RelicInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            token: "PlayerActivity.PlayerBossRushActivity.TokenInfo"
            level: dict[str, int]
            select: str

    class PlayerEnemyDuelActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestone: "PlayerActivity.PlayerEnemyDuelActivity.MilestoneInfo"
        dailyMission: "PlayerActivity.PlayerEnemyDuelActivity.DailyMission"
        modeInfo: dict[str, "PlayerActivity.PlayerEnemyDuelActivity.ModeInfo"]
        globalBan: bool

        class MilestoneInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class DailyMissionState(StrEnum):
            NOT_CLAIM = "NOT_CLAIM"
            CLAIMED = "CLAIMED"

        class DailyMission(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            process: int
            state: "PlayerActivity.PlayerEnemyDuelActivity.DailyMissionState"

        class ModeInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            highScore: int
            curStage: str
            isUnlock: bool

    class PlayerVecBreakV2(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestone: "PlayerActivity.MilestoneInfo"
        activatedBuff: list[str]
        defendStages: dict[str, "PlayerActivity.PlayerVecBreakV2.DefendStageInfo"]

        class DefendCharInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            charInstId: int
            currentTmpl: str

        class DefendStageInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            defendSquad: "list[PlayerActivity.PlayerVecBreakV2.DefendCharInfo]"
            recvTimeLimited: bool
            recvNormal: bool

    class PlayerArcadeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestone: "PlayerActivity.PlayerArcadeActivity.MilestoneInfo"
        badge: dict[str, "PlayerActivity.PlayerArcadeActivity.BadgeInfo"]
        score: dict[str, dict[str, int]]

        class MilestoneInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class BadgeStatus(StrEnum):
            Error = "Error"
            InProgress = "InProgress"
            Unlocked = "Unlocked"

        class BadgeInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            status: "PlayerActivity.PlayerArcadeActivity.BadgeStatus"

    class PlayerAct20SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        actBase: "PlayerActivity.PlayerAct20SideActivity.ActBaseInfo"
        dailyJudgeTimes: int
        entertainmentCompetition: dict[str, "PlayerActivity.PlayerAct20SideActivity.EntertainCompBestRecord"]
        hotValue: "PlayerActivity.PlayerAct20SideActivity.HotValueInfo"
        hasJoinedExhibition: bool
        campaignCnt: int
        favorList: list[str]

        class ActBaseInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            actCoin: int
            milestone: "PlayerActivity.PlayerAct20SideActivity.MilestoneStateInfo"

        class MilestoneStateInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: int

        class HotValueInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            hotVal: int
            dailyHotVal: int

        class EntertainCompBestRecord(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            performance: int
            expression: int
            operation: int
            level: CartCompetitionRank

    class PlayerActFloatParadeActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        day: int
        canRaffle: bool
        result: "PlayerActivity.PlayerActFloatParadeActivity.Result"

        class Result(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            strategy: int
            eventId: str

    class PlayerAct21SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isOpen: bool
        coin: int
        favorList: list[str]

    class PlayerActMainlineBuff(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        favorList: list[str]

    class PlayerAct24SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        meal: "PlayerActivity.PlayerAct24SideActivity.Meal"
        alchemy: "PlayerActivity.PlayerAct24SideActivity.Alchemy"
        tool: dict[str, "PlayerActivity.PlayerAct24SideActivity.ToolState"]
        favorList: list[str]

        class ToolState(StrEnum):
            LOCK = "LOCK"
            UNSELECT = "UNSELECT"
            SELECT = "SELECT"

        class Meal(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            chance: int
            id: str
            digested: bool

        class Alchemy(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            price: int
            item: dict[str, int]
            gacha: dict[str, dict[str, int]]

    class PlayerAct25SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        investigativeToken: int
        actCoin: int
        dailyTokenRefresh: bool
        areas: dict[str, "PlayerActivity.PlayerAct25SideActivity.Area"]
        favorList: list[str]
        incremenalGame: "PlayerActivity.PlayerAct25SideActivity.DailyHarvest"
        tokenRecvCnt: int
        buff: list[str]

        class MissionState(StrEnum):
            UNFINISH = "UNFINISH"
            FINISHED = "FINISHED"
            OBTAINED = "OBTAINED"

        class MissionProgress(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            target: int
            value: int

        class Mission(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: "PlayerActivity.PlayerAct25SideActivity.MissionState"
            progress: "PlayerActivity.PlayerAct25SideActivity.MissionProgress"

        class Area(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            missions: dict[str, "PlayerActivity.PlayerAct25SideActivity.Mission"]
            missionId: str
            lastFinMissionId: str

        class DailyHarvest(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            harvenessTimeline: list[int]
            additionalHarvest: int
            currentRate: int
            preparedRate: int
            lastHarvenessTs: int

    class PlayerAct27SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        day: int
        signedIn: bool
        stock: dict[str, int]
        reward: ItemBundle
        state: "PlayerActivity.PlayerAct27SideActivity.SaleState"
        sale: "PlayerActivity.PlayerAct27SideActivity.Sale"
        milestone: "PlayerActivity.PlayerAct27SideActivity.MilestoneInfo"
        favorList: list[str]
        coin: int
        campaignCnt: int

        class SaleState(StrEnum):
            BEFORE_SALE = "BEFORE_SALE"
            PURCHASE = "PURCHASE"
            SELL = "SELL"
            BEFORE_SETTLE = "BEFORE_SETTLE"
            AFTER_SETTLE = "AFTER_SETTLE"

        class SellGoodState(StrEnum):
            NONE = "NONE"
            DRINK = "DRINK"
            FOOD = "FOOD"
            SOUVENIR = "SOUVENIR"

        class InquireInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            cur: int
            max: int

        class PrePurchaseInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            strategy: int
            shops: dict[str, list[int]]

        class PurchaseInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            strategy: int
            count: int

        class PreSellInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            price: int
            shops: dict[str, list[int]]

        class SellInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            price: int
            count: int
            bonus: int

        class Sale(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stateSell: "PlayerActivity.PlayerAct27SideActivity.SellGoodState"
            inquire: "PlayerActivity.PlayerAct27SideActivity.InquireInfo"
            groupId: str
            buyers: dict[str, int]
            purchasesTmp: dict[str, "list[PlayerActivity.PlayerAct27SideActivity.PrePurchaseInfo]"]
            purchases: dict[str, dict[str, "PlayerActivity.PlayerAct27SideActivity.PurchaseInfo"]]
            sellsTmp: dict[str, "list[PlayerActivity.PlayerAct27SideActivity.PreSellInfo]"]
            sells: dict[str, dict[str, "PlayerActivity.PlayerAct27SideActivity.SellInfo"]]

        class MilestoneInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

    class PlayerAct42D0Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestone: int
        areas: dict[str, "PlayerActivity.PlayerAct42D0Activity.AreaInfo"]
        spStages: dict[str, "PlayerActivity.PlayerAct42D0Activity.ChallengeStageInfo"]
        milestoneRecv: list[str]
        theHardestStage: str

        class AreaInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            canUseBuff: bool
            stages: dict[str, "PlayerActivity.PlayerAct42D0Activity.NoramlStageInfo"]

        class NoramlStageInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            rating: int

        class ChallengeStageInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            missions: dict[str, "PlayerActivity.PlayerAct42D0Activity.ChallengeStageMissionInfo"]

        class ChallengeStageMissionInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            target: int
            value: int
            state: int

    class PlayerUniqueOnlyActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        reward: int

    class PlayerBlessOnlyActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        history: list[int]
        festivalHistory: "list[PlayerActivity.PlayerBlessOnlyActivity.BlessOnlyFestival]"
        lastTs: int

        class BlessOnlyFestival(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: int
            charId: str

    class PlayerRecruitOnlyAct(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        used: int

    class PlayerAct29SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        actCoin: int
        accessToken: int
        favorList: list[str]
        rareMelodyMade: bool
        majorNPC: "PlayerActivity.PlayerAct29SideActivity.MajorNpcInfo"
        hidenNPC: "PlayerActivity.PlayerAct29SideActivity.HiddenNpcInfo"
        dailyNPC: "PlayerActivity.PlayerAct29SideActivity.DailyNpcInfo"
        fragmentBag: dict[str, int]
        melodyBag: dict[str, int]
        melodyNax: dict[str, int]
        majorFinDic: dict[str, int]

        class NpcInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            npc: str
            tryTimes: int
            hasRecv: bool

        class MajorNpcInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            isOpen: bool
            npc: "PlayerActivity.PlayerAct29SideActivity.NpcInfo"

        class HiddenNpcInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            needShow: bool
            npc: "PlayerActivity.PlayerAct29SideActivity.NpcInfo"

        class DailyNpcInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            slot: dict[str, "PlayerActivity.PlayerAct29SideActivity.NpcInfo"]

    class PlayerYear5GeneralActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unconfirmedPoints: int
        nextRewardIndex: int
        coin: int
        favorList: list[str]

    class PlayerAct36SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        dexNav: "PlayerActivity.PlayerAct36SideActivity.FoodHandbookInfo"
        coin: int
        favorList: list[str]

        class RewardState(StrEnum):
            UNFINISH = "UNFINISH"
            FINISHED = "FINISHED"
            CLAIMED = "CLAIMED"

        class FoodHandbookInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            enemySlot: dict[str, bool]
            food: dict[str, bool]
            rewardState: "PlayerActivity.PlayerAct36SideActivity.RewardState"

    class PlayerAct35SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        carving: "PlayerActivity.PlayerAct35SideActivity.PlayerAct35SideCarving"
        unlock: dict[str, int]
        record: dict[str, int]
        milestone: "PlayerActivity.PlayerAct35SideActivity.MilestoneState"
        coin: int
        campaignCnt: int
        favorList: list[str]

        class GameState(StrEnum):
            NONE = "NONE"
            BUY = "BUY"
            PROCESS = "PROCESS"
            NEXT = "NEXT"
            SETTLE = "SETTLE"
            INFO = "INFO"

        class PlayerAct35SideCarving(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            round: int
            score: int
            state: "PlayerActivity.PlayerAct35SideActivity.GameState"
            roundCoinAdd: int
            material: dict[str, int]
            card: dict[str, int]
            slotCnt: int
            shop: "PlayerActivity.PlayerAct35SideActivity.PlayerAct35SideCarvingShop"
            mission: "PlayerActivity.PlayerAct35SideActivity.CarvingTask"

        class PlayerAct35SideCarvingShop(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            coin: int
            good: "list[PlayerActivity.PlayerAct35SideActivity.ShopGood]"
            freeCardCnt: int
            refreshPrice: int
            slotPrice: int

        class ShopGood(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            price: int

        class CarvingTask(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            progress: list[int]

        class MilestoneState(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

    class PlayerAct38SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        favorList: list[str]
        fireworkPuzzleDict: dict[str, "PlayerActivity.PlayerAct38SideActivity.PlayerAct38SidePuzzle"]

        class PuzzleStatus(StrEnum):
            LOCKED = "LOCKED"
            UNLOCK = "UNLOCK"
            COMPLETE = "COMPLETE"

        class PlayerAct38SidePuzzle(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            puzzleStatus: "PlayerActivity.PlayerAct38SideActivity.PuzzleStatus"
            solutionList: "list[FireworkData.PlateSlotData]"

    class PlayerAutoChessV1Activity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        chessPool: dict[str, "PlayerActivity.PlayerAutoChessV1Activity.AutoChessCharCard"]
        dailyMission: "PlayerActivity.PlayerAutoChessV1Activity.DailyMission"
        protectTs: int
        milestone: "PlayerActivity.PlayerAutoChessV1Activity.Milestone"
        game: AutoChessGame
        band: dict[str, "PlayerActivity.PlayerAutoChessV1Activity.AutoChessBandUnlockInfo"]
        mode: dict[str, "PlayerActivity.PlayerAutoChessV1Activity.ModeRecord"]

        class ModeRecord(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            unlock: bool
            completeCnt: int

        class Milestone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class AutoChessCharType(StrEnum):
            OWN = "OWN"
            BACK_UP = "BACK_UP"
            ASSIST_BY_FRIEND = "ASSIST_BY_FRIEND"
            DIY = "DIY"

        class AutoChessCharCard(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            chessId: str
            type: "PlayerActivity.PlayerAutoChessV1Activity.AutoChessCharType"
            diyChar: str
            potentialRank: int
            cultivateEffect: str
            skillIndex: int
            currentEquip: str
            skin: str
            assistInfo: "PlayerActivity.PlayerAutoChessV1Activity.AutoChessAssistInfo"
            diyOrigChessId: str

        class AutoChessAssistInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            uid: str
            nickName: str
            nickNumber: str
            alias: str

        class AutoChessBandUnlockInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: int
            progress: "PlayerActivity.PlayerAutoChessV1Activity.AutoChessBandUnlockProgress"

        class AutoChessBandUnlockProgress(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            value: int
            target: int

        class DailyMission(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            process: int
            state: int

    class PlayerActMainSSActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        favorList: list[str]
        coin: int

    class PlayerAct42SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        favorList: list[str]
        outerPlayerOpen: bool
        taskMap: dict[str, "PlayerActivity.PlayerAct42SideActivity.PlayerAct42sideTask"]
        gunMap: dict[str, int]
        fileMap: dict[str, int]
        trustedItem: "PlayerActivity.PlayerAct42SideActivity.PlayerAct42sideTrustedItem"
        dailyRewardState: "PlayerActivity.PlayerAct42SideActivity.RewardState"

        class TaskState(StrEnum):
            LOCKED = "LOCKED"
            UNLOCK = "UNLOCK"
            ACCEPTED = "ACCEPTED"
            CAN_SUBMIT = "CAN_SUBMIT"
            COMPLETE = "COMPLETE"

        class RewardState(StrEnum):
            UNAVAILABLE = "UNAVAILABLE"
            AVAILABLE = "AVAILABLE"

        class PlayerAct42sideTask(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: "PlayerActivity.PlayerAct42SideActivity.TaskState"

        class PlayerAct42sideTrustedItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            has: int
            got: int
            dailyState: int

    class PlayerAct45SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        favorList: list[str]
        platformUnlock: bool
        charState: dict[str, "PlayerActivity.PlayerAct45SideActivity.State"]
        mailState: dict[str, "PlayerActivity.PlayerAct45SideActivity.State"]

        class State(StrEnum):
            LOCKED = "LOCKED"
            UNLOCK = "UNLOCK"
            ACCEPTED = "ACCEPTED"

    class PlayerAct44SideActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int
        favorList: list[str]
        campaignCnt: int
        informantPt: int
        milestone: "PlayerActivity.PlayerAct44SideActivity.Milestone"
        businessDay: int
        unlockedCustomers: dict[str, int]
        unlockedTags: dict[str, int]
        isNew: bool
        outerOpen: bool
        game: "PlayerActivity.PlayerAct44SideActivity.PlayerInformant"

        class Milestone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class InformantState(StrEnum):
            ENTRY = "ENTRY"
            CHOICE = "CHOICE"
            CHOICE_END = "CHOICE_END"
            BEFORE_SINGLE_RESULT = "BEFORE_SINGLE_RESULT"
            SINGLE_RESULT = "SINGLE_RESULT"
            RESULT = "RESULT"

        class PlayerInformantInsight(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            patienceRE: int
            trustRE: int
            attentionRE: int
            patienceMAX: int
            trustMAX: int
            attentionMAX: int

        class PlayerInformantTrader(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            patience: int
            trust: int
            attention: int
            choices: list[str]
            lastChoice: str

        class PlayerInformantSettle(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            customerId: str
            tagId: str
            success: bool
            successRate: float
            incomeRate: float
            income: int

        class PlayerInformant(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: "PlayerActivity.PlayerAct44SideActivity.InformantState"
            customerList: list[int]
            curCustomer: int
            newsId: str
            customerId: str
            round: int
            basicIncome: int
            tagId: str
            customerLine: str
            keeperLine: str
            insightTimes: int
            boom: bool
            insight: "PlayerActivity.PlayerAct44SideActivity.PlayerInformantInsight"
            tradeInfo: "PlayerActivity.PlayerAct44SideActivity.PlayerInformantTrader"
            settle: "list[PlayerActivity.PlayerAct44SideActivity.PlayerInformantSettle]"

    class PlayerAct1VHalfIdleActivity(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        coin: int | None = None
        troop: "PlayerActivity.PlayerAct1VHalfIdleActivity.Act1VHalfIdleTroop"
        stage: dict[str, "PlayerActivity.PlayerAct1VHalfIdleActivity.StageInfo"]
        settleInfo: "PlayerActivity.PlayerAct1VHalfIdleActivity.SettleStageInfo | None"
        production: "PlayerActivity.PlayerAct1VHalfIdleActivity.ProductionInfo"
        recruit: "PlayerActivity.PlayerAct1VHalfIdleActivity.RecruitInfo"
        milestone: "PlayerActivity.PlayerAct1VHalfIdleActivity.Milestone"
        inventory: dict[str, int]
        tech: "PlayerActivity.PlayerAct1VHalfIdleActivity.TechTree"
        globalBan: bool

        class BossState(IntEnum):
            NO_APPEAR = 0
            NO_KILL = 1
            KILL = 2

        class StageInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            rate: dict[str, int] | None
            bossState: "PlayerActivity.PlayerAct1VHalfIdleActivity.BossState"

        class SettleStageInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            rate: dict[str, int]
            bossState: "PlayerActivity.PlayerAct1VHalfIdleActivity.BossState"
            stageId: str
            progress: int

        class ProductionInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            rate: dict[str, int]
            product: dict[str, int]
            refreshTs: int
            harvestTs: int

        class Act1VHalfIdleTroop(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            char: dict[str, "PlayerActivity.PlayerAct1VHalfIdleActivity.Act1VHalfIdleCharData"]
            trap: list[str]
            npc: list[str]
            assist: list[SharedCharData | None]
            extraAssist: bool

        class Act1VHalfIdleCharData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            instId: int
            charId: str
            level: int
            skillLvl: int
            evolvePhase: int
            isAssist: bool
            defaultSkillId: str
            defaultEquipId: str

        class RecruitInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            poolGain: dict[str, list[str]]
            poolTimes: dict[str, int]

        class Milestone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            point: int
            got: list[str]

        class TechTree(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            unlock: list[str]
