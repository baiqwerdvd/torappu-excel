from typing import Any

from ..common import BaseStruct


class PlayerSandboxV3(BaseStruct):
    band: dict[str, "PlayerSandboxV3.Band"]
    base: "PlayerSandboxV3.Basement"
    collect: "PlayerSandboxV3.Collect"
    current: dict[str, Any] | None
    dungeon: "PlayerSandboxV3.Dungeon"
    game: "PlayerSandboxV3.Game"
    inventory: "PlayerSandboxV3.Inventory"
    map: "PlayerSandboxV3.Map"
    npc: "PlayerSandboxV3.Npc"
    quest: "PlayerSandboxV3.QuestGroup"
    tech: "PlayerSandboxV3.Development"

    class Band(BaseStruct):
        badge: bool
        cond: list[int]
        level: int

    class BaseAnimal(BaseStruct):
        pos: list[int]
        enemy: dict[str, int]

    class BaseBuilding(BaseStruct):
        pos: list[int]
        dir: int

    class BaseShopGood(BaseStruct):
        count: int

    class BaseShop(BaseStruct):
        good: dict[str, "PlayerSandboxV3.BaseShopGood"]

    class Harvest(BaseStruct):
        harvestTs: int
        rate: dict[str, int]
        refreshTs: int
        unlock: bool

    class Basement(BaseStruct):
        animal: list["PlayerSandboxV3.BaseAnimal"]
        building: dict[str, list["PlayerSandboxV3.BaseBuilding"]]
        cond: list[list[int]]
        debris: list[list[int]]
        level: int
        production: "PlayerSandboxV3.Harvest"
        score: int
        shop: "PlayerSandboxV3.BaseShop"
        wonder: list[str]

    class CollectComplete(BaseStruct):
        achievement: list[str]
        music: list[str]
        quest: list[str]

    class CollectPending(BaseStruct):
        achievement: dict[str, list[int]]

    class Collect(BaseStruct):
        complete: "PlayerSandboxV3.CollectComplete"
        pending: "PlayerSandboxV3.CollectPending"

    class Difficulty(BaseStruct):
        cond: list[bool]
        state: int

    class Dungeon(BaseStruct):
        difficulty: dict[str, "PlayerSandboxV3.Difficulty"]

    class Game(BaseStruct):
        modeId: str

    class Inventory(BaseStruct):
        coin: dict[str, int]
        cookbook: list[str]
        trap: dict[str, int]

    class ZoneDefend(BaseStruct):
        main: int
        sub: list[int]

    class Zone(BaseStruct):
        defend: "PlayerSandboxV3.ZoneDefend"

    class Node(BaseStruct):
        state: int

    class Map(BaseStruct):
        node: dict[str, "PlayerSandboxV3.Node"]
        zone: dict[str, "PlayerSandboxV3.Zone"]

    class NpcBaseTrap(BaseStruct):
        instId: int
        id: str
        enable: bool

    class NpcBase(BaseStruct):
        enemy: list[str]
        trap: list["PlayerSandboxV3.NpcBaseTrap"]

    class NpcSource(BaseStruct):
        id: str
        type: int

    class NpcNormal(BaseStruct):
        badge: int
        dialog: list[int]
        enable: bool
        id: str
        instId: int
        src: "PlayerSandboxV3.NpcSource"

    class Npc(BaseStruct):
        base: "PlayerSandboxV3.NpcBase"
        normal: dict[str, list["PlayerSandboxV3.NpcNormal"]]

    class Quest(BaseStruct):
        id: str
        progress: list[list[int]]
        state: int

    class QuestGroup(BaseStruct):
        complete: list[str]
        pending: list["PlayerSandboxV3.Quest"]

    class Development(BaseStruct):
        token: int
        unlock: list[str]
