from enum import StrEnum

from msgspec import field

from .PlayerRoguelikeV2_CurrentData_Char import Char
from .avatar_info import AvatarInfo
from .char_star_mark_state import CharStarMarkState
from .date_time import DateTime
from .evolve_phase import EvolvePhase
from .player_char_patch import PlayerCharPatch
from .player_roguelike_challenge_status import PlayerRoguelikeChallengeStatus
from .player_roguelike_difficulty_status import PlayerRoguelikeDifficultyStatus
from .player_roguelike_pending_event import PlayerRoguelikePendingEvent
from .player_roguelike_player_state import PlayerRoguelikePlayerState
from .player_roguelike_v2_dungeon import PlayerRoguelikeV2Dungeon
from .roguelike_archive_item_unlock_status import RoguelikeArchiveItemUnlockStatus
from .roguelike_char_state import RoguelikeCharState
from .roguelike_game_month_task_class import RoguelikeGameMonthTaskClass
from .roguelike_node_position import RoguelikeNodePosition
from .roguelike_topic_mode import RoguelikeTopicMode
from .shared_char_data import SharedCharData
from ..common import BaseStruct


class PlayerRoguelikeV2(BaseStruct):
    current: "PlayerRoguelikeV2.CurrentData"
    outer: dict[str, "PlayerRoguelikeV2.OuterData"]
    pinned: str

    class CurrentData(BaseStruct):
        player: "PlayerRoguelikeV2.CurrentData.PlayerStatus"
        map: PlayerRoguelikeV2Dungeon
        inventory: "PlayerRoguelikeV2.CurrentData.Inventory"
        game: "PlayerRoguelikeV2.CurrentData.Game"
        troop: "PlayerRoguelikeV2.CurrentData.Troop"
        buff: "PlayerRoguelikeV2.CurrentData.Buff"
        record: "PlayerRoguelikeV2.CurrentData.Record"
        module: "PlayerRoguelikeV2.CurrentData.Module"

        class PlayerStatus(BaseStruct):
            state: PlayerRoguelikePlayerState
            property: "PlayerRoguelikeV2.CurrentData.PlayerStatus.Properties"
            cursor: "PlayerRoguelikeV2.CurrentData.PlayerStatus.NodePosition"
            pending: list[PlayerRoguelikePendingEvent]
            trace: "list[PlayerRoguelikeV2.CurrentData.PlayerStatus.NodePosition]"
            status: "PlayerRoguelikeV2.CurrentData.PlayerStatus.Status"
            toEnding: str
            chgEnding: bool
            innerMission: "list[PlayerRoguelikeV2.CurrentData.PlayerStatus.InnerMission] | None" = None
            nodeMission: "PlayerRoguelikeV2.CurrentData.PlayerStatus.NodeMission | None" = None
            zoneReward: dict[str, "list[PlayerRoguelikeV2.CurrentData.PlayerStatus.ZoneRewardItem]"] | None = None
            traderReturn: dict[str, "list[PlayerRoguelikeV2.CurrentData.PlayerStatus.ZoneRewardItem]"] | None = None

            class Properties(BaseStruct):
                exp: int
                level: int
                maxLevel: int
                hp: "PlayerRoguelikeV2.CurrentData.PlayerStatus.Properties.Hp"
                shield: int
                gold: int
                capacity: int
                population: "PlayerRoguelikeV2.CurrentData.PlayerStatus.Properties.Population"
                conPerfectBattle: int

                class Hp(BaseStruct):
                    current: int
                    max: int

                class Population(BaseStruct):
                    cost: int
                    max: int

                class RewardHpShowStatus(StrEnum):
                    NONE = "NONE"
                    NORMAL = "NORMAL"
                    HIDDEN = "HIDDEN"

            class NodePosition(BaseStruct):
                zone: int
                position: RoguelikeNodePosition | None

            class Status(BaseStruct):
                bankPut: int

            class InnerMission(BaseStruct):
                tmpl: str
                id: str
                progress: list[int]

            class NodeMission(BaseStruct):
                id: str
                state: "PlayerRoguelikeV2.CurrentData.PlayerStatus.NodeMission.NodeMissionState"
                tip: bool
                progress: list[int]

                class NodeMissionState(StrEnum):
                    NOT_COMPLETED = "NOT_COMPLETED"
                    COMPLETED = "COMPLETED"
                    ALL_FINISHED = "ALL_FINISHED"

            class ZoneRewardItem(BaseStruct):
                id: str
                count: int
                instId: str

        class RecruitChar(BaseStruct):
            type: RoguelikeCharState
            upgradePhase: int
            upgradeLimited: bool
            population: int
            isUpgrade: bool
            troopInstId: int
            instId: int
            charId: str
            level: int
            exp: int
            evolvePhase: EvolvePhase
            potentialRank: int
            favorPoint: int
            mainSkillLvl: int
            gainTime: int
            starMark: CharStarMarkState
            currentTmpl: str
            tmpl: dict[str, PlayerCharPatch]

        class ExpeditionReturn(BaseStruct):
            char: "list[PlayerRoguelikeV2.CurrentData.ExpeditionReturn.Char]"
            rewards: "list[PlayerRoguelikeV2.CurrentData.ExpeditionReturn.Reward]"

            class Char(BaseStruct):
                instId: str
                isUpgrade: bool
                isCure: bool
                isCandle: bool

            class Reward(BaseStruct):
                id: str
                count: int
                instId: str

        class Troop(BaseStruct):
            chars: dict[str, Char]
            expedition: list[str]
            expeditionDetails: dict[str, "PlayerRoguelikeV2.CurrentData.Troop.ExpedType"]
            expeditionReturn: "PlayerRoguelikeV2.CurrentData.ExpeditionReturn | None"
            hasExpeditionReturn: bool

            class ExpedType(StrEnum):
                EXPED = "EXPED"
                TRAVEL = "TRAVEL"
                CANDLE = "CANDLE"
                NO_UPGRADE = "NO_UPGRADE"
                GUIDED = "GUIDED"
                NON_GUIDED = "NON_GUIDED"

        class Relic(BaseStruct):
            index: str
            id: str
            count: int
            layer: int
            ts: int
            used: bool

        class Trap(BaseStruct):
            id: str
            ts: int

        class ExploreTool(BaseStruct):
            id: str
            ts: int

        class Recruit(BaseStruct):
            index: str
            id: str
            state: "PlayerRoguelikeV2.CurrentData.Recruit.State"
            result: "PlayerRoguelikeV2.CurrentData.RecruitChar"
            ts: int
            needAssist: bool
            assistList: dict[str, list["PlayerRoguelikeV2.CurrentData.Recruit.FriendAssistData"]]
            starFriendAssistList: dict[str, list["PlayerRoguelikeV2.CurrentData.Recruit.FriendAssistData"]]
            list_: list["PlayerRoguelikeV2.CurrentData.RecruitChar"] = field(name="list")

            class State(StrEnum):
                CREATE = "CREATE"
                ACTIVE = "ACTIVE"
                DONE = "DONE"

            class OrigChar(BaseStruct):
                assistSlotIndex: int
                aliasName: str
                assistCharList: list[SharedCharData]
                isFriend: bool
                canRequestFriend: bool
                isStarFriend: bool
                nickName: str
                uid: str
                serverName: str
                nickNumber: str
                level: int
                lastOnlineTime: DateTime
                recentVisited: bool
                avatar: AvatarInfo

            class FriendAssistData(BaseStruct):
                orig: "PlayerRoguelikeV2.CurrentData.Recruit.OrigChar"
                recruit: "PlayerRoguelikeV2.CurrentData.RecruitChar"

        class Inventory(BaseStruct):
            relic: dict[str, "PlayerRoguelikeV2.CurrentData.Relic"]
            recruit: dict[str, "PlayerRoguelikeV2.CurrentData.Recruit"]
            trap: "PlayerRoguelikeV2.CurrentData.Trap | None"
            exploreTool: dict[str, "PlayerRoguelikeV2.CurrentData.ExploreTool"]
            consumable: dict[str, int]
            stashRecruit: list[str] | None = None
            stashRecruitLimit: int | None = None

        class Buff(BaseStruct):
            tmpHP: int
            capsule: "PlayerRoguelikeV2.CurrentData.Capsule | None"
            squadBuff: list[str]

        class Capsule(BaseStruct):
            id: str
            ts: int
            active: bool

        class Game(BaseStruct):
            theme: str
            mode: RoguelikeTopicMode
            modeGrade: int
            equivalentGrade: int
            start: int
            outer: "PlayerRoguelikeV2.CurrentData.Game.Outer"
            uid: str | None = None
            predefined: str | None = None
            difficult: int | None = None
            outerBuff: "PlayerRoguelikeV2.CurrentData.Game.OuterBuff  | None" = None
            activity: str | None = None

            class OuterBuff(BaseStruct):
                pass

            class Outer(BaseStruct):
                support: bool

        class Record(BaseStruct):
            brief: "PlayerRoguelikeV2.CurrentData.Record.EndingBrief | None"

            class EndingBrief(BaseStruct):
                level: int
                successL: int
                ending: str
                theme: str
                mode: str
                predefined: str
                band: str
                startTs: int
                endTs: int
                endZoneId: str
                modeGrade: int

        class Module(BaseStruct):
            san: "PlayerRoguelikeV2.CurrentData.Module.San | None" = None
            dice: "PlayerRoguelikeV2.CurrentData.Module.Dice | None" = None
            totem: "PlayerRoguelikeV2.CurrentData.Module.Totem | None" = None
            vision: "PlayerRoguelikeV2.CurrentData.Module.Vision | None" = None
            chaos: "PlayerRoguelikeV2.CurrentData.Module.Chaos | None" = None
            fragment: "PlayerRoguelikeV2.CurrentData.Module.Fragment | None" = None
            disaster: "PlayerRoguelikeV2.CurrentData.Module.Disaster | None" = None
            nodeUpgrade: "PlayerRoguelikeV2.CurrentData.Module.NodeUpgrade | None" = None
            copper: "PlayerRoguelikeV2.CurrentData.Module.Copper | None" = None
            wrath: "PlayerRoguelikeV2.CurrentData.Module.Wrath | None" = None
            sky: "PlayerRoguelikeV2.CurrentData.Module.Sky | None" = None

            class San(BaseStruct):
                sanity: int

            class Dice(BaseStruct):
                id: str
                count: int

            class InventoryTotem(BaseStruct):
                id: str
                index: str
                used: bool
                affix: str
                ts: int

            class Totem(BaseStruct):
                totemPiece: "list[PlayerRoguelikeV2.CurrentData.Module.InventoryTotem]"
                predictTotemId: str

            class Vision(BaseStruct):
                value: int
                isMax: bool

            class ChaosZoneDelta(BaseStruct):
                dValue: int
                preLevel: int
                afterLevel: int
                dChaos: list[str]

            class Chaos(BaseStruct):
                value: int
                level: int
                curMaxValue: int
                chaosList: list[str]
                predict: str
                deltaChaos: "PlayerRoguelikeV2.CurrentData.Module.ChaosZoneDelta"
                lastBattleGain: int

            class Fragment(BaseStruct):
                totalWeight: int
                limitWeight: int
                overWeight: int
                fragments: dict[str, "PlayerRoguelikeV2.CurrentData.Module.InventoryFragment"]
                troopWeights: dict[int, int]
                troopCarry: list[int]
                sellCount: int
                currInspiration: "PlayerRoguelikeV2.CurrentData.Module.InventoryInspiration"

            class InventoryFragment(BaseStruct):
                id: str
                index: str
                used: bool
                ts: int
                weight: int
                value: int
                price: int

            class InventoryInspiration(BaseStruct):
                instId: str
                id: str

            class Disaster(BaseStruct):
                curDisaster: str
                disperseStep: int

            class NodeUpgrade(BaseStruct):
                nodeTypeInfoMap: dict[str, "PlayerRoguelikeV2.CurrentData.Module.NodeUpgradeInfo"]

            class NodeUpgradeInfo(BaseStruct):
                tempUpgrade: str
                upgradeList: list[str]

            class Copper(BaseStruct):
                bag: dict[str, "PlayerRoguelikeV2.CurrentData.Module.InventoryCopper"]
                redrawCost: int

            class InventoryCopper(BaseStruct):
                id: str
                isDrawn: bool
                layer: int
                countDown: int
                ts: int

            class Wrath(BaseStruct):
                wraths: list[str]
                newWrath: int

            class WrathInfo(BaseStruct):
                wrathId: str
                level: int

            class Sky(BaseStruct):
                zones: dict[int, "PlayerRoguelikeV2.CurrentData.Module.SkyZoneInfo"]

            class SkyZoneInfo(BaseStruct):
                id: str
                ap: int
                nodes: dict[int, "PlayerRoguelikeV2.CurrentData.Module.SkyZoneNodeInfo"]
                mapExPad: "PlayerRoguelikeV2.CurrentData.Module.SkyZoneExPadInfo"

            class SkyZoneExPadInfo(BaseStruct):
                left: int
                right: int

            class SkyZoneNodeState(StrEnum):
                LOCK = "LOCK"
                UNLOCK = "UNLOCK"
                FINISH = "FINISH"
                CLOSE = "CLOSE"

            class SkyZoneNodeInfo(BaseStruct):
                state: "PlayerRoguelikeV2.CurrentData.Module.SkyZoneNodeState"
                type: int
                sceneSubType: int
                battleProgress: list[int]
                shopIsEmpty: bool
                shopGoodIds: list[str]
                shopRefreshShow: bool
                shopRefreshCnt: int
                shopRefreshCost: int

    class OuterData(BaseStruct):
        bp: "PlayerRoguelikeV2.OuterData.BattlePass"
        buff: "PlayerRoguelikeV2.OuterData.Buff"
        mission: "PlayerRoguelikeV2.OuterData.Mission"
        collect: "PlayerRoguelikeV2.OuterData.Collection"
        bank: "PlayerRoguelikeV2.OuterData.Bank"
        record: "PlayerRoguelikeV2.OuterData.Record"
        monthTeam: "PlayerRoguelikeV2.OuterData.MonthTeam"
        challenge: "PlayerRoguelikeV2.OuterData.Challenge"
        activity: "PlayerRoguelikeV2.OuterData.PlayerRogueActivity"

        class Record(BaseStruct):
            last: int
            stageCnt: dict[str, int]
            modeCnt: dict[RoguelikeTopicMode, int]
            bandCnt: dict[str, dict[str, int]]
            endingCnt: dict[RoguelikeTopicMode, dict[str, int]]
            bandGrade: dict[str, dict[str, int]] | None = None
            history: list["PlayerRoguelikeV2.OuterData.Record.History"] | None = None

            class History(BaseStruct):
                seed: str
                bandId: str
                mode: RoguelikeTopicMode
                modeGrade: int
                ending: str
                result: int
                endTs: int
                failEnding: str | None = None

        class BattlePass(BaseStruct):
            point: int
            reward: dict[str, int]

        class Mission(BaseStruct):
            updateId: str
            refresh: int
            list_: list["PlayerRoguelikeV2.OuterData.Mission.MissionSlot"] = field(name="list")

            class MissionSlot(BaseStruct):
                type: RoguelikeGameMonthTaskClass
                mission: "PlayerRoguelikeV2.OuterData.Mission.MissionItem"

            class MissionItem(BaseStruct):
                type: RoguelikeGameMonthTaskClass
                id: str
                state: int
                target: int
                value: int
                tmpl: "PlayerRoguelikeV2.OuterData.Mission.MissionItem.MissionTmpl"

                class MissionTmpl(StrEnum):
                    KillCerternEnemy = "KillCerternEnemy"
                    PassNodeType = "PassNodeType"
                    UsePopulation = "UsePopulation"
                    CandleCharacter = "CandleCharacter"

        class TotemCollection(BaseStruct):
            totem: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            affix: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]

        class Collection(BaseStruct):
            band: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            relic: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            capsule: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            activeTool: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            mode: dict[RoguelikeTopicMode, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            modeGrade: dict[
                RoguelikeTopicMode, dict[str, "PlayerRoguelikeV2.OuterData.Collection.DifficultyUnlockInfo"]
            ]
            recruitSet: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            bgm: dict[str, int]
            pic: dict[str, int]
            chatV2: dict[str, list[str]]
            endBook: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            buff: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"]
            totem: "PlayerRoguelikeV2.OuterData.TotemCollection | None" = None
            chaos: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"] | None = None
            fragment: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"] | None = None
            disaster: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"] | None = None
            nodeUpgrade: dict[str, "PlayerRoguelikeV2.OuterData.NodeUpgradeInfo"] | None = None
            copper: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"] | None = None
            wrath: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"] | None = None
            chat: dict[str, int] | None = None

            class ItemUnlockInfo(BaseStruct):
                state: RoguelikeArchiveItemUnlockStatus
                progress: list[int] | None

            class DifficultyUnlockInfo(BaseStruct):
                state: PlayerRoguelikeDifficultyStatus
                progress: list[int] | None

        class Bank(BaseStruct):
            show: bool
            current: int
            record: int
            totalPut: int
            reward: dict[str, int]

        class Buff(BaseStruct):
            pointOwned: int
            pointCost: int
            unlocked: dict[str, int]
            score: int

        class MonthTeam(BaseStruct):
            valid: list[str]
            reward: dict[str, int]
            mission: dict[str, list[int]]

        class ChallengeCollection(BaseStruct):
            exploreTool: dict[str, "PlayerRoguelikeV2.OuterData.Collection.ItemUnlockInfo"] | None = None

        class Challenge(BaseStruct):
            reward: dict[str, int]
            grade: dict[str, PlayerRoguelikeChallengeStatus]
            collect: "PlayerRoguelikeV2.OuterData.ChallengeCollection"
            highScore: dict[str, int]

        class NodeUpgradeInfo(BaseStruct):
            unlockList: list[str]

        class PlayerRogueActivity(BaseStruct):
            SEED_MODE: (
                dict[str, "PlayerRoguelikeV2.OuterData.PlayerRogueActivity.PlayerRoguelikeActivitySeedModeData"] | None
            ) = None

            class PlayerRoguelikeActivitySeedModeData(BaseStruct):
                unlockState: "PlayerRoguelikeV2.OuterData.PlayerRogueActivity.PlayerRogueActivityUnlockInfo"
                seed: str

            class PlayerRogueActivityUnlockInfo(BaseStruct):
                state: "PlayerRoguelikeV2.OuterData.PlayerRogueActivity.PlayerRogueActivityUnlockInfo.PlayerRogueActivityUnlockState"
                progress: list[int]

                class PlayerRogueActivityUnlockState(StrEnum):
                    LOCKED = "LOCKED"
                    UNLOCKED_UNPLAYED = "UNLOCKED_UNPLAYED"
                    UNLOCKED_PLAYED = "UNLOCKED_PLAYED"
