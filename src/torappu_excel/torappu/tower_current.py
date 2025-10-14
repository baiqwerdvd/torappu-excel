from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .char_star_mark_state import CharStarMarkState
from .evolve_phase import EvolvePhase
from .player_char_patch import PlayerCharPatch
from .tower_tactical import TowerTactical


class TowerCurrent(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class Status(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        state: "TowerCurrent.TowerGameState"
        tower: str
        coord: int
        tactical: TowerTactical
        start: int
        isHard: bool
        strategy: str

    class TowerGodCard(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        subGodCardId: str

    class TowerGameLayer(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        try_: int = Field(alias="try")
        pass_: bool = Field(alias="pass")

    class GameCard(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class TowerTrapInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        alias: str

    class HalftimeRecruit(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        count: int
        candidate: "list[TowerCurrent.HalftimeCandidateGroup]"
        canGiveUp: bool

    class HalftimeCandidateGroup(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        groupId: str
        type: "TowerCurrent.TowerCardType"
        cards: "list[TowerCurrent.GameCard]"
