from enum import StrEnum

from msgspec import field

from .char_star_mark_state import CharStarMarkState
from .evolve_phase import EvolvePhase
from .player_char_patch import PlayerCharPatch
from .tower_tactical import TowerTactical
from ..common import BaseStruct


class TowerCurrent(BaseStruct):
    status: "TowerCurrent.Status"
    godCard: "TowerCurrent.TowerGodCard"
    layer: "list[TowerCurrent.TowerGameLayer]"
    cards: dict[str, "TowerCurrent.GameCard"]
    trap: "list[TowerCurrent.TowerTrapInfo]"
    halftime: "TowerCurrent.HalftimeRecruit"

    class TowerGameState(StrEnum):
        NONE = "NONE"
        INIT_GOD_CARD = "INIT_GOD_CARD"
        INIT_BUFF = "INIT_BUFF"
        INIT_CARD = "INIT_CARD"
        STANDBY = "STANDBY"
        RECRUIT = "RECRUIT"
        SUB_GOD_CARD_RECRUIT = "SUB_GOD_CARD_RECRUIT"
        END = "END"

    class TowerCardType(StrEnum):
        CHAR = "CHAR"
        ASSIST = "ASSIST"
        NPC = "NPC"

    class Status(BaseStruct):
        state: "TowerCurrent.TowerGameState"
        tower: str
        coord: int
        tactical: TowerTactical
        start: int
        isHard: bool
        strategy: str

    class TowerGodCard(BaseStruct):
        id: str
        subGodCardId: str

    class TowerGameLayer(BaseStruct):
        id: str
        try_: int = field(name="try")
        pass_: bool = field(name="pass")

    class GameCard(BaseStruct):
        relation: str
        type: "TowerCurrent.TowerCardType"
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

    class TowerTrapInfo(BaseStruct):
        id: str
        alias: str

    class HalftimeRecruit(BaseStruct):
        count: int
        candidate: "list[TowerCurrent.HalftimeCandidateGroup]"
        canGiveUp: bool

    class HalftimeCandidateGroup(BaseStruct):
        groupId: str
        type: "TowerCurrent.TowerCardType"
        cards: "list[TowerCurrent.GameCard]"
