from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .mail_archive_item_type import MailArchiveItemType


class MailArchiveItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: MailArchiveItemType
    sortId: int
    displayReceiveTs: int
    year: int
    dateDelta: int
    senderId: str
    title: str
    content: str
    rewardList: list[ItemBundle]
