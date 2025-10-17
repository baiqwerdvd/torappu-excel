from .building_buff_display import BuildingBuffDisplay
from .building_data import BuildingData
from .player_building_trading_buff import PlayerBuildingTradingBuff
from .player_building_trading_next import PlayerBuildingTradingNext
from .player_building_trading_order import PlayerBuildingTradingOrder
from .player_room_state import PlayerRoomState
from ..common import BaseStruct


class PlayerBuildingTrading(BaseStruct):
    buff: PlayerBuildingTradingBuff
    state: PlayerRoomState
    lastUpdateTime: int
    strategy: "BuildingData.OrderType"
    stockLimit: int
    apCost: int
    stock: list[PlayerBuildingTradingOrder]
    next: PlayerBuildingTradingNext
    completeWorkTime: int
    display: BuildingBuffDisplay
    presetQueue: list[list[int]]
