from pydantic import BaseModel, ConfigDict, Field

from .illust_npc_res_type import IllustNPCResType
from .npc_unlock import NPCUnlock


class NPCData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    appellation: str
    cv: str
    designerList: list[str] | None
    displayNumber: str
    groupId: str | None
    illustList: list[str]
    name: str
    nationId: str
    npcId: str
    npcShowAudioInfoFlag: bool
    profession: str
    resType: IllustNPCResType
    teamId: None
    unlockDict: dict[str, NPCUnlock]
    minPowerId: str | None = Field(default=None)
