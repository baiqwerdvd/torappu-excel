from pydantic import BaseModel, ConfigDict

from .battle_dialog_type import BattleDialogType
from .sandbox_v2_npc_type import SandboxV2NpcType
from .shared_consts import SharedConsts


class SandboxV2NpcData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    npcId: str
    trapId: str
    npcType: SandboxV2NpcType
    dialogIds: dict[BattleDialogType, str]
    npcLocation: list[int] | None
    npcOrientation: SharedConsts.DirectionStr | None
    picId: str
    picName: str
    showPic: bool
    reactSkillIndex: int
