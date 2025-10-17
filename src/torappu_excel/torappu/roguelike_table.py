from .roguelike_choice_data import RoguelikeChoiceData
from .roguelike_choice_scene_data import RoguelikeChoiceSceneData
from .roguelike_const_table import RoguelikeConstTable
from .roguelike_ending_data import RoguelikeEndingData
from .roguelike_item_table import RoguelikeItemTable
from .roguelike_mode_data import RoguelikeModeData
from .roguelike_out_buff_data import RoguelikeOutBuffData
from .roguelike_stage_data import RoguelikeStageData
from .roguelike_zone_data import RoguelikeZoneData
from ..common import BaseStruct


class RoguelikeTable(BaseStruct):
    constTable: RoguelikeConstTable
    itemTable: RoguelikeItemTable
    stages: dict[str, RoguelikeStageData]
    zones: dict[str, RoguelikeZoneData]
    choices: dict[str, RoguelikeChoiceData]
    choiceScenes: dict[str, RoguelikeChoiceSceneData]
    modes: dict[str, RoguelikeModeData]
    endings: dict[str, RoguelikeEndingData]
    outBuffs: dict[str, RoguelikeOutBuffData]
