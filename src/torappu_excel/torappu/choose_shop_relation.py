from ..common import BaseStruct


class ChooseShopRelation(BaseStruct):
    goodId: str
    optionList: list[str]
