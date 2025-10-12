from pydantic import BaseModel, ConfigDict

from .act_4fun_perform_word_data import Act4funPerformWordData


class Act4funPerformInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    performId: str
    performFinishedPicId: str | None
    fixedCmpGroup: str | None
    cmpGroups: list[str | None]
    words: list[Act4funPerformWordData]
