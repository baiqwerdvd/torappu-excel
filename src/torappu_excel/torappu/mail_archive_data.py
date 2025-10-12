from pydantic import BaseModel, ConfigDict

from .mail_archive_const_data import MailArchiveConstData
from .mail_archive_item_data import MailArchiveItemData


class MailArchiveData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    mailArchiveInfoDict: dict[str, MailArchiveItemData]
    constData: MailArchiveConstData
