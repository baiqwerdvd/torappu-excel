from pydantic import BaseModel, ConfigDict

from .rune_table import RuneTable


class ActMultiV3SquadEffectData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    iconId: str
    sortId: int
    name: str
    themeColor: str
    buffDesc: str
    debuffDesc: str
    token: "ActMultiV3SquadEffectData.Token"
    runeData: "RuneTable.PackedRuneData"
    isInitial: bool

    class Token(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        name: str
        desc: str
        iconId: str
