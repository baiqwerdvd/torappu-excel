from pydantic import BaseModel, ConfigDict, Field

from .based_recruit_pool import RecruitConstants


class RecruitPool(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    recruitTimeTable: list["RecruitPool.RecruitTime"]
    recruitConstants: "RecruitConstants"
    recruitCharacterList: None = Field(default=None)
    maskTypeWeightTable: None = Field(default=None)

    class RecruitTime(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        timeLength: int
        recruitPrice: int
        accumRate: float | None = Field(default=None)
