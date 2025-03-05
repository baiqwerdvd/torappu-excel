from .character_data import CharacterData
from .player_battle_rank import PlayerBattleRank
from ..common import BaseStruct

from msgspec import field


class CharPatchData(BaseStruct):
    infos: dict[str, "CharPatchData.PatchInfo"]
    patchChars: dict[str, CharacterData]
    unlockConds: dict[str, "CharPatchData.UnlockCond"]
    patchDetailInfoList: dict[str, "CharPatchData.PatchDetailInfo"]

    class PatchInfo(BaseStruct):
        tmplIds: list[str]
        default: str

    class UnlockCond(BaseStruct):
        conds: list["CharPatchData.UnlockCond.Item"]

        class Item(BaseStruct):
            stageId: str
            completeState: PlayerBattleRank
            unlockTs: int | None = field(default=None)

    class PatchDetailInfo(BaseStruct):
        patchId: str
        sortId: int
        infoParam: str
        transSortId: int
