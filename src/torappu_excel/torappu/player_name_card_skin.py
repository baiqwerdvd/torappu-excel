from pydantic import BaseModel, ConfigDict


class PlayerNameCardSkin(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    selected: str
    state: dict[str, "PlayerNameCardSkin.SkinState"]
    tmpl: dict[str, int]

    class SkinState(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlock: bool
        progress: list[list[int]] | None
