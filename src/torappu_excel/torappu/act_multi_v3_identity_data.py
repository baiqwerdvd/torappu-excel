from .act_multi_v3_identity_type import ActMultiV3IdentityType
from ..common import BaseStruct


class ActMultiV3IdentityData(BaseStruct):
    id: str
    sortId: int
    picId: str
    type: ActMultiV3IdentityType
    maxNum: int
    color: str
