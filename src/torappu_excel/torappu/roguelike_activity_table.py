from pydantic import BaseModel, ConfigDict

from .roguelike_activity_seed_mode_data import RoguelikeActivitySeedModeData


class RoguelikeActivityTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    SEED_MODE: dict[str, RoguelikeActivitySeedModeData]
