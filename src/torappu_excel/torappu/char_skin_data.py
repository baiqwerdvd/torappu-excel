from .skin_voice_type import SkinVoiceType
from ..common import BaseStruct


class CharSkinData(BaseStruct):
    skinId: str
    charId: str
    tokenSkinMap: list["CharSkinData.TokenSkinInfo"] | None
    illustId: str | None
    dynIllustId: str | None
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

    class TokenSkinInfo(BaseStruct):
        tokenId: str
        tokenSkinId: str

    class BattleSkin(BaseStruct):
        overwritePrefab: bool
        skinOrPrefabId: str | None

    class DisplaySkin(BaseStruct):
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
