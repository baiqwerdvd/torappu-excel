from ..common import BaseStruct


class OpenServerChainLogin(BaseStruct):
    isAvailable: bool
    nowIndex: int
    history: list[int]
