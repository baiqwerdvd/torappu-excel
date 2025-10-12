from pydantic import BaseModel, ConfigDict


class MapThemeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    themeId: str
    unitColor: str
    buildableColor: str | None
    themeType: str | None
    trapTintColor: str | None
    emissionColor: str | None
