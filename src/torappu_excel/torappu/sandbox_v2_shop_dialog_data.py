from ..common import BaseStruct


class SandboxV2ShopDialogData(BaseStruct):
    seasonDialogs: dict[str, list[str]]
    afterBuyDialogs: list[str]
    shopEmptyDialogs: list[str]
