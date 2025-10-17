from ..common import BaseStruct


class PlayerNodeDetailContent(BaseStruct):
    scene: str
    battleShop: "PlayerNodeDetailContent.BattleShop"
    wish: list[str]
    battle: list[str]
    hasShopBoss: bool

    class BattleShop(BaseStruct):
        hasShopBoss: bool
        goods: list[str]
