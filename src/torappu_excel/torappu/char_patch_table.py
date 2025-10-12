from pydantic import BaseModel, ConfigDict

from .character_data import CharacterData
from .player_battle_rank import PlayerBattleRank


class CharPatchData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    infos: dict[str, "CharPatchData.PatchInfo"]
    patchChars: dict[str, CharacterData]
    unlockConds: dict[str, "CharPatchData.UnlockCond"]
    patchDetailInfoList: dict[str, "CharPatchData.PatchDetailInfo"]

    class PatchInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        tmplIds: list[str]
        default: str

    class UnlockCond(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        conds: list["CharPatchData.UnlockCond.Item"]

        class Item(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            completeState: PlayerBattleRank
            unlockTs: int

    class PatchDetailInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        patchId: str
        sortId: int
        infoParam: str
        transSortId: int
