from pydantic import BaseModel, ConfigDict, Field


class BasedRecruitPool(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    recruitConstants: "BasedRecruitPool.RecruitConstants"

    class RecruitConstants(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        tagPriceList: dict[str, int]
        maxRecruitTime: int
        rarityWeights: None = Field(default=None)
        recruitTimeFactorList: None = Field(default=None)


class RecruitConstants(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tagPriceList: dict[str, int]
    maxRecruitTime: int
    rarityWeights: None = Field(default=None)
    recruitTimeFactorList: None = Field(default=None)
