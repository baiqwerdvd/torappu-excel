from pydantic import BaseModel, ConfigDict

from .act_archive_challenge_book_item_data import ActArchiveChallengeBookItemData


class ActArchiveChallengeBookData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stories: dict[str, ActArchiveChallengeBookItemData]
