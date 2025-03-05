from .roguelike_activity_seed_mode_data import RoguelikeActivitySeedModeData
from ..common import BaseStruct


class RoguelikeActivityTable(BaseStruct):
    SEED_MODE: dict[str, RoguelikeActivitySeedModeData]
