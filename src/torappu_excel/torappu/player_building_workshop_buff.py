from pydantic import BaseModel, ConfigDict, Field

from .player_building_workshop_buff_bonus import PlayerBuildingWorkshopBuffBonus
from .player_room_state import PlayerRoomState


class PlayerBuildingWorkshopBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rate: dict[str, float]
    apRate: dict[str, dict[str, float]]
    frate: "list[PlayerBuildingWorkshopBuff.Frate]"
    fFix: "PlayerBuildingWorkshopBuff.FFix"
    goldFree: dict[str, int]
    cost: "PlayerBuildingWorkshopBuff.Cost"
    costRe: "PlayerBuildingWorkshopBuff.CostRe"
    recovery: "PlayerBuildingWorkshopBuff.Recovery"
    costFormula: "PlayerBuildingWorkshopBuff.CostFormula | None"
    costForce: "PlayerBuildingWorkshopBuff.CostForce"
    costDevide: "PlayerBuildingWorkshopBuff.CostDevide"
    activeBonus: dict[str, dict[str, list[PlayerBuildingWorkshopBuffBonus]]]
    state: PlayerRoomState | None = None

    class Cost(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: str
        limit: int
        reduction: int

    class CostRe(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: str
        from_: int = Field(alias="from")
        change: int

    class Recovery(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: str
        pace: int
        recover: int

    class CostFormula(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        formulaIds: list[str]
        reduction: int

    class CostForce(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: str
        cost: int

    class CostDevide(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        type: str
        limit: int
        denominator: int

    class Frate(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        fid: str
        rate: float

    class FFix(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        asRarity: dict[str, dict[str, str]]
