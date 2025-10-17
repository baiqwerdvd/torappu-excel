from enum import IntEnum, StrEnum

from msgspec import field

from .player_squad_item import PlayerSquadItem
from .sandbox_v2_enemy_rush_type import SandboxV2EnemyRushType
from .sandbox_v2_node_type import SandboxV2NodeTypeEnum
from .sandbox_v2_quest_line_badge_type import SandboxV2QuestLineBadgeTypeEnum
from .sandbox_v2_rare_animal_type import SandboxV2RareAnimalType
from .sandbox_v2_season_type import SandboxV2SeasonTypeEnum
from .sandbox_v2_weather_type import SandboxV2WeatherTypeEnum
from ..common import BaseStruct


class PlayerSandboxV2(BaseStruct):
    status: "PlayerSandboxV2.Status"
    base: "PlayerSandboxV2.BaseInfo"
    main: "PlayerSandboxV2.Dungeon"
    rift: "PlayerSandboxV2.Dungeon | None"
    quest: "PlayerSandboxV2.QuestGroup"
    mission: "PlayerSandboxV2.Expedition"
    troop: "PlayerSandboxV2.Troop"
    cook: "PlayerSandboxV2.Cook"
    build: "PlayerSandboxV2.Build"
    bag: "PlayerSandboxV2.Bag"
    bank: "PlayerSandboxV2.Bank"
    shop: "PlayerSandboxV2.Shop"
    riftInfo: "PlayerSandboxV2.RiftInfo"
    supply: "PlayerSandboxV2.Supply"
    tech: "PlayerSandboxV2.Tech"
    month: "PlayerSandboxV2.Month"
    archive: "PlayerSandboxV2.Archive"
    collect: "PlayerSandboxV2.Collect"
    buff: "PlayerSandboxV2.Buff"
    racing: "PlayerSandboxV2.Racing"
    challenge: "PlayerSandboxV2.Challenge"

    class GameState(IntEnum):
        INACTIVE = 0
        ACTIVE = 1
        SETTLE_DATE = 2
        READING_ARCHIVE = 3

    class NodeState(IntEnum):
        LOCKED = 0
        UNLOCKED = 1
        COMPLETED = 2

    class StageState(IntEnum):
        UNEXPLORED = 0
        EXPLORED = 1
        COMPLETED = 2

    class Status(BaseStruct):
        state: "PlayerSandboxV2.GameState"
        ts: int
        ver: int
        isRift: bool
        isGuide: bool
        isChallenge: bool
        mode: int
        exploreMode: bool

    class BaseInfo(BaseStruct):
        baseLv: int
        portableUnlock: bool
        outpostUnlock: bool
        trapLimit: dict[str, int]
        upgradeProgress: list[list[int]]
        repairDiscount: int
        bossKill: list[str]
        ver: int | None = None

    class Dungeon(BaseStruct):
        game: "PlayerSandboxV2.Dungeon.Game"
        map: "PlayerSandboxV2.Dungeon.Map"
        stage: "PlayerSandboxV2.Dungeon.Stage"
        enemy: "PlayerSandboxV2.Dungeon.Enemy"
        npc: "PlayerSandboxV2.Dungeon.NpcGroup"
        event: "PlayerSandboxV2.Dungeon.EventGroup"
        report: "PlayerSandboxV2.Dungeon.Report"

        class Game(BaseStruct):
            mapId: str
            day: int
            maxDay: int
            ap: int
            maxAp: int

        class Zone(BaseStruct):
            state: int
            weather: SandboxV2WeatherTypeEnum

        class NodeRelate(BaseStruct):
            pos: list[float]
            adj: list[str]
            depth: int

        class Node(BaseStruct):
            zone: str
            type: SandboxV2NodeTypeEnum
            state: "PlayerSandboxV2.NodeState"
            relate: "PlayerSandboxV2.Dungeon.NodeRelate"
            stageId: str
            weatherLv: int

        class Season(BaseStruct):
            type: SandboxV2SeasonTypeEnum
            remain: int
            total: int

        class Map(BaseStruct):
            season: "PlayerSandboxV2.Dungeon.Season"
            zone: dict[str, "PlayerSandboxV2.Dungeon.Zone"]
            node: dict[str, "PlayerSandboxV2.Dungeon.Node"]

        class Stage(BaseStruct):
            node: dict[str, "PlayerSandboxV2.Dungeon.NodeStage"]

        class Report(BaseStruct):
            settle: "PlayerSandboxV2.Dungeon.ReportSettle"
            daily: "PlayerSandboxV2.Dungeon.ReportDaily"

        class ReportDetail(BaseStruct):
            dayScore: int
            hasRift: bool
            riftScore: int
            apScore: int
            exploreScore: int
            enemyRush: dict[int, list[int]]
            home: dict[str, int]
            make: "PlayerSandboxV2.Dungeon.ReportMake"

        class ReportMake(BaseStruct):
            tactical: int
            food: int

        class ReportDaily(BaseStruct):
            isLoad: bool
            fromDay: int
            seasonChange: bool
            mission: "PlayerSandboxV2.Dungeon.ReportMission"
            baseProduct: "list[PlayerSandboxV2.Dungeon.ReportGainItem]"

        class ReportMission(BaseStruct):
            squad: list[list[int]]
            reward: "list[PlayerSandboxV2.Dungeon.ReportGainItem]"

        class ReportGainItem(BaseStruct):
            id: str
            count: int

        class ReportSettle(BaseStruct):
            score: int
            scoreRatio: str
            techToken: int
            techCent: int
            shopCoin: int
            shopCoinMax: bool
            detail: "PlayerSandboxV2.Dungeon.ReportDetail"

        class EntityStatus(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class BaseInfo(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Portable(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Nest(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Cave(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int
            extraParam: int | None = None

        class Gate(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Mine(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Selection(BaseStruct):
            count: list[int]
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Collect(BaseStruct):
            count: list[int]
            extraParam: int
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Hunt(BaseStruct):
            key: str
            count: list[int]

        class Trap(BaseStruct):
            key: str
            pos: list[int]
            isDead: int
            hpRatio: int

        class Building(BaseStruct):
            key: str
            pos: list[int]
            hpRatio: int
            dir: int

        class CatchAnimal(BaseStruct):
            room: int
            enemy: "list[PlayerSandboxV2.Dungeon.CatchAnimal.CatchAnimalInfo]"

            class CatchAnimalInfo(BaseStruct):
                id: str
                count: int

        class NodeStage(BaseStruct):
            id: str
            state: "PlayerSandboxV2.StageState"
            view: str
            action: list[list[int]]
            base: "list[PlayerSandboxV2.Dungeon.BaseInfo] | None" = None
            port: "list[PlayerSandboxV2.Dungeon.Portable] | None" = None
            nest: "list[PlayerSandboxV2.Dungeon.Nest] | None" = None
            cave: "list[PlayerSandboxV2.Dungeon.Cave] | None" = None
            gate: "list[PlayerSandboxV2.Dungeon.Gate] | None" = None
            mine: "list[PlayerSandboxV2.Dungeon.Mine] | None" = None
            insect: "list[PlayerSandboxV2.Dungeon.Selection] | None" = None
            collect: "list[PlayerSandboxV2.Dungeon.Collect] | None" = None
            hunt: "list[PlayerSandboxV2.Dungeon.Hunt] | None" = None
            trap: "list[PlayerSandboxV2.Dungeon.Trap] | None" = None
            building: "list[PlayerSandboxV2.Dungeon.Building] | None" = None
            actionKill: list[list[int]] | None = None
            animal: "list[PlayerSandboxV2.Dungeon.CatchAnimal] | None" = None

        class FloatSourceType(IntEnum):
            NONE = 0
            SRC_QUEST = 1
            SRC_MARKET = 2
            SRC_RIFT_MAIN = 3

        class FloatSource(BaseStruct):
            type: "PlayerSandboxV2.Dungeon.FloatSourceType"
            id: str

        class EnemyRushBossStatus(BaseStruct):
            hpRatio: int
            modeIndex: int

        class EnemyRush(BaseStruct):
            enemyRushType: SandboxV2EnemyRushType
            groupKey: str
            state: int
            day: int
            path: list[str]
            enemy: list[int]
            boss: dict[str, "PlayerSandboxV2.Dungeon.EnemyRushBossStatus"]
            badge: SandboxV2QuestLineBadgeTypeEnum
            src: "PlayerSandboxV2.Dungeon.FloatSource"

        class RareAnimal(BaseStruct):
            rareAnimalType: SandboxV2RareAnimalType
            enemyId: str
            enemyGroupKey: str
            day: int
            path: list[str]
            badge: SandboxV2QuestLineBadgeTypeEnum
            src: "PlayerSandboxV2.Dungeon.FloatSource"
            extra: "PlayerSandboxV2.Dungeon.RareAnimalExtraInfo"

        class RareAnimalExtraInfo(BaseStruct):
            hpRatio: int
            found: bool

        class Enemy(BaseStruct):
            enemyRush: dict[str, "PlayerSandboxV2.Dungeon.EnemyRush"]
            rareAnimal: dict[str, "PlayerSandboxV2.Dungeon.RareAnimal"]

        class NpcGroup(BaseStruct):
            node: dict[str, "list[PlayerSandboxV2.Dungeon.NpcGroup.Npc]"]
            favor: dict[str, int]

            class Npc(BaseStruct):
                id: str
                instId: int
                type: int
                enable: bool
                day: int
                dialog: dict[str, "PlayerSandboxV2.Dungeon.NpcGroup.Npc.NpcMeta"]
                badge: SandboxV2QuestLineBadgeTypeEnum
                src: "PlayerSandboxV2.Dungeon.FloatSource"

                class NpcMeta(BaseStruct):
                    gacha: "list[PlayerSandboxV2.Dungeon.NpcGroup.Npc.NpcMeta.GachaItemPair] | None" = None

                    class GachaItemPair(BaseStruct):
                        count: int
                        id: str
                        idx: int

        class Effect(BaseStruct):
            instId: int
            id: str
            day: int

        class EventGroup(BaseStruct):
            node: dict[str, "list[PlayerSandboxV2.Dungeon.EventGroup.Event]"]
            effect: "list[PlayerSandboxV2.Dungeon.Effect]"

            class Event(BaseStruct):
                id: str
                instId: int
                scene: str
                state: int
                badge: SandboxV2QuestLineBadgeTypeEnum
                src: "PlayerSandboxV2.Dungeon.FloatSource"

    class Troop(BaseStruct):
        food: dict[str, "PlayerSandboxV2.Troop.CharFood"]
        squad: "list[PlayerSandboxV2.Troop.Squad]"
        usedChar: list[int]

        class CharFood(BaseStruct):
            id: str
            sub: list[str]
            day: int

        class Squad(BaseStruct):
            slots: list[PlayerSquadItem]
            tools: list[str]

    class Cook(BaseStruct):
        drink: int
        extraDrink: int
        book: dict[str, int]
        food: dict[str, "PlayerSandboxV2.Cook.Food"]

        class Food(BaseStruct):
            id: str
            sub: list[str]
            count: int

    class Build(BaseStruct):
        book: dict[str, int]
        building: dict[str, int]
        tactical: dict[str, int]
        animal: dict[str, int]

    class Bag(BaseStruct):
        material: dict[str, int]
        craft: list[str]

    class Bank(BaseStruct):
        book: list[str]
        coin: dict[str, int]

    class Tech(BaseStruct):
        token: int
        cent: int
        unlock: list[str]

    class QuestGroup(BaseStruct):
        pending: "list[PlayerSandboxV2.QuestGroup.Quest]"
        complete: list[str]

        class Quest(BaseStruct):
            id: str
            state: int
            progIdx: int
            progress: list[list[int]]

    class Shop(BaseStruct):
        unlock: bool
        day: int
        slots: "list[PlayerSandboxV2.Shop.ShopSlotData]"

        class ShopSlotData(BaseStruct):
            id: str
            count: int
            price: int | None = None

    class Month(BaseStruct):
        rushPass: list[str]

    class RiftInfo(BaseStruct):
        isUnlocked: bool
        reserveTimes: dict[str, int]
        difficultyLvMax: dict[str, int]
        teamLv: int
        fixFinish: list[str]
        reservation: "PlayerSandboxV2.RiftInfo.Reservation | None"
        gameInfo: "PlayerSandboxV2.RiftInfo.GameInfo | None"
        settleInfo: "PlayerSandboxV2.RiftInfo.SettleInfo | None"
        randomRemain: int | None = None

        class RewardItem(BaseStruct):
            id: str
            count: int

        class Reservation(BaseStruct):
            instId: int
            rift: str
            mainTarget: str
            subTarget: str
            climate: str
            terrain: str
            map: str
            enemy: str
            effect: str
            difficulty: str
            team: str

        class RiftGameStatus(StrEnum):
            ACTIVE = "ACTIVE"
            SETTLE = "SETTLE"
            INVALID = "INVALID"

        class GameInfo(BaseStruct):
            status: "PlayerSandboxV2.RiftInfo.RiftGameStatus"
            mainProgress: list[int]
            subProgress: list[int]
            mainFail: bool
            pin: "PlayerSandboxV2.RiftInfo.GameInfo.RiftFloat"

            class RiftFloat(BaseStruct):
                nodeId: str
                badge: SandboxV2QuestLineBadgeTypeEnum
                src: "PlayerSandboxV2.Dungeon.FloatSource"

        class SettleReward(BaseStruct):
            main: "list[PlayerSandboxV2.RiftInfo.RewardItem]"
            sub: "list[PlayerSandboxV2.RiftInfo.RewardItem]"

        class SettleInfo(BaseStruct):
            reward: "PlayerSandboxV2.RiftInfo.SettleReward"
            portHp: int

    class Supply(BaseStruct):
        unlock: bool
        enable: bool
        slotCnt: int
        char: list[int]

    class Expedition(BaseStruct):
        squad: "list[PlayerSandboxV2.Expedition.Squad]"

        class Squad(BaseStruct):
            id: str
            day: int
            char: list[int]

    class Save(BaseStruct):
        day: int
        maxAp: int
        season: "PlayerSandboxV2.Dungeon.Season"
        ts: int
        slot: int

    class Archive(BaseStruct):
        save: "list[PlayerSandboxV2.Save]"
        nextLoadTs: int
        loadTs: int
        daily: "PlayerSandboxV2.Save | None"
        loadTimes: int

    class Collect(BaseStruct):
        pending: "PlayerSandboxV2.Collect.Pending"
        complete: "PlayerSandboxV2.Collect.Complete"

        class Pending(BaseStruct):
            achievement: dict[str, list[int]]

        class Complete(BaseStruct):
            achievement: list[str]
            quest: list[str]
            music: list[str]

    class Buff(BaseStruct):
        rune: "PlayerSandboxV2.Buff.Runes"

        class Runes(BaseStruct):
            global_: list[str] = field(name="global")
            node: dict[str, list[str]]
            char: dict[str, list[str]]

    class Racing(BaseStruct):
        unlock: bool
        bag: "PlayerSandboxV2.Racing.RacerBag"
        bagTmp: "PlayerSandboxV2.Racing.TempRacerBag"
        token: int

        class RacerName(BaseStruct):
            prefix: str
            suffix: str

        class RacerTalent(BaseStruct):
            born: str | None
            learned: str | None

        class RacerBaseInfo(BaseStruct):
            id: str
            inst: int
            level: int
            attrib: list[int]
            skill: "PlayerSandboxV2.Racing.RacerTalent"

        class TempRacerInfo(BaseStruct):
            id: str
            inst: int
            level: int
            attrib: list[int]
            skill: "PlayerSandboxV2.Racing.RacerTalent"

        class RacerInfo(BaseStruct):
            name: "PlayerSandboxV2.Racing.RacerName"
            mark: bool
            medal: list[str]
            id: str
            inst: int
            level: int
            attrib: list[int]
            skill: "PlayerSandboxV2.Racing.RacerTalent"

        class RacerBagBase(BaseStruct):
            cap: int

        class TempRacerBag(BaseStruct):
            racer: dict[str, "PlayerSandboxV2.Racing.TempRacerInfo"]
            cap: int

        class RacerBag(BaseStruct):
            racer: dict[str, "PlayerSandboxV2.Racing.RacerInfo"]
            cap: int

    class Challenge(BaseStruct):
        unlock: dict[str, list[int]]
        status: "PlayerSandboxV2.Challenge.ChallengeStatus | None"
        cur: "PlayerSandboxV2.Challenge.Current | None"
        best: "PlayerSandboxV2.Challenge.History | None"
        last: "PlayerSandboxV2.Challenge.History | None"
        reward: dict[str, int]
        hasSettleDayDoc: bool
        hasEnteredOnce: bool

        class ChallengeStatus(IntEnum):
            NOT_IN_CHALLENGE = 0
            IN_CHALLENGE = 1
            CHALLENGE_SETTLE = 2
            UNDEFINED = 3

        class Current(BaseStruct):
            startDay: int
            startLoadTimes: int
            hardRatio: int
            enemyKill: int

        class History(BaseStruct):
            startDay: int
            startLoadTimes: int
            ts: int
            day: int
