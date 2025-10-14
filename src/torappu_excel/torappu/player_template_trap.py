from pydantic import BaseModel, ConfigDict


class PlayerTemplateTrap(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    domains: dict[str, "PlayerTemplateTrap.Domin"]

    class Trap(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        count: int

    class Domin(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        traps: dict[str, "PlayerTemplateTrap.Trap"]
        squad: list[str]
