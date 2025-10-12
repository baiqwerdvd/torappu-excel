from pydantic import BaseModel, ConfigDict

from .rl01_customize_data import RL01CustomizeData
from .rl02_customize_data import RL02CustomizeData
from .rl03_customize_data import RL03CustomizeData
from .rl04_customize_data import RL04CustomizeData
from .rl05_customize_data import RL05CustomizeData


class RoguelikeTopicCustomizeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rogue_1: RL01CustomizeData
    rogue_2: RL02CustomizeData
    rogue_3: RL03CustomizeData
    rogue_4: RL04CustomizeData
    rogue_5: RL05CustomizeData
