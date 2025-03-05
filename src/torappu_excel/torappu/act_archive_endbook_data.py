from .act_archive_endbook_group_data import ActArchiveEndbookGroupData
from ..common import BaseStruct


class ActArchiveEndbookData(BaseStruct):
    endbook: dict[str, ActArchiveEndbookGroupData]
