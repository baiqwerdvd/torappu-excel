from pydantic import BaseModel, ConfigDict


class Act5FunSettleRatingData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    minRating: int
    maxRating: int
    ratingDesc: str
