from pydantic import BaseModel, ConfigDict

from .skin_voice_type import SkinVoiceType


class CharSkinData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skinId: str
    charId: str
    tokenSkinMap: list["CharSkinData.TokenSkinInfo"] | None
    illustId: str | None
    spIllustId: str | None
    dynIllustId: str | None
    spDynIllustId: str | None
    avatarId: str
    portraitId: str | None
    dynPortraitId: str | None
    dynEntranceId: str | None
    buildingId: str | None
    battleSkin: "CharSkinData.BattleSkin"
    isBuySkin: bool
    tmplId: str | None
    voiceId: str | None
    voiceType: SkinVoiceType
    displaySkin: "CharSkinData.DisplaySkin"

    class TokenSkinInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        tokenId: str
        tokenSkinId: str

    class BattleSkin(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        overwritePrefab: bool
        skinOrPrefabId: str | None

    class DisplaySkin(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        skinName: str | None
        colorList: list[str] | None
        titleList: list[str] | None
        modelName: str | None
        drawerList: list[str] | None
        designerList: list[str] | None
        skinGroupId: str | None
        skinGroupName: str | None
        skinGroupSortIndex: int
        content: str | None
        dialog: str | None
        usage: str | None
        description: str | None
        obtainApproach: str | None
        sortId: int
        displayTagId: str | None
        getTime: int
        onYear: int
        onPeriod: int
