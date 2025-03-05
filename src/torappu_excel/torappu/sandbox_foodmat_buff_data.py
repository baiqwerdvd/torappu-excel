from .sandbox_food_mat_type import SandboxFoodMatType
from ..common import BaseStruct


class SandboxFoodmatBuffData(BaseStruct):
    itemId: str
    buffId: str | None
    buffDesc: str | None
    matType: SandboxFoodMatType
    sortId: int
