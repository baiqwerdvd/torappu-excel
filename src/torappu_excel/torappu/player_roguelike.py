from .player_roguelike_character import PlayerRoguelikeCharacter
from .player_roguelike_dungeon import PlayerRoguelikeDungeon
from .player_roguelike_initial_reward import PlayerRoguelikeInitialReward
from .player_roguelike_item import PlayerRoguelikeItem
from .player_roguelike_record import PlayerRoguelikeRecord
from .player_roguelike_status import PlayerRoguelikeStatus
from ..common import BaseStruct


class PlayerRoguelike(BaseStruct):
    current: "PlayerRoguelike.CurrentData | None"
    stable: "PlayerRoguelike.StableData | None"

    class CurrentData(BaseStruct):
        status: PlayerRoguelikeStatus
        initialRewards: PlayerRoguelikeInitialReward
        map: PlayerRoguelikeDungeon
        inventory: dict[str, PlayerRoguelikeItem]
        chars: dict[str, PlayerRoguelikeCharacter]
        record: PlayerRoguelikeRecord

    class StableData(BaseStruct):
        outBuff: dict[str, int]
        relic: dict[str, "PlayerRoguelike.StableData.RelicRecord"]
        stages: dict[str, "PlayerRoguelike.StableData.StageRecord"]
        ending: dict[str, "PlayerRoguelike.StableData.EndingRecord"]
        mode: dict[str, "PlayerRoguelike.StableData.ModeRecord"]
        stats: "PlayerRoguelike.StableData.StatsRecords"

        class RelicRecord(BaseStruct):
            uts: int
            cnt: int

        class StageRecord(BaseStruct):
            count: int

        class EndingRecord(BaseStruct):
            cnt: int
            initialRelic: dict[str, int]

        class ModeRecord(BaseStruct):
            uts: int
            cnt: int

        class StatsRecords(BaseStruct):
            complete_battle: int
            cost_hp: int
            recruit_char: int
            into_node_nobattle: int
            shop_cost_gold: int
            upgrade_char: int
            enemy_kill: dict[str, int]
            gain_resource: dict[str, int]
            scene_count: dict[str, int]
            choice_count: dict[str, int]
