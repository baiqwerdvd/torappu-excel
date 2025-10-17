from msgspec import field

from .player_building_workshop_buff_bonus import PlayerBuildingWorkshopBuffBonus
from .player_room_state import PlayerRoomState
from ..common import BaseStruct


class PlayerBuildingWorkshopBuff(BaseStruct):
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

    class Cost(BaseStruct):
        type: str
        limit: int
        reduction: int

    class CostRe(BaseStruct):
        type: str
        from_: int = field(name="from")
        change: int

    class Recovery(BaseStruct):
        type: str
        pace: int
        recover: int

    class CostFormula(BaseStruct):
        formulaIds: list[str]
        reduction: int

    class CostForce(BaseStruct):
        type: str
        cost: int

    class CostDevide(BaseStruct):
        type: str
        limit: int
        denominator: int

    class Frate(BaseStruct):
        fid: str
        rate: float

    class FFix(BaseStruct):
        asRarity: dict[str, dict[str, str]]
