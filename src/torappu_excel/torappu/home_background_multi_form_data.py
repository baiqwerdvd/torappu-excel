from pydantic import BaseModel, ConfigDict


class HomeBackgroundMultiFormData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    multiFormBgId: str
    sortId: int
    bgMusicId: str
