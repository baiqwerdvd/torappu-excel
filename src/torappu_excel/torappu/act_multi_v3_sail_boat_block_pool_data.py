from .act_multi_v3_block_dir_type import ActMultiV3BlockDirType
from ..common import BaseStruct


class ActMultiV3SailBoatBlockPoolData(BaseStruct):
    blockPool: str
    blockId: str
    startDirType: ActMultiV3BlockDirType
    endDirType: ActMultiV3BlockDirType
    weight: int
