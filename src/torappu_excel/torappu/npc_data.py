from .illust_npc_res_type import IllustNPCResType
from .npc_unlock import NPCUnlock
from ..common import BaseStruct

from msgspec import field


class NPCData(BaseStruct):
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
    minPowerId: str | None = field(default=None)
