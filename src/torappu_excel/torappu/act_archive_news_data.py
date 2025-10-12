from pydantic import BaseModel, ConfigDict

from .act_archive_news_item_data import ActArchiveNewsItemData


class ActArchiveNewsData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    news: dict[str, ActArchiveNewsItemData]
