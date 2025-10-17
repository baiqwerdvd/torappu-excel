from ..common import BaseStruct


class PlayerFormulaUnlockRecord(BaseStruct):
    shop: dict[str, int]
    manufacture: dict[str, int]
    workshop: dict[str, int]
