from pydantic import BaseModel, ConfigDict


class PlayerNodeDetailContent(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    scene: str
    battleShop: "PlayerNodeDetailContent.BattleShop"
    wish: list[str]
    battle: list[str]
    hasShopBoss: bool

    class BattleShop(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        hasShopBoss: bool
        goods: list[str]
