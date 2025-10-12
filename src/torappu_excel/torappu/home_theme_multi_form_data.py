from pydantic import BaseModel, ConfigDict


class HomeThemeMultiFormData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    multiFormTmId: str
    sortId: int
