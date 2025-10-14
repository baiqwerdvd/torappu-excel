from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .player_squad_item import PlayerSquadItem
from .sandbox_v2_enemy_rush_type import SandboxV2EnemyRushType
from .sandbox_v2_node_type import SandboxV2NodeType
from .sandbox_v2_quest_line_badge_type import SandboxV2QuestLineBadgeType
from .sandbox_v2_rare_animal_type import SandboxV2RareAnimalType
from .sandbox_v2_season_type import SandboxV2SeasonType
from .sandbox_v2_weather_type import SandboxV2WeatherType


class PlayerSandboxV2(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Status(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        state: "PlayerSandboxV2.GameState"
        ts: int
        ver: int
        isRift: bool
        isGuide: bool
        isChallenge: bool
        mode: int
        exploreMode: bool

    class BaseInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        ver: int | None = None
        baseLv: int
        portableUnlock: bool
        outpostUnlock: bool
        trapLimit: dict[str, int]
        upgradeProgress: list[list[int]]
        repairDiscount: int
        bossKill: list[str]

    class Dungeon(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        game: "PlayerSandboxV2.Dungeon.Game"
        map: "PlayerSandboxV2.Dungeon.Map"
        stage: "PlayerSandboxV2.Dungeon.Stage"
        enemy: "PlayerSandboxV2.Dungeon.Enemy"
        npc: "PlayerSandboxV2.Dungeon.NpcGroup"
        event: "PlayerSandboxV2.Dungeon.EventGroup"
        report: "PlayerSandboxV2.Dungeon.Report"

        class Game(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            mapId: str
            day: int
            maxDay: int
            ap: int
            maxAp: int

        class Zone(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: bool
            weather: SandboxV2WeatherType

        class NodeRelate(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            pos: list[float]
            adj: list[str]
            depth: int

        class Node(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            zone: str
            type: SandboxV2NodeType
            state: "PlayerSandboxV2.NodeState"
            relate: "PlayerSandboxV2.Dungeon.NodeRelate"
            stageId: str
            weatherLv: int

        class Season(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            type: SandboxV2SeasonType
            remain: int
            total: int

        class Map(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            season: "PlayerSandboxV2.Dungeon.Season"
            zone: dict[str, "PlayerSandboxV2.Dungeon.Zone"]
            node: dict[str, "PlayerSandboxV2.Dungeon.Node"]

        class Stage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            node: dict[str, "PlayerSandboxV2.Dungeon.NodeStage"]

        class Report(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            settle: "PlayerSandboxV2.Dungeon.ReportSettle"
            daily: "PlayerSandboxV2.Dungeon.ReportDaily"

        class ReportDetail(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            dayScore: int
            hasRift: bool
            riftScore: int
            apScore: int
            exploreScore: int
            enemyRush: dict[int, list[int]]
            home: dict[str, int]
            make: "PlayerSandboxV2.Dungeon.ReportMake"

        class ReportMake(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            tactical: int
            food: int

        class ReportDaily(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            isLoad: bool
            fromDay: int
            seasonChange: bool
            mission: "PlayerSandboxV2.Dungeon.ReportMission"
            baseProduct: "list[PlayerSandboxV2.Dungeon.ReportGainItem]"

        class ReportMission(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            squad: list[list[int]]
            reward: "list[PlayerSandboxV2.Dungeon.ReportGainItem]"

        class ReportGainItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            count: int

        class ReportSettle(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            score: int
            scoreRatio: str
            techToken: int
            techCent: int
            shopCoin: int
            shopCoinMax: bool
            detail: "PlayerSandboxV2.Dungeon.ReportDetail"

        class EntityStatus(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class BaseInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Portable(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Nest(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Cave(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            extraParam: int | None = None
            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Gate(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Mine(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Selection(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            count: list[int]
            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Collect(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            count: list[int]
            extraParam: int
            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Hunt(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            count: list[int]

        class Trap(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            isDead: bool
            hpRatio: int

        class Building(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            key: str
            pos: list[int]
            hpRatio: int
            dir: int

        class CatchAnimal(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            room: int
            enemy: "list[PlayerSandboxV2.Dungeon.CatchAnimal.CatchAnimalInfo]"

            class CatchAnimalInfo(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                id: str
                count: int

        class NodeStage(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            state: "PlayerSandboxV2.StageState"
            view: str
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
            action: list[list[int]]
            actionKill: list[list[int]] | None = None
            animal: "list[PlayerSandboxV2.Dungeon.CatchAnimal] | None" = None

        class FloatSourceType(IntEnum):
            NONE = 0
            SRC_QUEST = 1
            SRC_MARKET = 2
            SRC_RIFT_MAIN = 3

        class FloatSource(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            type: "PlayerSandboxV2.Dungeon.FloatSourceType"
            id: str

        class EnemyRushBossStatus(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            hpRatio: int
            modeIndex: int

        class EnemyRush(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            enemyRushType: SandboxV2EnemyRushType
            groupKey: str
            state: int
            day: int
            path: list[str]
            enemy: list[int]
            boss: dict[str, "PlayerSandboxV2.Dungeon.EnemyRushBossStatus"]
            badge: SandboxV2QuestLineBadgeType
            src: "PlayerSandboxV2.Dungeon.FloatSource"

        class RareAnimal(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            rareAnimalType: SandboxV2RareAnimalType
            enemyId: str
            enemyGroupKey: str
            day: int
            path: list[str]
            badge: SandboxV2QuestLineBadgeType
            src: "PlayerSandboxV2.Dungeon.FloatSource"
            extra: "PlayerSandboxV2.Dungeon.RareAnimalExtraInfo"

        class RareAnimalExtraInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            hpRatio: int
            found: bool

        class Enemy(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            enemyRush: dict[str, "PlayerSandboxV2.Dungeon.EnemyRush"]
            rareAnimal: dict[str, "PlayerSandboxV2.Dungeon.RareAnimal"]

        class NpcGroup(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            node: dict[str, "list[PlayerSandboxV2.Dungeon.NpcGroup.Npc]"]
            favor: dict[str, int]

            class Npc(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                id: str
                instId: int
                type: bool
                enable: bool
                day: int
                dialog: dict[int, "PlayerSandboxV2.Dungeon.NpcGroup.Npc.NpcMeta"]
                badge: SandboxV2QuestLineBadgeType
                src: "PlayerSandboxV2.Dungeon.FloatSource"

                class NpcMeta(BaseModel):
                    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                    gacha: "list[PlayerSandboxV2.Dungeon.NpcGroup.Npc.NpcMeta.GachaItemPair] | None" = None

                    class GachaItemPair(BaseModel):
                        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                        count: int
                        id: str
                        idx: int

        class Effect(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            instId: int
            id: str
            day: int

        class EventGroup(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            node: dict[str, "list[PlayerSandboxV2.Dungeon.EventGroup.Event]"]
            effect: "list[PlayerSandboxV2.Dungeon.Effect]"

            class Event(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                id: str
                instId: int
                scene: str
                state: int
                badge: SandboxV2QuestLineBadgeType
                src: "PlayerSandboxV2.Dungeon.FloatSource"

    class Troop(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        food: dict[int, "PlayerSandboxV2.Troop.CharFood"]
        squad: "list[PlayerSandboxV2.Troop.Squad]"
        usedChar: list[int]

        class CharFood(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            sub: list[str]
            day: int

        class Squad(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            slots: list[PlayerSquadItem]
            tools: list[str]

    class Cook(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        drink: int
        extraDrink: int
        book: dict[str, int]
        food: dict[str, "PlayerSandboxV2.Cook.Food"]

        class Food(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            sub: list[str]
            count: int

    class Build(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        book: dict[str, int]
        building: dict[str, int]
        tactical: dict[str, int]
        animal: dict[str, int]

    class Bag(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        material: dict[str, int]
        craft: list[str]

    class Bank(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        book: list[str]
        coin: dict[str, int]

    class Tech(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        token: int
        cent: int
        unlock: list[str]

    class QuestGroup(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        pending: "list[PlayerSandboxV2.QuestGroup.Quest]"
        complete: list[str]

        class Quest(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            state: bool
            progIdx: int
            progress: list[list[int]]

    class Shop(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlock: bool
        day: int
        slots: "list[PlayerSandboxV2.Shop.ShopSlotData]"

        class ShopSlotData(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            count: int
            price: int | None = None

    class Month(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rushPass: list[str]

    class RiftInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        isUnlocked: bool
        reserveTimes: dict[str, int]
        difficultyLvMax: dict[str, int]
        teamLv: int
        fixFinish: list[str]
        reservation: "PlayerSandboxV2.RiftInfo.Reservation | None"
        gameInfo: "PlayerSandboxV2.RiftInfo.GameInfo | None"
        settleInfo: "PlayerSandboxV2.RiftInfo.SettleInfo | None"
        randomRemain: int | None = None

        class RewardItem(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            count: int

        class Reservation(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

        class GameInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            status: "PlayerSandboxV2.RiftInfo.RiftGameStatus"
            mainProgress: list[int]
            subProgress: list[int]
            mainFail: bool
            pin: "PlayerSandboxV2.RiftInfo.GameInfo.RiftFloat"

            class RiftFloat(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                nodeId: str
                badge: SandboxV2QuestLineBadgeType
                src: "PlayerSandboxV2.Dungeon.FloatSource"

        class SettleReward(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            main: "list[PlayerSandboxV2.RiftInfo.RewardItem]"
            sub: "list[PlayerSandboxV2.RiftInfo.RewardItem]"

        class SettleInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            reward: "PlayerSandboxV2.RiftInfo.SettleReward"
            portHp: int

    class Supply(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlock: bool
        enable: bool
        slotCnt: int
        char: list[int]

    class Expedition(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        squad: "list[PlayerSandboxV2.Expedition.Squad]"

        class Squad(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            day: int
            char: list[int]

    class Save(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        day: int
        maxAp: int
        season: "PlayerSandboxV2.Dungeon.Season"
        ts: int
        slot: int

    class Archive(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        save: "list[PlayerSandboxV2.Save]"
        nextLoadTs: int
        loadTs: int
        daily: "PlayerSandboxV2.Save | None"
        loadTimes: int

    class Collect(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        pending: "PlayerSandboxV2.Collect.Pending"
        complete: "PlayerSandboxV2.Collect.Complete"

        class Pending(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            achievement: dict[str, list[int]]

        class Complete(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            achievement: list[str]
            quest: list[str]
            music: list[str]

    class Buff(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        rune: "PlayerSandboxV2.Buff.Runes"

        class Runes(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            global_: list[str] = Field(alias="global")
            node: dict[str, list[str]]
            char: dict[str, list[str]]

    class Racing(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlock: bool
        bag: "PlayerSandboxV2.Racing.RacerBag"
        bagTmp: "PlayerSandboxV2.Racing.TempRacerBag"
        token: int

        class RacerName(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            prefix: str
            suffix: str

        class RacerTalent(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            born: str | None
            learned: str | None

        class RacerBaseInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            inst: int
            level: int
            attrib: list[int]
            skill: "PlayerSandboxV2.Racing.RacerTalent"

        class TempRacerInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            id: str
            inst: int
            level: int
            attrib: list[int]
            skill: "PlayerSandboxV2.Racing.RacerTalent"

        class RacerInfo(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            name: "PlayerSandboxV2.Racing.RacerName"
            mark: bool
            medal: list[str]
            id: str
            inst: int
            level: int
            attrib: list[int]
            skill: "PlayerSandboxV2.Racing.RacerTalent"

        class RacerBagBase(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            cap: int

        class TempRacerBag(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            racer: dict[str, "PlayerSandboxV2.Racing.TempRacerInfo"]
            cap: int

        class RacerBag(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            racer: dict[str, "PlayerSandboxV2.Racing.RacerInfo"]
            cap: int

    class Challenge(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

        class Current(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            startDay: int
            startLoadTimes: int
            hardRatio: int
            enemyKill: int

        class History(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            startDay: int
            startLoadTimes: int
            ts: int
            day: int
