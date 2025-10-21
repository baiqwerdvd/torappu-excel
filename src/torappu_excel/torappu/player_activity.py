from enum import IntEnum, StrEnum
from typing import Any

from .act_multi_v3_match_pos_type import ActMultiV3MatchPosIntType
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
from ..common import BaseStruct


class PlayerActivity(BaseStruct):
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
    VEC_BREAK: Any  # TODO: 临时占位
    TEAM_QUEST: dict[str, Any] | None = None
    RECRUIT_ONLY: dict[str, "PlayerActivity.PlayerRecruitOnlyAct"] | None = None

    class PlayerDefaultActivity(BaseStruct):
        coin: int
        shop: dict[str, int]

    class PlayerMissionOnlyTypeActivity(BaseStruct):
        pass

    class PlayerCheckinOnlyTypeActivity(BaseStruct):
        history: list[int]
        dynOpt: list[str]
        extraHistory: list[int]

    class PlayerCheckinVsTypeActivity(BaseStruct):
        sweetVote: int
        saltyVote: int
        canVote: bool
        todayVoteState: int
        voteRewardState: int
        signedCnt: int
        availSignCnt: int
        socialState: int
        actDay: int

    class PlayerCheckinAllTypeActivity(BaseStruct):
        history: list[int]
        allRecord: dict[str, int]
        allRewardStatus: dict[str, int]
        personalRecord: dict[str, int]

    class MilestoneInfo(BaseStruct):
        point: int
        got: list[str]

    class PlayerCollectionTypeActivity(BaseStruct):
        point: dict[str, int]
        history: dict[str, "PlayerActivity.PlayerCollectionTypeActivity.PlayerCollectionInfo"]

        class PlayerCollectionInfo(BaseStruct):
            ts: str

    class PlayerAVGOnlyTypeActivity(BaseStruct):
        isOpen: bool

    class PlayerLoginOnlyTypeActivity(BaseStruct):
        reward: int

    class PlayerMiniStoryActivity(BaseStruct):
        coin: int
        favorList: list[str]

    class PlayerRoguelikeActivity(BaseStruct):
        buffToken: int
        milestone: "PlayerActivity.PlayerRoguelikeActivity.MileStone"
        game: "PlayerActivity.PlayerRoguelikeActivity.GameStatus"

        class MileStone(BaseStruct):
            token: int
            got: dict[str, int]

        class GameStatus(BaseStruct):
            lastTs: int

    class PlayerActSandbox(BaseStruct):
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

        class Map(BaseStruct):
            zone: dict[str, "PlayerActivity.PlayerActSandbox.Map.Zone"]
            node: dict[str, "PlayerActivity.PlayerActSandbox.Map.Node"]

            class Zone(BaseStruct):
                weather: int

            class Node(BaseStruct):
                zone: str
                tag: int
                type: int
                state: int
                relate: "PlayerActivity.PlayerActSandbox.Map.Node.NodeRelate"
                weather: "PlayerActivity.PlayerActSandbox.Map.Node.NodeWeather"
                stageId: str

                class NodeRelate(BaseStruct):
                    adj: list[str]
                    layer: int
                    angle: float | int
                    depth: int

                class NodeWeather(BaseStruct):
                    level: int

        class GameStatus(BaseStruct):
            state: int
            flag: "PlayerActivity.PlayerActSandbox.GameStatus.GameFlag"

            class GameFlag(BaseStruct):
                guide: int

        class Game(BaseStruct):
            day: int
            totalDay: int
            ap: int
            maxAp: int
            initCharCount: int
            crossDay: "PlayerActivity.PlayerActSandbox.Game.CrossDay | None"
            settleType: int
            ts: int

            class CrossDay(BaseStruct):
                enemyRushNew: list[str]
                enemyRushMove: dict[str, str]
                trapRewards: list["PlayerActivity.PlayerActSandbox.Game.CrossDay.SandboxRewardItem"]
                missionRewards: list["PlayerActivity.PlayerActSandbox.Game.CrossDay.SandboxRewardItem"]
                missionIds: list[str]
                vagabond: dict[str, int]

                class SandboxRewardItem(BaseStruct):
                    id: str
                    type: str
                    count: int

        class Cook(BaseStruct):
            water: int
            foodSum: int
            cookbook: dict[str, int]
            food: dict[str, "PlayerActivity.PlayerActSandbox.Cook.Food"]

            class Food(BaseStruct):
                itemId: str
                minorBuff: list[str]
                count: int

        class Build(BaseStruct):
            blueprint: dict[str, int]
            building: dict[str, int]
            tactical: dict[str, int]

        class NodeStage(BaseStruct):
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

            class BaseInfo(BaseStruct):
                key: str
                pos: list[int]
                isDead: int
                hpRatio: int

            class EntityStatus(BaseStruct):
                key: str
                pos: list[int]
                isDead: int
                hpRatio: int

            class Nest(EntityStatus):
                pass

            class Cave(EntityStatus):
                pass

            class Enemy(BaseStruct):
                key: str
                count: list[int]

            class Building(BaseStruct):
                key: str
                pos: list[int]
                hpRatio: int
                direction: int

            class Trap(EntityStatus):
                count: list[int] | None
                extraParam: int | None

        class NodeEvent(BaseStruct):
            eventList: list["PlayerActivity.PlayerActSandbox.NodeEvent.Event"]
            originId: str

            class Event(BaseStruct):
                id: str
                enter: str
                state: bool | int
                scene: str | None

        class Npc(BaseStruct):
            id: str
            life: int
            skillId: int
            startDialog: str | None
            npcDialog: str | None

        class MapEnemyData(BaseStruct):
            enemyRush: dict[str, "PlayerActivity.PlayerActSandbox.MapEnemyData.EnemyRush"]
            rareAnimal: dict[str, "PlayerActivity.PlayerActSandbox.MapEnemyData.RareAnimal"]

            class EnemyRush(BaseStruct):
                path: list[str]
                groupKey: str
                days: int
                enemyRushType: int
                enemy: dict[str, list[int]]
                boss: dict[str, "PlayerActivity.PlayerActSandbox.MapEnemyData.EnemyRush.RushBossStatus"] | None

                class RushBossStatus(BaseStruct):
                    hpRatio: int
                    modeIndex: int

            class RareAnimal(BaseStruct):
                nodeId: str
                enemyId: str
                enemyGroupKey: str
                life: int

        class Mission(BaseStruct):
            missionId: str
            days: int
            charList: list[int]

        class TroopData(BaseStruct):
            charAp: dict[str, int]
            todayAddAp: list[str | int]
            charFood: dict[str | int, "PlayerActivity.PlayerActSandbox.TroopData.CharFood"]

            class CharFood(BaseStruct):
                itemId: str
                minorBuff: list[str]
                ts: int

        class Tech(BaseStruct):
            techs: list[str]
            researchTechs: list[str]
            researchTasks: dict[str, list[int]]
            token: int
            cent: int

        class Box(BaseStruct):
            enabled: bool
            foods: dict[str, "PlayerActivity.PlayerActSandbox.Box.Food"]
            items: dict[str, dict[str, int]]
            cap: int
            day: int

            class Food(BaseStruct):
                itemId: str
                minorBuff: list[str]
                count: int

        class Bank(BaseStruct):
            enabled: bool
            count: int
            ratio: int

        class Trigger(BaseStruct):
            flag: dict[str, int]

        class Task(BaseStruct):
            token: dict[str, int]

        class Milestone(BaseStruct):
            point: int
            got: list[str]

    class PlayerPrayOnlyActivity(BaseStruct):
        lastTs: int
        extraCount: int
        prayDaily: int
        prayMaxIndex: int
        praying: bool
        prayArray: "list[PlayerActivity.PlayerPrayOnlyActivity.RewardInfo]"

        class RewardInfo(BaseStruct):
            index: int
            count: int

    class PlayerSwitchOnlyActivity(BaseStruct):
        rewards: dict[str, int]

    class PlayerFlipOnlyActivity(BaseStruct):
        raffleCount: int
        todayRaffleCount: int
        remainingRaffleCount: int
        luckyToday: bool
        normalRewards: dict[int, "PlayerActivity.PlayerFlipOnlyActivity.ActFlipItemBundle"]
        grandStatus: int

        class ActFlipItemBundle(BaseStruct):
            id: str
            type: str
            count: int
            ts: int
            prizeId: str

    class PlayerGridGachaActivity(BaseStruct):
        lastDay: bool
        firstDay: bool
        openedPosition: list[int]
        openedType: int
        rewardCount: int
        grandPositions: list[int]

    class PlayerMultiplayActivity(BaseStruct):
        troop: dict[str, "PlayerActivity.PlayerMultiplayActivity.Troop"]
        stages: dict[str, "PlayerActivity.PlayerMultiplayActivity.Stage"]

        class Troop(BaseStruct):
            init: int
            squads: list[PlayerSquad]

        class Stage(BaseStruct):
            stageId: str
            state: PlayerStageState
            completeTimes: int

    class PlayerMultiplayV2Activity(BaseStruct):
        squads: "PlayerActivity.PlayerMultiplayV2Activity.Squads"
        dailyMission: "PlayerActivity.PlayerMultiplayV2Activity.DailyMission"
        milestone: "PlayerActivity.PlayerMultiplayV2Activity.MilestoneInfo"
        stage: dict[str, "PlayerActivity.PlayerMultiplayV2Activity.StageInfo"]
        match: "PlayerActivity.PlayerMultiplayV2Activity.Match"
        globalBan: bool

        class PlayerMultiplayV2SquadItem(BaseStruct):
            instId: int
            charInstId: int
            currentTmpl: str
            tmpl: dict[str, PlayerSquadTmpl]

        class Squads(BaseStruct):
            prefer: "list[PlayerActivity.PlayerMultiplayV2Activity.PlayerMultiplayV2SquadItem]"
            backup: "list[PlayerActivity.PlayerMultiplayV2Activity.PlayerMultiplayV2SquadItem]"

        class DailyMissionState(StrEnum):
            NOT_CLAIM = "NOT_CLAIM"
            CLAIMED = "CLAIMED"

        class DailyMission(BaseStruct):
            process: int
            state: "PlayerActivity.PlayerMultiplayV2Activity.DailyMissionState"

        class StageState(StrEnum):
            LOCK = "LOCK"
            UNLOCKED = "UNLOCKED"

        class StageInfo(BaseStruct):
            stageId: str
            score: int
            state: "PlayerActivity.PlayerMultiplayV2Activity.StageState"
            startTimes: int
            completeTimes: int

        class Match(BaseStruct):
            beMentorCnt: int
            lockMentor: bool
            bannedUntilTs: int

        class MilestoneInfo(BaseStruct):
            point: int
            got: list[str]

    class PlayerMultiV3Activity(BaseStruct):
        collection: "PlayerActivity.PlayerMultiV3Activity.Collection"
        troop: "PlayerActivity.PlayerMultiV3Activity.Troop"
        match: "PlayerActivity.PlayerMultiV3Activity.MatchInfo"
        milestone: "PlayerActivity.PlayerMultiV3Activity.Milestone"
        daily: "PlayerActivity.PlayerMultiV3Activity.Daily"
        stage: dict[str, "PlayerActivity.PlayerMultiV3Activity.StageInfo"]
        scene: "PlayerActivity.PlayerMultiV3Activity.Scene"
        globalBan: bool
        team: "PlayerActivity.PlayerMultiV3Activity.Team"

        class Collection(BaseStruct):
            info: "PlayerActivity.PlayerMultiV3Activity.CollectionInfo"
            title: "PlayerActivity.PlayerMultiV3Activity.Title"
            photo: "PlayerActivity.PlayerMultiV3Activity.Photo"

        class CollectionInfo(BaseStruct):
            finishCnt: int
            mentorCnt: int
            likeCnt: int

        class Title(BaseStruct):
            unlock: list[str]
            select: list[str]

        class Photo(BaseStruct):
            template: dict[str, dict[str, "PlayerActivity.PlayerMultiV3Activity.PhotoInstance"]]
            album: dict[str, "PlayerActivity.PlayerMultiV3Activity.Album"]

        class PhotoInstance(BaseStruct):
            players: "PlayerActivity.PlayerMultiV3Activity.PhotoPlayerInfo"
            chars: "list[PlayerActivity.PlayerMultiV3Activity.PhotoCharInfo]"
            stageId: str
            ts: int

        class PhotoPlayerInfo(BaseStruct):
            mine: "PlayerActivity.PlayerMultiV3Activity.PhotoSelfInfo"
            mate: "PlayerActivity.PlayerMultiV3Activity.PhotoAssistInfo"

        class PhotoSelfInfo(BaseStruct):
            title: list[str]

        class PhotoAssistInfo(BaseStruct):
            uid: str
            sameChannel: bool
            title: list[str]
            nickName: str
            avatar: AvatarInfo
            level: int
            nameCardSkinId: str
            nameCardSkinTmpl: int

        class PhotoCharInfo(BaseStruct):
            charId: str
            currentTmpl: str
            skinId: str
            slotIdx: int
            frame: int
            flip: bool

        class Album(BaseStruct):
            commit: bool
            slot: dict[str, str]

        class Troop(BaseStruct):
            buff: "PlayerActivity.PlayerMultiV3Activity.TroopBuff"
            squads: dict[str, "PlayerActivity.PlayerMultiV3Activity.Squad"]

        class TroopBuff(BaseStruct):
            unlock: list[str]
            coin: int
            star: int

        class Squad(BaseStruct):
            prefer: "list[PlayerActivity.PlayerMultiV3Activity.SquadItem]"
            backup: "list[PlayerActivity.PlayerMultiV3Activity.SquadItem]"
            buffId: str

        class SquadItem(BaseStruct):
            innerInstId: int
            charInstId: int
            currentTmpl: str
            tmpl: dict[str, PlayerSquadTmpl]

        class StageInfo(BaseStruct):
            star: int
            exScore: int
            matchTimes: int
            startTimes: int
            finishTimes: int

        class MatchInfo(BaseStruct):
            bannedUntilTs: int
            lastModeList: list[str]
            lastMentorType: ActMultiV3MatchPosIntType
            lastReverse: int

        class Milestone(BaseStruct):
            point: int
            got: list[str]

        class Daily(BaseStruct):
            process: int
            state: int

        class Scene(BaseStruct):
            lastMate: list[str]
            endTs: int
            reverse: int
            sceneId: str
            stageId: str
            startTs: int

        class Team(BaseStruct):
            startTs: int
            teamId: str
            teamType: int

    class PlayerInterlockActivity(BaseStruct):
        milestoneCoin: int
        milestoneGot: list[str]
        specialDefendStageId: str
        defend: dict[str, "list[PlayerActivity.PlayerInterlockActivity.DefendCharData]"]
        squad: dict[str, list[PlayerSquadItem]]

        class DefendCharData(BaseStruct):
            charInstId: int
            currentTmpl: str

    class PlayerAct3D0Activity(BaseStruct):
        faction: str
        gachaCoin: int
        ticket: int
        clue: dict[str, int]
        box: dict[str, "PlayerActivity.PlayerAct3D0Activity.BoxState"]
        milestone: "PlayerActivity.PlayerAct3D0Activity.MileStone"
        favorList: list[str]

        class BoxState(BaseStruct):
            content: dict[str, int]

        class MileStone(BaseStruct):
            point: int
            rewards: dict[str, int]

    class PlayerAct4D0Activity(BaseStruct):
        story: dict[str, int]
        milestone: "PlayerActivity.PlayerAct4D0Activity.MileStone"

        class MileStone(BaseStruct):
            point: int
            rewards: dict[str, int]

    class PlayerAct5D0Activity(BaseStruct):
        point_reward: MileStonePlayerInfo

    class PlayerAct5D1Activity(BaseStruct):
        coin: int
        pt: int
        shop: "PlayerActivity.PlayerAct5D1Activity.PlayerAct5D1Shop"
        runeStage: dict[str, "PlayerActivity.PlayerAct5D1Activity.PlayerActRuneStage"]
        stageEnemy: dict[str, list[str]]

        class PlayerAct5D1Shop(BaseStruct):
            info: dict[str, int]
            progressInfo: dict[str, "PlayerActivity.PlayerAct5D1Activity.PlayerAct5D1Shop.ProgressInfo"]

            class ProgressInfo(BaseStruct):
                count: int
                order: int

        class PlayerActRuneStage(BaseStruct):
            schedule: str
            available: int
            scores: int
            rune: dict[str, int]

    class PlayerAct9D0Activity(BaseStruct):
        coin: int
        favorList: list[str]
        news: dict[str, int]
        campaignCnt: int

    class PlayerAct12sideActivity(BaseStruct):
        coin: int
        campaignCnt: int
        favorList: list[str]
        milestone: "PlayerActivity.PlayerAct12sideActivity.MilestoneInfo"
        charm: "PlayerActivity.PlayerAct12sideActivity.CharmInfo"

        class MilestoneInfo(BaseStruct):
            point: int
            got: list[str]

        class CharmInfo(BaseStruct):
            recycleStack: int
            firstGotReward: list[str]

    class PlayerAct13sideActivity(BaseStruct):
        token: int
        favorList: list[str]
        milestone: "PlayerActivity.PlayerAct13sideActivity.MilestoneInfo"
        agenda: int
        flag: "PlayerActivity.PlayerAct13sideActivity.Flag"
        mission: "PlayerActivity.PlayerAct13sideActivity.DailyMissionPoolData"

        class MilestoneInfo(BaseStruct):
            point: int
            got: list[str]

        class Flag(BaseStruct):
            agenda: bool
            mission: bool

        class SearchReward(BaseStruct):
            id: str
            type: ItemType

        class SearchCondition(BaseStruct):
            orgId: str
            reward: "PlayerActivity.PlayerAct13sideActivity.SearchReward"

        class DailyMissionData(BaseStruct):
            missionId: str
            orgId: str
            principalId: str
            principalDescIdx: int
            rewardGroupId: str

        class DailyMissionProgress(BaseStruct):
            target: int
            value: int

        class DailyMissionWithProgressData(BaseStruct):
            mission: "PlayerActivity.PlayerAct13sideActivity.DailyMissionData"
            progress: "PlayerActivity.PlayerAct13sideActivity.DailyMissionProgress"

        class DailyMissionPoolData(BaseStruct):
            random: int
            condition: "PlayerActivity.PlayerAct13sideActivity.SearchCondition"
            pool: "list[PlayerActivity.PlayerAct13sideActivity.DailyMissionData]"
            board: "list[PlayerActivity.PlayerAct13sideActivity.DailyMissionWithProgressData]"

    class PlayerAct17D7Activity(BaseStruct):
        isOpen: bool

    class PlayerAct38D1Activity(BaseStruct):
        coin: int
        permanent: "PlayerActivity.PlayerAct38D1Activity.PermanentMapInfo"
        temporary: dict[str, "PlayerActivity.PlayerAct38D1Activity.BasicMapInfo"]

        class BasicMapInfo(BaseStruct):
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

            class RewardInfo(BaseStruct):
                state: int
                progress: int

    class PlayerAprilFoolActivity(BaseStruct):
        isOpen: bool

    class PlayerAct17SideActivity(BaseStruct):
        isOpen: bool
        coin: int
        favorList: list[str]

    class PlayerBossRushActivity(BaseStruct):
        milestone: "PlayerActivity.PlayerBossRushActivity.MilestoneInfo"
        relic: "PlayerActivity.PlayerBossRushActivity.RelicInfo"
        best: dict[str, int]

        class MilestoneInfo(BaseStruct):
            point: int
            got: list[str]

        class TokenInfo(BaseStruct):
            current: int
            total: int

        class RelicInfo(BaseStruct):
            token: "PlayerActivity.PlayerBossRushActivity.TokenInfo"
            level: dict[str, int]
            select: str

    class PlayerEnemyDuelActivity(BaseStruct):
        milestone: "PlayerActivity.PlayerEnemyDuelActivity.MilestoneInfo"
        dailyMission: "PlayerActivity.PlayerEnemyDuelActivity.DailyMission"
        modeInfo: dict[str, "PlayerActivity.PlayerEnemyDuelActivity.ModeInfo"]
        globalBan: bool

        class MilestoneInfo(BaseStruct):
            point: int
            got: list[str]

        class DailyMissionState(StrEnum):
            NOT_CLAIM = "NOT_CLAIM"
            CLAIMED = "CLAIMED"

        class DailyMission(BaseStruct):
            process: int
            state: "PlayerActivity.PlayerEnemyDuelActivity.DailyMissionState"

        class ModeInfo(BaseStruct):
            highScore: int
            curStage: str
            isUnlock: bool

    class PlayerVecBreakV2(BaseStruct):
        milestone: "PlayerActivity.MilestoneInfo"
        activatedBuff: list[str]
        defendStages: dict[str, "PlayerActivity.PlayerVecBreakV2.DefendStageInfo"]

        class DefendCharInfo(BaseStruct):
            charInstId: int
            currentTmpl: str

        class DefendStageInfo(BaseStruct):
            stageId: str
            defendSquad: "list[PlayerActivity.PlayerVecBreakV2.DefendCharInfo]"
            recvTimeLimited: bool
            recvNormal: bool

    class PlayerArcadeActivity(BaseStruct):
        milestone: "PlayerActivity.PlayerArcadeActivity.MilestoneInfo"
        badge: dict[str, "PlayerActivity.PlayerArcadeActivity.BadgeInfo"]
        score: dict[str, dict[str, int]]

        class MilestoneInfo(BaseStruct):
            point: int
            got: list[str]

        class BadgeStatus(StrEnum):
            Error = "Error"
            InProgress = "InProgress"
            Unlocked = "Unlocked"

        class BadgeInfo(BaseStruct):
            status: "PlayerActivity.PlayerArcadeActivity.BadgeStatus"

    class PlayerAct20SideActivity(BaseStruct):
        actBase: "PlayerActivity.PlayerAct20SideActivity.ActBaseInfo"
        dailyJudgeTimes: int
        entertainmentCompetition: dict[str, "PlayerActivity.PlayerAct20SideActivity.EntertainCompBestRecord"]
        hotValue: "PlayerActivity.PlayerAct20SideActivity.HotValueInfo"
        hasJoinedExhibition: bool
        campaignCnt: int
        favorList: list[str]

        class ActBaseInfo(BaseStruct):
            actCoin: int
            milestone: "PlayerActivity.PlayerAct20SideActivity.MilestoneStateInfo"

        class MilestoneStateInfo(BaseStruct):
            point: int
            got: int

        class HotValueInfo(BaseStruct):
            hotVal: int
            dailyHotVal: int

        class EntertainCompBestRecord(BaseStruct):
            performance: int
            expression: int
            operation: int
            level: CartCompetitionRank

    class PlayerActFloatParadeActivity(BaseStruct):
        day: int
        canRaffle: bool
        result: "PlayerActivity.PlayerActFloatParadeActivity.Result"

        class Result(BaseStruct):
            strategy: int
            eventId: str

    class PlayerAct21SideActivity(BaseStruct):
        isOpen: bool
        coin: int
        favorList: list[str]

    class PlayerActMainlineBuff(BaseStruct):
        favorList: list[str]

    class PlayerAct24SideActivity(BaseStruct):
        meal: "PlayerActivity.PlayerAct24SideActivity.Meal"
        alchemy: "PlayerActivity.PlayerAct24SideActivity.Alchemy"
        tool: dict[str, "PlayerActivity.PlayerAct24SideActivity.ToolState"]
        favorList: list[str]

        class ToolState(StrEnum):
            LOCK = "LOCK"
            UNSELECT = "UNSELECT"
            SELECT = "SELECT"

        class Meal(BaseStruct):
            chance: int
            id: str
            digested: bool

        class Alchemy(BaseStruct):
            price: int
            item: dict[str, int]
            gacha: dict[str, dict[str, int]]

    class PlayerAct25SideActivity(BaseStruct):
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

        class MissionProgress(BaseStruct):
            target: int
            value: int

        class Mission(BaseStruct):
            state: "PlayerActivity.PlayerAct25SideActivity.MissionState"
            progress: "PlayerActivity.PlayerAct25SideActivity.MissionProgress"

        class Area(BaseStruct):
            missions: dict[str, "PlayerActivity.PlayerAct25SideActivity.Mission"]
            missionId: str
            lastFinMissionId: str

        class DailyHarvest(BaseStruct):
            harvenessTimeline: list[int]
            additionalHarvest: int
            currentRate: int
            preparedRate: int
            lastHarvenessTs: int

    class PlayerAct27SideActivity(BaseStruct):
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

        class InquireInfo(BaseStruct):
            cur: int
            max: int

        class PrePurchaseInfo(BaseStruct):
            strategy: int
            shops: dict[str, list[int]]

        class PurchaseInfo(BaseStruct):
            strategy: int
            count: int

        class PreSellInfo(BaseStruct):
            price: int
            shops: dict[str, list[int]]

        class SellInfo(BaseStruct):
            price: int
            count: int
            bonus: int

        class Sale(BaseStruct):
            stateSell: "PlayerActivity.PlayerAct27SideActivity.SellGoodState"
            inquire: "PlayerActivity.PlayerAct27SideActivity.InquireInfo"
            groupId: str
            buyers: dict[str, int]
            purchasesTmp: dict[str, "list[PlayerActivity.PlayerAct27SideActivity.PrePurchaseInfo]"]
            purchases: dict[str, dict[str, "PlayerActivity.PlayerAct27SideActivity.PurchaseInfo"]]
            sellsTmp: dict[str, "list[PlayerActivity.PlayerAct27SideActivity.PreSellInfo]"]
            sells: dict[str, dict[str, "PlayerActivity.PlayerAct27SideActivity.SellInfo"]]

        class MilestoneInfo(BaseStruct):
            point: int
            got: list[str]

    class PlayerAct42D0Activity(BaseStruct):
        milestone: int
        areas: dict[str, "PlayerActivity.PlayerAct42D0Activity.AreaInfo"]
        spStages: dict[str, "PlayerActivity.PlayerAct42D0Activity.ChallengeStageInfo"]
        milestoneRecv: list[str]
        theHardestStage: str

        class AreaInfo(BaseStruct):
            canUseBuff: bool
            stages: dict[str, "PlayerActivity.PlayerAct42D0Activity.NoramlStageInfo"]

        class NoramlStageInfo(BaseStruct):
            rating: int

        class ChallengeStageInfo(BaseStruct):
            missions: dict[str, "PlayerActivity.PlayerAct42D0Activity.ChallengeStageMissionInfo"]

        class ChallengeStageMissionInfo(BaseStruct):
            target: int
            value: int
            state: int

    class PlayerUniqueOnlyActivity(BaseStruct):
        reward: int

    class PlayerBlessOnlyActivity(BaseStruct):
        history: list[int]
        festivalHistory: "list[PlayerActivity.PlayerBlessOnlyActivity.BlessOnlyFestival]"
        lastTs: int

        class BlessOnlyFestival(BaseStruct):
            state: int
            charId: str

    class PlayerRecruitOnlyAct(BaseStruct):
        used: int

    class PlayerAct29SideActivity(BaseStruct):
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

        class NpcInfo(BaseStruct):
            npc: str
            tryTimes: int
            hasRecv: bool

        class MajorNpcInfo(BaseStruct):
            isOpen: bool
            npc: "PlayerActivity.PlayerAct29SideActivity.NpcInfo"

        class HiddenNpcInfo(BaseStruct):
            needShow: bool
            npc: "PlayerActivity.PlayerAct29SideActivity.NpcInfo"

        class DailyNpcInfo(BaseStruct):
            slot: dict[str, "PlayerActivity.PlayerAct29SideActivity.NpcInfo"]

    class PlayerYear5GeneralActivity(BaseStruct):
        unconfirmedPoints: int
        nextRewardIndex: int
        coin: int
        favorList: list[str]

    class PlayerAct36SideActivity(BaseStruct):
        dexNav: "PlayerActivity.PlayerAct36SideActivity.FoodHandbookInfo"
        coin: int
        favorList: list[str]

        class RewardState(StrEnum):
            UNFINISH = "UNFINISH"
            FINISHED = "FINISHED"
            CLAIMED = "CLAIMED"

        class FoodHandbookInfo(BaseStruct):
            enemySlot: dict[str, bool]
            food: dict[str, bool]
            rewardState: "PlayerActivity.PlayerAct36SideActivity.RewardState"

    class PlayerAct35SideActivity(BaseStruct):
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

        class PlayerAct35SideCarving(BaseStruct):
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

        class PlayerAct35SideCarvingShop(BaseStruct):
            coin: int
            good: "list[PlayerActivity.PlayerAct35SideActivity.ShopGood]"
            freeCardCnt: int
            refreshPrice: int
            slotPrice: int

        class ShopGood(BaseStruct):
            id: str
            price: int

        class CarvingTask(BaseStruct):
            id: str
            progress: list[int]

        class MilestoneState(BaseStruct):
            point: int
            got: list[str]

    class PlayerAct38SideActivity(BaseStruct):
        coin: int
        favorList: list[str]
        fireworkPuzzleDict: dict[str, "PlayerActivity.PlayerAct38SideActivity.PlayerAct38SidePuzzle"]

        class PuzzleStatus(StrEnum):
            LOCKED = "LOCKED"
            UNLOCK = "UNLOCK"
            COMPLETE = "COMPLETE"

        class PlayerAct38SidePuzzle(BaseStruct):
            puzzleStatus: "PlayerActivity.PlayerAct38SideActivity.PuzzleStatus"
            solutionList: "list[FireworkData.PlateSlotData]"

    class PlayerAutoChessV1Activity(BaseStruct):
        chessPool: dict[str, "PlayerActivity.PlayerAutoChessV1Activity.AutoChessCharCard"]
        dailyMission: "PlayerActivity.PlayerAutoChessV1Activity.DailyMission"
        protectTs: int
        milestone: "PlayerActivity.PlayerAutoChessV1Activity.Milestone"
        game: AutoChessGame
        band: dict[str, "PlayerActivity.PlayerAutoChessV1Activity.AutoChessBandUnlockInfo"]
        mode: dict[str, "PlayerActivity.PlayerAutoChessV1Activity.ModeRecord"]

        class ModeRecord(BaseStruct):
            unlock: bool
            completeCnt: int

        class Milestone(BaseStruct):
            point: int
            got: list[str]

        class AutoChessCharType(StrEnum):
            OWN = "OWN"
            BACK_UP = "BACK_UP"
            ASSIST_BY_FRIEND = "ASSIST_BY_FRIEND"
            DIY = "DIY"

        class AutoChessCharCard(BaseStruct):
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

        class AutoChessAssistInfo(BaseStruct):
            uid: str
            nickName: str
            nickNumber: str
            alias: str

        class AutoChessBandUnlockInfo(BaseStruct):
            state: int
            progress: "PlayerActivity.PlayerAutoChessV1Activity.AutoChessBandUnlockProgress"

        class AutoChessBandUnlockProgress(BaseStruct):
            value: int
            target: int

        class DailyMission(BaseStruct):
            process: int
            state: int

    class PlayerActMainSSActivity(BaseStruct):
        favorList: list[str]
        coin: int

    class PlayerAct42SideActivity(BaseStruct):
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

        class PlayerAct42sideTask(BaseStruct):
            state: "PlayerActivity.PlayerAct42SideActivity.TaskState"

        class PlayerAct42sideTrustedItem(BaseStruct):
            has: int
            got: int
            dailyState: int

    class PlayerAct45SideActivity(BaseStruct):
        coin: int
        favorList: list[str]
        platformUnlock: bool
        charState: dict[str, "PlayerActivity.PlayerAct45SideActivity.State"]
        mailState: dict[str, "PlayerActivity.PlayerAct45SideActivity.State"]

        class State(StrEnum):
            LOCKED = "LOCKED"
            UNLOCK = "UNLOCK"
            ACCEPTED = "ACCEPTED"

    class PlayerAct44SideActivity(BaseStruct):
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

        class Milestone(BaseStruct):
            point: int
            got: list[str]

        class InformantState(StrEnum):
            ENTRY = "ENTRY"
            CHOICE = "CHOICE"
            CHOICE_END = "CHOICE_END"
            BEFORE_SINGLE_RESULT = "BEFORE_SINGLE_RESULT"
            SINGLE_RESULT = "SINGLE_RESULT"
            RESULT = "RESULT"

        class PlayerInformantInsight(BaseStruct):
            patienceRE: int
            trustRE: int
            attentionRE: int
            patienceMAX: int
            trustMAX: int
            attentionMAX: int

        class PlayerInformantTrader(BaseStruct):
            patience: int
            trust: int
            attention: int
            choices: list[str]
            lastChoice: str

        class PlayerInformantSettle(BaseStruct):
            customerId: str
            tagId: str
            success: bool
            successRate: float
            incomeRate: float
            income: int

        class PlayerInformant(BaseStruct):
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

    class PlayerAct1VHalfIdleActivity(BaseStruct):
        troop: "PlayerActivity.PlayerAct1VHalfIdleActivity.Act1VHalfIdleTroop"
        stage: dict[str, "PlayerActivity.PlayerAct1VHalfIdleActivity.StageInfo"]
        settleInfo: "PlayerActivity.PlayerAct1VHalfIdleActivity.SettleStageInfo | None"
        production: "PlayerActivity.PlayerAct1VHalfIdleActivity.ProductionInfo"
        recruit: "PlayerActivity.PlayerAct1VHalfIdleActivity.RecruitInfo"
        milestone: "PlayerActivity.PlayerAct1VHalfIdleActivity.Milestone"
        inventory: dict[str, int]
        tech: "PlayerActivity.PlayerAct1VHalfIdleActivity.TechTree"
        globalBan: bool
        coin: int | None = None

        class BossState(IntEnum):
            NO_APPEAR = 0
            NO_KILL = 1
            KILL = 2

        class StageInfo(BaseStruct):
            rate: dict[str, int] | None
            bossState: "PlayerActivity.PlayerAct1VHalfIdleActivity.BossState"

        class SettleStageInfo(BaseStruct):
            rate: dict[str, int]
            bossState: "PlayerActivity.PlayerAct1VHalfIdleActivity.BossState"
            stageId: str
            progress: int

        class ProductionInfo(BaseStruct):
            rate: dict[str, int]
            product: dict[str, int]
            refreshTs: int
            harvestTs: int

        class Act1VHalfIdleTroop(BaseStruct):
            char: dict[str, "PlayerActivity.PlayerAct1VHalfIdleActivity.Act1VHalfIdleCharData"]
            trap: list[str]
            npc: list[str]
            assist: list[SharedCharData | None]
            extraAssist: bool

        class Act1VHalfIdleCharData(BaseStruct):
            instId: int
            charId: str
            level: int
            skillLvl: int
            evolvePhase: int
            isAssist: bool
            defaultSkillId: str
            defaultEquipId: str

        class RecruitInfo(BaseStruct):
            poolGain: dict[str, list[str]]
            poolTimes: dict[str, int]

        class Milestone(BaseStruct):
            point: int
            got: list[str]

        class TechTree(BaseStruct):
            unlock: list[str]
