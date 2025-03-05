from ..common import BaseStruct

from msgspec import field


class SandboxV2RiftDifficultyData(BaseStruct):
    id_: str = field(name="id")
    riftId: str
    desc: str
    difficultyLevel: int
    rewardGroupId: str
