from .act_archive_component_data import ActArchiveComponentData
from ..common import BaseStruct


class ActArchiveComponentTable(BaseStruct):
    components: dict[str, ActArchiveComponentData]
