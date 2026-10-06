from ..common import BaseStruct


class Anniv7thClueData(BaseStruct):
    clueId: str
    clueGroupId: str
    sortId: int
    clueLink: list[str]
    clueName: str
    clueOwner: str
    clueDesc: str
    unlockDesc: str
    clueOwnerPic: str
    pageRes: str
